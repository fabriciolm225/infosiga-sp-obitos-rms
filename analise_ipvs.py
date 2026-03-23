# =============================================================================
# ANÁLISE INTRAURBANA — ÓBITOS EM SINISTROS DE TRÂNSITO E
# VULNERABILIDADE SOCIAL (IPVS 2022)
# Regiões Metropolitanas do Estado de São Paulo — 2016–2025
# Fonte: INFOSIGA-SP + IPVS 2022 (SEADE/IBGE)
# =============================================================================
#
# AUTORES
#   Fabrício Leite Momenti
#   Vitor Favali Kruger
#   Thiago Rodrigues Araújo Calderan
#   Gustavo Pereira Fraga
#   Divisão de Cirurgia de Trauma — FCM UNICAMP
#
# DECISÕES METODOLÓGICAS
#   - Unidade de análise: sinistro fatal georreferenciado
#   - Cada sinistro recebeu o grupo IPVS do setor censitário
#     onde ocorreu via spatial join ponto-polígono (GeoPandas)
#   - Cobertura: 88,3% dos sinistros fatais possuíam lat/lon válidos;
#     99,9% destes foram atribuídos a um setor censitário classificado
#   - IPVS 2022 (Censo IBGE): caracteriza vulnerabilidade social do
#     LOCAL do sinistro, não da vítima
#   - IPVS é transversal (2022); sinistros cobrem 2016–2025
#     (limitação de temporalidade)
#   - Análise ecológica municipal também realizada como complemento,
#     com corte mínimo de 10 óbitos por município para estabilidade
#     das taxas
#   - Correlação: Spearman (dados não paramétricos)
#   - Populações municipais: moradores em DPPO — Censo IBGE 2022
#     (IPVS/SEADE)
#
# ARQUIVOS DE ENTRADA
#   dados/obitos_sinistros_2016-2025.csv  (gerado por analise.py)
#   dados/obitos_pessoas_2016-2025.csv    (gerado por analise.py)
#   ipvs_2022/IPVS_2022.shp               (SEADE — shapefile)
#   ipvs.xlsx                             (SEADE — tabelas IPVS)
#
# DEPENDÊNCIAS
#   pip install pandas geopandas shapely pyproj scipy openpyxl
#
# USO
#   1. Rode analise.py primeiro para gerar os CSVs filtrados em dados/
#   2. Baixe o shapefile IPVS 2022 do SEADE e extraia em ipvs_2022/
#   3. Baixe o ipvs.xlsx do SEADE
#   4. Execute: python3 analise_ipvs.py
# =============================================================================

import pandas as pd
import numpy as np
import geopandas as gpd
from scipy import stats
import os

# =============================================================================
# CONFIGURAÇÕES
# =============================================================================

RMs = [
    'METROPOLITANA DE SÃO PAULO',
    'CAMPINAS',
    'BAIXADA SANTISTA',
    'SOROCABA',
    'SÃO JOSÉ DOS CAMPOS',
]

ORDEM_IPVS = {
    1.0: '1 - Baixíssima',
    2.0: '2 - Muito Baixa',
    3.0: '3 - Baixa',
    4.0: '4 - Média',
    5.0: '5 - Alta',
    6.0: '6 - Muito Alta',
}

POPULACAO_RM = {
    'METROPOLITANA DE SÃO PAULO': 21571281,
    'CAMPINAS':                    3656363,
    'BAIXADA SANTISTA':            1861800,
    'SOROCABA':                    1643766,
    'SÃO JOSÉ DOS CAMPOS':         1354884,
}


def interpretar_r(r):
    a = abs(r)
    if a < 0.2:   return 'muito fraca'
    elif a < 0.4: return 'fraca'
    elif a < 0.6: return 'moderada'
    elif a < 0.8: return 'forte'
    else:          return 'muito forte'


def sep(titulo, nivel=1):
    if nivel == 1:
        print('\n' + '█' * 65)
        print(f'  {titulo}')
        print('█' * 65)
    else:
        print(f'\n── {titulo} ──')


# =============================================================================
# ETAPA 1 — SPATIAL JOIN: SINISTROS x IPVS
# =============================================================================

def spatial_join():
    print('\n' + '=' * 65)
    print('ETAPA 1 — SPATIAL JOIN: SINISTROS FATAIS x IPVS 2022')
    print('=' * 65)

    # Carregar shapefile
    print('\nCarregando shapefile IPVS 2022...')
    gdf = gpd.read_file('ipvs_2022/IPVS_2022.shp')
    gdf = gdf[gdf['C_IPVS'].notna()].copy()
    print(f'  Setores censitários classificados: {len(gdf):,}')
    print(f'  CRS: {gdf.crs}')

    # Carregar sinistros fatais
    print('\nCarregando sinistros fatais...')
    sin = pd.read_csv('dados/obitos_sinistros_2016-2025.csv', low_memory=False)
    sin_geo = sin.dropna(subset=['latitude', 'longitude']).copy()

    # Corrigir formato brasileiro (vírgula → ponto)
    sin_geo['latitude']  = sin_geo['latitude'].astype(str).str.replace(',', '.').astype(float)
    sin_geo['longitude'] = sin_geo['longitude'].astype(str).str.replace(',', '.').astype(float)
    print(f'  Sinistros com coordenadas: {len(sin_geo):,} de {len(sin):,} ({len(sin_geo)/len(sin)*100:.1f}%)')

    # Converter para GeoDataFrame
    gdf_sin = gpd.GeoDataFrame(
        sin_geo,
        geometry=gpd.points_from_xy(sin_geo['longitude'], sin_geo['latitude']),
        crs='EPSG:4674'
    )

    # Spatial join
    print('\nRealizando spatial join (pode demorar alguns minutos)...')
    joined = gpd.sjoin(
        gdf_sin,
        gdf[['C_IPVS', 'N_IPVS', 'CD_MUN', 'NM_MUN', 'geometry']],
        how='left', predicate='within'
    )

    # C_IPVS = número, N_IPVS = texto (conforme estrutura do shapefile)
    joined = joined.rename(columns={'C_IPVS': 'num_ipvs', 'N_IPVS': 'txt_ipvs'})
    joined_clean = joined[joined['num_ipvs'].notna()].copy()

    print(f'\n  Sinistros com IPVS atribuído: {len(joined_clean):,}')
    print(f'  Sinistros sem IPVS (fora de polígono): {joined["num_ipvs"].isna().sum():,}')

    return joined_clean, sin


def carregar_vitimas_ipvs(joined_clean):
    """Join sinistros (com IPVS) com vítimas fatais."""
    pes = pd.read_csv('dados/obitos_pessoas_2016-2025.csv', low_memory=False)
    pes_ipvs = pes.merge(
        joined_clean[['id_sinistro', 'num_ipvs', 'txt_ipvs']],
        on='id_sinistro', how='inner'
    )
    pes_ipvs['grupo'] = pes_ipvs['num_ipvs'].map(ORDEM_IPVS)
    print(f'\nVítimas fatais com IPVS: {len(pes_ipvs):,} de {len(pes):,} ({len(pes_ipvs)/len(pes)*100:.1f}%)')
    return pes_ipvs, pes


# =============================================================================
# ETAPA 2 — ANÁLISE INTRAURBANA (nível de setor censitário)
# =============================================================================

def analisar_intraurbano(pes_ipvs):

    sep('ANÁLISE INTRAURBANA — GRUPO IPVS DO LOCAL DO SINISTRO', nivel=1)

    print("""
NOTA METODOLÓGICA
- Unidade de análise: sinistro fatal georreferenciado
- Cada sinistro recebeu o grupo IPVS do setor censitário
  onde ocorreu (spatial join ponto-polígono)
- Cobertura: 88,3% dos sinistros fatais possuíam coordenadas
  válidas; 99,9% destes atribuídos a setor classificado
- IPVS 2022: caracteriza o LOCAL do sinistro, não a vítima
- IPVS é transversal (2022); sinistros cobrem 2016–2025
  (limitação de temporalidade)
- Correlação de Spearman entre grupo IPVS ordinal (1→6)
  e distribuição percentual dos óbitos
""")

    # ── A1. Distribuição geral ────────────────────────────────
    sep('A1. DISTRIBUIÇÃO DE ÓBITOS POR GRUPO IPVS — TODAS AS RMs', nivel=2)
    dist_g = pes_ipvs.groupby('grupo').size().reset_index(name='obitos')
    dist_g['%'] = (dist_g['obitos'] / dist_g['obitos'].sum() * 100).round(1)
    dist_g = dist_g.sort_values('grupo')
    print(dist_g.to_string(index=False))

    # ── A2. Distribuição por RM ───────────────────────────────
    sep('A2. DISTRIBUIÇÃO DE ÓBITOS POR GRUPO IPVS E RM', nivel=2)
    tab_n = pes_ipvs.groupby(['regiao_administrativa', 'grupo']).size().unstack(fill_value=0)
    tab_n = tab_n[[c for c in sorted(tab_n.columns)]]
    tab_n['TOTAL'] = tab_n.sum(axis=1)
    tab_pct = tab_n.div(tab_n['TOTAL'], axis=0).multiply(100).round(1)
    tab_pct['TOTAL'] = tab_n['TOTAL']
    print('\nAbsoluto (N):')
    print(tab_n.to_string())
    print('\nProporcional (%):')
    print(tab_pct.to_string())

    # ── A3. Tendência Spearman por RM ─────────────────────────
    sep('A3. TENDÊNCIA — GRUPO IPVS x CONCENTRAÇÃO DE ÓBITOS (Spearman)', nivel=2)
    print('  Rho entre grupo numérico (1→6) e % de óbitos no grupo')
    rows = []
    for rm in RMs:
        sub = pes_ipvs[pes_ipvs['regiao_administrativa'] == rm]
        dist = sub.groupby('num_ipvs').size().reset_index(name='n')
        dist['pct'] = dist['n'] / dist['n'].sum() * 100
        if len(dist) < 4:
            continue
        rho, p = stats.spearmanr(dist['num_ipvs'], dist['pct'])
        rows.append({
            'RM': rm.title(),
            'N óbitos': len(sub),
            'Spearman rho': round(rho, 3),
            'p-valor': round(p, 4),
            'Sig. (p<0,05)': 'sim' if p < 0.05 else 'não',
            'Direção': 'positiva' if rho > 0 else 'negativa',
            'Força': interpretar_r(rho),
        })
    print(pd.DataFrame(rows).to_string(index=False))

    dist_ger = pes_ipvs.groupby('num_ipvs').size().reset_index(name='n')
    dist_ger['pct'] = dist_ger['n'] / dist_ger['n'].sum() * 100
    rho_g, p_g = stats.spearmanr(dist_ger['num_ipvs'], dist_ger['pct'])
    print(f'\nGeral (todas as RMs):')
    print(f'  N óbitos: {len(pes_ipvs):,}')
    print(f'  Spearman rho = {rho_g:.3f} | p = {p_g:.4f}')
    print(f'  Direção: {"positiva" if rho_g > 0 else "negativa"} | Força: {interpretar_r(rho_g)}')
    print(f'  Significativo: {"sim" if p_g < 0.05 else "não"} (p<0,05)')

    # ── A4. Tendência temporal ────────────────────────────────
    sep('A4. TENDÊNCIA TEMPORAL — ÓBITOS POR GRUPO IPVS E ANO', nivel=2)
    tab_ano = pes_ipvs.groupby(['ano_sinistro', 'grupo']).size().unstack(fill_value=0)
    tab_ano = tab_ano[[c for c in sorted(tab_ano.columns)]]
    print(tab_ano.to_string())

    # ── A5. Perfil das vítimas ────────────────────────────────
    sep('A5. PERFIL DAS VÍTIMAS POR GRUPO IPVS', nivel=2)

    print('\nSexo (% masculino por grupo):')
    sexo = pes_ipvs[pes_ipvs['sexo'].isin(['MASCULINO', 'FEMININO'])].copy()
    sexo_grp = sexo.groupby(['grupo', 'sexo']).size().unstack(fill_value=0)
    sexo_grp['TOTAL'] = sexo_grp.sum(axis=1)
    sexo_grp['% MASC'] = (sexo_grp['MASCULINO'] / sexo_grp['TOTAL'] * 100).round(1)
    print(sexo_grp.sort_index().to_string())

    print('\nTipo de veículo por grupo IPVS (%):')
    vei = pes_ipvs[~pes_ipvs['tipo_veiculo_vitima'].isin(['NAO DISPONIVEL'])].copy()
    vei_grp = vei.groupby(['grupo', 'tipo_veiculo_vitima']).size().unstack(fill_value=0)
    vei_pct = vei_grp.div(vei_grp.sum(axis=1), axis=0).multiply(100).round(1)
    print(vei_pct.sort_index().to_string())

    print('\nTipo de vítima por grupo IPVS (%):')
    tv = pes_ipvs[pes_ipvs['tipo_de_vitima'].isin(['CONDUTOR', 'PASSAGEIRO', 'PEDESTRE'])].copy()
    tv_grp = tv.groupby(['grupo', 'tipo_de_vitima']).size().unstack(fill_value=0)
    tv_pct = tv_grp.div(tv_grp.sum(axis=1), axis=0).multiply(100).round(1)
    print(tv_pct.sort_index().to_string())


# =============================================================================
# ETAPA 3 — ANÁLISE ECOLÓGICA MUNICIPAL (complementar)
# =============================================================================

def analisar_ecologico():

    sep('ANÁLISE ECOLÓGICA COMPLEMENTAR — NÍVEL MUNICIPAL', nivel=1)

    print("""
NOTA METODOLÓGICA
- Unidade de análise: município
- Desfecho: taxa de mortalidade por sinistros de trânsito
  (óbitos/100.000 hab/ano, média 2016–2025)
- Exposição: % de moradores em setores de alta e muito alta
  vulnerabilidade social (grupos 5 e 6 do IPVS 2022)
- Denominador: moradores em DPPO — Censo IBGE 2022
- Municípios com < 10 óbitos excluídos por instabilidade das taxas
- Estudo ecológico: associações refletem nível municipal,
  não individual (atenção à falácia ecológica)
""")

    # Carregar IPVS municipal
    df_raw = pd.read_excel('ipvs.xlsx', sheet_name='Moradores_ESP', header=None, skiprows=3)
    df_ipvs = df_raw.iloc[:, :8].copy()
    df_ipvs.columns = ['municipio_raw', 'total', 'g1_baixissima', 'g2_muito_baixa',
                       'g3_baixa', 'g4_media', 'g5_alta', 'g6_muito_alta']
    df_ipvs = df_ipvs[df_ipvs['municipio_raw'].notna()]
    df_ipvs = df_ipvs[~df_ipvs['municipio_raw'].astype(str).str.startswith('Fonte')]
    df_ipvs = df_ipvs[~df_ipvs['municipio_raw'].astype(str).str.startswith('35 -')]
    df_ipvs['cod_ibge'] = df_ipvs['municipio_raw'].astype(str).str[:7].astype(int)
    for col in ['total', 'g1_baixissima', 'g2_muito_baixa', 'g3_baixa',
                'g4_media', 'g5_alta', 'g6_muito_alta']:
        df_ipvs[col] = pd.to_numeric(df_ipvs[col], errors='coerce')
    df_ipvs['pct_alta_vulnerabilidade'] = (
        (df_ipvs['g5_alta'] + df_ipvs['g6_muito_alta']) / df_ipvs['total'] * 100
    ).round(1)
    df_ipvs = df_ipvs.reset_index(drop=True)

    # Carregar óbitos por município
    pes = pd.read_csv('dados/obitos_pessoas_2016-2025.csv', low_memory=False)
    obitos_mun = pes.groupby(['cod_ibge', 'municipio', 'regiao_administrativa']).size().reset_index(name='obitos')

    # Join
    df_join = obitos_mun.merge(
        df_ipvs[['cod_ibge', 'total', 'g5_alta', 'g6_muito_alta', 'pct_alta_vulnerabilidade']],
        on='cod_ibge', how='left'
    )
    df_join['taxa_obitos_100k'] = (df_join['obitos'] / df_join['total'] * 100000 / 10).round(1)

    # Filtro ≥ 10 óbitos
    df_analise = df_join[df_join['obitos'] >= 10].copy()
    print(f'Municípios incluídos (≥10 óbitos): {len(df_analise)} de {len(df_join)}')

    # ── B1. Descritiva por RM ─────────────────────────────────
    sep('B1. ESTATÍSTICAS DESCRITIVAS POR RM', nivel=2)
    rows_desc = []
    for rm in RMs:
        sub = df_analise[df_analise['regiao_administrativa'] == rm]
        if len(sub) == 0:
            continue
        rows_desc.append({
            'RM': rm.title(),
            'N municípios': len(sub),
            'Óbitos totais': int(sub['obitos'].sum()),
            'Taxa mediana (óbitos/100k/ano)': sub['taxa_obitos_100k'].median().round(1),
            'Taxa mín–máx': f"{sub['taxa_obitos_100k'].min():.1f}–{sub['taxa_obitos_100k'].max():.1f}",
            '% Alta vuln. mediana': sub['pct_alta_vulnerabilidade'].median().round(1),
            '% Alta vuln. mín–máx': f"{sub['pct_alta_vulnerabilidade'].min():.1f}–{sub['pct_alta_vulnerabilidade'].max():.1f}",
        })
    print(pd.DataFrame(rows_desc).to_string(index=False))

    # ── B2. Correlação Spearman por RM ────────────────────────
    sep('B2. CORRELAÇÃO DE SPEARMAN — TAXA DE ÓBITOS x % ALTA VULNERABILIDADE', nivel=2)
    rows_corr = []
    for rm in RMs:
        sub = df_analise[df_analise['regiao_administrativa'] == rm].dropna(
            subset=['taxa_obitos_100k', 'pct_alta_vulnerabilidade'])
        if len(sub) < 5:
            continue
        rho, p = stats.spearmanr(sub['taxa_obitos_100k'], sub['pct_alta_vulnerabilidade'])
        rows_corr.append({
            'RM': rm.title(),
            'N municípios': len(sub),
            'Spearman rho': round(rho, 3),
            'p-valor': round(p, 4),
            'Sig. (p<0,05)': 'sim' if p < 0.05 else 'não',
            'Direção': 'positiva' if rho > 0 else 'negativa',
            'Força': interpretar_r(rho),
        })
    print(pd.DataFrame(rows_corr).to_string(index=False))

    # Geral
    df_g = df_analise.dropna(subset=['taxa_obitos_100k', 'pct_alta_vulnerabilidade'])
    rho_g, p_g = stats.spearmanr(df_g['taxa_obitos_100k'], df_g['pct_alta_vulnerabilidade'])
    print(f'\nGeral (todas as RMs):')
    print(f'  N municípios: {len(df_g)}')
    print(f'  Spearman rho = {rho_g:.3f} | p = {p_g:.4f}')
    print(f'  Direção: {"positiva" if rho_g > 0 else "negativa"} | Força: {interpretar_r(rho_g)}')
    print(f'  Significativo: {"sim" if p_g < 0.05 else "não"} (p<0,05)')

    # ── B3. Top municípios ────────────────────────────────────
    sep('B3. TOP 10 MUNICÍPIOS — MAIOR TAXA DE ÓBITOS', nivel=2)
    print(df_analise.sort_values('taxa_obitos_100k', ascending=False)
          [['municipio', 'regiao_administrativa', 'obitos',
            'taxa_obitos_100k', 'pct_alta_vulnerabilidade']]
          .head(10).to_string(index=False))

    sep('B4. TOP 10 MUNICÍPIOS — MENOR TAXA DE ÓBITOS', nivel=2)
    print(df_analise.sort_values('taxa_obitos_100k', ascending=True)
          [['municipio', 'regiao_administrativa', 'obitos',
            'taxa_obitos_100k', 'pct_alta_vulnerabilidade']]
          .head(10).to_string(index=False))


# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

if __name__ == '__main__':

    # Etapa 1 — Spatial join
    joined_clean, sin = spatial_join()

    # Etapa 2 — Análise intraurbana
    pes_ipvs, pes = carregar_vitimas_ipvs(joined_clean)
    analisar_intraurbano(pes_ipvs)

    # Etapa 3 — Análise ecológica municipal (complementar)
    analisar_ecologico()

    print('\n\n' + '=' * 65)
    print('✅ ANÁLISE IPVS CONCLUÍDA')
    print('=' * 65)
