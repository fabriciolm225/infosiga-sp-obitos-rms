# Parte IV — Casos clínicos e exercícios resolvidos

> Faça **primeiro sem olhar a resposta**. Depois confira o passo a passo.

---

## A. Exercícios de cálculo de risco (o tipo que mais cai)

### Exercício 1 — Infarto e hipertensão
| Grupo | Infartos | Total |
|---|:---:|:---:|
| Normotensão | 10 | 1.000 |
| Hipertensão | 20 | 1.000 |

**a)** RA de cada grupo? **b)** RR (hipertensos vs. normotensos)? **c)** RR (normotensos vs.
hipertensos)?

<details><summary>Resposta</summary>

- **a)** RA normo = 10/1000 = **1%**; RA hiper = 20/1000 = **2%**.
- **b)** RR = 2%/1% = **2** (hipertensos têm risco **2× maior**).
- **c)** RR = 1%/2% = **0,5** (normotensos têm **50%** do risco dos hipertensos).
</details>

---

### Exercício 2 — Tratamento e infarto (RRA, RRR, NNT)
| Grupo | Infartos | Total |
|---|:---:|:---:|
| Controle | 30 | 1.000 |
| Tratado | 15 | 1.000 |

Calcule **RA de cada grupo, RR, RRR, RRA e NNT**.

<details><summary>Resposta</summary>

- RA controle = 3% ; RA tratado = 1,5%.
- **RR** = 1,5%/3% = **0,5**.
- **RRR** = 1 − 0,5 = **50%**.
- **RRA** = 3% − 1,5% = **1,5%**.
- **NNT** = 1/0,015 = **≈ 67** (trate ~67 para evitar 1 infarto).
</details>

---

### Exercício 3 — A armadilha do risco basal (mesmo RRR, NNT diferente)
| Cenário | Controle | Tratado |
|---|:---:|:---:|
| **A** | 0,3% | 0,1% |
| **B** | 0,04% | 0,01% |

Calcule RRR, RRA e NNT de cada. O que você conclui?

<details><summary>Resposta</summary>

- **A:** RR = 0,1/0,3 = 0,33 → **RRR 67%**; RRA = 0,2% → **NNT 500**.
- **B:** RR = 0,01/0,04 = 0,25 → **RRR 75%**; RRA = 0,03% → **NNT ≈ 3.333**.
- **Conclusão:** o RRR até **aumenta** (67→75%), mas a RRA **despenca** e o **NNT explode** —
  em baixo risco basal, um "grande" RRR evita **pouquíssimos** eventos reais. **Sempre olhe a
  RRA/NNT.**
</details>

---

### Exercício 4 — Impacto do tratamento (RAR, RRR, NNT, impacto)
| Grupo | Óbitos | Total |
|---|:---:|:---:|
| Controle | 100 | 1.000 |
| Tratado | 50 | 1.000 |

Calcule RRA, RRR, NNT e classifique o impacto.

<details><summary>Resposta</summary>

- RA controle 10% ; RA tratado 5%.
- **RRA** = 10 − 5 = **5%** ; **RRR** = 1 − 0,5 = **50%** ; **NNT** = 100/5 = **20**.
- **Impacto = Muito grande** (NNT baixo).
</details>

---

### Exercício 5 — Dissecção de aorta por HAS (NNT clínico)
Tratamento reduz mortalidade de **12% → 8%**.

<details><summary>Resposta</summary>

- **RR** = 8/12 = 0,67 → **RRR = 33%**.
- **RRA** = 12 − 8 = **4%** → **NNT = 100/4 = 25** (tratar 25 para evitar 1 morte).
- Se o risco basal fosse 3%→2%: RRA = 1% → **NNT = 100** (mesmo RRR de 33%, mas 4× mais
  pacientes por vida salva).
</details>

---

### Exercício 6 — Risco atribuível ao tabagismo (coorte, 10 anos)
| Grupo | n | IAM | Incidência |
|---|:---:|:---:|:---:|
| Fumantes | 1.000 | 80 | 8% |
| Não fumantes | 1.000 | 30 | 3% |

Calcule **RA, RR, RRR, NNT (cessação), NNH (tabagismo)**.

<details><summary>Resposta</summary>

- **RA** = 8 − 3 = **5%** (5 IAM extras por 100 fumantes/10 anos).
- **RR** = 8/3 = **2,67**.
- **RRR** = (2,67 − 1)/2,67 = **62,5%**.
- **NNT** (cessação) = 1/0,05 = **20** ; **NNH** (tabagismo) = 1/0,05 = **20**.
- **Crítica:** RRR 62,5% impressiona, mas o NNT de 20 mostra o benefício **absoluto**; em
  baixo risco basal o NNT seria muito maior.
</details>

---

### Exercício 7 — Sódio e DCV (risco atribuível, fração, NNH)
| Ingesta | Risco DCV |
|---|:---:|
| 5 g/dia (exposto) | 24% |
| 4 g/dia | 8% |

Calcule **RR, RA atribuível, fração atribuível, NNH**.

<details><summary>Resposta</summary>

- **RR** = 24/8 = **3**.
- **RA atribuível** = 24 − 8 = **16%** (na aula, versão com 26−8 = 18%).
- **Fração atribuível** = 18/24 ≈ **75%**.
- **NNH** = 1/0,18 ≈ **6**.
</details>

---

### Exercício 8 — Interpretar um HR
Um ECR relata **HR 0,84 (IC 95% 0,73–0,97; p = 0,016)** para mortalidade com o tratamento.
Interprete.

<details><summary>Resposta</summary>

- HR < 1 → **tratamento protetor**. **1 − 0,84 = 0,16 → 16% de redução relativa** na taxa
  instantânea de morte.
- **IC 0,73–0,97 não cruza 1** e **p < 0,05** → **estatisticamente significativo**.
- (É o resultado de sobrevida do **UPLIFT**.)
</details>

---

## B. Casos clínicos (raciocínio evidência → decisão)

### Caso 1 — Pré-hipertensão em jovem de baixo risco
RPL, 38a, PA 138/88–134/88 (3 consultas), assintomático, alto sódio, sedentário, sem DM, Col
210, IMC 27, TFG 95.

**Perguntas:** (1) critérios de HAS (SBC)? (2) risco CV (PREVENT)? (3) conduta?

<details><summary>Raciocínio</summary>

- PA na faixa **pré-hipertensão / HAS estágio 1 limítrofe** (confirmar com MAPA/MRPA).
- **Risco basal baixo** (jovem, sem DM, LDL/colesterol pouco alterado).
- **Decisão baseada em MBE:** como o **NNT** de farmacoterapia seria **alto** (baixa RRA em
  baixo risco), priorizar **mudança de estilo de vida** — **restrição de sódio** (sustentada
  por Bradford-Hill + RCTs; ver aula do sódio), atividade física, controle de peso. Reavaliar
  o risco e a PA. *Trate mais agressivamente quem tem maior risco basal.*
</details>

---

### Caso 2 — HAS resistente + DAC
Homem 43–45a, PA 158/98–160/96 em **3 anti-hipertensivos (incl. diurético)**, angioTC com
lesão obstrutiva, assintomático, sem DM, LDL 118, HVE, IMC 29, sem causa secundária.

**Perguntas:** (1) definição de HAS resistente (SBC)? (2) quais medicações incluir e com que
base de evidência?

<details><summary>Raciocínio</summary>

- **HAS resistente:** PA não controlada apesar de **≥ 3 fármacos otimizados, incluindo
  diurético** (ou controlada exigindo ≥ 4).
- **Condutas e nível de evidência (duro vs. surrogate):**
  - **Espironolactona** (4º agente) → **PATHWAY-2** (ECR, mas desfecho **PA = surrogate** →
    cautela).
  - **Estatina de alta potência** → **4S** (ECR, **desfecho duro**, ↓ eventos e mortalidade).
    Meta **LDL < 55** (paciente de alto risco com DAC).
  - **iSGLT2** (empa/dapagliflozina) → **EMPA-REG** (desfecho duro).
  - **GLP-1** (semaglutida) → **SELECT** (desfecho duro, ↓ eventos).
- **Mensagem:** priorizar intervenções com **desfechos duros comprovados**; interpretar as de
  desfecho **substituto** (PA) com cautela.
</details>

---

### Caso 3 — Leitura crítica de um trial de DPOC (UPLIFT)
Um ECR duplo-cego (tiotrópio vs. placebo, 4 anos) tem **desfecho primário negativo** (taxa de
declínio do VEF1 sem diferença) mas **secundários positivos** (menos exacerbações, melhor QV,
sobrevida HR 0,84).

**Pergunta:** o estudo deve ser descartado?

<details><summary>Raciocínio</summary>

- **Não.** O desfecho primário (declínio do VEF1) é um **surrogate**; a decisão clínica pesa
  mais os desfechos que importam ao paciente (**exacerbações, qualidade de vida**).
- **Cautela metodológica:** desfechos **secundários** e o benefício de sobrevida "durante o
  tratamento" **geram hipótese/dão suporte**, mas o estudo **não teve poder primário** para
  mortalidade → não são "prova" definitiva. Ainda assim, sustentam o uso do tiotrópio.
</details>

---

### Caso 4 — Decisão sobre anticorpo anti-amiloide (Alzheimer)
Paciente com DA inicial, PET amiloide positivo, **APOE ε4** heterozigoto. Droga reduz amiloide
em 85 centiloides, mas o ganho clínico é ~3 pontos em escala e o risco de **ARIA-E** é ~27%
(6% sintomática); custo ~R$ 30 mil/mês.

**Pergunta:** como decidir?

<details><summary>Raciocínio</summary>

- **Dissociação surrogate × duro:** amiloide cai muito, benefício clínico **modesto**.
- **Risco × benefício × custo × acesso:** ARIA-E frequente (maior em **APOE ε4**), custo alto,
  necessidade de **monitorização por RM** e biomarcadores.
- **Decisão compartilhada e individualizada:** discutir com paciente/família expectativas
  realistas ("atraso na progressão", não cura), monitorização de ARIA, custo. Significância
  estatística **não** equivale a relevância clínica. ("E se fosse sua mãe?" — o dilema ético.)
</details>

---

### Caso 5 — Escolher a profilaxia secundária no AVC
Paciente com AVC isquêmico. Como a **classificação etiológica** muda a conduta?

<details><summary>Raciocínio</summary>

- **Aterosclerose intracraniana:** AAS + clopidogrel (21–90 d) + estatina → depois AAS +
  estatina.
- **Carótida (extracraniana):** AAS + estatina ± cirurgia (endarterectomia/stent); LDL < 55.
- **Dissecção:** intracraniana → AAS; extracraniana → AAS **ou** anticoagulação.
- **ESUS:** **antiagregação** (anticoagulação **refutada** por NAVIGATE-ESUS/RE-SPECT ESUS).
- **Todos:** controle de HAS/DM, parar de fumar, **LDL < 55**, **HbA1c < 7%**.
- **Mensagem:** **classificar = decidir**. O mecanismo define a droga.
</details>

---

## C. Questões conceituais rápidas (V/F comentado)

1. *"Um RRR de 50% sempre representa grande benefício clínico."*
   → **FALSO.** Depende do risco basal; em baixo risco a RRA é ínfima e o NNT enorme.
2. *"Desfecho primário negativo invalida todo o estudo."*
   → **FALSO** (UPLIFT). Secundários clinicamente úteis mantêm valor.
3. *"Melhorar um biomarcador garante melhorar o desfecho clínico."*
   → **FALSO** (torcetrapib ↑HDL mas ↑mortalidade; dissociação surrogate).
4. *"Kappa = 0,16 indica ótima concordância entre patologistas."*
   → **FALSO.** É concordância **baixa** (DCF tipo 1).
5. *"A curva 'J/U' do sódio prova que pouco sal faz mal."*
   → **FALSO.** Explicada por **causalidade reversa** e **viés de diluição**.
6. *"O ECR é sempre superior à coorte para qualquer pergunta."*
   → **FALSO.** Cada desenho responde a uma pergunta; para etiologia de longo prazo, a coorte
   pode ser mais adequada. A hierarquia **não é absoluta**.
7. *"HR 0,84 significa que o tratamento aumentou o risco."*
   → **FALSO.** HR < 1 = **proteção** (16% menos risco).
8. *"rtPA só pode ser usado até 3 horas."*
   → **FALSO.** ECASS III estendeu a janela para **3–4,5 h** em selecionados.
