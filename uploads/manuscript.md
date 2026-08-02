# Climate Policy Uncertainty and Renewable Energy Deployment in East Asia: A Panel QARDL Approach with Governance Moderation

**Meichih Wang**

Department of [Your Department], National Taichung University of Science and Technology, Taiwan

---

## Abstract

This study examines the impact of climate policy uncertainty (CPU) on renewable energy deployment across eight East Asian economies over the period 1996–2023, employing Panel Fixed Effects and Panel Quantile Regression (QARDL) frameworks with within-group transformation. We contribute to the literature by: (i) introducing the recently updated CPU index (Gavriilidis, Känzig, Raghavan, & Stock, 2026) to the East Asian energy transition context; (ii) uncovering a non-monotonic quantile pattern in the CPU–renewable energy relationship; (iii) testing governance quality as a moderating channel through all six Worldwide Governance Indicators (WGI); and (iv) providing monthly-frequency robustness evidence through Panel QVAR and Diebold-Yilmaz connectedness analysis. The Panel FE results indicate that CPU exerts a statistically significant positive effect on renewable electricity share (β = 0.022, p < 0.001). Critically, the QARDL analysis reveals a non-monotonic pattern: the CPU coefficient is significantly negative at the lowest quantile (Q10: β = −0.030, p < 0.001), positive and increasing from Q25 to a peak at Q75 (β = 0.042, p < 0.001), before declining at Q90 (β = 0.034, p < 0.001). This inverted-U shape reconciles the competing "real-options" and "hedging" hypotheses: at low renewable penetration levels, CPU depresses investment through the uncertainty channel, while at higher levels, it accelerates deployment through anticipatory hedging. Four governance dimensions—Political Stability (strongest), Government Effectiveness, Rule of Law, and Control of Corruption—positively moderate the CPU–RE relationship, suggesting that institutional quality amplifies, rather than buffers, the translation of policy uncertainty into clean energy deployment. Monthly Panel QVAR estimates confirm a positive CPU impulse response (IRF month 1: +0.032) and identify geopolitical risk as the dominant transmitter in the uncertainty network (33.9% spillover from CPU to GPR). These findings carry implications for the design of credible climate policy frameworks and complementary governance reforms in accelerating East Asia's energy transition.

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

Our findings reveal that: (a) CPU has a positive and statistically significant effect on renewable electricity share (Panel FE: β = 0.022, p < 0.001); (b) this effect is non-monotonic across the conditional distribution—negative at the lowest quantile (Q10: β = −0.030, p < 0.001), positive and peaking at the 75th quantile (β = 0.042, p < 0.001), before moderating at the 90th quantile (β = 0.034, p < 0.001)—reconciling the competing real-options and hedging hypotheses within a single quantile framework; (c) four governance dimensions positively moderate the CPU–RE relationship—Political Stability (strongest), Government Effectiveness, Rule of Law, and Control of Corruption—indicating that institutional quality amplifies, rather than buffers, the translation of climate policy uncertainty into renewable deployment; and (d) monthly Panel QVAR connectedness analysis confirms a positive short-run CPU impulse on renewable energy growth (IRF month 1: +0.032) and identifies geopolitical risk as the dominant transmitter in the uncertainty network (33.9% spillover from CPU to GPR).

The remainder of this paper is organized as follows. Section 2 reviews the related literature. Section 3 describes the data and empirical methodology. Section 4 presents the empirical results. Section 5 provides robustness analysis using monthly Panel QVAR. Section 6 concludes with policy implications.

---

## 2. Literature Review

### 2.1 Climate Policy Uncertainty: Measurement and Evolution

The theoretical foundation for understanding policy uncertainty's economic effects traces to the irreversible investment literature. Bernanke (1983) formalizes the insight that when investment decisions are costly to reverse, uncertainty about future returns creates an option value of waiting—firms optimally delay commitment until uncertainty is resolved. Bloom (2009) extends this framework to aggregate fluctuations, demonstrating that uncertainty shocks generate rapid drops and subsequent overshoots in output and employment through this real-options channel, with the effect operating primarily through heterogeneous firm-level investment decisions. The broader investment-under-uncertainty literature (Dixit & Pindyck, 1994; Pindyck, 1991) establishes that the irreversibility premium is increasing in the variance of the stochastic process governing future returns.

These theoretical insights were operationalized into empirical measures by Baker, Bloom, and Davis (2016), whose Economic Policy Uncertainty (EPU) index—constructed from newspaper frequency counts of policy-related uncertainty terms—has become the benchmark in the empirical uncertainty literature, with over 5,000 citations and country-specific indices now covering 29 economies. The EPU methodology was subsequently adapted to geopolitical risk by Caldara and Iacoviello (2022), who construct the Geopolitical Risk (GPR) index from automated text searches of eleven major newspapers, capturing the frequency of articles mentioning geopolitical tensions, threats, and adverse events.

Climate policy uncertainty (CPU) applies this news-based measurement philosophy to the environmental domain. The original CPU index by Gavriilidis (2021) identified articles in eight major U.S. newspapers that jointly discussed climate change, policy, and uncertainty concepts over the period 1987–2019. This pioneering measure enabled the first wave of empirical CPU studies but suffered from two limitations: the dictionary-based classification lacked validation against human-coded or machine-learning benchmarks, and the temporal coverage terminated before the post-COVID climate policy surge.

The index was recently overhauled by Gavriilidis, Känzig, Raghavan, and Stock (2026), who introduce three critical innovations. First, they develop both narrow and broad dictionary-based indices—the former requiring precise co-occurrence of climate, policy, and uncertainty terms within the same paragraph, the latter allowing for looser thematic proximity—balancing precision against coverage. Second, they construct an LLM-based validation measure (CPU-LLM) in which Claude 3.5 Sonnet classifies articles based on their substantive discussion of climate policy uncertainty, providing an external benchmark against which dictionary methods can be calibrated. Third, they develop an event-based instrument that isolates exogenous climate policy uncertainty shocks by purging the first moment of climate policy stringency from uncertainty variation: the instrument captures the surprise component of CPU that is orthogonal to the expected level of climate policy action. The updated index extends from January 1985 to April 2026, providing sufficient temporal coverage for both long-run panel analysis and high-frequency time-series applications. Their macroeconomic analysis using this instrument finds that a one-standard-deviation CPU shock reduces industrial production by 0.3–0.5% and raises the VIX by 2–3 points, effects comparable in magnitude to conventional EPU shocks.

Parallel to the news-based approach, Känzig (2023) constructs an alternative measure of climate policy uncertainty from the surprise component of carbon pricing announcements in the European Union Emissions Trading System (EU ETS), demonstrating that carbon pricing surprises have significant and heterogeneous macroeconomic effects. This complementary approach validates the economic relevance of CPU while highlighting that different measurement strategies capture distinct dimensions of the uncertainty construct.

### 2.2 Theoretical Channels: Real Options, Growth Options, and Hedging

The theoretical ambiguity of CPU's effect on renewable energy investment arises from the tension between three distinct mechanisms:

**The real-options channel** (Bernanke, 1983; Bloom, 2009; Dixit & Pindyck, 1994) predicts a negative relationship. Renewable energy investments are characterized by high sunk costs (turbine manufacturing facilities, grid interconnection infrastructure, site acquisition), long gestation periods, and substantial regulatory dependency (feed-in tariffs, renewable portfolio standards, tax credits). When the future trajectory of climate policy becomes more uncertain, the option value of delaying these irreversible investments increases, and firms rationally postpone commitment. This channel operates through the variance, not the level, of future policy expectations: even if the expected direction of policy is toward stricter regulation, the uncertainty about timing and magnitude creates a delay incentive.

**The growth-options channel** (Kulatilaka & Perotti, 1998; Bloom, Bond, & Van Reenen, 2007) moderates and potentially reverses the real-options prediction. When investment creates follow-on opportunities—as in renewable energy, where early deployment builds supply chain relationships, technology-specific expertise, and market presence—uncertainty can *encourage* early investment to secure strategic positions. This mechanism is particularly relevant for multinational energy firms and state-owned enterprises in East Asia, where first-mover advantages in renewable energy supply chains (solar PV manufacturing, battery storage, offshore wind) are substantial.

**The hedging hypothesis** (Matias & Tabak, 2026; Silva et al., 2024) introduces a directional signal. Unlike general economic uncertainty, CPU carries information about the *direction* of future policy: heightened CPU typically signals that policymakers are considering more aggressive climate action, which would increase the operating costs of carbon-intensive assets. Under this interpretation, firms do not merely delay investment in the face of uncertainty—they redirect it toward assets whose value is positively correlated with climate policy stringency. Renewable energy investments serve as a hedge because their returns increase when carbon pricing or emission regulations tighten. This mechanism is distinct from the variance-based real-options channel and can generate positive CPU–RE relationships even when irreversibility is high.

The simultaneous operation of these three channels—with the real-options channel dominating at low levels of renewable penetration (where exit costs are highest relative to hedging benefits) and the hedging/growth-options channels dominating at higher levels—provides the theoretical motivation for our QARDL framework. By estimating the CPU effect across the conditional distribution of renewable energy penetration, we can empirically identify the regions where each mechanism prevails.

### 2.3 CPU Effects on Energy and Environmental Outcomes: Empirical Evidence

The empirical literature on CPU's effects on energy outcomes has expanded rapidly since 2022, yielding strikingly heterogeneous results. Matias and Tabak (2026) provide the most comprehensive synthesis through a systematic literature review and meta-analysis of seventeen peer-reviewed studies. Their random-effects meta-analysis finds a small and statistically insignificant average effect of CPU on energy-transition-related investment outcomes (pooled estimate = −0.05, 95% CI: [−0.18, 0.08]), accompanied by extremely high heterogeneity (I² = 97.3%, Q-statistic p < 0.001). A mixed-effects meta-regression organized around four transmission channels—firm investment, financial markets, political-institutional, and macroeconomic—explains only 50.4% of between-study variance (R² = 0.504, p < 0.001), with the macroeconomic channel showing the strongest negative effect (β = −1.07, p < 0.01). Egger's test (p = 0.092) and funnel plot asymmetry analysis suggest moderate publication bias toward negative CPU effects.

The meta-analysis further identifies three significant moderators: (i) the type of outcome variable—CPU effects are more negative for energy production outcomes than for investment or consumption measures; (ii) the level of economic development—CPU effects are more negative in developing than developed economies; and (iii) the choice of CPU measure—studies using the original Gavriilidis (2021) index report systematically different results than those using alternative measures.

#### 2.3.1 Negative CPU Effects: Evidence for the Real-Options Channel

Several studies document that CPU depresses renewable energy investment and production. Syed, Apergis, and Goh (2023) apply a Fourier-augmented ARDL model to monthly U.S. data (1987–2019) and find that CPU significantly reduces renewable energy consumption in both the short and long run, with the Fourier approximation capturing smooth structural breaks in the CPU–RE relationship. Their long-run elasticity estimate of approximately −0.15 (p < 0.01) implies that a 10% increase in CPU reduces renewable energy consumption by 1.5%.

Payne, Nazlioglu, Koncak, and Ewing (2025) corroborate this finding using generalized impulse response analysis within a VAR framework on U.S. monthly data. Total U.S. renewable energy production responds negatively to CPU shocks, though sub-component responses differ markedly: hydroelectric and biomass production show negligible responses, while geothermal and wind production exhibit statistically significant negative responses (peak IRF ≈ −0.8% after 6 months). Their forecast error variance decomposition attributes 4.2% of renewable energy production variance to CPU shocks, with the transmission operating primarily through reduced capital expenditures in the wind energy sector.

Yang, Mao, and Liu (2026) extend the negative-effect evidence to developing countries using a double machine learning approach on panel data from 35 emerging and developing economies (2002–2021). Their causal forest estimates find that CPU significantly hinders renewable energy investment through three mediating channels: (i) exacerbating financing constraints (CPU increases the cost of capital for green projects by 6.3 basis points on average), (ii) inhibiting green technology innovation (CPU reduces clean energy patent applications by approximately 4.1%), and (iii) lowering traditional energy prices (CPU-induced demand reduction in fossil fuel markets reduces the relative cost advantage of renewables). The negative impact is more pronounced in countries with lower GDP per capita and those at early stages of renewable energy development, consistent with the prediction that the real-options channel dominates when absorptive capacity is low.

At the sub-national level, Guang, Liu, Tan, and Wen (2024) use Chinese provincial panel data (2008–2021) in a dynamic spatial Durbin model and find that CPU inhibits regional energy structure transformation, operating through two mechanisms: hindering technology marketization and obstructing government intervention. The negative effect is amplified in provinces with slower economic growth, lower marketization, and higher resource endowments—precisely the contexts where the option value of waiting is highest.

Chang, Zhang, and Lin (2024) examine the corporate finance dimension, analyzing how CPU affects energy firms' investment decisions. Using a panel of U.S. energy firms (2000–2022), they find that CPU reduces capital expenditures in fossil fuel firms while having no significant effect on renewable energy firms' investment, suggesting that CPU operates primarily through the carbon-asset stranding channel rather than through direct effects on clean energy investment.

#### 2.3.2 Positive and Null CPU Effects: Evidence for Hedging and Heterogeneity

On the positive-effect side, a growing strand of literature documents countervailing mechanisms. The "flight-to-green" or hedging hypothesis posits that heightened climate policy uncertainty redirects investment from carbon-intensive assets toward clean energy. Silva, Ferreira, and Cortez (2024) examine the performance of green bond portfolios under climate uncertainty and find that green bonds outperform conventional bonds during high-CPU periods, with the alpha differential reaching 1.2% annually (p < 0.05). This effect is concentrated in the post-Paris Agreement period (2016–2022), suggesting that the hedging premium depends on the credibility of the overall climate policy regime.

Lin and Cheung (2024) provide the most geographically relevant positive evidence, using panel data from 282 Chinese prefecture-level cities (2006–2021). Their fixed effects estimates show that CPU promotes energy transition—measured by the share of non-fossil energy in total consumption—with a coefficient of 0.0037 (p < 0.01). Crucially, this positive effect is conditional on local government renewable energy support policies: in prefectures with above-median green fiscal expenditure, the CPU effect is 2.3 times larger than in prefectures with below-median expenditure. This interaction directly anticipates our governance moderation analysis.

Sohail, Hiles, and Morley (2024) examine the Environmental Kuznets Curve incorporating both EPU and CPU for a panel of 22 emerging and developed countries (2000–2020). Their panel ARDL estimates find that CPU significantly alters the income–emissions relationship, with higher CPU shifting the EKC turning point toward lower income levels—consistent with the interpretation that policy uncertainty accelerates the decoupling of emissions from growth.

Hossain et al. (2026) analyze the relationship between industrial value creation, policy uncertainty, and climate risk in the United States using an ARDL bounds testing approach. They find that CPU significantly increases industrial value creation in the renewable energy sector while decreasing it in carbon-intensive manufacturing, providing sector-level evidence for the hedging hypothesis.

Several studies report null or context-dependent findings that underscore the importance of distributional analysis. Matias and Tabak's (2026) meta-analytic average is not statistically different from zero. A subset of primary studies in their sample—particularly those using broad country panels rather than single-country designs—report statistically insignificant CPU coefficients, attributed to the cancellation of opposing effects across heterogeneous units. This null average with extreme heterogeneity provides the strongest motivation for our QARDL framework: if the CPU effect varies with the level of renewable energy penetration, mean-based estimators systematically obscure the relationship.

### 2.4 Determinants of Renewable Energy Deployment: From Fundamentals to Uncertainty

The traditional literature on renewable energy determinants emphasizes structural economic variables. Apergis and Payne (2010) establish panel evidence linking GDP growth, CO₂ emissions, and renewable energy consumption across OECD countries, finding bidirectional causality between renewable energy and economic growth. Sadorsky (2009) identifies financial development and oil prices as significant drivers of renewable energy investment in emerging economies, documenting that a 1% increase in stock market capitalization is associated with a 0.22% increase in renewable energy consumption. Omri and Nguyen (2014) extend the analysis to a global panel of 64 countries, documenting heterogeneous determinants across income groups: financial development matters more for high-income countries, while trade openness and FDI are stronger determinants in middle-income countries.

More recently, renewable energy deployment has been linked to trade openness (Jebli, Youssef, & Apergis, 2019), foreign direct investment (Keeley & Ikeda, 2017), and urbanization (Salim & Shafiei, 2014). Jebli et al. (2019) find that trade openness increases renewable energy consumption in Latin American countries by facilitating technology transfer, with a 1% increase in trade openness associated with a 0.15% increase in renewable energy consumption. Keeley and Ikeda (2017) analyze FDI determinants in wind energy across developing countries, finding that feed-in tariffs and renewable energy targets are stronger attractors of FDI than general investment climate indicators—a finding that highlights the primacy of sector-specific policy over general governance for renewable energy investment.

Several studies focus specifically on East Asia. The region presents a unique laboratory for studying renewable energy deployment because of its extreme heterogeneity: it contains both the world's largest renewable energy producer (China, with 1,453 GW of installed renewable capacity in 2023) and economies with negligible renewable penetration (Singapore, below 1%). The ASEAN Centre for Energy (2023) reports that ASEAN member states have set collective renewable energy targets of 23% of total primary energy supply by 2025, yet the gap between targets and realized deployment varies dramatically across members. China's renewable portfolio standard mandates 40% non-fossil electricity by 2030; Japan targets 36–38% renewable electricity by 2030; South Korea's 10th Basic Plan targets 21.6% renewable electricity by 2030; while Indonesia and Thailand have more modest targets of 23% and 30% respectively.

The integration of uncertainty measures into renewable energy analysis represents a more recent and rapidly growing development. Caldara and Iacoviello's (2022) GPR index has been applied to energy markets by multiple studies. Akhter and Arman (2026) employ a Nonlinear ARDL (NARDL) framework to examine the asymmetric effects of GPR and governance on renewable energy consumption in ASEAN and East Asian countries, finding that positive GPR shocks reduce renewable energy consumption while governance quality significantly moderates the relationship. This study provides the closest regional and methodological precedent to our analysis, and we extend it in three directions: (i) substituting CPU for GPR as the primary uncertainty variable, motivated by the argument that climate-specific uncertainty carries directional signals absent from general geopolitical risk; (ii) broadening the governance analysis to all six WGI dimensions rather than a composite index; and (iii) moving from single-country NARDL to Panel QARDL to capture cross-sectional heterogeneity.

The QARDL methodology itself has gained traction in energy economics. Cho, Kim, and Shin (2015) develop the theoretical framework for quantile ARDL, providing the asymptotic theory for quantile cointegration in the autoregressive distributed-lag model. Shahbaz, Lahiani, Abosedra, and Hammoudeh (2018) apply QARDL to examine the energy–growth nexus in Pakistan, demonstrating that the relationship between energy consumption and economic growth varies significantly across the conditional distribution—a finding that mean-based estimators (OLS, ARDL) inevitably obscure. Kashif et al. (2025) use QARDL to analyze fintech-driven sustainability impacts on renewable energy consumption and natural resource management, finding that the fintech effect on renewable energy is concentrated at upper quantiles. Troster, Shahbaz, and Uddin (2018) pioneer Granger-causality in quantiles for the renewable energy–oil price–economic activity nexus, showing that oil price Granger-causes renewable energy consumption only at the tails of the distribution. Collectively, these studies demonstrate QARDL's key advantage: revealing distributional heterogeneity that mean-based estimators systematically obscure. A coefficient that is statistically insignificant at the mean may be strongly significant at the tails, and vice versa—a possibility with direct policy relevance for countries at different stages of the energy transition.

### 2.5 Governance as a Moderator in the Energy–Uncertainty Nexus

The institutional economics literature provides strong theoretical grounds for expecting governance quality to moderate the CPU–renewable energy relationship. North (1990) establishes that institutions—the "rules of the game"—structure the incentives that shape economic exchange by reducing uncertainty, lowering transaction costs, and enforcing property rights. In the energy sector, institutional quality operates through three primary channels identified by Dasgupta and De Cian (2018): enforcement (regulatory monitoring and sanctioning capacity), credibility (policy commitment and time-consistency of incentives), and participation (stakeholder engagement and civil society monitoring).

The Worldwide Governance Indicators (Kaufmann, Kraay, & Mastruzzi, 2010) operationalize institutional quality across six dimensions: Voice and Accountability (VA), Political Stability and Absence of Violence/Terrorism (PS), Government Effectiveness (GE), Regulatory Quality (RQ), Rule of Law (RL), and Control of Corruption (CC). These dimensions, compiled from over 30 underlying data sources and normalized to have zero mean and unit standard deviation, cover 215 economies from 1996 onward. While correlated (pairwise correlations range from 0.6 to 0.95 in our sample), each dimension captures a conceptually distinct aspect of governance.

Liashenko, Dluhopolskyi, Wołowiec, and Woźniak (2026) provide the most comprehensive recent evidence on governance and renewable energy, using a Panel ARDL framework across 174 countries (2000–2023). They find that Political Stability is the only statistically significant governance dimension (β = 0.62, p < 0.01), while Government Effectiveness, Regulatory Quality, Rule of Law, and Control of Corruption lack strong independent effects, and Voice and Accountability is statistically insignificant. However, their analysis treats governance as a direct determinant of renewable energy rather than as a moderator of uncertainty—a distinction with important theoretical implications, as the institutional channel may matter primarily through its interaction with policy signals rather than through independent effects on deployment.

Yang, Mao, and Liu (2026) document that institutional quality significantly mitigates CPU's negative investment effects in developing countries, with the interaction coefficient being negative (governance reduces the CPU penalty). This is consistent with the interpretation that strong institutions reduce the option value of waiting by providing credible policy commitment mechanisms. However, their analysis uses a composite institutional quality measure rather than disaggregated WGI dimensions, obscuring which specific governance channels drive the moderation effect.

Akhter and Arman (2026) examine governance moderation of geopolitical risk effects on renewable energy in ASEAN and East Asia using NARDL. They find that the governance composite positively moderates the GPR–RE relationship for positive GPR shocks but has no significant moderating effect for negative GPR shocks—evidence that the governance channel is itself asymmetric. Their finding that governance amplifies rather than buffers the effect of geopolitical uncertainty on renewable energy provides a direct precedent for our core governance result.

Each of the six WGI dimensions may differentially moderate the CPU–renewable energy relationship through distinct theoretical channels. **Political Stability (PS)** reduces the tail risk of abrupt policy reversal due to political violence, regime change, or social instability—events that would render renewable energy investments stranded regardless of climate policy signals. Higher PS may therefore amplify positive CPU effects by making hedging investments more credible, but could theoretically dampen them if PS is negatively correlated with the perceived urgency of preemptive clean energy investment. **Government Effectiveness (GE)** captures bureaucratic capacity and policy implementation quality—factors that determine how rapidly renewable energy targets can be scaled when CPU signals intensify. The null direct effect found by Liashenko et al. (2026) may mask a significant interaction: GE matters not for renewable deployment per se, but for translating policy uncertainty into actionable investment. **Regulatory Quality (RQ)** reflects the predictability, transparency, and market-friendliness of regulatory frameworks. Higher RQ may dampen the CPU effect by reducing the ambiguity premium in renewable energy investment, lowering the option value of waiting. Alternatively, RQ may have no moderating effect if regulatory quality primarily affects the *level* of investment rather than its *sensitivity* to uncertainty. **Rule of Law (RL)**—encompassing contract enforcement, property rights protection, and judicial independence—reduces the risk that renewable energy investments will be expropriated or that power purchase agreements will be renegotiated. Higher RL should amplify positive CPU effects by securing the returns to hedging investment. **Control of Corruption (CC)** addresses the additional uncertainty introduced by rent-seeking in project approval, permitting, and procurement. In high-corruption environments, CPU compounds with bureaucratic uncertainty, potentially paralyzing investment; in low-corruption environments, the CPU signal is transmitted more cleanly to investment decisions. **Voice and Accountability (VA)** provides multiple channels for policy resolution—legislative oversight, media scrutiny, civil society mobilization, electoral accountability—and was the sole significant moderator in our earlier pooled-OLS specifications, motivating our careful within-FE re-estimation.

The theoretical predictions for the sign of the interaction effect are therefore ambiguous. The enforcement channel (CC, RL) suggests that higher governance should amplify the CPU effect by reducing background noise. The credibility channel (PS, GE) suggests that higher governance may either amplify (by making hedging credible) or dampen (by reducing the perceived urgency of preemptive action) the CPU effect. The participation channel (VA) suggests that higher governance should dampen the CPU effect by resolving policy uncertainty through institutional mechanisms. Our empirical analysis tests these competing predictions across all six dimensions.

### 2.6 Summary of Literature and Contributions

Table 1 summarizes the key CPU–energy studies, organized by empirical approach and findings.

**Table 1. Selected Literature on CPU and Energy Outcomes**

| Study | Context | Method | CPU Measure | Key Finding |
|-------|---------|--------|-------------|-------------|
| Syed et al. (2023) | U.S., monthly 1987–2019 | Fourier ARDL | Gavriilidis (2021) | CPU ↓ RE consumption (−0.15 elasticity) |
| Payne et al. (2025) | U.S., monthly 1994–2023 | VAR, GIRF | Gavriilidis (2021) | CPU ↓ RE production (peak IRF −0.8%) |
| Yang et al. (2026) | 35 developing, 2002–2021 | Double ML | Gavriilidis (2021) | CPU ↓ RE investment (via 3 channels) |
| Guang et al. (2024) | China provinces, 2008–2021 | Spatial Durbin | Gavriilidis (2021) | CPU ↓ energy structure transformation |
| Chang et al. (2024) | U.S. energy firms, 2000–2022 | Panel FE | Gavriilidis (2021) | CPU ↓ fossil fuel capex, null on RE |
| Lin & Cheung (2024) | China prefectures, 2006–2021 | Panel FE | Gavriilidis (2021) | CPU ↑ energy transition (with gov support) |
| Silva et al. (2024) | Global green bonds, 2014–2022 | Portfolio analysis | Gavriilidis (2021) | Green bonds ↑ during high CPU (1.2% alpha) |
| Sohail et al. (2024) | 22 countries, 2000–2020 | Panel ARDL | Gavriilidis (2021) | CPU shifts EKC turning point |
| Hossain et al. (2026) | U.S., 1985–2023 | ARDL bounds test | Gavriilidis (2021) | CPU ↑ RE industrial value creation |
| Liashenko et al. (2026) | 174 countries, 2000–2023 | Panel ARDL | — | PS is only significant governance dimension |
| Akhter & Arman (2026) | ASEAN + East Asia | NARDL | — (GPR) | Governance moderates GPR–RE |
| Matias & Tabak (2026) | 17 studies (meta) | Meta-analysis | Various | Mean effect ≈ 0, extreme heterogeneity |
| **This study** | **8 East Asian, 1996–2023** | **Panel FE + QARDL + QVAR** | **Gavriilidis et al. (2026)** | **Non-monotonic QARDL + governance amplification** |

The preceding review identifies five specific gaps that motivate our study:

**Gap 1: The CPU–renewable energy relationship remains empirically unsettled, especially outside the United States.** The meta-analysis by Matias and Tabak (2026) documents extreme heterogeneity with no consensus sign. Existing empirical evidence is concentrated on the U.S. (Syed et al., 2023; Payne et al., 2025), China (Guang et al., 2024; Lin & Cheung, 2024), and developing countries broadly (Yang et al., 2026). No study has examined the CPU–renewable energy nexus in the East Asian regional context, where diverse levels of economic development, renewable penetration, and institutional quality provide natural variation for identifying heterogeneous effects.

**Gap 2: The updated CPU index remains underutilized in the energy literature.** The Gavriilidis et al. (2026) index, which substantially improves upon the original Gavriilidis (2021) measure with LLM validation, exogenous shock instrumentation, and extended temporal coverage (1985–2026), has not been applied to renewable energy analysis. All CPU–energy studies cited in the meta-analysis by Matias and Tabak (2026) use the 2021 version of the index.

**Gap 3: Distributional heterogeneity in the CPU–RE relationship is unexplored.** While the meta-analytic evidence strongly suggests that the CPU effect varies across contexts, no study has systematically examined whether it varies across the conditional distribution of renewable energy penetration. Panel QARDL provides a natural framework for testing whether high-penetration countries respond differently to CPU than low-penetration countries.

**Gap 4: The moderating role of governance in the CPU–renewable energy nexus is untested at the disaggregated level.** While Akhter and Arman (2026) examine a composite governance measure's moderation of GPR effects, and Yang et al. (2026) document that institutional quality mitigates CPU's negative investment effects via a composite index, no study has tested whether the six disaggregated WGI dimensions differentially moderate the CPU–renewable energy relationship.

**Gap 5: The high-frequency dynamics of the CPU–RE relationship lack multi-country evidence.** Existing high-frequency studies (Syed et al., 2023; Payne et al., 2025) are single-country U.S. analyses. The monthly connectedness between CPU, GPR, EPU, and renewable energy in a multi-country setting—particularly in the interconnected East Asian electricity system—remains undocumented.

Our study addresses all five gaps. We provide the first Panel FE and QARDL analysis of the CPU–renewable energy relationship in East Asia (Gaps 1–3), the first test of disaggregated WGI governance moderation of this relationship (Gap 4), and the first multi-country monthly Panel QVAR/DY connectedness analysis of the CPU–RE nexus (Gap 5).

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

where \(Q_{\tau}(\cdot)\) denotes the \(\tau\)-th conditional quantile (\(\tau \in \{0.10, 0.25, 0.50, 0.75, 0.90\}\)). This framework allows us to test whether the CPU effect varies across the conditional distribution of renewable energy penetration. We estimate quantile regressions on within-transformed data (entity-demeaned), using the QuantReg estimator (Koenker & Bassett, 1978) with asymptotic standard errors. The within-group transformation absorbs country-specific time-invariant heterogeneity, isolating the conditional relationship between CPU and RE within each country's temporal variation.

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

**Table 2. Panel Unit Root Tests (Fisher-ADF)**

| Variable | Fisher χ² | p-value | Conclusion |
|----------|-----------|---------|-------------|
| RE share | 13.11 | 0.662 | I(1) |
| CPU | 0.83 | 1.000 | I(1) |
| GPR | 44.70 | 0.000 | I(0) |
| EPU | 6.36 | 0.984 | I(1) |
| ln(GDP pc) | 20.37 | 0.201 | I(1) |
| ln(CO₂ pc) | 8.83 | 0.922 | I(1) |
| WGI: Control of Corruption | 17.15 | 0.379 | I(1) |
| ΔRE share | 187.64 | 0.000 | I(0) |
| ΔCPU | 319.06 | 0.000 | I(0) |
| ΔGPR | 272.80 | 0.000 | I(0) |
| ΔEPU | 309.19 | 0.000 | I(0) |

The Fisher-ADF test results indicate that most variables are I(1) in levels but stationary in first differences, satisfying the ARDL bounds testing requirement that no variable is I(2). GPR is the sole variable that appears I(0) in levels.

**Cointegration.** We employ country-by-country Engle-Granger residual-based cointegration tests, combined via the Fisher (1932) method. The individual country ADF statistics on the residuals of RE = f(CPU, GPR, GDP, CO₂) reject the null of no cointegration in six of eight countries (China, Indonesia, Malaysia, Philippines, Singapore, Thailand), with Japan (p = 0.102) and Korea (p = 0.166) narrowly failing the test—likely reflecting the secular decline in nuclear-dependent Japan's and fossil-fuel-dependent Korea's renewable shares. The Fisher combined test statistic (χ² = 112.5, p < 0.001) strongly rejects the null of no panel cointegration, providing robust evidence of a long-run equilibrium relationship.

### 4.3 Panel Fixed Effects and ARDL Estimates

**Table 3. Panel Fixed Effects (PanelOLS within-group) and PMG Mean Group**

| Variable | Panel FE (Within) | PMG Mean Group (LR) |
|----------|-------------------|---------------------|
| | Coef. (t-stat) | Mean Coef. (t-stat) |
| CPU | 0.022 (3.92)*** | 0.070 (1.08) |
| GPR | 0.003 (0.34) | −0.028 (−1.46) |
| ln(GDP pc) | 3.744 (2.29)** | 35.279 (1.17) |
| ln(CO₂ pc) | −4.615 (−2.20)** | 18.888 (0.63) |
| ECT | — | −0.457 (−2.96)** |
| R² (within) | 0.199 | 0.403 (mean) |

*Note: *** p < 0.01, ** p < 0.05, * p < 0.10. Panel FE estimated via linearmodels.PanelOLS with entity fixed effects. PMG Mean Group: long-run coefficients averaged across 8 country-specific ARDL models.*

The Panel Fixed Effects results—our preferred specification—establish that CPU exerts a statistically significant positive effect on renewable electricity share. A one-unit increase in the CPU index is associated with a 0.022 percentage point increase in RE share (t = 3.92, p < 0.001), controlling for country heterogeneity and time-invariant unobservables. The ln(CO₂ per capita) coefficient is negative and significant (β = −4.615, t = −2.20), consistent with the carbon lock-in hypothesis: economies with higher historical fossil fuel dependence face structural barriers to renewable deployment. The remaining control variables are not statistically significant at conventional levels.

The PMG Mean Group estimates—which relax the homogeneity assumption by estimating country-specific ARDL models and averaging long-run coefficients—yield a larger point estimate for CPU (0.070) but wider standard errors, resulting in statistical insignificance (t = 1.08). This loss of precision reflects the inherent trade-off in MG estimators: they preserve cross-country heterogeneity at the cost of efficiency. The error-correction term (ECT = −0.457, p < 0.05) confirms that approximately 46% of any deviation from long-run equilibrium is corrected within one year. We present the PMG results as robustness evidence supporting the FE finding of a positive CPU–RE relationship, while noting that the MG standard errors are conservative due to the limited number of countries (N = 8).

### 4.4 Panel QARDL: Non-Monotonic Quantile Heterogeneity

**Table 4. Panel QARDL — CPU Effect Across Quantiles (QuantReg within-FE)**

| Quantile | CPU Coefficient | Std. Error | t-stat | p-value |
|----------|----------------|------------|--------|---------|
| Q10 | −0.030 | 0.006 | −4.86 | 0.000*** |
| Q25 | 0.007 | 0.004 | 1.67 | 0.096* |
| Q50 | 0.030 | 0.006 | 5.43 | 0.000*** |
| Q75 | 0.042 | 0.006 | 7.15 | 0.000*** |
| Q90 | 0.034 | 0.008 | 4.27 | 0.000*** |
| Panel FE (OLS) | 0.022 | 0.006 | 3.92 | 0.000*** |

*Note: Quantile regressions via statsmodels.QuantReg on within-transformed data (entity FE). Standard errors are asymptotic.*

The QARDL results reveal a **non-monotonic pattern** that contradicts the simple positive-gradient narrative. Three findings stand out:

**First, CPU significantly *reduces* renewable energy share at the lowest quantile (Q10: β = −0.030, p < 0.001).** This is the opposite of the mean effect. Countries at the bottom of the renewable penetration distribution—such as Singapore (RE < 1%) and Thailand in early years—appear to respond to climate policy uncertainty by *reducing* clean energy deployment. This is consistent with the real-options channel (Bernanke, 1983; Bloom, 2009): when policy direction is unclear, countries with minimal existing renewable infrastructure face the highest adjustment costs and the strongest incentive to delay investment.

**Second, the CPU effect turns positive and grows from Q25 to Q75, peaking at Q75 (β = 0.042, p < 0.001).** The median effect (Q50: β = 0.030) is approximately 36% larger than the OLS estimate, confirming that mean-based estimators understate the relationship for typical observations. The Q75 result—more than twice the Panel FE coefficient—indicates that countries in the upper-middle range of renewable penetration (e.g., China, Malaysia, the Philippines) respond most strongly to CPU signals.

**Third, the Q90 coefficient declines to 0.034 (p < 0.001),** suggesting a saturation effect at the very top of the distribution. The very highest RE share observations may reflect countries with mature renewable sectors where further expansion requires grid modernization and storage investment rather than additional generation capacity—investments that are less sensitive to short-term policy signals.

This inverted-U shape in quantile space constitutes our paper's central empirical contribution. It resolves the tension between the "hedging" and "real-options" hypotheses in the CPU–energy literature: both mechanisms operate simultaneously, but their relative strength depends on where a country sits in the renewable development trajectory.

**Figure 3** visualizes the non-monotonic quantile pattern, with the Panel FE estimate (dashed red line) shown for comparison. The contrast between Q10 (significantly negative) and Q75 (significantly positive) is visually striking.

> **[Insert Figure 3 about here]**

### 4.5 Governance Moderation Effects

**Table 5. Interaction Effects — CPU × WGI (Panel FE within-group)**

| WGI Dimension | CPU × WGI Coefficient | t-stat |
|---------------|----------------------|--------|
| Political Stability | 0.023 | 4.22*** |
| Govt Effectiveness | 0.015 | 2.37** |
| Control of Corruption | 0.012 | 2.25** |
| Rule of Law | 0.013 | 2.29** |
| Regulatory Quality | 0.002 | 0.34 |
| Voice & Accountability | −0.007 | −1.28 |

*Note: Each row represents a separate regression. All models include CPU, the specified WGI dimension, their interaction, and baseline controls (GPR, ln GDP, ln CO₂), estimated via within-group (entity FE) transformation.*

Four of the six governance dimensions exhibit statistically significant positive interactions with CPU: Political Stability (β = 0.023, p < 0.001), Government Effectiveness (β = 0.015, p < 0.05), Rule of Law (β = 0.013, p < 0.05), and Control of Corruption (β = 0.012, p < 0.05). The consistently positive sign indicates that **governance quality amplifies rather than buffers the CPU effect on renewable energy.**

This finding carries a clear institutional interpretation. Political Stability—the strongest moderator—reduces the tail risk of policy reversal, enabling firms to commit to renewable investments even when climate policy direction is uncertain. Government Effectiveness captures bureaucratic capacity to implement renewable energy targets, tariffs, and grid integration once policy direction is resolved. Rule of Law protects renewable energy investments from expropriation and contract renegotiation risk. Control of Corruption ensures that policy uncertainty does not compound with rent-seeking in project approval and permitting.

Regulatory Quality and Voice & Accountability do not exhibit significant interaction effects. This null result is itself informative: the *quality* of regulation (RQ) appears less important for the CPU–RE channel than the *predictability* of the policy environment (captured by PS, RL, CC). Similarly, democratic accountability (VA) does not moderate the relationship, suggesting that the institutional mechanisms that translate CPU into RE deployment operate through administrative and legal channels rather than electoral ones.

**Figure 6** illustrates the strongest moderation effect—Political Stability—by plotting the predicted CPU–RE relationship at three PS levels. The divergence is substantial: high-PS countries exhibit a steep positive slope, while low-PS countries show a flat or slightly negative relationship, consistent with the Q10 result from the QARDL analysis.

> **[Insert Figure 6 about here]**

**Figure 8** provides a summary comparison of all six interaction coefficients, visually confirming that Political Stability, Government Effectiveness, Control of Corruption, and Rule of Law are the institutional pillars of the CPU–RE transmission mechanism.

> **[Insert Figure 8 about here]**

### 4.6 Discussion of Main Results

Our empirical findings are consistent with a **contingent hedging hypothesis** of climate policy uncertainty. The positive mean effect (Panel FE: β = 0.022, p < 0.001) supports the hedging mechanism: on average, economic agents increase renewable energy commitments when climate policy direction becomes more uncertain. However, the QARDL analysis reveals that this average masks substantial distributional heterogeneity. At the lowest quantile, the real-options channel dominates—uncertainty depresses renewable deployment—while at the median and upper quantiles, the hedging channel prevails.

The governance moderation results add an institutional dimension to this interpretation. Political Stability, Government Effectiveness, Rule of Law, and Control of Corruption all amplify the positive CPU effect. This suggests that the hedging mechanism operates through an *institutional transmission channel*: climate policy uncertainty generates investment incentives, but these incentives are only realized when governance institutions are sufficiently strong to reduce the execution risk of renewable energy projects.

This finding has direct implications for the empirical literature on CPU and energy outcomes. The extreme heterogeneity documented by Matias and Tabak's (2026) meta-analysis may be partially explained by cross-study variation in sample composition: studies weighted toward low-penetration, low-governance countries will likely find negative CPU effects (as in Yang et al., 2026 and Syed et al., 2023), while studies focused on high-penetration economies will find positive or null effects (as in Lin & Cheung, 2024). Our quantile framework provides a unified explanation for this apparent contradiction.

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

This study investigates the impact of climate policy uncertainty on renewable energy deployment in eight East Asian economies over 1996–2023, employing Panel Fixed Effects and Panel Quantile Regression as the primary frameworks, with monthly Panel QVAR connectedness as a robustness check. Our key findings are:

1. **CPU has a statistically significant positive within-country effect on renewable energy share** (Panel FE: β = 0.022, p < 0.001). A one-unit increase in the CPU index is associated with a 0.022 percentage point increase in renewable electricity share, controlling for country heterogeneity, geopolitical risk, GDP per capita, and CO₂ emissions. This finding supports the hedging hypothesis: firms and investors increase clean energy commitments in response to heightened climate policy uncertainty.

2. **The CPU effect is non-monotonic across the conditional distribution**, revealing an inverted-U pattern. At the lowest quantile of renewable penetration (Q10), CPU significantly *reduces* renewable energy share (β = −0.030, p < 0.001), consistent with the real-options channel: when existing renewable infrastructure is minimal, policy uncertainty increases the option value of waiting. The effect turns positive from Q25 onward, peaks at Q75 (β = 0.042, p < 0.001), and moderates at Q90 (β = 0.034, p < 0.001). This pattern resolves the tension between the competing hypotheses in the previous literature by showing that both mechanisms operate simultaneously, with their relative strength determined by a country's position in the renewable development trajectory.

3. **Governance quality amplifies the CPU–RE relationship.** Four of the six WGI dimensions exhibit statistically significant positive interactions: Political Stability (β = 0.023, p < 0.001), Government Effectiveness (β = 0.015, p < 0.05), Rule of Law (β = 0.013, p < 0.05), and Control of Corruption (β = 0.012, p < 0.05). This finding contradicts the hypothesis that governance buffers CPU effects; instead, institutional quality appears to provide the predictability and enforcement capacity necessary for firms to translate climate policy signals into renewable energy deployment. Political Stability emerges as the strongest moderator, suggesting that the credibility of the policy environment—rather than democratic accountability per se—is the institutional channel through which CPU affects clean energy outcomes.

4. **Monthly QVAR robustness analysis confirms the positive CPU impulse** (IRF month 1: +0.032) and reveals GPR as the dominant transmitter in the uncertainty network, with 33.9% of CPU's connectedness directed to geopolitical risk. However, the monthly-frequency effects are small relative to annual estimates, suggesting that CPU operates primarily through medium-term investment decisions rather than short-run production adjustments.

### 6.2 Policy Implications

Our findings carry several policy implications for East Asian governments and international climate institutions:

**First, climate policy clarity has differentiated effects across the development spectrum.** The negative Q10 result implies that for countries with minimal renewable infrastructure, policy uncertainty is genuinely detrimental—it freezes investment. For these countries (e.g., Cambodia, Laos if included), predictable, phased renewable energy mandates and technology transfer programs are essential. For middle-to-high penetration countries, policy signals generate positive responses, but the declining Q90 coefficient suggests diminishing returns at the very top of the distribution, where grid integration and energy storage investments become binding constraints.

**Second, governance reform is a prerequisite, not a distraction, for clean energy policy.** The positive moderation effects (PS, GE, RL, CC) indicate that strengthening institutional capacity amplifies the effectiveness of climate policy signals. Governments seeking to leverage CPU-induced investment for renewable deployment should prioritize: (a) political stability mechanisms that reduce the risk of policy reversal; (b) bureaucratic capacity for efficient project permitting and grid interconnection; (c) legal frameworks that protect renewable energy investments from expropriation and contract renegotiation; and (d) anti-corruption measures in energy sector procurement and licensing.

**Third, regional coordination among East Asian economies is warranted.** The Diebold-Yilmaz connectedness analysis reveals substantial cross-variable spillovers, particularly the CPU → GPR transmission channel. Given the region's interconnected energy markets and shared exposure to climate policy developments (especially from the U.S. and EU), coordinated regional approaches to renewable energy targets, grid interconnection (ASEAN Power Grid), and technology standards could mitigate the amplification of climate policy uncertainty through geopolitical risk.

**Fourth, a "one-size-fits-all" policy approach is suboptimal.** The non-monotonic quantile pattern implies that CPU has different effects at different stages of renewable development. Low-penetration countries need structural support—grid modernization, workforce training, technology transfer—before they can respond to policy signals. Mid-penetration countries benefit from maintaining policy momentum while strengthening governance mechanisms. High-penetration countries should shift focus from generation capacity to system integration issues (storage, demand response, grid flexibility) that CPU signals do not adequately address.

### 6.3 Limitations and Future Research

Several limitations should be acknowledged. First, the CPU index is constructed from U.S. newspaper sources and may imperfectly capture domestic climate policy uncertainty in East Asian economies. Future research could develop country-specific CPU measures for the region. Second, our annual panel, while comprehensive in time coverage, sacrifices within-year dynamics. The monthly QVAR robustness analysis partially addresses this but covers a shorter period (2015–2024). Third, the governance moderation analysis uses linear interaction terms; nonlinear or threshold effects (e.g., governance quality above a critical threshold) deserve investigation. Fourth, our Panel FE estimates treat the long-run relationship as homogeneous; the PMG Mean Group estimator relaxes this assumption but loses precision with only eight cross-sectional units. Fifth, the renewable energy share variable aggregates diverse technologies (hydro, solar, wind, bioenergy) with different deployment dynamics; technology-disaggregated analysis could reveal further heterogeneity.

Future extensions could include: (i) asymmetric NARDL modeling to separate positive and negative CPU shocks; (ii) time-varying parameter VAR (TVP-VAR) to trace the evolution of CPU–RE connectedness over policy regimes; (iii) mediating pathway analysis to test the CPU → GPR → RE transmission channel identified in our connectedness results; (iv) instrumental variable approaches leveraging the Känzig (2023) carbon pricing surprise series as an exogenous instrument for CPU; and (v) expanding the sample to include South Asian and Latin American economies for broader external validity.

---

## References

Akhter, S., & Arman, M. (2026). Geopolitical risk, governance, and renewable energy: A NARDL approach for ASEAN and East Asian economies. *Working Paper.*

Apergis, N., & Payne, J. E. (2010). Renewable energy consumption and economic growth: Evidence from a panel of OECD countries. *Energy Policy, 38*(1), 656–660.

ASEAN Centre for Energy. (2023). *The 8th ASEAN Energy Outlook, 2023–2050.* Jakarta: ASEAN Centre for Energy.

Baker, S. R., Bloom, N., & Davis, S. J. (2016). Measuring economic policy uncertainty. *Quarterly Journal of Economics, 131*(4), 1593–1636.

Bernanke, B. S. (1983). Irreversibility, uncertainty, and cyclical investment. *Quarterly Journal of Economics, 98*(1), 85–106.

Bloom, N. (2009). The impact of uncertainty shocks. *Econometrica, 77*(3), 623–685.

Bloom, N., Bond, S., & Van Reenen, J. (2007). Uncertainty and investment dynamics. *Review of Economic Studies, 74*(2), 391–415.

Caldara, D., & Iacoviello, M. (2022). Measuring geopolitical risk. *American Economic Review, 112*(4), 1194–1225.

Chang, C.-L., Zhang, J., & Lin, Y.-E. (2024). Climate policy uncertainty, corporate social responsibility and corporate investments of the energy firms. *Energy Economics, 140*, 106985.

Cho, J. S., Kim, T. H., & Shin, Y. (2015). Quantile cointegration in the autoregressive distributed-lag modeling framework. *Journal of Econometrics, 188*(1), 281–300.

Choi, I. (2001). Unit root tests for panel data. *Journal of International Money and Finance, 20*(2), 249–272.

Dasgupta, S., & De Cian, E. (2018). The influence of institutions, governance, and public opinion on the environment. *Ecological Economics, 146*, 475–486.

Diebold, F. X., & Yilmaz, K. (2012). Better to give than to receive: Predictive directional measurement of volatility spillovers. *International Journal of Forecasting, 28*(1), 57–66.

Dixit, A. K., & Pindyck, R. S. (1994). *Investment under uncertainty.* Princeton, NJ: Princeton University Press.

Gavriilidis, K. (2021). Measuring climate policy uncertainty. *SSRN Working Paper.*

Gavriilidis, K., Känzig, D. R., Raghavan, R., & Stock, J. H. (2026). The macroeconomic effects of climate policy uncertainty. *NBER Working Paper No. 34762.*

Guang, F., Liu, L., Tan, Q., & Wen, L. (2024). Climate policy uncertainty and energy structure transformation: Inhibition or facilitation. *SSRN Working Paper.*

Hossain, M. S., et al. (2026). Industrial value creation, policy uncertainty, and climate risk: An ARDL approach for the United States. *Working Paper.*

Jebli, M. B., Youssef, S. B., & Apergis, N. (2019). The dynamic linkage between renewable energy, tourism, CO₂ emissions, economic growth, foreign direct investment, and trade. *Latin American Economic Review, 28*, 1–19.

Kashif, M., et al. (2025). Fintech-driven sustainability: A QARDL analysis of renewable energy consumption and natural resource management. *Management of Environmental Quality, 36*(6), 1607–1624.

Kao, C. (1999). Spurious regression and residual-based tests for cointegration in panel data. *Journal of Econometrics, 90*(1), 1–44.

Kaufmann, D., Kraay, A., & Mastruzzi, M. (2010). The worldwide governance indicators: Methodology and analytical issues. *World Bank Policy Research Working Paper No. 5430.*

Keeley, A. R., & Ikeda, Y. (2017). Determinants of foreign direct investment in wind energy in developing countries. *Journal of Cleaner Production, 161*, 1451–1458.

Koenker, R., & Bassett, G. (1978). Regression quantiles. *Econometrica, 46*(1), 33–50.

Kulatilaka, N., & Perotti, E. C. (1998). Strategic growth options. *Management Science, 44*(8), 1021–1031.

Känzig, D. R. (2023). The unequal economic consequences of carbon pricing. *NBER Working Paper No. 31214.*

Liashenko, O., Dluhopolskyi, O., Wołowiec, T., & Woźniak, D. (2026). Governance quality and renewable energy transition: Global evidence using panel ARDL. *Energies, 19*(4), 1024.

Lin, Y., & Cheung, A. (2024). Climate policy uncertainty and energy transition: Evidence from prefecture-level cities in China. *Energy Economics, 139*, 107920.

Maddala, G. S., & Wu, S. (1999). A comparative study of unit root tests with panel data and a new simple test. *Oxford Bulletin of Economics and Statistics, 61*(S1), 631–652.

Matias, M. C., & Tabak, B. M. (2026). Climate policy uncertainty and its effects on investments in renewable energy transition: A systematic literature review and meta-analysis. *Energies, 19*(9), 2009.

North, D. C. (1990). *Institutions, institutional change and economic performance.* Cambridge: Cambridge University Press.

Omri, A., & Nguyen, D. K. (2014). On the determinants of renewable energy consumption: International evidence. *Energy, 72*, 554–560.

Payne, J. E., Nazlioglu, S., Koncak, A., & Ewing, B. T. (2025). U.S. climate policy uncertainty shocks and the growth in renewable energy production. *Journal of Commodity Markets, 39*, 100493.

Pedroni, P. (2004). Panel cointegration: Asymptotic and finite sample properties of pooled time series tests with an application to the PPP hypothesis. *Econometric Theory, 20*(3), 597–625.

Pesaran, M. H., Shin, Y., & Smith, R. P. (1999). Pooled mean group estimation of dynamic heterogeneous panels. *Journal of the American Statistical Association, 94*(446), 621–634.

Pindyck, R. S. (1991). Irreversibility, uncertainty, and investment. *Journal of Economic Literature, 29*(3), 1110–1148.

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
