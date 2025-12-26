
# Global Human Capital Accumulation & Educational Attainment (1950-2015)

## 📊 Project Overview
This mini project provides a data-driven exploration of global education trends using the **Barro-Lee Educational Attainment Dataset**. The analysis covers 146 countries over 65 years, focusing on how human capital has deepened across different regions and specifically within **Turkey**.

## 🛠️ Key Features
- **Data Wrangling:** Automated cleaning of historical panel data, handling decimal inconsistencies and regional mapping.
- **Structural Analysis:** Visualizing the transition from 'No Schooling' to 'Tertiary Education' (University level).
- **Regional Benchmarking:** Comparing emerging markets against advanced economies to detect "catch-up" effects.
- **Econometric Modeling:** Using **OLS Regression** to estimate the global time trend while controlling for **Regional Fixed Effects**.

## 📈 Principal Findings
- **Global Growth:** On average, global schooling years have increased by **0.1 years annually** since 1950.
- **Turkey's Catch-up:** Turkey successfully reduced its uneducated population from **78% in 1950** to **4% in 2015**, showing a massive leap in human capital deepening.
- **Convergence:** While most regions are converging, a significant gap (approx. 5.5 years) remains between Advanced Economies and Sub-Saharan Africa.

## 💻 Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas (Data manipulation), Matplotlib/Seaborn (Visualization), Statsmodels (Econometrics)

## 📁 Repository Structure
- `script.py`: The complete analysis pipeline.
- `Cleaned_Education_Data.csv`: Processed dataset for immediate research use.
- `results/`: Visual exports (PNG) of the analysis.

- ## Source
- Barro, R. J., & Lee, J. W. (2013). A new data set of educational attainment in the world, 1950–2010. Journal of Development Economics, 104, 184-198. (Updated v3.0, 2015).

Official Website: barrolee.com
