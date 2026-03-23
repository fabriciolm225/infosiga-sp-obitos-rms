# Caracterização Epidemiológica dos Óbitos em Sinistros de Trânsito
## Regiões Metropolitanas do Estado de São Paulo — 2016–2025

Repositório de dados e código para análise epidemiológica dos óbitos em sinistros de trânsito nas regiões metropolitanas do Estado de São Paulo, com base nos dados do INFOSIGA-SP.

---

### Autores

- Fabrício Leite Momenti
- Vitor Favali Kruger
- Thiago Rodrigues Araújo Calderan
- Gustavo Pereira Fraga

Divisão de Cirurgia de Trauma — Faculdade de Ciências Médicas, UNICAMP

---

### Fonte dos dados

Os dados utilizados são de acesso público e disponibilizados pelo **Sistema de Informações Gerenciais de Acidentes de Trânsito do Estado de São Paulo (INFOSIGA-SP)**.

- URL: https://www.infosiga.sp.gov.br
- Tabelas utilizadas: `sinistros` e `pessoas`
- Período bruto disponível: 2015–2026
- Arquivos baixados: `sinistros_2015-2021.csv`, `sinistros_2022-2026.csv`, `pessoas_2015-2021.csv`, `pessoas_2022-2026.csv`

Os arquivos brutos originais não estão incluídos neste repositório por excederem o limite de tamanho do GitHub (>100 MB). Devem ser baixados diretamente pelo INFOSIGA-SP e colocados na raiz do repositório antes de rodar o script pela primeira vez.

---

### Estrutura do repositório

```
📁 infosiga-rms-sp/
├── dados/
│   ├── obitos_sinistros_2016-2025.csv   ← gerado automaticamente na 1ª execução
│   └── obitos_pessoas_2016-2025.csv     ← gerado automaticamente na 1ª execução
├── analise.py                           ← script completo de análise
└── README.md
```

---

### Como reproduzir

**Pré-requisitos**

```bash
pip3 install pandas
```

**Passos**

1. Clone o repositório:
```bash
git clone https://github.com/<usuario>/infosiga-rms-sp.git
cd infosiga-rms-sp
```

2. Baixe os 4 arquivos CSV do INFOSIGA-SP e coloque na raiz do repositório:
   - `sinistros_2015-2021.csv`
   - `sinistros_2022-2026.csv`
   - `pessoas_2015-2021.csv`
   - `pessoas_2022-2026.csv`

3. Execute o script:
```bash
python3 analise.py
```

Na primeira execução, os CSVs filtrados são gerados automaticamente em `dados/`. Nas execuções seguintes, os dados brutos originais não são mais necessários.

---

### Recorte analítico

| Parâmetro | Valor |
|---|---|
| Período | 2016–2025 |
| Desfecho | Óbitos (sinistros fatais) |
| Unidade geográfica | Região Metropolitana |
| Regiões incluídas | RMSP, Campinas, Baixada Santista, Sorocaba, São José dos Campos |

---

### Decisões metodológicas

- **Período:** 2016–2025. O sistema INFOSIGA registrava apenas óbitos em 2015–2018; a série completa (incluindo não fatais) começa em 2019. Como este estudo foca exclusivamente em óbitos, todos os anos a partir de 2016 são válidos para comparação.
- **Duplicatas:** 1.436 linhas com registros 100% idênticos foram removidas da tabela `pessoas` (provável erro de processamento do sistema). As 5 duplicatas de `id_veiculo` na tabela `veículos` foram mantidas por apresentarem campos conflitantes.
- **Tabela veículos:** não utilizada. As variáveis de interesse (tipo de veículo da vítima) já estão disponíveis em `pessoas` via `tipo_veiculo_vitima`.
- **Profissão:** normalizada por conversão para maiúsculas e remoção de espaços para corrigir inconsistências de capitalização entre os dois arquivos de período.
- **Grau de instrução e nacionalidade:** ambos os campos são 100% nulos para vítimas fatais no INFOSIGA — excluídos das análises com nota metodológica.
- **Populações:** Censo IBGE 2022.
- **2026:** excluído por ser ano incompleto no momento do download dos dados.

---

### Blocos de análise

**Bloco A — Sinistros fatais**
Tendência anual, tipo de sinistro, tipo de via, turno, dia da semana, mês, circunscrição, administração, tipo de local, municípios com maior frequência e subtipos de sinistro.

**Bloco B — Vítimas fatais**
Tendência anual, taxa de mortalidade por 100 mil habitantes, tipo de veículo, tipo de vítima, sexo, faixa etária, local do óbito, tempo sinistro-óbito, local da via e profissão.

---

### Licença

Código disponibilizado sob licença MIT. Os dados são de domínio público (INFOSIGA-SP / Governo do Estado de São Paulo).
