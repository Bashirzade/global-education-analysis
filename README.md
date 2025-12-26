Project Overview
This mini project provides a data-driven exploration of global education trends using the Barro-Lee Dataset. Covering 146 countries over 65 years, the analysis quantifies how human capital has evolved, with a deep dive into Turkey's structural transformation and regional convergence patterns.

🛠️ What Does This Project Do?
This pipeline handles the entire data lifecycle:

Advanced Data Cleaning: Processed historical panel data, fixed decimal formatting issues, and handled longitudinal data gaps.

Structural Visualization: Tracked the shift from "No Schooling" to "Higher Education" over half a century.

Regional Benchmarking: Measured the "Catch-up Effect" by comparing emerging markets against advanced economies.

Econometric Modeling: Ran an OLS Regression to calculate the global education growth rate while controlling for Regional Fixed Effects (isolating geographic and historical factors).

📈 Key Findings
The 0.1 Year Rule: Globally, average schooling years increase by approximately 0.1 years every single year.

Turkey’s Massive Leap: Turkey reduced its "No Schooling" rate from 78% (1950) to 4% (2015), a significant achievement in human capital deepening.

The Gap: Despite global progress, a gap of ~5.5 years remains between Advanced Economies and regions like Sub-Saharan Africa.

📁 Repository Structure
Education_Analysis.py: The complete Python code (Cleaning, Viz, Econometrics).

Education_Data.pdf: Dataset documentation and sources.

results/: Contains high-resolution PNG exports of all charts and the regression summary.

1_regional_trends.png

2_turkey_benchmark.png

3_turkey_structure.png

6_regression_summary.png

📚 Data Source & Citation (APA)
The analysis is based on the gold standard for human capital research:

Barro, R. J., & Lee, J. W. (2013). A new data set of educational attainment in the world, 1950–2010. Journal of Development Economics, 104, 184-198. (Updated v3.0, 2015). Official Link: barrolee.com

