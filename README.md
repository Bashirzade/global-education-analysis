Global Human Capital Analysis (1950-2015)
Project Overview
This project provides a data-driven exploration of global education trends using the Barro-Lee Dataset. Covering 146 countries over 65 years, the analysis quantifies the evolution of human capital, focusing on Turkey's structural transformation and regional convergence patterns.

Methodology
The analytical pipeline handles the entire data lifecycle:

Data Cleaning: Processed historical panel data, standardized decimal formats, and handled longitudinal data gaps.

Structural Visualization: Tracked the shift from "No Schooling" to "Higher Education" over half a century.

Regional Benchmarking: Measured the "Catch-up Effect" by comparing emerging markets against advanced economies.

Econometric Modeling: Implemented an OLS Regression to estimate the global education growth rate while controlling for Regional Fixed Effects.

Key Findings
Education Growth: Globally, average schooling years increase by approximately 0.1 years annually.

Turkey Case Study: Successfully reduced the "No Schooling" rate from 78% (1950) to 4% (2015).

Global Gaps: Identified a persistent ~5.5-year gap between Advanced Economies and developing regions.

Repository Structure
Education_Analysis.py: Core Python script for analysis and modeling.

Education_Data.pdf: Documentation regarding the dataset source.

results/: Directory containing all visual outputs and statistical summaries.

1_regional_trends.png

2_turkey_benchmark.png

3_turkey_structure.png

6_regression_summary.png

Data Source & Citation (APA)
The analysis is based on the following academic source:

Barro, R. J., & Lee, J. W. (2013). A new data set of educational attainment in the world, 1950–2010. Journal of Development Economics, 104, 184-198. (Updated v3.0, 2015).

Official Website: barrolee.com
