# Caracterização Epidemiológica dos Óbitos em Sinistros de Trânsito
## Regiões Metropolitanas do Estado de São Paulo — 2016–2025

Repositório de dados e código para análise epidemiológica dos óbitos em sinistros de trânsito nas regiões metropolitanas do Estado de São Paulo, com base nos dados do INFOSIGA-SP e do Índice Paulista de Vulnerabilidade Social (IPVS 2022).

---

### Autores

- Fabrício Leite Momenti
- Vitor Favali Kruger
- Thiago Rodrigues Araújo Calderan
- Gustavo Pereira Fraga

Divisão de Cirurgia de Trauma — Faculdade de Ciências Médicas, UNICAMP

---

### Fontes dos dados

| Dado | Fonte | URL |
|---|---|---|
| Sinistros de trânsito | INFOSIGA-SP | https://www.infosiga.sp.gov.br |
| IPVS — Shapefile setores censitários | SEADE/IBGE | https://repositorio.seade.gov.br |
| IPVS — Tabelas municipais | SEADE/IBGE | https://repositorio.seade.gov.br |
| Municípios do Estado de SP | SEADE | https://repositorio.seade.gov.br |

Os arquivos brutos do INFOSIGA-SP (>100 MB) não estão incluídos neste repositório. Devem ser baixados diretamente e colocados na raiz antes da primeira execução. O shapefile do IPVS também deve ser baixado e extraído em `ipvs_2022/`.

---

### Estrutura do repositório

```
infosiga-sp-obitos-rms/
├── dados/
│   ├── obitos_sinistros_2016-2025.csv
│   └── obitos_pessoas_2016-2025.csv
├── analise.py
├── analise_ipvs.py
└── README.md
```

---

### Como reproduzir

**Pré-requisitos**

```bash
pip3 install pandas geopandas shapely pyproj scipy openpyxl
```

**Passos**

1. Clone o repositório:
```bash
git clone https://github.com/fabriciolm225/infosiga-sp-obitos-rms.git
cd infosiga-sp-obitos-rms
```

2. Baixe os arquivos do INFOSIGA-SP e coloque na raiz: `sinistros_2015-2021.csv`, `sinistros_2022-2026.csv`, `pessoas_2015-2021.csv`, `pessoas_2022-2026.csv`

3. Baixe o shapefile IPVS 2022 do SEADE, extraia e coloque em `ipvs_2022/`: `IPVS_2022.shp`, `IPVS_2022.dbf`, `IPVS_2022.shx`, `IPVS_2022.prj`

4. Baixe o `ipvs.xlsx` do SEADE e coloque na raiz.

5. Execute em ordem:
```bash
python3 analise.py
python3 analise_ipvs.py
```

---

### Recorte analítico

| Parâmetro | Valor |
|---|---|
| Período | 2016–2025 |
| Desfecho | Óbitos em sinistros de trânsito |
| Regiões | RMSP, Campinas, Baixada Santista, Sorocaba, São José dos Campos |
| Sinistros fatais | 36.425 |
| Vítimas fatais | 38.367 |
| Sinistros georreferenciados | 32.168 (88,3%) |

---

### Decisões metodológicas

- **Período:** 2016–2025. O INFOSIGA registrava apenas óbitos em 2015–2018; a série completa começa em 2019. Como o foco é exclusivamente em óbitos, todos os anos a partir de 2016 são válidos.
- **Duplicatas:** 1.436 linhas 100% idênticas removidas da tabela `pessoas`.
- **Tabela veículos:** não utilizada — variáveis de interesse já presentes em `pessoas`.
- **Profissão:** normalizada por `.str.upper().str.strip()`.
- **Grau de instrução e nacionalidade:** 100% nulos para fatais no INFOSIGA — excluídos.
- **Populações municipais:** moradores em DPPO, Censo IBGE 2022 (IPVS/SEADE).
- **Corte mínimo municipal:** municípios com menos de 10 óbitos excluídos da análise ecológica.
- **IPVS — spatial join:** cada sinistro georreferenciado recebeu o grupo IPVS do setor censitário onde ocorreu. O IPVS caracteriza o local do sinistro, não a vítima.
- **IPVS — temporalidade:** índice de 2022 aplicado a sinistros de 2016–2025 — limitação reconhecida.
- **2026:** excluído por ser ano incompleto.

---

### Análises disponíveis

**`analise.py` — Epidemiologia dos óbitos**

Bloco A — Sinistros fatais: tendência anual, tipo de sinistro, tipo de via, turno, dia da semana, mês, circunscrição, administração, tipo de local, top municípios e subtipos binários.

Bloco B — Vítimas fatais: tendência anual, taxa de mortalidade por 100k hab, tipo de veículo, tipo de vítima, sexo, faixa etária, local do óbito, tempo sinistro-óbito, local da via e profissão.

**`analise_ipvs.py` — Vulnerabilidade social**

Análise intraurbana (setor censitário): distribuição de óbitos por grupo IPVS (1–6), por RM e por ano; correlação de Spearman; perfil das vítimas por grupo IPVS.

Análise ecológica municipal (complementar): taxa de mortalidade por município cruzada com % de alta+muito alta vulnerabilidade; correlação de Spearman por RM e geral.

---

### Licença

MIT. Dados de domínio público: INFOSIGA-SP (Governo do Estado de SP) e IPVS (SEADE/IBGE).
