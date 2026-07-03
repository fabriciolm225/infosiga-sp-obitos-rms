# Parte II.5 — Evidências epidemiológicas e risco cardiovascular

> **Prof. Thiago Quinaglia A. C. Silva — Pós-Graduação em Farmacologia, FCM-Unicamp**
>
> **Fio condutor (evidência → decisão):** esta é a aula "âncora" de MBE em cardiologia.
> Percorre a **hierarquia da evidência**, o **risco atribuível**, os **critérios de
> Bradford-Hill** (aplicados ao **sódio**), as **grandes coortes e ensaios** (Framingham,
> INTERHEART, ELSA-Brasil, 4S, JUPITER, SPRINT, EMPA-REG) e o conceito de **desfechos duros
> vs. substitutos** — sempre ligando à **decisão** (diretrizes SBC, casos clínicos).

---

## 1. Hierarquia da evidência e desenhos (revisão aplicada)

Ver `01-fundamentos-mbe.md` §2–3. Resumo com exemplos CV:

| Nível | Desenho | Exemplo CV | Melhor para |
|:---:|---|---|---|
| 1 | Meta-análise / RS | CTT (estatinas), BPLTTC | Síntese, efeitos modestos |
| 2 | ECR | 4S, SPRINT, EMPA-REG, JUPITER | **Causalidade / eficácia** |
| 3 | Coorte prospectiva | **Framingham, ARIC, MESA, ELSA-Brasil** | Incidência, fatores de risco |
| 4 | Caso-controle | **INTERHEART** | Doenças raras, rápido |
| 5 | Transversal/ecológico | — | Gerar hipóteses |

---

## 2. Risco atribuível (RA) e derivados ⭐

$$\text{RA} = \text{Risco}_{\text{expostos}} - \text{Risco}_{\text{não expostos}}$$

- **RAP (Risco Atribuível Populacional):** fração do total de casos que sumiria se a
  exposição fosse removida → **medida de impacto para saúde pública**.
- **RRA:** o RA aplicado a ensaios (controle − intervenção).
- **NNT = 1/RRA** (evitar 1 evento) | **NNH = 1/ARI** (causar 1 dano).

> ⚠️ Diferente do **RR** (força de associação), o RA/RAP dependem da **prevalência da
> exposição** e da **incidência** na população — medem **impacto**, não só associação.
> **Sempre reporte RRA e NNT** — o RRR isolado **superestima** o benefício.

### Exemplo do sódio (Yuan Ma et al., NEJM 2022)

| Ingesta | Risco DCV (IAM/AVC) |
|---|:---:|
| 5 g/dia (exposto) | 24% |
| 4 g/dia (não exposto) | 8% |

- **RR** = 24%/8% = **3**.
- **RA atribuível** = 24% − 8% = **16%** (na aula, exemplo com 26−8 = 18%).
- **Fração atribuível** = RA/Risco exposto = 18%/24% ≈ **75%**.
- **NNH** = 1/RA = 1/0,18 ≈ **6** (a cada ~6 pessoas na maior ingesta, 1 evento a mais).

---

## 3. Critérios de Bradford-Hill aplicados ao sódio ⭐

(Ver tabela completa em `01-fundamentos-mbe.md` §8.)

| Critério | Evidência sobre sódio |
|---|---|
| **Plausibilidade biológica** | Sal ↑ sódio plasmático ↑ PA (He F et al., *Hypertension* 2005) |
| **Temporalidade** | RCTs de dieta hipossódica reduzem a PA (a intervenção precede a queda) |
| **Gradiente biológico** | Estudo populacional UK: mais sódio, mais PA (dose-resposta) |
| **Especificidade** | RCT de efeito **agudo** de dieta hipossódica (Gupta D. et al., *JAMA* 2023) |
| **Consistência** | > 30 coortes mostram relação (a maioria **linear**) sódio ↔ risco CV/morte |

**Meta-análise de RCTs** (Huang L et al., *BMJ* 2020): efeito de curto e longo prazo da dieta
com baixo sódio reduzindo a PA — reforça **temporalidade** e **plausibilidade**.

### A controvérsia da curva "J/U" e o viés
- Algumas coortes recentes sugeriram relação em **"J" ou "U"** (pouco sal também faria mal).
- **Explicação por vieses:**
  - **Causalidade reversa:** esses estudos incluíam pacientes **já com DCV/alto risco** —
    pacientes muito doentes **comem menos** (menos sal) *ou* já receberam recomendação de
    reduzir sal → parece que "pouco sal → mais doença", quando é a doença que causa o baixo
    consumo.
  - **Viés de diluição:** usar **uma única** medida (ruidosa) de sódio urinário em vez da
    **média de longo prazo** (múltiplas coletas de 24h) atenua/distorce a associação
    (Engberink RHG et al., *Circulation* 2017). A coleta seriada e longitudinal mostra
    relação **linear** (He et al., *JACC* 2020; Trials of Hypertension Prevention, 20 anos).

> **Decisão/saúde pública:** a evidência integrada (Hill) sustenta **reduzir o sódio** para
> baixar PA e risco CV; as curvas "J/U" são majoritariamente **artefato de viés**.

---

## 4. Desfechos duros vs. substitutos (surrogate) ⭐

(Ver `01-fundamentos-mbe.md` §7.)

- **Duros:** morte CV, IAM não fatal, AVC não fatal, hospitalização por ICC → **Classe I /
  Nível A**.
- **Substitutos:** LDL-c, PCR-us, PA, HbA1c, EIM → rápidos/baratos, mas **risco de
  dissociação** (ex.: **torcetrapib** ↑ HDL mas ↑ mortalidade). Só surrogate → **máx. IIa/IIb**.
- **Continuum aterosclerótico:** PA/PCR (10 anos) → microalbuminúria/calcificação (20–30
  anos) → IAM/AVC/isquemia de MMII (40 anos).
- **Pergunta-chave ao ler um trial:** *o desfecho primário é duro ou substituto?*

---

## 5. As grandes coortes e ensaios (linha do tempo) ⭐

### Coortes / observacionais

| Estudo | Ano | Desenho | Legado |
|---|:---:|---|---|
| **Seven Countries** (Ancel Keys) | 1958 | Coorte/ecológico | Hipótese lipídica; gordura saturada ↔ colesterol ↔ mortalidade DAC; dieta mediterrânea |
| **Framingham** | 1948–hoje | **Coorte prospectiva** (5.209, avaliações bienais, 3 gerações) | Cunhou **"risk factor"**; base do **Escore de Framingham**; identificou HAS, tabagismo, dislipidemia, DM, sedentarismo como FR independentes |
| **MRFIT** | 1973–82 | Intervenção/coorte (360.000 triados) | Relação **contínua** entre PA, colesterol e mortalidade CV |
| **Nurses' Health Study** | 1976 | Coorte (121.700 enfermeiras) | Risco CV **feminino** (ACO, TRH, dieta) — população antes sub-representada |
| **INTERHEART** | 2004 | **Caso-controle** (52 países, 15.152 casos IAM / 14.820 controles) | **9 fatores modificáveis explicam > 90% do risco atribuível** de IAM, independente de etnia/geografia |
| **ELSA-Brasil** | 2008– | **Coorte prospectiva** (15.105 servidores, 6 instituições) | **Representatividade étnica brasileira**; recalibrou o Framingham para o Brasil; incorpora determinantes sociais |

**Os 9 fatores do INTERHEART:** (1) dislipidemia (ApoB/ApoA1 ↑), (2) tabagismo, (3) HAS, (4)
diabetes, (5) obesidade abdominal, (6) fatores psicossociais, (7) baixo consumo de
frutas/vegetais, (8) inatividade física, (9) álcool (protetor em consumo moderado).

### Ensaios clínicos (ECR) — tabela de prova ⭐

| Estudo | Ano | População / foco | Desfecho | Métrica | Ponto crítico |
|---|:---:|---|---|---|---|
| **4S** (sinvastatina) | 1994 | DAC estabelecida + hipercolesterolemia (**prevenção secundária**), ~4.400 | **Duros:** mortalidade total, eventos coronarianos | **RRA ~8% / NNT 12** (5 anos) | 1º a mostrar ↓ mortalidade total com estatina. **Classe I/A.** Pop. masculina/caucasiana → validade externa moderada |
| **JUPITER** (rosuvastatina) | 2008 | LDL normal (<130) + **PCR-us ≥ 2** (prevenção primária), ~17.800, 26 países | Composto duro (IAM, AVC, revasc., angina instável, morte CV) | **RRA ~1,2% / NNT 95** (2 anos) | **PCR-us = surrogate**; **interrompido precocemente (~1,9 ano)** → superestima benefício; patrocínio AstraZeneca (viés de publicação) |
| **SPRINT** | 2015 | Hipertensos **sem diabetes**; PAS-alvo <120 vs. <140 | Composto CV + morte CV (**duros**) | **RRA ~1,6% / NNT 61** (3 anos) | **Medida automática (AOBP)** → alvo real ≈ 130 mmHg no método convencional; **exclui diabéticos** (generalização); interrompido cedo (~3,3 anos) |
| **EMPA-REG OUTCOME** (empagliflozina, iSGLT2) | 2015 | DM2 + **DCV estabelecida** (99%), ~7.020 | **3P-MACE** (morte CV + IAM não fatal + AVC não fatal) | **RRA ~2,2% / NNT 45** (3 anos) | 1º antidiabético a ↓ mortalidade CV; efeito **não** necessariamente de classe; pop. de altíssimo risco → não extrapolar p/ prevenção primária. **Classe I/A** p/ DM2 + DCV |

> **Como estudar a tabela:** para **cada** trial saiba (1) desenho, (2) população, (3) se o
> desfecho é duro ou substituto, (4) a **força** e a **fraqueza** (viés). O professor adora
> perguntar "qual a principal limitação do estudo X?".

---

## 6. Linha histórica "da observação à diretriz"

1. **1948** — início do Framingham (1ª coorte CV de longo prazo).
2. **1961** — publicação do termo **"risk factor"** (Kannel et al.).
3. **1980s** — 1ºs escores de predição baseados no Framingham.
4. **2004** — INTERHEART confirma **universalidade** dos fatores de risco (52 países).
5. **2013** — ACC/AHA lança as **Pooled Cohort Equations**; SBC adapta para o Brasil.
6. **2019–2024** — Diretriz SBC de Dislipidemias/Prevenção incorpora escores nacionais e
   **escore de cálcio coronariano**.
7. **Atual** — Escore **PREVENT** (desfechos IAM, AVE e **IC**) adotado como principal
   calculadora de risco pela SBC.

---

## 7. Casos clínicos da aula (raciocínio evidência → decisão)

### Caso 1 — Jovem de 38 anos com pré-hipertensão
RPL, 38a, masculino, PA 138/88, 136/86, 134/88; assintomático; alto consumo de sódio,
sedentário; sem DM; Col total 210; IMC 27; TFG 95.
- **Tarefas:** (1) critérios diagnósticos de HAS (definição SBC); (2) classificação de risco
  CV (**PREVENT**).
- **Decisão:** baixo risco basal → **RRA de fármaco seria pequena (NNT alto)** → priorizar
  **mudança de estilo de vida** (restrição de sódio — sustentada por Hill/RCTs, atividade
  física, peso). Reforça o §4 da aula de HAS: *tratar mais agressivamente quem tem maior
  risco basal*.

### Caso 2 — Homem 43–45 anos com HAS resistente e DAC
PA 158/98, 162/100, 160/96 em uso de **3 anti-hipertensivos (incl. diurético)**; angioTC com
lesão obstrutiva; assintomático; sem DM; LDL 118; HVE no ECG; IMC 29; sem causa secundária.
- **HAS resistente (definição SBC):** PA não controlada apesar de **≥ 3 fármacos em doses
  otimizadas, incluindo um diurético** (ou controlada exigindo ≥ 4).
- **Condutas baseadas em evidência (duros vs. surrogate):**
  - **Espironolactona** como 4º agente — suporte do **PATHWAY-2** (ECR, mas **desfecho = PA,
    surrogate** → generalizar com cautela).
  - **Estatina de alta potência** — **4S** (ECR, **desfecho duro**, ↓ eventos).
  - **iSGLT2** (empagliflozina/dapagliflozina) — **EMPA-REG** (ECR, desfecho duro).
  - **Análogo de GLP-1** (semaglutida) — **SELECT** (ECR, ↓ eventos).

---

## 8. Exercício de risco atribuível (resolvido)

Coorte hipotética, tabagismo × IAM em 10 anos:

| Grupo | n | IAM | Incidência |
|---|:---:|:---:|:---:|
| Fumantes (expostos) | 1.000 | 80 | 8,0% |
| Não fumantes | 1.000 | 30 | 3,0% |

1. **RA** = 8% − 3% = **5%** (5 IAM extras por 100 fumantes em 10 anos).
2. **RR** = 8%/3% = **2,67**.
3. **RRR** = (RR−1)/RR = 1,67/2,67 = **62,5%** (redução se parar de fumar).
4. **NNT** (cessação) = 1/0,05 = **20** (parar 20 fumantes evita 1 IAM em 10 anos).
5. **NNH** (tabagismo) = 1/0,05 = **20** (20 fumantes para 1 IAM extra).

> **Interpretação crítica:** o RRR de 62,5% parece enorme, mas o **NNT de 20** contextualiza o
> benefício **absoluto**. Em população de **baixo risco basal**, o **mesmo RR** gera **NNT
> muito maior** → o benefício absoluto depende do **risco basal**.

---

## 9. Síntese: da observação à prática

```
Observação populacional (coortes: Framingham, ELSA)  →  identificam padrões e associações
        ↓
Teste de hipóteses (caso-controle e ECR: INTERHEART, 4S, HOPE)  →  causalidade e eficácia
        ↓
Síntese (meta-análises)  →  precisão e subgrupos
        ↓
Diretriz (SBC traduz em recomendações graduadas p/ o Brasil)
        ↓
Prática clínica (médico aplica ao paciente → gera novos dados → alimenta novas pesquisas)
```

## 10. Pontos que mais caem
1. Hierarquia + **força/fraqueza de cada desenho** e o **exemplo CV** de cada.
2. **RA, RAP, fração atribuível, NNH** (exemplo do sódio) e o exercício do tabagismo.
3. **Bradford-Hill** aplicado ao sódio; **causalidade reversa** e **viés de diluição** na
   curva "J/U".
4. **Duros vs. surrogate** (torcetrapib; PCR-us no JUPITER).
5. **Tabela dos ECR** (4S, JUPITER, SPRINT, EMPA-REG): população, desfecho, NNT e **limitação**.
6. **INTERHEART:** 9 fatores > 90% do risco atribuível. **ELSA-Brasil:** calibração nacional.
