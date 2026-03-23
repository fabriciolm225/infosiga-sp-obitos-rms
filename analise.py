# =============================================================================
# CARACTERIZAÇÃO EPIDEMIOLÓGICA DOS ÓBITOS EM SINISTROS DE TRÂNSITO
# Regiões Metropolitanas do Estado de São Paulo — 2016–2025
# Fonte: INFOSIGA-SP (https://www.infosiga.sp.gov.br)
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
#   - Período: 2016–2025 (década completa)
#   - Desfecho: óbitos (gravidade_lesao == 'FATAL' em pessoas;
#               tipo_registro == 'SINISTRO FATAL' em sinistros)
#   - Recorte geográfico: 5 Regiões Metropolitanas do Estado de SP
#     (campo regiao_administrativa do INFOSIGA)
#   - 1.436 duplicatas exatas removidas da tabela pessoas
#   - Tabela veículos não utilizada (variáveis de interesse já presentes
#     em pessoas via tipo_veiculo_vitima)
#   - grau_de_instrucao: 100% nulo para fatais — excluído das análises
#   - nacionalidade: 100% nulo para fatais — excluído das análises
#   - profissao: normalizada por str.upper().str.strip()
#   - Populações: IBGE Censo 2022
#
# ARQUIVOS DE ENTRADA (originais do INFOSIGA)
#   sinistros_2015-2021.csv
#   sinistros_2022-2026.csv
#   pessoas_2015-2021.csv
#   pessoas_2022-2026.csv
#
# ARQUIVOS DE SAÍDA (gerados na Etapa 1)
#   dados/obitos_sinistros_2016-2025.csv
#   dados/obitos_pessoas_2016-2025.csv
#
# USO
#   1. Coloque os 4 CSVs originais na mesma pasta deste script
#   2. Execute: python3 analise.py
#   3. Na primeira execução, os CSVs filtrados são gerados em dados/
#   4. Nas execuções seguintes, os CSVs filtrados são lidos diretamente
# =============================================================================

import pandas as pd
import os

# =============================================================================
# CONFIGURAÇÕES GLOBAIS
# =============================================================================

RMs = [
    'METROPOLITANA DE SÃO PAULO',
    'CAMPINAS',
    'BAIXADA SANTISTA',
    'SOROCABA',
    'SÃO JOSÉ DOS CAMPOS',
]

POPULACAO_RM = {
    'METROPOLITANA DE SÃO PAULO': 21571281,
    'CAMPINAS':                    3656363,
    'BAIXADA SANTISTA':            1861800,
    'SOROCABA':                    1643766,
    'SÃO JOSÉ DOS CAMPOS':         1354884,
}

ANO_INICIO = 2016
ANO_FIM    = 2025
N_ANOS     = ANO_FIM - ANO_INICIO + 1

ORDEM_DIA = [
    'Segunda-feira', 'Terça-feira', 'Quarta-feira',
    'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo'
]

DIR_DADOS  = 'dados'
PATH_SIN   = os.path.join(DIR_DADOS, 'obitos_sinistros_2016-2025.csv')
PATH_PES   = os.path.join(DIR_DADOS, 'obitos_pessoas_2016-2025.csv')


# =============================================================================
# FUNÇÕES AUXILIARES
# =============================================================================

def ler_csv(path, nrows=None):
    """Lê CSV tentando diferentes encodings e separadores."""
    for enc in ['latin1', 'utf-8']:
        for sep in [';', ',']:
            try:
                return pd.read_csv(path, encoding=enc, sep=sep,
                                   low_memory=False, nrows=nrows)
            except Exception:
                continue
    raise ValueError(f"Não foi possível ler: {path}")


def sep(titulo, nivel=1):
    """Imprime separador de seção formatado."""
    if nivel == 1:
        print('\n' + '█' * 65)
        print(f'  {titulo}')
        print('█' * 65)
    else:
        print(f'\n── {titulo} ──')


def nd_info(df, col):
    """Retorna string com contagem e % de não disponíveis/nulos."""
    total = len(df)
    nd = (df[col].isna() | (df[col].astype(str).str.strip() == 'NAO DISPONIVEL')).sum()
    return f'  [NÃO DISPONÍVEL: {nd:,} / {nd/total*100:.1f}%]'


# =============================================================================
# ETAPA 1 — PREPARAR CSVs FILTRADOS
# =============================================================================

def preparar_dados():
    """
    Lê os 4 CSVs brutos do INFOSIGA, aplica filtros e salva os
    CSVs filtrados em dados/.
    Executado apenas se os arquivos filtrados ainda não existirem.
    """
    print('\n' + '=' * 65)
    print('ETAPA 1 — PREPARANDO CSVs FILTRADOS')
    print('=' * 65)

    os.makedirs(DIR_DADOS, exist_ok=True)

    # ── Carregar e concatenar sinistros ──────────────────────────
    print('\nCarregando sinistros...')
    s1 = ler_csv('sinistros_2015-2021.csv')
    s2 = ler_csv('sinistros_2022-2026.csv')
    s1['periodo_arquivo'] = '2015-2021'
    s2['periodo_arquivo'] = '2022-2026'
    sinistros = pd.concat([s1, s2], ignore_index=True)
    print(f'  Total bruto: {len(sinistros):,} sinistros')

    # ── Carregar e concatenar pessoas ────────────────────────────
    print('Carregando pessoas...')
    p1 = ler_csv('pessoas_2015-2021.csv')
    p2 = ler_csv('pessoas_2022-2026.csv')
    p1['periodo_arquivo'] = '2015-2021'
    p2['periodo_arquivo'] = '2022-2026'
    pessoas = pd.concat([p1, p2], ignore_index=True)
    print(f'  Total bruto: {len(pessoas):,} pessoas')

    # ── Remover duplicatas exatas em pessoas ─────────────────────
    pessoas = pessoas.drop_duplicates()
    print(f'  Após remoção de duplicatas: {len(pessoas):,} pessoas')

    # ── Normalizar profissão ─────────────────────────────────────
    pessoas['profissao'] = pessoas['profissao'].str.upper().str.strip()

    # ── Filtrar: óbitos + RMs + período ─────────────────────────
    sin_filtrado = sinistros[
        (sinistros['tipo_registro'] == 'SINISTRO FATAL') &
        (sinistros['regiao_administrativa'].isin(RMs)) &
        (sinistros['ano_sinistro'].between(ANO_INICIO, ANO_FIM))
    ].copy()

    pes_filtrado = pessoas[
        (pessoas['gravidade_lesao'] == 'FATAL') &
        (pessoas['regiao_administrativa'].isin(RMs)) &
        (pessoas['ano_sinistro'].between(ANO_INICIO, ANO_FIM))
    ].copy()

    print(f'\nApós filtros (óbitos, 5 RMs, {ANO_INICIO}–{ANO_FIM}):')
    print(f'  sinistros fatais: {len(sin_filtrado):,}')
    print(f'  vítimas fatais:   {len(pes_filtrado):,}')

    # ── Salvar ───────────────────────────────────────────────────
    sin_filtrado.to_csv(PATH_SIN, index=False, encoding='utf-8')
    pes_filtrado.to_csv(PATH_PES, index=False, encoding='utf-8')

    tam_sin = os.path.getsize(PATH_SIN) / (1024 * 1024)
    tam_pes = os.path.getsize(PATH_PES) / (1024 * 1024)
    print(f'\nArquivos salvos em {DIR_DADOS}/:')
    print(f'  obitos_sinistros_2016-2025.csv  {tam_sin:.1f} MB')
    print(f'  obitos_pessoas_2016-2025.csv    {tam_pes:.1f} MB')


# =============================================================================
# ETAPA 2 — CARREGAR CSVs FILTRADOS
# =============================================================================

def carregar_dados():
    """Carrega os CSVs filtrados e retorna sinistros e pessoas."""
    print('\n' + '=' * 65)
    print('ETAPA 2 — CARREGANDO CSVs FILTRADOS')
    print('=' * 65)
    sin = pd.read_csv(PATH_SIN, low_memory=False)
    pes = pd.read_csv(PATH_PES, low_memory=False)
    print(f'  Sinistros fatais: {len(sin):,} | Vítimas fatais: {len(pes):,}')
    return sin, pes


# =============================================================================
# ETAPA 3 — ANÁLISE COMPLETA
# =============================================================================

def analisar(sin, pes):

    print('\n' + '=' * 65)
    print('ETAPA 3 — ANÁLISE EPIDEMIOLÓGICA')
    print(f'Óbitos em Sinistros de Trânsito — RMs de SP — {ANO_INICIO}–{ANO_FIM}')
    print('=' * 65)
    print(f'\nBase: {len(sin):,} sinistros fatais | {len(pes):,} vítimas fatais')
    print(f'Regiões: {", ".join(RMs)}')

    # ══════════════════════════════════════════════════════════════
    # BLOCO A — SINISTROS FATAIS
    # ══════════════════════════════════════════════════════════════
    sep('BLOCO A — SINISTROS FATAIS', nivel=1)

    sep('A1. SINISTROS FATAIS POR ANO E RM', nivel=2)
    print(sin.groupby(['ano_sinistro', 'regiao_administrativa'])
          .size().unstack(fill_value=0).to_string())

    sep('A2. TIPO DE SINISTRO PRIMÁRIO POR RM', nivel=2)
    print(nd_info(sin, 'tp_sinistro_primario'))
    print(sin.groupby(['regiao_administrativa', 'tp_sinistro_primario'])
          .size().unstack(fill_value=0).to_string())

    sep('A3. TIPO DE SINISTRO PRIMÁRIO POR ANO', nivel=2)
    print(sin.groupby(['ano_sinistro', 'tp_sinistro_primario'])
          .size().unstack(fill_value=0).to_string())

    sep('A4. TIPO DE VIA POR RM', nivel=2)
    print(nd_info(sin, 'tipo_via'))
    fat_via = sin.groupby(['regiao_administrativa', 'tipo_via']).size().unstack(fill_value=0)
    fat_via['TOTAL'] = fat_via.sum(axis=1)
    print(fat_via.to_string())

    sep('A5. TIPO DE VIA POR ANO', nivel=2)
    print(sin.groupby(['ano_sinistro', 'tipo_via'])
          .size().unstack(fill_value=0).to_string())

    sep('A6. TURNO POR RM', nivel=2)
    print(nd_info(sin, 'turno'))
    print(sin.groupby(['regiao_administrativa', 'turno'])
          .size().unstack(fill_value=0).to_string())

    sep('A7. TURNO POR ANO', nivel=2)
    print(sin.groupby(['ano_sinistro', 'turno'])
          .size().unstack(fill_value=0).to_string())

    sep('A8. DIA DA SEMANA POR RM', nivel=2)
    dia_rm = sin.groupby(['regiao_administrativa', 'dia_da_semana']).size().unstack(fill_value=0)
    print(dia_rm.reindex(columns=[c for c in ORDEM_DIA if c in dia_rm.columns]).to_string())

    sep('A9. DIA DA SEMANA POR ANO', nivel=2)
    dia_ano = sin.groupby(['ano_sinistro', 'dia_da_semana']).size().unstack(fill_value=0)
    print(dia_ano.reindex(columns=[c for c in ORDEM_DIA if c in dia_ano.columns]).to_string())

    sep('A10. MÊS POR RM', nivel=2)
    print(sin.groupby(['regiao_administrativa', 'mes_sinistro'])
          .size().unstack(fill_value=0).to_string())

    sep('A11. MÊS POR ANO', nivel=2)
    print(sin.groupby(['ano_sinistro', 'mes_sinistro'])
          .size().unstack(fill_value=0).to_string())

    sep('A12. CIRCUNSCRIÇÃO POR RM', nivel=2)
    print(nd_info(sin, 'circunscricao'))
    print(sin.groupby(['regiao_administrativa', 'circunscricao'])
          .size().unstack(fill_value=0).to_string())

    sep('A13. ADMINISTRAÇÃO POR RM', nivel=2)
    print(nd_info(sin, 'administracao'))
    print(sin.groupby(['regiao_administrativa', 'administracao'])
          .size().unstack(fill_value=0).to_string())

    sep('A14. TIPO LOCAL POR RM', nivel=2)
    print(nd_info(sin, 'tipo_local'))
    print(sin.groupby(['regiao_administrativa', 'tipo_local'])
          .size().unstack(fill_value=0).to_string())

    sep('A15. TOP 20 MUNICÍPIOS — SINISTROS FATAIS', nivel=2)
    print(sin.groupby(['municipio', 'regiao_administrativa'])
          .size().reset_index(name='n')
          .sort_values('n', ascending=False).head(20).to_string(index=False))

    sep('A16. SUBTIPOS DE SINISTRO (colunas binárias)', nivel=2)
    cols_tp = [c for c in sin.columns if c.startswith('tp_sinistro_')
               and c != 'tp_sinistro_primario']
    for col in cols_tp:
        total_s = (sin[col] == 'S').sum()
        nd_c    = sin[col].isna().sum()
        print(f'  {col}: {total_s:,} marcados S | nulos: {nd_c:,} ({nd_c/len(sin)*100:.1f}%)')

    # ══════════════════════════════════════════════════════════════
    # BLOCO B — VÍTIMAS FATAIS
    # ══════════════════════════════════════════════════════════════
    sep('BLOCO B — VÍTIMAS FATAIS', nivel=1)

    sep('B1. VÍTIMAS FATAIS POR ANO E RM', nivel=2)
    print(pes.groupby(['ano_sinistro', 'regiao_administrativa'])
          .size().unstack(fill_value=0).to_string())

    sep('B2. TAXA DE MORTALIDADE POR 100K HAB (média anual — período completo)', nivel=2)
    vt = pes.groupby('regiao_administrativa').size()
    for rm, total in vt.items():
        if rm in POPULACAO_RM:
            taxa = (total / N_ANOS / POPULACAO_RM[rm]) * 100000
            print(f'  {rm}: {taxa:.1f} óbitos/100k hab/ano '
                  f'(pop. IBGE 2022: {POPULACAO_RM[rm]:,})')

    sep('B3. TIPO DE VEÍCULO DA VÍTIMA POR RM', nivel=2)
    print(nd_info(pes, 'tipo_veiculo_vitima'))
    fat_v = pes.groupby(['regiao_administrativa', 'tipo_veiculo_vitima']).size().unstack(fill_value=0)
    fat_v['TOTAL'] = fat_v.sum(axis=1)
    for col in ['MOTOCICLETA', 'AUTOMOVEL', 'BICICLETA', 'CAMINHAO', 'ONIBUS']:
        if col in fat_v.columns:
            fat_v[f'PCT_{col}'] = (fat_v[col] / fat_v['TOTAL'] * 100).round(1)
    print(fat_v.to_string())

    sep('B4. TIPO DE VEÍCULO DA VÍTIMA POR ANO', nivel=2)
    print(pes.groupby(['ano_sinistro', 'tipo_veiculo_vitima'])
          .size().unstack(fill_value=0).to_string())

    sep('B5. TIPO DE VÍTIMA (CONDUTOR/PASSAGEIRO/PEDESTRE) POR RM', nivel=2)
    print(nd_info(pes, 'tipo_de_vitima'))
    tv = pes.groupby(['regiao_administrativa', 'tipo_de_vitima']).size().unstack(fill_value=0)
    tv['TOTAL'] = tv.sum(axis=1)
    print(tv.to_string())

    sep('B6. TIPO DE VÍTIMA POR ANO', nivel=2)
    print(pes.groupby(['ano_sinistro', 'tipo_de_vitima'])
          .size().unstack(fill_value=0).to_string())

    sep('B7. SEXO POR RM', nivel=2)
    print(nd_info(pes, 'sexo'))
    sx = pes.groupby(['regiao_administrativa', 'sexo']).size().unstack(fill_value=0)
    sx['TOTAL'] = sx.sum(axis=1)
    sx['PCT_MASC'] = (sx['MASCULINO'] / sx['TOTAL'] * 100).round(1)
    print(sx.to_string())

    sep('B8. SEXO POR ANO', nivel=2)
    print(pes.groupby(['ano_sinistro', 'sexo'])
          .size().unstack(fill_value=0).to_string())

    sep('B9. FAIXA ETÁRIA — TODAS AS RMs', nivel=2)
    print(nd_info(pes, 'faixa_etaria_demografica'))
    fe = pes[pes['faixa_etaria_demografica'] != 'NAO DISPONIVEL']
    fe_counts = fe['faixa_etaria_demografica'].value_counts().sort_index()
    for k, v in fe_counts.items():
        print(f'  {k}: {v:,} ({v/fe_counts.sum()*100:.1f}%)')

    sep('B10. FAIXA ETÁRIA POR RM', nivel=2)
    print(pes.groupby(['regiao_administrativa', 'faixa_etaria_demografica'])
          .size().unstack(fill_value=0).to_string())

    sep('B11. FAIXA ETÁRIA POR ANO', nivel=2)
    print(pes.groupby(['ano_sinistro', 'faixa_etaria_demografica'])
          .size().unstack(fill_value=0).to_string())

    sep('B12. FAIXA ETÁRIA LEGAL POR RM', nivel=2)
    print(pes.groupby(['regiao_administrativa', 'faixa_etaria_legal'])
          .size().unstack(fill_value=0).to_string())

    sep('B13. TIPO DE VIA POR RM', nivel=2)
    print(pes.groupby(['regiao_administrativa', 'tipo_via'])
          .size().unstack(fill_value=0).to_string())

    sep('B14. LOCAL DO ÓBITO POR RM', nivel=2)
    print(nd_info(pes, 'local_obito'))
    print(pes.groupby(['regiao_administrativa', 'local_obito'])
          .size().unstack(fill_value=0).to_string())

    sep('B15. LOCAL DO ÓBITO POR ANO', nivel=2)
    print(pes.groupby(['ano_sinistro', 'local_obito'])
          .size().unstack(fill_value=0).to_string())

    sep('B16. TEMPO SINISTRO-ÓBITO (dias)', nivel=2)
    print(nd_info(pes, 'tempo_sinistro_obito'))
    tso = pes['tempo_sinistro_obito'].dropna()
    print(tso.describe().round(1).to_string())
    print(f'\n  Óbito no local (0 dias):      {(tso==0).sum():,} ({(tso==0).sum()/len(tso)*100:.1f}%)')
    print(f'  Óbito em até 24h (≤1 dia):    {(tso<=1).sum():,} ({(tso<=1).sum()/len(tso)*100:.1f}%)')
    print(f'  Óbito em até 30 dias:         {(tso<=30).sum():,} ({(tso<=30).sum()/len(tso)*100:.1f}%)')

    sep('B17. LOCAL DA VIA POR RM', nivel=2)
    print(nd_info(pes, 'local_via'))
    print(pes.groupby(['regiao_administrativa', 'local_via'])
          .size().unstack(fill_value=0).to_string())

    sep('B18. PROFISSÃO — TOP 30 (todas as RMs)', nivel=2)
    print(nd_info(pes, 'profissao'))
    print(pes['profissao'].value_counts().head(30).to_string())

    sep('B19. PROFISSÃO — TOP 30 (vítimas fatais por RM)', nivel=2)
    for rm in RMs:
        print(f'\n  {rm}:')
        sub = pes[pes['regiao_administrativa'] == rm]
        print(sub['profissao'].value_counts().head(10).to_string())

    sep('B20. CAMPOS EXCLUÍDOS — NOTA METODOLÓGICA', nivel=2)
    print('  Os campos abaixo não são preenchidos pelo INFOSIGA para vítimas fatais')
    print('  e foram excluídos das análises:')
    print('  - grau_de_instrucao: 100.0% nulo para fatais')
    print('  - nacionalidade:     100.0% nulo para fatais')

    print('\n\n' + '=' * 65)
    print('✅ ANÁLISE CONCLUÍDA')
    print('=' * 65)


# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

if __name__ == '__main__':

    # Gerar CSVs filtrados se ainda não existirem
    if not os.path.exists(PATH_SIN) or not os.path.exists(PATH_PES):
        preparar_dados()
    else:
        print(f'\nCSVs filtrados já existem em {DIR_DADOS}/ — pulando Etapa 1.')
        print('Para regenerar, delete os arquivos em dados/ e rode novamente.')

    # Carregar e analisar
    sin, pes = carregar_dados()
    analisar(sin, pes)
