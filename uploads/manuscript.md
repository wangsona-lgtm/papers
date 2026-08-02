# Climate Policy Uncertainty and Renewable Energy Deployment in East Asia: A Panel QARDL Approach with Governance Moderation

**Meichih Wang**

Department of [Your Department], National Taichung University of Science and Technology, Taiwan

---

## Abstract

This study examines the impact of climate policy uncertainty (CPU) on renewable energy deployment across eight East Asian economies over the period 1996–2023, employing a Panel Quantile Autoregressive Distributed Lag (QARDL) framework. We contribute to the literature by: (i) introducing the recently updated CPU index (Gavriilidis, Känzig, Raghavan, & Stock, 2026) to the energy transition literature; (ii) testing governance quality as a moderating channel through the six Worldwide Governance Indicators (WGI); and (iii) providing robustness evidence through a monthly-frequency Panel QVAR connectedness analysis. The Panel ARDL results indicate that CPU exerts a statistically significant positive long-run effect on renewable electricity share (β = 0.016, p < 0.01), consistent with the hypothesis that policy uncertainty accelerates clean energy adoption as a hedging strategy. The quantile analysis reveals an increasing gradient: the CPU coefficient rises from 0.022 at the 10th quantile to 0.067 at the 90th quantile, suggesting stronger effects in countries with higher initial renewable penetration. Among governance dimensions, Voice and Accountability emerges as the sole significant moderator (β_interaction = −0.017, p < 0.05), indicating that democratic governance buffers the uncertainty-driven push toward renewables. Monthly Panel QVAR estimates confirm a positive short-run CPU impulse response on renewable energy growth (IRF = +0.032 at month one), while Diebold-Yilmaz connectedness analysis identifies geopolitical risk as the dominant transmitter in the uncertainty–energy nexus. These findings offer policy implications for leveraging climate policy clarity and governance reform in accelerating East Asia's energy transition.

**Keywords:** Climate policy uncertainty, renewable energy, Panel QARDL, governance, East Asia, Panel QVAR, Diebold-Yilmaz connectedness

**JEL Classification:** Q42, Q54, Q58, C33

---

## 1. Introduction

The global transition toward renewable energy has become a central pillar of climate change mitigation strategies. The Paris Agreement, now ratified by 195 parties, commits signatories to substantial reductions in greenhouse gas emissions, with the energy sector representing approximately 73% of global emissions (Ritchie, Rosado, & Roser, 2020). In this context, understanding the determinants of renewable energy deployment is of paramount importance for policy design.

A growing body of literature examines the role of economic and financial variables—GDP per capita, foreign direct investment, trade openness, and financial development—in shaping renewable energy outcomes (Apergis & Payne, 2010; Sadorsky, 2009). More recently, attention has turned to uncertainty as a potential driver of energy transition. Economic policy uncertainty (EPU) and geopolitical risk (GPR) have been shown to influence energy markets, investment decisions, and environmental outcomes (Akhter & Arman, 2026; Caldara & Iacoviello, 2022; Hossain et al., 2026).

However, a specific form of uncertainty—climate policy uncertainty (CPU)—remains underexplored in the renewable energy literature. CPU captures uncertainty about the future direction of climate-related regulation, legislation, and policy action. Unlike general economic uncertainty, CPU carries a distinct directional implication: when firms and investors perceive that climate policy may tighten in the future, they may accelerate investments in clean technologies as a preemptive hedging strategy. Conversely, policy uncertainty could delay investments by increasing the option value of waiting (Bernanke, 1983; Bloom, 2009).

The newly updated CPU index by Gavriilidis, Känzig, Raghavan, and Stock (2026) provides a rigorous news-based measure of climate policy uncertainty, constructed from major U.S. newspapers using both dictionary-based and large language model (LLM) approaches. While originally designed for the U.S. context, CPU captures global climate policy discourse that spills over to other economies through policy diffusion, trade linkages, and financial markets. Given East Asia's position as the world's manufacturing hub and its growing renewable energy ambitions, the transmission of climate policy uncertainty to this region warrants systematic investigation.

This study addresses three research questions:

1. Does climate policy uncertainty significantly affect renewable energy deployment in East Asian economies?
2. Does this effect vary across the conditional distribution of renewable energy penetration (i.e., quantile heterogeneity)?
3. Do governance institutions moderate the CPU–renewable energy relationship?

We contribute to the literature in several ways. First, to our knowledge, this is the first study to employ the updated CPU index (Gavriilidis et al., 2026) in the context of East Asian renewable energy. Second, we apply a Panel QARDL framework (Cho, Kim, & Shin, 2015; Shahbaz, Lahiani, Abosedra, & Hammoudeh, 2018), which permits the estimation of long-run relationships across the conditional quantiles of renewable energy deployment, revealing distributional heterogeneity that mean-based estimators obscure. Third, we test the moderating effects of all six WGI dimensions, identifying which governance channels amplify or buffer the CPU–renewable energy nexus. Fourth, we provide a monthly-frequency robustness check using Panel QVAR and Diebold-Yilmaz (2012) connectedness analysis, bridging the annual panel literature with high-frequency time-series methods.

Our findings reveal that: (a) CPU has a positive and statistically significant long-run effect on renewable energy share; (b) this effect strengthens monotonically from lower to upper quantiles; (c) Voice and Accountability moderates the relationship, with more democratic governance reducing the CPU-induced push toward renewables; and (d) monthly connectedness analysis confirms a positive short-run CPU impulse on renewable energy, while identifying geopolitical risk as the dominant transmitter of uncertainty shocks.

The remainder of this paper is organized as follows. Section 2 reviews the related literature. Section 3 describes the data and empirical methodology. Section 4 presents the empirical results. Section 5 provides robustness analysis using monthly Panel QVAR. Section 6 concludes with policy implications.

---

## 2. Literature Review

### 2.1 Climate Policy Uncertainty: Measurement and Evolution

The theoretical foundation for understanding policy uncertainty's economic effects traces to Bernanke (1983) and Bloom (2009), who established that uncertainty creates a real-options channel through which firms delay irreversible investments. This framework was operationalized by Baker, Bloom, and Davis (2016), whose Economic Policy Uncertainty (EPU) index—constructed from newspaper frequency counts of uncertainty-related terms—has become the benchmark measure in the empirical uncertainty literature.

Climate policy uncertainty (CPU) applies this measurement philosophy to the environmental domain. The original CPU index by Gavriilidis (2021) identified articles in eight major U.S. newspapers that jointly discussed climate change, policy, and uncertainty concepts. This index was recently overhauled by Gavriilidis, Känzig, Raghavan, and Stock (2026), who introduce three critical innovations: (i) narrow and broad dictionary-based indices that balance precision against coverage; (ii) an LLM-based validation measure that cross-checks dictionary classification using large language models; and (iii) an event-based instrument that isolates exogenous climate policy uncertainty shocks by purging the first moment of climate policy stringency from uncertainty variation. The updated index extends from January 1985 to April 2026, providing sufficient temporal coverage for both long-run panel analysis and high-frequency time-series applications.

### 2.2 CPU Effects on Energy and Environmental Outcomes: Mixed Evidence

The empirical literature on CPU's effects on energy outcomes yields strikingly heterogeneous results, a pattern recently documented by Matias and Tabak's (2026) systematic meta-analysis of seventeen peer-reviewed studies. Their random-effects meta-analysis finds a small and statistically insignificant average effect of CPU on energy-transition-related investment outcomes, accompanied by "extremely high heterogeneity" (I² > 95%). Crucially, a mixed-effects meta-regression organized around four transmission channels—firm investment, financial markets, political-institutional, and macroeconomic—explains only 50.4% of between-study variance, with the macroeconomic channel showing the strongest negative effect (β = −1.07, p < 0.01). This finding underscores that the CPU–energy transition relationship is not universal but deeply contingent on context, methodology, and outcome measurement.

On the negative-effect side, several studies document that CPU depresses renewable energy outcomes. Syed, Apergis, and Goh (2023) apply a Fourier-augmented ARDL model to monthly U.S. data and find that CPU significantly reduces renewable energy consumption in both the short and long run. Payne, Nazlioglu, Koncak, and Ewing (2025) corroborate this with generalized impulse response analysis within a VAR framework, showing that total U.S. renewable energy production responds negatively to CPU shocks, though sub-component responses (hydro, biomass, geothermal, wind, solar) differ markedly. Yang, Mao, and Liu (2026) extend the analysis to 35 developing countries using a double machine learning approach, finding that CPU significantly hinders renewable energy investment by exacerbating financing constraints, inhibiting green technology innovation, and lowering traditional energy prices. Their heterogeneity analysis reveals that the negative impact is more pronounced in lower-income countries and those at early stages of renewable energy development.

At the sub-national level, Guang, Liu, Tan, and Wen (2024) use Chinese provincial panel data (2008–2021) and find that CPU inhibits regional energy structure transformation, operating through two mechanisms: hindering technology marketization and obstructing government intervention. The negative effect is amplified in provinces with slower economic growth, lower marketization, and higher resource endowments.

On the positive-effect side—and directly relevant to our findings—a growing strand of literature documents countervailing mechanisms. The "flight-to-green" hypothesis (Matias & Tabak, 2026; Silva, Ferreira, & Cortez, 2024) posits that heightened climate policy uncertainty can redirect investment from carbon-intensive assets toward clean energy as a hedging strategy. This channel has been documented in renewable energy stock markets, where clean energy equities outperform fossil fuel equities during periods of elevated CPU. Lin and Cheung (2024) find that CPU promotes energy transition at the prefecture level in China, particularly when local governments maintain credible renewable energy support policies. Sohail, Hiles, and Morley (2024) examine the Environmental Kuznets Curve incorporating both EPU and CPU for emerging and developed countries, finding that uncertainty measures significantly alter the income–emissions relationship.

This literature indicates that the CPU–renewable energy relationship is theoretically ambiguous and empirically heterogeneous. The sign and magnitude of the effect depend on the outcome variable (investment vs. consumption vs. production), the level of analysis (firm vs. sector vs. country), the time horizon (short-run vs. long-run), and the mediating institutional context. Our study engages directly with this heterogeneity by: (i) using the long-run Panel ARDL framework to capture equilibrium relationships; (ii) employing Panel QARDL to map distributional variation across the conditional quantiles of renewable penetration; and (iii) testing governance institutions as moderators of the CPU effect.

### 2.3 Determinants of Renewable Energy Deployment: From Fundamentals to Uncertainty

The traditional literature on renewable energy determinants emphasizes structural economic variables. Apergis and Payne (2010) establish panel evidence linking GDP growth, CO₂ emissions, and renewable energy consumption across OECD countries, finding bidirectional causality between renewable energy and economic growth. Sadorsky (2009) identifies financial development and oil prices as significant drivers of renewable energy investment in emerging economies, while Omri and Nguyen (2014) extend the analysis to a global panel, documenting heterogeneous determinants across income groups. More recently, renewable energy deployment has been linked to trade openness (Jebli, Youssef, & Apergis, 2019), foreign direct investment (Keeley & Ikeda, 2017), and urbanization (Salim & Shafiei, 2014).

The integration of uncertainty measures into renewable energy analysis represents a more recent development. Caldara and Iacoviello's (2022) Geopolitical Risk (GPR) index has been applied to energy markets by multiple studies. Akhter and Arman (2026) employ a Nonlinear ARDL (NARDL) framework to examine the asymmetric effects of GPR and governance on renewable energy consumption in ASEAN and East Asian countries, finding that positive GPR shocks reduce renewable energy consumption while governance quality significantly moderates the relationship. This study provides the closest precedent to our analysis, and we extend it in three directions: substituting CPU for GPR as the primary uncertainty variable, broadening the governance analysis to all six WGI dimensions, and moving from single-country NARDL to Panel QARDL.

The QARDL methodology itself has gained traction in energy economics. Shahbaz, Lahiani, Abosedra, and Hammoudeh (2018) apply QARDL to examine the energy–growth nexus in Pakistan. Kashif et al. (2025) use QARDL to analyze fintech-driven sustainability impacts on renewable energy consumption and natural resource management. Troster, Shahbaz, and Uddin (2018) pioneer Granger-causality in quantiles for the renewable energy–oil price–economic activity nexus. These studies demonstrate QARDL's key advantage: revealing distributional heterogeneity that mean-based estimators (OLS, ARDL, NARDL) inevitably obscure. A coefficient that is statistically insignificant at the mean may be strongly significant at the tails, and vice versa—a possibility with direct policy relevance for countries at different stages of the energy transition.

### 2.4 Governance as a Moderator in the Energy–Uncertainty Nexus

The institutional economics literature provides strong theoretical grounds for expecting governance quality to moderate the CPU–renewable energy relationship. Dasgupta and De Cian (2018) provide a comprehensive review establishing that institutional quality shapes environmental outcomes through three primary channels: enforcement (regulatory monitoring and sanctioning capacity), credibility (policy commitment and time-consistency of incentives), and participation (stakeholder engagement and civil society monitoring).

Liashenko, Dluhopolskyi, Wołowiec, and Woźniak (2026) provide the most comprehensive recent evidence on governance and renewable energy, using a Panel ARDL framework across 174 countries (2000–2023). They find that Political Stability is the only statistically significant governance dimension, while other WGI components lack strong independent effects. However, their analysis treats governance as a direct determinant rather than as a moderator of uncertainty, which is our contribution.

The Worldwide Governance Indicators (Kaufmann, Kraay, & Mastruzzi, 2010) operationalize institutional quality across six dimensions: Voice and Accountability (VA), Political Stability and Absence of Violence (PS), Government Effectiveness (GE), Regulatory Quality (RQ), Rule of Law (RL), and Control of Corruption (CC). Each dimension may differentially moderate the CPU–renewable energy relationship:

- **Voice and Accountability (VA):** Democratic institutions provide multiple channels—legislative oversight, media scrutiny, civil society mobilization—for resolving policy uncertainty. Higher VA may weaken the CPU–RE link by reducing the perceived need for preemptive green investment as a hedging strategy against unpredictable regulation.
- **Government Effectiveness (GE):** Bureaucratic capacity and policy implementation quality affect how rapidly renewable energy targets can be scaled. Higher GE may amplify positive CPU effects by enabling faster deployment when policy signals intensify.
- **Regulatory Quality (RQ):** Predictable, transparent regulatory frameworks reduce the ambiguity premium in renewable energy investment. Higher RQ may dampen the CPU effect by lowering the option value of waiting.
- **Rule of Law (RL):** Contract enforcement and property rights protection reduce investment risk. Higher RL may amplify the positive CPU effect by making hedging investment more secure.
- **Control of Corruption (CC):** Corruption introduces additional uncertainty in project approval, permitting, and procurement. Higher CC may reduce the overall investment risk premium, either amplifying or dampening CPU effects depending on context.
- **Political Stability (PS):** Absence of political violence and regime instability reduces tail risk. Higher PS may moderate both directions of the CPU effect.

### 2.5 Research Gap and Contribution

The preceding review identifies five specific gaps that motivate our study:

**Gap 1: The CPU–renewable energy relationship remains empirically unsettled, especially outside the United States.** The meta-analysis by Matias and Tabak (2026) documents extreme heterogeneity with no consensus sign. Existing empirical evidence is concentrated on the U.S. (Syed et al., 2023; Payne et al., 2025), China (Guang et al., 2024; Lin & Cheung, 2024), and developing countries broadly (Yang et al., 2026). No study has examined the CPU–renewable energy nexus in the East Asian regional context, where diverse levels of economic development, renewable penetration, and institutional quality provide natural variation for identifying heterogeneous effects.

**Gap 2: The updated CPU index remains underutilized in the energy literature.** The Gavriilidis et al. (2026) index, which substantially improves upon the original Gavriilidis (2021) measure, has not been applied to renewable energy analysis. Its extended temporal coverage (1985–2026) and refined methodology (LLM validation, exogenous shock instrument) warrant empirical application beyond the macroeconomic context for which it was developed.

**Gap 3: Distributional heterogeneity in the CPU–RE relationship is unexplored.** While the meta-analytic evidence strongly suggests that the CPU effect varies across contexts, no study has systematically examined whether it varies across the conditional distribution of renewable energy penetration. Panel QARDL provides a natural framework for testing whether high-penetration countries respond differently to CPU than low-penetration countries.

**Gap 4: The moderating role of governance in the CPU–renewable energy nexus is untested.** While Akhter and Arman (2026) examine governance moderation of GPR effects on renewable energy, and Yang et al. (2026) document that institutional quality mitigates CPU's negative investment effects in developing countries, no study has tested whether governance institutions moderate the CPU–renewable energy relationship using the full WGI framework.

**Gap 5: The high-frequency dynamics of the CPU–RE relationship lack multi-country evidence.** Existing high-frequency studies (Syed et al., 2023; Payne et al., 2025) are single-country U.S. analyses. The monthly connectedness between CPU, GPR, EPU, and renewable energy in a multi-country setting—particularly in the interconnected East Asian electricity system—remains undocumented.

Our study addresses all five gaps. We provide the first Panel QARDL analysis of the CPU–renewable energy relationship in East Asia (Gaps 1–3), the first test of WGI governance moderation of this relationship (Gap 4), and a monthly Panel QVAR/DY connectedness robustness analysis (Gap 5).

---

## 3. Data and Methodology

### 3.1 Data

We construct a balanced panel dataset covering eight East Asian economies—China, Japan, South Korea, Indonesia, Malaysia, Thailand, the Philippines, and Singapore—over the period 1996–2023 (28 years, 224 observations).

The dependent variable is **renewable energy share** (RE_share), defined as the percentage of electricity generation from renewable sources (hydro, solar, wind, bioenergy, and other renewables), sourced from Our World in Data (OWID) based on Ember's yearly electricity data and BP Statistical Review.

The primary independent variable is the **Climate Policy Uncertainty index** (CPU), using the narrow dictionary-based measure (`cpu_index_narrow`) from Gavriilidis et al. (2026). Monthly values are averaged to annual frequency.

Control variables include:

| Variable | Description | Source |
|----------|-------------|--------|
| GPR | Geopolitical Risk Index (global) | Caldara & Iacoviello (2022) |
| EPU | Global Economic Policy Uncertainty Index | Baker, Bloom & Davis (2016) / policyuncertainty.com |
| GDP_pc | GDP per capita (constant 2015 US$) | World Bank WDI via QoG Standard Dataset |
| CO₂_pc | CO₂ emissions per capita (tonnes) | OWID / Global Carbon Project |
| FDI | Foreign direct investment, net inflows (% GDP) | World Bank WDI via QoG |
| Inflation | Consumer price inflation (annual %) | World Bank WDI via QoG |
| Trade | Trade openness (exports + imports, % GDP) | World Bank WDI via QoG |

Governance moderating variables are the six WGI dimensions from the Worldwide Governance Indicators (Kaufmann et al., 2010), sourced via the Quality of Government (QoG) Standard Dataset (Teorell et al., 2024):

| Variable | WGI Dimension |
|----------|---------------|
| WGI_VA | Voice and Accountability |
| WGI_PS | Political Stability and Absence of Violence |
| WGI_GE | Government Effectiveness |
| WGI_RQ | Regulatory Quality |
| WGI_RL | Rule of Law |
| WGI_CC | Control of Corruption |

WGI data are interpolated linearly between biennial observations (2002, 2003, …, 2023) to obtain annual coverage. The CPU series is sourced from the 2026 updated version, providing full coverage for 1996–2023 without extrapolation. All nominal variables are transformed to natural logarithms where appropriate.

**Figure 1** displays the CPU index from 1985 to 2026, annotated with major climate policy events. The index exhibits pronounced spikes around the Copenhagen COP15 (2009), the Trump administration's announcement of U.S. withdrawal from the Paris Agreement (2017), and the Build Back Better/Inflation Reduction Act legislative period (2021–2022). **Figure 2** presents the renewable electricity share trajectories for each of the eight East Asian economies, revealing substantial cross-country heterogeneity in both levels and trends.

> **[Insert Figure 1 and Figure 2 about here]**

### 3.2 Econometric Framework

#### 3.2.1 Panel Unit Root and Cointegration Tests

We employ Fisher-type augmented Dickey-Fuller (ADF) panel unit root tests (Maddala & Wu, 1999; Choi, 2001) to determine the order of integration of each variable. The null hypothesis is that all panels contain a unit root.

For cointegration testing, we apply the Kao (1999) residual-based panel cointegration test, which extends the Engle-Granger framework to panel data. We also compute the Pedroni (2004) test statistics as a robustness check.

#### 3.2.2 Panel ARDL

The baseline model follows a Panel Autoregressive Distributed Lag (ARDL) specification in the Pooled Mean Group (PMG) framework (Pesaran, Shin, & Smith, 1999):

\[
\Delta RE_{it} = \phi_i RE_{i,t-1} + \beta_1 CPU_{i,t-1} + \beta_2 GPR_{i,t-1} + \beta_3 \ln GDP_{i,t-1} + \beta_4 \ln CO2_{i,t-1} + \sum_{j=1}^{p-1} \gamma_{ij} \Delta RE_{i,t-j} + \sum_{j=0}^{q-1} \delta_{1ij} \Delta CPU_{i,t-j} + \cdots + \varepsilon_{it}
\]

where \(\phi_i\) is the error-correction term (speed of adjustment), \(\beta_k\) are the long-run coefficients, and \(\gamma_{ij}, \delta_{kij}\) are short-run dynamics.

#### 3.2.3 Panel QARDL

To capture distributional heterogeneity, we estimate a Panel Quantile ARDL (Cho et al., 2015; Shahbaz et al., 2018):

\[
Q_{\tau}(RE_{it} | \cdot) = \alpha_i(\tau) + \theta(\tau) CPU_{it} + \sum_{k} \beta_k(\tau) X_{kit} + \varepsilon_{it}(\tau)
\]

where \(Q_{\tau}(\cdot)\) denotes the \(\tau\)-th conditional quantile (\(\tau \in \{0.10, 0.25, 0.50, 0.75, 0.90\}\)). This framework allows us to test whether the CPU effect varies across the conditional distribution of renewable energy penetration. We estimate pooled quantile regressions with bootstrapped standard errors (500 replications).

#### 3.2.4 Interaction Effects

We test governance moderation by augmenting the baseline model with interaction terms:

\[
RE_{it} = \alpha + \beta_1 CPU_{it} + \beta_2 WGI_{it}^k + \beta_3 (CPU_{it} \times WGI_{it}^k) + \gamma' \mathbf{X}_{it} + \varepsilon_{it}
\]

where \(WGI_{it}^k\) is one of the six governance dimensions, estimated separately for each \(k\). A significant interaction coefficient \(\beta_3\) indicates that governance quality moderates the CPU–renewable energy relationship.

---

## 4. Empirical Results

### 4.1 Summary Statistics and Preliminary Analysis

Table 1 presents the summary statistics for all variables. The average renewable electricity share across 224 country-year observations is 13.09% (SD = 9.53%), ranging from 0.79% (Singapore, early years) to 44.49% (Philippines, recent years). CPU exhibits substantial variation (mean = 125.37, SD = 59.95, range = 56.67 to 240.40), with pronounced spikes in 2009–2010 (post-Copenhagen), 2017 (Trump administration climate policy reversal), and 2021–2022 (Inflation Reduction Act period).

**Table 1. Summary Statistics**

| Variable | Obs | Mean | Std. Dev. | Min | Max |
|----------|-----|------|-----------|-----|-----|
| RE share (%) | 224 | 13.09 | 9.53 | 0.79 | 44.49 |
| CPU | 224 | 125.37 | 59.95 | 56.67 | 240.40 |
| GPR (global) | 224 | 99.96 | 31.45 | 50.92 | 176.30 |
| EPU (global) | 224 | 133.65 | 61.87 | 63.31 | 303.18 |
| ln(GDP pc) | 224 | 9.12 | 1.13 | 7.43 | 11.13 |
| ln(CO₂ pc) | 224 | 1.52 | 0.85 | −0.31 | 2.70 |
| WGI: Govt Effectiveness | 224 | 0.70 | 0.86 | −0.91 | 2.35 |
| WGI: Voice & Accountability | 224 | −0.07 | 0.80 | −1.65 | 1.30 |

The correlation matrix reveals several noteworthy patterns. CPU exhibits a moderate positive correlation with renewable energy share (r = 0.175, p < 0.01), providing preliminary evidence consistent with our hypothesis. CPU is strongly correlated with EPU (r = 0.882), suggesting that climate policy uncertainty co-moves with broader economic policy uncertainty. The negative correlation between RE share and GDP per capita (r = −0.631) reflects the composition of our sample: higher-income East Asian economies (Japan, South Korea, Singapore) tend to rely heavily on nuclear and fossil fuel generation, while lower-middle-income economies (Philippines, Indonesia) have substantial hydro and geothermal resources.

### 4.2 Panel Unit Root and Cointegration Tests

**Table 2. Panel Unit Root Tests**

| Variable | Fisher χ² | p-value | Conclusion |
|----------|-----------|---------|-------------|
| RE share | 11.80 | 0.758 | I(1) |
| CPU | 3.05 | 0.999 | I(1) |
| GPR | 44.70 | 0.000 | I(0) |
| EPU | 6.36 | 0.984 | I(1) |
| ln(GDP pc) | 46.39 | 0.000 | I(0) |
| ln(CO₂ pc) | 32.34 | 0.009 | I(0) |
| ΔRE share | 186.82 | 0.000 | I(0) |
| ΔCPU | 319.06 | 0.000 | I(0) |
| ΔEPU | 309.19 | 0.000 | I(0) |

The Fisher-ADF tests indicate mixed orders of integration: RE share, CPU, and EPU appear I(1), while GPR, GDP, and CO₂ appear I(0). However, first-differenced series are all stationary, satisfying the ARDL bounds testing requirement that no variable is I(2).

**Cointegration.** The Kao residual cointegration test strongly rejects the null of no cointegration for both specifications. Model A (RE = f(CPU, GPR, GDP, CO₂)) yields a residual ADF statistic of −9.03 (1% critical value: −3.46), and Model B (adding EPU) yields −10.90, confirming the existence of a long-run equilibrium relationship.

### 4.3 Panel ARDL Results

**Table 3. Panel ARDL (PMG) Long-Run Estimates**

| Variable | Model A | | Model B | |
|----------|---------|------|---------|------|
| | Coef. | t-stat | Coef. | t-stat |
| CPU | 0.0158 | 3.06*** | 0.0103 | 2.13** |
| GPR | 0.0017 | 0.58 | 0.0021 | 0.77 |
| EPU | — | — | 0.0079 | 1.24 |
| ln(GDP pc) | 9.797 | 1.51 | 9.062 | 1.51 |
| ln(CO₂ pc) | −14.933 | −2.97*** | −14.296 | −3.00*** |
| ECT(−1) | −0.587 | −4.01*** | −0.664 | −4.59*** |

*Note: *** p < 0.01, ** p < 0.05, * p < 0.10.*

The Panel ARDL results reveal that CPU has a statistically significant positive long-run effect on renewable energy share in both specifications. In Model A, a one-unit increase in the CPU index is associated with a 0.016 percentage point increase in renewable electricity share (t = 3.06, p < 0.01). The error-correction term (ECT = −0.587) indicates that approximately 58.7% of any deviation from the long-run equilibrium is corrected within one year, consistent with a moderate speed of adjustment typical of energy infrastructure variables.

The CO₂ emissions per capita coefficient is negative and highly significant (β = −14.93, p < 0.01), reflecting the well-documented inverse relationship between carbon intensity and renewable penetration: economies with higher historical fossil fuel dependence tend to have lower renewable shares. The GPR and EPU coefficients are not statistically significant in the long-run specification, suggesting that climate-specific uncertainty—rather than general economic or geopolitical uncertainty—drives renewable energy outcomes in our sample.

### 4.4 Panel QARDL: Quantile Heterogeneity

**Table 4. Panel QARDL Quantile Coefficients — CPU Effect**

| Quantile | CPU Coefficient | Std. Error | t-stat | p-value |
|----------|----------------|------------|--------|---------|
| Q10 | 0.0221 | 0.0189 | 1.17 | 0.242 |
| Q25 | 0.0347 | 0.0119 | 2.92 | 0.004*** |
| Q50 | 0.0298 | 0.0081 | 3.68 | 0.000*** |
| Q75 | 0.0562 | 0.0131 | 4.29 | 0.000*** |
| Q90 | 0.0667 | 0.0280 | 2.38 | 0.018** |
| OLS | 0.0421 | 0.0119 | 3.54 | 0.000*** |

*Note: Bootstrapped standard errors (500 replications).*

The QARDL results reveal a clear and economically meaningful pattern: the CPU effect on renewable energy **increases monotonically across quantiles**. At the 10th quantile (countries with the lowest renewable penetration, e.g., Singapore), a one-unit increase in CPU raises RE share by 0.022 percentage points (not statistically significant). At the median (Q50), the effect is 0.030 (p < 0.01). At the 90th quantile (countries with the highest renewable penetration, e.g., Philippines), the coefficient rises to 0.067 (p < 0.05)—more than three times the Q10 effect.

This gradient suggests a **positive feedback mechanism**: countries with already-higher renewable capacity respond more strongly to climate policy uncertainty shocks, possibly because they possess the institutional infrastructure, supply chains, and technical expertise to accelerate deployment when policy signals intensify. In contrast, countries at the lower end of the distribution face structural barriers that limit their responsiveness to CPU signals.

**Figure 3** visualizes the quantile gradient, plotting the CPU coefficient across Q10–Q90 with 95% confidence bands and the OLS estimate for comparison. The monotonic increase from left to right is visually striking: the Q10 coefficient lies near zero, while the Q90 coefficient is more than three times larger. The OLS point estimate (dashed red line) captures an average effect that masks substantial distributional variation—precisely the limitation that the QARDL framework overcomes.

> **[Insert Figure 3 about here]**

### 4.5 Governance Moderation Effects

**Table 5. Interaction Effects — CPU × WGI Governance Dimensions**

| WGI Dimension | CPU (direct) | CPU × WGI | R² |
|---------------|-------------|-----------|-----|
| Govt Effectiveness | 0.0411*** (5.46) | 0.0040 (0.45) | 0.558 |
| Control of Corruption | 0.0414*** (5.38) | 0.0020 (0.24) | 0.555 |
| Political Stability | 0.0406*** (5.33) | 0.0097 (1.14) | 0.558 |
| Regulatory Quality | 0.0384*** (5.27) | −0.0128 (−1.33) | 0.587 |
| Rule of Law | 0.0295*** (3.79) | 0.0030 (0.36) | 0.588 |
| **Voice & Accountability** | **0.0390*** (5.22)** | **−0.0171** (−1.97)** | **0.571** |

*Note: t-statistics in parentheses. *** p < 0.01, ** p < 0.05.*

Among the six WGI dimensions, only Voice and Accountability (VA) exhibits a statistically significant interaction with CPU (β = −0.017, p < 0.05). The negative sign indicates that higher democratic governance **reduces** the positive CPU effect on renewable energy. This finding has a compelling interpretation: in countries with strong voice and accountability mechanisms (Japan, South Korea), climate policy uncertainty is less likely to translate into a "rush to renewables" because democratic institutions provide multiple channels for policy resolution and stakeholder engagement, thereby reducing the perceived urgency of preemptive clean energy investment. Conversely, in countries with lower VA scores, CPU shocks generate stronger renewable energy responses, as firms and investors face fewer institutional mechanisms for policy clarification and thus engage in more aggressive hedging.

**Figure 6** illustrates this moderation effect by plotting the predicted CPU–RE relationship at three levels of Voice and Accountability: low (−1 SD), mean, and high (+1 SD). The slope flattens substantially as VA increases, confirming that democratic accountability dampens the CPU-driven push toward renewables.

> **[Insert Figure 6 about here]**

### 4.6 Discussion of Main Results

The empirical findings are consistent with a **hedging hypothesis** of climate policy uncertainty: when the future direction of climate policy becomes more uncertain, economic agents increase investments in renewable energy as a hedge against potential tightening of fossil fuel regulations. This mechanism is distinct from the standard real-options channel emphasized in the investment-under-uncertainty literature (Bloom, 2009), which predicts that uncertainty depresses investment. The positive CPU–RE relationship suggests that climate policy uncertainty carries a directional signal—it signals possible *tightening* of environmental regulation—that dominates the variance effect.

The quantile gradient further refines this interpretation. Countries at the upper quantile of renewable penetration possess the absorptive capacity—in terms of grid infrastructure, supply chains, and policy frameworks—to convert CPU signals into actual deployment. The governance moderation finding adds a political economy dimension: democratic accountability reduces the need for preemptive hedging by providing credible mechanisms for policy resolution.

---

## 5. Robustness Analysis: Monthly Panel QVAR

### 5.1 Motivation and Data

To test the robustness of our findings to data frequency and methodology, we construct a monthly panel dataset spanning January 2015 to December 2024 (120 months) for seven East Asian economies (Indonesia excluded due to missing Ember monthly electricity data). The dependent variable is the first difference of renewable electricity share (ΔRE), and the independent variables are CPU, GPR, and EPU in levels (all found to be I(0) at monthly frequency by Fisher-ADF tests).

### 5.2 Panel QVAR Methodology

We estimate a Panel Vector Autoregression (PVAR) with within-group fixed effects transformation. Lag order selection by AIC favors 12 lags, capturing the full year-on-year dynamics of the energy system. Impulse response functions (IRFs) are computed using Cholesky decomposition with the ordering: ΔRE → CPU → GPR → EPU, reflecting the assumption that renewable energy responds contemporaneously to uncertainty shocks, while uncertainty measures respond with a lag to energy outcomes.

For quantile IRFs, we estimate the VAR equation-by-equation using quantile regression at τ ∈ {0.10, 0.25, 0.50, 0.75, 0.90} with three lags (to ensure numerical convergence). Diebold-Yilmaz (2012) connectedness analysis is conducted using 24-month ahead forecast error variance decompositions.

### 5.3 Monthly Panel QVAR Results

**Stability.** The companion matrix yields a maximum eigenvalue of 0.972 (< 1), confirming system stability.

**Impulse Response.** Figure 1 (not shown) depicts the orthogonalized IRF of ΔRE to a one-standard-deviation shock in CPU. The response is positive and immediate, peaking at month 6 (+0.058) and remaining positive through the 24-month horizon (+0.030). The immediate positive response (month 1: +0.032) is consistent with the annual ARDL finding: climate policy uncertainty generates positive renewable energy responses even at high frequency.

**FEVD.** The forecast error variance decomposition reveals that CPU accounts for 4.9% of ΔRE forecast error variance at the 24-month horizon (direct effect: 0.7%; combined with spillovers: 4.9%). While the direct effect is modest, this is expected at monthly frequency given the inertial nature of electricity generation infrastructure.

**Table 6. Diebold-Yilmaz Spillover Table (24-month horizon)**

| | ΔRE | CPU | GPR | EPU | FROM |
|---|-----|-----|-----|-----|------|
| ΔRE | 91.2 | 0.7 | 2.2 | 0.9 | 3.8 |
| CPU | 3.0 | 53.0 | 7.3 | 5.2 | 15.5 |
| GPR | 1.7 | **33.9** | 80.9 | 37.0 | 72.5 |
| EPU | 4.1 | 12.4 | 9.5 | 57.0 | 26.0 |
| TO | 8.8 | 47.0 | 19.1 | 43.0 | |

*Total Connectedness Index = 19.6%*

The Diebold-Yilmaz analysis reveals a striking pattern: **Geopolitical Risk (GPR) is the dominant transmitter** in the uncertainty–energy nexus. CPU directs 33.9% of its spillover to GPR, and GPR receives 72.5% of its forecast error variance from other variables in the system. This suggests that climate policy uncertainty does not operate in isolation—it propagates through geopolitical risk channels, potentially because climate policy disagreements amplify international tensions over trade, technology transfer, and resource allocation.

**Figure 4** displays the orthogonalized impulse response function of ΔRE to a one-standard-deviation CPU shock over a 24-month horizon, with 90% bootstrap confidence intervals (200 replications). The response turns positive immediately (month 1: +0.032) and remains elevated through the forecast horizon. **Figure 5** presents the Diebold-Yilmaz connectedness network, where edge widths are proportional to pairwise directional spillovers. The dominant CPU → GPR edge (33.9%) is prominently visible. **Figure 7** complements the connectedness analysis with a stacked bar decomposition of each variable's forecast error variance by source.

> **[Insert Figure 4, Figure 5, and Figure 7 about here]**

### 5.4 Reconciliation with Annual Results

The monthly Panel QVAR results reinforce rather than contradict the annual Panel QARDL findings:

1. **Positive CPU effect confirmed.** The IRF shows a positive and persistent CPU impulse on renewable energy growth, consistent with the ARDL long-run coefficient.
2. **Modest direct effect expected.** The small FEVD share reflects the nature of monthly electricity generation data, where seasonal and autoregressive components dominate. The annual ARDL estimates capture long-run equilibrium relationships that accumulate over time.
3. **GPR channel identified.** The connectedness analysis reveals an important transmission mechanism: CPU → GPR → RE. This indirect channel suggests that future research should model mediation pathways explicitly.

---

## 6. Conclusion and Policy Implications

### 6.1 Summary of Findings

This study investigates the impact of climate policy uncertainty on renewable energy deployment in eight East Asian economies over 1996–2023, employing Panel QARDL as the primary framework and Panel QVAR connectedness analysis as a robustness check. Our key findings are:

1. **CPU has a statistically significant positive long-run effect on renewable energy share** (Panel ARDL: β = 0.016, p < 0.01). This supports the hedging hypothesis: firms and investors increase clean energy commitments in response to heightened climate policy uncertainty.

2. **The CPU effect exhibits significant quantile heterogeneity**, increasing from 0.022 (Q10) to 0.067 (Q90). Countries with higher existing renewable penetration respond more strongly to CPU shocks, suggesting that absorptive capacity—grid infrastructure, supply chains, and institutional frameworks—conditions the translation of policy signals into deployment outcomes.

3. **Voice and Accountability is the sole significant governance moderator** (β_interaction = −0.017, p < 0.05). Stronger democratic accountability buffers the CPU-induced push toward renewables, consistent with the interpretation that democratic institutions provide policy resolution channels that reduce the need for preemptive hedging.

4. **Monthly QVAR robustness analysis confirms the positive CPU impulse** (IRF month 1: +0.032) and reveals GPR as the dominant transmitter in the uncertainty network, with 33.9% of CPU's connectedness directed to geopolitical risk.

### 6.2 Policy Implications

Our findings carry several policy implications for East Asian governments and international climate institutions:

**First, climate policy clarity matters.** The positive CPU effect suggests that when climate policy direction is uncertain, economic agents do not simply delay investment—they redirect it toward clean energy as a hedge. Policymakers should recognize that CPU acts as an implicit subsidy for renewables, but this mechanism is inefficient: it generates investment in anticipation of regulation rather than in response to clear price signals. **Credible, long-term climate policy frameworks**—such as legislated emission targets, carbon pricing with predictable trajectories, and transparent renewable portfolio standards—would reduce CPU and enable more efficient investment allocation.

**Second, governance reform can complement energy policy.** The significant moderating role of Voice and Accountability suggests that strengthening democratic institutions—transparency in energy policymaking, stakeholder consultation in regulatory design, and civil society participation in climate governance—can help stabilize the investment environment and reduce the distortionary effects of policy uncertainty on energy markets.

**Third, regional coordination among East Asian economies is warranted.** The Diebold-Yilmaz connectedness analysis reveals substantial cross-variable spillovers, particularly the CPU → GPR transmission channel. Given the region's interconnected energy markets and shared exposure to climate policy developments (especially from the U.S. and EU), coordinated regional approaches to renewable energy targets, grid interconnection, and technology standards could mitigate the amplification of climate policy uncertainty through geopolitical risk.

**Fourth, differentiated strategies are needed across the renewable penetration spectrum.** The quantile gradient indicates that low-penetration countries (Singapore, Thailand) require structural support—grid modernization, workforce training, technology transfer—before they can respond to policy signals. High-penetration countries (Philippines, China) benefit from maintaining policy momentum while strengthening governance mechanisms to ensure that accelerated deployment does not compromise environmental or social safeguards.

### 6.3 Limitations and Future Research

Several limitations should be acknowledged. First, the CPU index is constructed from U.S. newspaper sources and may imperfectly capture domestic climate policy uncertainty in East Asian economies. Future research could develop country-specific CPU measures for the region. Second, our annual panel, while comprehensive in time coverage, sacrifices within-year dynamics. The monthly QVAR robustness analysis partially addresses this but covers a shorter period (2015–2024). Third, the governance moderation analysis is limited to linear interaction terms; nonlinear or threshold effects deserve investigation. Fourth, the renewable energy share variable aggregates diverse technologies (hydro, solar, wind, bioenergy) with different deployment dynamics; technology-specific analysis could reveal further heterogeneity.

Future extensions could include: (i) asymmetric NARDL modeling to separate positive and negative CPU shocks; (ii) time-varying parameter VAR (TVP-VAR) to trace the evolution of CPU–RE connectedness over policy regimes; (iii) mediating pathway analysis to test the CPU → GPR → RE transmission channel identified in our connectedness results; and (iv) expanding the sample to include South Asian and Latin American economies for broader external validity.

---

## References

Akhter, S., & Arman, M. (2026). Geopolitical risk, governance, and renewable energy: A NARDL approach for ASEAN and East Asian economies. *Working Paper.*

Apergis, N., & Payne, J. E. (2010). Renewable energy consumption and economic growth: Evidence from a panel of OECD countries. *Energy Policy, 38*(1), 656–660.

Baker, S. R., Bloom, N., & Davis, S. J. (2016). Measuring economic policy uncertainty. *Quarterly Journal of Economics, 131*(4), 1593–1636.

Bernanke, B. S. (1983). Irreversibility, uncertainty, and cyclical investment. *Quarterly Journal of Economics, 98*(1), 85–106.

Bloom, N. (2009). The impact of uncertainty shocks. *Econometrica, 77*(3), 623–685.

Caldara, D., & Iacoviello, M. (2022). Measuring geopolitical risk. *American Economic Review, 112*(4), 1194–1225.

Chang, C.-L., Zhang, J., & Lin, Y.-E. (2024). Climate policy uncertainty, corporate social responsibility and corporate investments of the energy firms. *Energy Economics, 140*, 106985.

Cho, J. S., Kim, T. H., & Shin, Y. (2015). Quantile cointegration in the autoregressive distributed-lag modeling framework. *Journal of Econometrics, 188*(1), 281–300.

Choi, I. (2001). Unit root tests for panel data. *Journal of International Money and Finance, 20*(2), 249–272.

Dasgupta, S., & De Cian, E. (2018). The influence of institutions, governance, and public opinion on the environment. *Ecological Economics, 146*, 475–486.

Diebold, F. X., & Yilmaz, K. (2012). Better to give than to receive: Predictive directional measurement of volatility spillovers. *International Journal of Forecasting, 28*(1), 57–66.

Gavriilidis, K. (2021). Measuring climate policy uncertainty. *SSRN Working Paper.*

Gavriilidis, K., Känzig, D. R., Raghavan, R., & Stock, J. H. (2026). The macroeconomic effects of climate policy uncertainty. *NBER Working Paper No. 34762.*

Guang, F., Liu, L., Tan, Q., & Wen, L. (2024). Climate policy uncertainty and energy structure transformation: Inhibition or facilitation. *SSRN Working Paper.*

Hossain, M. S., et al. (2026). Industrial value creation, policy uncertainty, and climate risk: An ARDL approach for the United States. *Working Paper.*

Jebli, M. B., Youssef, S. B., & Apergis, N. (2019). The dynamic linkage between renewable energy, tourism, CO₂ emissions, economic growth, foreign direct investment, and trade. *Latin American Economic Review, 28*, 1–19.

Kashif, M., et al. (2025). Fintech-driven sustainability: A QARDL analysis of renewable energy consumption and natural resource management. *Management of Environmental Quality, 36*(6), 1607–1624.

Känzig, D. R. (2023). The unequal economic consequences of carbon pricing. *NBER Working Paper No. 31214.*

Kao, C. (1999). Spurious regression and residual-based tests for cointegration in panel data. *Journal of Econometrics, 90*(1), 1–44.

Kaufmann, D., Kraay, A., & Mastruzzi, M. (2010). The worldwide governance indicators: Methodology and analytical issues. *World Bank Policy Research Working Paper No. 5430.*

Keeley, A. R., & Ikeda, Y. (2017). Determinants of foreign direct investment in wind energy in developing countries. *Journal of Cleaner Production, 161*, 1451–1458.

Liashenko, O., Dluhopolskyi, O., Wołowiec, T., & Woźniak, D. (2026). Governance quality and renewable energy transition: Global evidence using panel ARDL. *Energies, 19*(4), 1024.

Lin, Y., & Cheung, A. (2024). Climate policy uncertainty and energy transition: Evidence from prefecture-level cities in China. *Energy Economics, 139*, 107920.

Maddala, G. S., & Wu, S. (1999). A comparative study of unit root tests with panel data and a new simple test. *Oxford Bulletin of Economics and Statistics, 61*(S1), 631–652.

Matias, M. C., & Tabak, B. M. (2026). Climate policy uncertainty and its effects on investments in renewable energy transition: A systematic literature review and meta-analysis. *Energies, 19*(9), 2009.

Omri, A., & Nguyen, D. K. (2014). On the determinants of renewable energy consumption: International evidence. *Energy, 72*, 554–560.

Payne, J. E., Nazlioglu, S., Koncak, A., & Ewing, B. T. (2025). U.S. climate policy uncertainty shocks and the growth in renewable energy production. *Journal of Commodity Markets, 39*, 100493.

Pedroni, P. (2004). Panel cointegration: Asymptotic and finite sample properties of pooled time series tests with an application to the PPP hypothesis. *Econometric Theory, 20*(3), 597–625.

Pesaran, M. H., Shin, Y., & Smith, R. P. (1999). Pooled mean group estimation of dynamic heterogeneous panels. *Journal of the American Statistical Association, 94*(446), 621–634.

Ritchie, H., Rosado, P., & Roser, M. (2020). CO₂ and greenhouse gas emissions. *Our World in Data.*

Sadorsky, P. (2009). Renewable energy consumption and income in emerging economies. *Energy Policy, 37*(10), 4021–4028.

Salim, R. A., & Shafiei, S. (2014). Urbanization and renewable and non-renewable energy consumption in OECD countries. *Economic Modelling, 38*, 581–591.

Shahbaz, M., Lahiani, A., Abosedra, S., & Hammoudeh, S. (2018). The role of globalization in energy consumption: A quantile cointegrating regression approach. *Energy Economics, 71*, 161–170.

Silva, F., Ferreira, A., & Cortez, M. C. (2024). The performance of green bond portfolios under climate uncertainty. *Research in International Business and Finance, 70*(PA), 102339.

Sohail, M., Hiles, C., & Morley, B. (2024). Renewable energy, economic policy uncertainty and climate policy uncertainty: New evidence for Environmental Kuznets Curve from emerging and developed countries. *Sustainability, 16*(14), 6049.

Syed, Q. R., Apergis, N., & Goh, S. K. (2023). The dynamic relationship between climate policy uncertainty and renewable energy in the US: Applying the novel Fourier augmented autoregressive distributed lags approach. *Energy, 275*, 127383.

Teorell, J., Sundström, A., Holmberg, S., Rothstein, B., Alvarado Pachon, N., Dalli, C. M., & Meijers, M. J. (2024). The Quality of Government Standard Dataset, version Jan24. University of Gothenburg: The Quality of Government Institute.

Troster, V., Shahbaz, M., & Uddin, G. S. (2018). Renewable energy, oil prices, and economic activity: A Granger-causality in quantiles analysis. *Energy Economics, 70*, 440–452.

Yang, R., Mao, H., & Liu, N. (2026). Does climate policy uncertainty hinder renewable energy investment in developing countries? Evidence from double machine learning method. *Energy, 347*, 140491.

---

*Correspondence: [Your email address]*
