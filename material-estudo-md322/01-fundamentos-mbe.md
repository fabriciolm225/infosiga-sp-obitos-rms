# Parte I — Fundamentos de Medicina Baseada em Evidências (MBE)

> **Esta é a parte mais importante da prova.** Todos os professores usam estes conceitos.
> Domine-os e você entende qualquer aula clínica da disciplina.

---

## 1. O ciclo da evidência à decisão

```
Problema do mundo real  →  Hipótese  →  Método científico  →  Estudo (desenho adequado)
        →  Evidência  →  Síntese (meta-análise)  →  Diretriz  →  Decisão clínica individual
```

Exemplo dado em aula (AVC): em 2014 criou-se o conceito de **ESUS** (AVC embólico de fonte
indeterminada). Problema real: *qual a melhor profilaxia?* → hipótese → ensaios clínicos →
evidência → guideline. A prática clínica ainda **gera novos dados** que alimentam pesquisas
futuras (o ciclo é uma espiral, não uma linha).

---

## 2. Hierarquia da evidência científica

Da **maior** para a **menor** certeza causal (formato de pirâmide):

| Nível | Desenho | Para que serve |
|:---:|---|---|
| **1** | **Meta-análises e Revisões Sistemáticas** | Sintetizam vários estudos; maior poder |
| **2** | **Ensaios Clínicos Randomizados (ECR/RCT)** | Testam **causalidade** e eficácia de intervenção |
| **3** | **Coorte prospectiva** | Incidência, temporalidade, fatores de risco |
| **4** | **Caso-controle** | Doenças raras, rápido e barato |
| **5** | **Transversais, ecológicos e séries de casos** | Geram hipóteses; menor certeza |

> ⚠️ **A hierarquia não é absoluta.** Cada desenho responde a uma pergunta diferente. Uma
> coorte bem-feita (Framingham) pode ser mais útil para *etiologia* do que um ECR. E "lixo
> entra, lixo sai" — uma meta-análise de estudos ruins continua ruim.

---

## 3. Forças e limitações de cada desenho (tabela de prova)

| Desenho | Força | Limitação | Exemplos CV |
|---|---|---|---|
| **Coorte prospectiva** | Temporalidade clara (exposição → desfecho); mede **incidência** e risco absoluto | Confundimento residual; perdas de seguimento; caro e demorado | Framingham, ARIC, MESA, ELSA-Brasil |
| **Caso-controle** | Eficiente para **doenças raras**; rápido; barato | **Viés de memória (recall)**; seleção de controles; não mede incidência direta | INTERHEART |
| **ECR** | Controla confundimento pela **randomização**; permite **inferência causal** | Validade externa variável; caro; critérios de exclusão limitam generalização | 4S, SPRINT, EMPA-REG, JUPITER, UPLIFT |
| **Meta-análise / RS** | Maior poder; detecta efeitos modestos; síntese | Viés de publicação; heterogeneidade; "lixo entra, lixo sai" | CTT (estatinas), BPLTTC |

**Como decorar:** coorte = *tempo*; caso-controle = *doença rara/rápido*; ECR = *causa
(randomização)*; meta-análise = *poder/síntese*.

---

## 4. PICOT — como estruturar (e ler) uma pergunta de pesquisa

| Letra | Significa | Exemplo (UPLIFT) |
|:---:|---|---|
| **P** | **P**opulação / paciente | Adultos com DPOC GOLD II–IV |
| **I** | **I**ntervenção | Tiotrópio 18 mcg/dia |
| **C** | **C**omparador | Placebo |
| **O** | **O**utcome (desfecho) | Taxa de declínio do VEF1 (primário) |
| **T** | **T**empo (seguimento) | 4 anos |

Sempre que ler um trial, identifique o PICOT — inclusive **se o desfecho é duro ou
substituto** (ver adiante).

---

## 5. Medidas de frequência e de efeito ⭐ (o coração da prova)

### 5.1 Risco absoluto (RA)
Probabilidade **real** de um evento ocorrer em um grupo, num período.

$$\text{RA} = \frac{\text{n.º de eventos}}{\text{n.º total do grupo}}$$

- Ex.: 30 infartos em 1.000 pacientes → RA = 30/1000 = **3%**.
- Responde: **"Qual a chance real de o evento acontecer?"**

### 5.2 Risco relativo (RR)
Compara o risco entre **dois grupos** (exposto/tratado vs. não exposto/controle).

$$\text{RR} = \frac{\text{RA no grupo exposto (ou tratado)}}{\text{RA no grupo não exposto (ou controle)}}$$

- **RR = 1** → sem diferença.
- **RR > 1** → exposição **aumenta** o risco (fator de risco).
- **RR < 1** → exposição **reduz** o risco (fator de proteção / efeito de tratamento).
- Responde: **"Quanto o risco muda comparado ao outro grupo?"**

> Exemplo de aula: hipertensos RA 2% vs. normotensos RA 1% → RR = 2%/1% = **2** (hipertensos
> têm risco 2× maior). Invertendo, normotensos vs. hipertensos → RR = 1%/2% = **0,5** (50%).

### 5.3 Redução do risco relativo (RRR)
Quanto o tratamento reduz o risco em **termos proporcionais**.

$$\text{RRR} = 1 - \text{RR} \qquad\left(\text{ou } \frac{\text{RR}-1}{\text{RR}}\text{ para fator de risco}\right)$$

- Ex.: RR do tratamento = 0,5 → RRR = 1 − 0,5 = **50%**.

### 5.4 Redução do risco absoluto (RRA / RAR / ARR)
Diferença **absoluta** de risco entre controle e tratamento.

$$\text{RRA} = \text{RA}_{\text{controle}} - \text{RA}_{\text{tratamento}}$$

- Ex.: controle 3% − tratado 1,5% → RRA = **1,5%**.

### 5.5 Número necessário para tratar (NNT)
Quantos pacientes preciso tratar para **evitar 1 evento**.

$$\boxed{\text{NNT} = \frac{1}{\text{RRA}}}$$

- Ex.: RRA = 4% → NNT = 100/4 = **25** (trato 25 para evitar 1 evento). Quanto **menor** o
  NNT, **maior** o impacto do tratamento.

### 5.6 Número necessário para causar dano (NNH)
Quantos pacientes preciso **expor** para causar 1 dano.

$$\text{NNH} = \frac{1}{\text{RA (atribuível ao dano)}} = \frac{1}{\text{ARI}}$$

### 5.7 Risco atribuível (RA_atr) e derivados
Quantos casos são **atribuíveis** à exposição, além do risco basal.

$$\text{Risco atribuível} = \text{Risco}_{\text{expostos}} - \text{Risco}_{\text{não expostos}}$$

$$\text{Fração atribuível} = \frac{\text{Risco atribuível}}{\text{Risco}_{\text{expostos}}}$$

- **RAP (Risco Atribuível Populacional):** fração do total de casos que seria **eliminada
  se a exposição fosse removida**. É a medida-chave para **saúde pública / políticas**.
- Exemplo do sódio (NEJM 2022): expostos (5 g/d) risco 24%, não expostos (4 g/d) 8% →
  RR = 24/8 = **3**; RA atribuível = 24 − 8 = 16% (na aula usaram 26−8=18%); fração
  atribuível ≈ 75%; NNH = 1/0,18 ≈ **6**.

> ⚠️ **Diferença conceitual:** o **RR** mede a *força da associação*; o **RA/RAP** mede o
> *impacto* (depende da prevalência da exposição e da incidência da doença na população).

### 5.8 Hazard Ratio (HR) — estudos de sobrevida
Compara a **taxa instantânea** de ocorrência do evento entre dois grupos **ao longo do
tempo** (análise de sobrevida / Cox / Kaplan-Meier).

- **HR = 1** → sem diferença.
- **HR < 1** → tratamento associado a **menor** risco.
- **HR > 1** → tratamento associado a **maior** risco.
- Ex. (UPLIFT): HR de mortalidade = **0,84** → o grupo tiotrópio teve taxa de morte **16%
  menor** (1 − 0,84 = 0,16) enquanto usava o tratamento. IC 95% 0,73–0,97; p = 0,016.

### 5.9 Odds Ratio (OR / razão de chances)
Usada em **caso-controle** e regressão logística. Aproxima o RR quando a doença é rara.

---

## 6. ⚠️ Cuidado ao interpretar: absoluto vs. relativo

O **mesmo RRR** pode significar impactos clínicos totalmente diferentes, porque o benefício
absoluto **depende do risco basal**:

| Cenário | Controle | Tratado | RRR | RRA | NNT | Impacto |
|---|:---:|:---:|:---:|:---:|:---:|---|
| Alto risco | 10% | 5% | 50% | 5% | 20 | **Muito grande** |
| Risco moderado | 4% | 2% | 50% | 2% | 50 | **Moderado** |
| Baixo risco | 0,4% | 0,1% | 75% | 0,3% | 333 | **Muito pequeno** |

> **Mensagem de ouro (repetida por vários professores):** *sempre reporte a RRA e o NNT.*
> O **RRR isolado superestima** o benefício percebido. "Reduz o risco pela metade" soa
> impressionante, mas se o risco basal é 0,4%, você evita pouquíssimos eventos.

---

## 7. Desfechos duros vs. substitutos (surrogate) ⭐

| | **Desfechos DUROS** | **Desfechos SUBSTITUTOS (surrogate)** |
|---|---|---|
| O que são | Eventos com relevância clínica direta: **morte CV, IAM não fatal, AVC não fatal, hospitalização por IC** | Biomarcadores/medidas fisiológicas que *supõem* predizer os duros: **LDL-c, PCR-us, PA, HbA1c, VEF1, espessura íntima-média** |
| Vantagem | Padrão-ouro; menor subjetividade; base para **recomendação Classe I / Nível A** | Mais **rápidos e baratos** de medir |
| Desvantagem | Exigem amostras grandes e longo seguimento | **Risco de dissociação:** melhora o substituto sem melhorar (ou até piorando) o desfecho duro |

**Exemplo clássico de dissociação:** o **torcetrapib** aumentava o HDL (surrogate "bom") mas
**aumentou a mortalidade**. Recomendações baseadas só em substitutos: no máximo Classe IIa/IIb.

> **Pergunta-chave ao ler qualquer trial:** *"O desfecho primário é duro ou substituto?"*

**Continuum aterosclerótico** (por que surrogate "antecipa" o evento): PA/PCR (0–10 anos) →
microalbuminúria/calcificação (20–30 anos) → IAM/AVC/isquemia crítica de MMII (40 anos).

---

## 8. Critérios de causalidade de Bradford-Hill ⭐

Associação **não** é causalidade. Hill propôs 9 critérios para inferir causa:

| # | Critério | Ideia central |
|:---:|---|---|
| 1 | **Força de associação** | Quanto maior o RR, mais provável a causa (fumante: 30× mais câncer de pulmão) |
| 2 | **Consistência** | Achado se repete em estudos diferentes |
| 3 | **Especificidade** | Retirar a causa cessa o efeito (cuidado: doenças são multicausais) |
| 4 | **Temporalidade** | A causa **precede** a doença (critério **obrigatório**) |
| 5 | **Gradiente biológico (dose-resposta)** | Mais exposição → mais doença |
| 6 | **Plausibilidade biológica** | A associação faz sentido mecanicamente |
| 7 | **Coerência** | Compatível com o conhecimento atual da doença |
| 8 | **Evidência experimental** | Comprovado em laboratório/experimento |
| 9 | **Analogia** | Relação causal semelhante já estabelecida reforça a inferência |

> Aplicação (sódio): plausibilidade biológica (sal ↑ Na plasmático ↑ PA), gradiente
> biológico (mais sal, mais risco), temporalidade (RCTs), especificidade (RCT agudo) — a
> soma dos critérios sustenta a causalidade sal → HAS → DCV.

---

## 9. Vieses (armadilhas que o professor cobra) ⭐

| Viés | O que é | Onde aparece na disciplina |
|---|---|---|
| **Confundimento** | 3ª variável associada à exposição e ao desfecho distorce a associação | Observacionais; randomização o controla |
| **Viés de memória (recall)** | Casos lembram exposições diferente dos controles | Caso-controle (INTERHEART) |
| **Viés de seleção** | Grupos não comparáveis por como foram escolhidos | Caso-controle; escolha de controles |
| **Viés de publicação** | Estudos "positivos" são mais publicados | Meta-análises |
| **Viés de diluição (regressão)** | Uma **única medida ruidosa** (ex.: 1 dosagem de Na urinário) subestima a associação vs. média de longo prazo | Sódio × DCV (Circulation 2017) |
| **Causalidade reversa** | A doença causa a "exposição", não o contrário | Curva "J/U" do sódio: doentes graves comem menos sal → parece que pouco sal faz mal |
| **Viés de interrupção precoce** | Parar o trial no pico do benefício **superestima** o efeito | JUPITER, SPRINT (interrompidos cedo) |
| **Viés de aferição** | Método de medida distorce o resultado | SPRINT: PA automática não-assistida (AOBP) mede ~10–15 mmHg a menos |

---

## 10. Concordância e consenso: Kappa e Delphi (aula de patologia/epilepsia)

### Coeficiente Kappa (κ) — concordância **interobservador**
Mede se dois avaliadores concordam **além do acaso** em variáveis **categóricas**.

| Kappa | Concordância |
|:---:|---|
| < 0,20 | Baixa (pobre) |
| 0,21–0,40 | Razoável (*fair*) |
| 0,41–0,60 | Moderada |
| 0,61–0,80 | Substancial / boa |
| 0,81–1,00 | Quase perfeita |

> Ex. displasia cortical: DCF **tipo 1 → κ = 0,16 (baixa)**; DCF **tipo 3 → κ = 0,68
> (substancial)**. Ou seja, patologistas concordam pouco em alguns subtipos → precisam de
> critérios objetivos (imuno-histoquímica, genética) para melhorar a concordância.

### Método Delphi — construção de **consenso** entre especialistas
- Rodadas iterativas e **anônimas** de questionários; respostas resumidas e reapresentadas.
- Escala tipo Likert (1 discordo totalmente … 5 concordo totalmente).
- **Consenso** definido como **≥ 75%** das respostas numa mesma categoria.
- Itens sem consenso são revisados e rediscutidos.

> Serve para padronizar diagnóstico/conduta quando **faltam ensaios randomizados** (ex.:
> classificação de tumores LEATs, definições em neuropatologia).

---

## 11. Como nasce uma diretriz (SBC) e as classes de recomendação

Fluxo: **pergunta clínica (PICOT) → revisão sistemática da evidência → avaliação da
qualidade → gradação da recomendação → redação → revisão externa → publicação/atualização.**

**Classe de recomendação** (força):
- **Classe I** — deve ser feito (benefício >> risco).
- **Classe IIa** — é razoável fazer (benefício > risco).
- **Classe IIb** — pode ser considerado (benefício ≥ risco).
- **Classe III** — não fazer (sem benefício ou com dano).

**Nível de evidência** (qualidade):
- **Nível A** — múltiplos ECR ou meta-análises.
- **Nível B** — 1 ECR ou estudos observacionais robustos.
- **Nível C** — opinião de especialistas / séries de casos.

> Recomendações baseadas em **desfecho duro** com **ECR** → Classe I, Nível A. Baseadas só
> em **surrogate** → no máximo IIa/IIb.

---

## 12. Glossário-relâmpago

- **RA** – risco absoluto | **RR** – risco relativo | **RRR** – redução do risco relativo
- **RRA/RAR/ARR** – redução do risco absoluto | **NNT** – número necessário para tratar
- **NNH** – número necessário para causar dano | **RAP** – risco atribuível populacional
- **HR** – hazard ratio | **OR** – odds ratio | **IC 95%** – intervalo de confiança 95%
- **ECR/RCT** – ensaio clínico randomizado | **RS** – revisão sistemática
- **PICOT** – População, Intervenção, Comparador, Outcome, Tempo
- **κ (Kappa)** – concordância interobservador | **Delphi** – método de consenso

> **Sobre o IC 95%:** se **cruza 1** (para RR/HR/OR) ou **cruza 0** (para diferenças), o
> resultado **não é estatisticamente significativo**. Ex.: HR 0,84 (IC 0,73–0,97) não cruza
> 1 → significativo.
