import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import os

# --- 1. DATA LOADING & CLEANING ---
path = "/BL_v3_MF1564.csv"
column_names = [
    'Country', 'Year', 'Age_Group', 'Age_To', 'No_Schooling',
    'Primary_Total', 'Primary_Completed', 'Secondary_Total', 'Secondary_Completed',
    'Tertiary_Total', 'Tertiary_Completed', 'Avg_Years_Total',
    'Avg_Years_Primary', 'Avg_Years_Secondary', 'Avg_Years_Tertiary',
    'Population', 'Region'
]

if os.path.exists(path):
    df = pd.read_csv(path, sep=';', skiprows=12, decimal=',', names=column_names)
    df['Country'] = df['Country'].ffill()
    df = df.dropna(subset=['Year'])
    df['Year'] = df['Year'].astype(int)
    print("✓ Data successfully loaded.")

# --- 2. REGIONAL TRENDS (LINE PLOT) ---
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")
reg_trends = df.groupby(['Region', 'Year'])['Avg_Years_Total'].mean().reset_index()
sns.lineplot(data=reg_trends, x='Year', y='Avg_Years_Total', hue='Region', marker='o')
plt.title('Global Education Trends by Region (1950-2015)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("/Users/alibashirzade/Downloads/1_regional_trends.png")
plt.show()

# --- 3. TURKEY VS BENCHMARKS (LINE PLOT) ---
comp_regions = reg_trends[reg_trends['Region'].isin(['Advanced Economies', 'Europe and Central Asia'])]
tr_trend = df[df['Country'] == 'Turkey'][['Year', 'Avg_Years_Total']].copy()
tr_trend['Region'] = 'Turkey (Country)'
final_comp = pd.concat([comp_regions, tr_trend])

plt.figure(figsize=(10, 6))
sns.lineplot(data=final_comp, x='Year', y='Avg_Years_Total', hue='Region', style='Region', markers=True, linewidth=2.5)
plt.title('Turkey vs Global Benchmarks')
plt.savefig("/Users/alibashirzade/Downloads/2_turkey_benchmark.png")
plt.show()

# --- 4. TURKEY STRUCTURE (STACKED AREA PLOT) ---
tr_edu = df[df['Country'] == 'Turkey'][['Year', 'No_Schooling', 'Primary_Total', 'Secondary_Total', 'Tertiary_Total']]
plt.figure(figsize=(10, 6))
plt.stackplot(tr_edu['Year'], tr_edu['No_Schooling'], tr_edu['Primary_Total'], tr_edu['Secondary_Total'], tr_edu['Tertiary_Total'],
              labels=['No Schooling', 'Primary', 'Secondary', 'Tertiary'], colors=['#e74c3c', '#f1c40f', '#2ecc71', '#3498db'], alpha=0.8)
plt.title('Turkey: Educational Transformation (1950-2015)')
plt.legend(loc='upper left')
plt.savefig("/Users/alibashirzade/Downloads/3_turkey_structure.png")
plt.show()

# --- 5. REGIONAL VARIATION (BOXPLOT 2015) ---
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[df['Year'] == 2015], x='Region', y='Avg_Years_Total', palette='Set3')
plt.xticks(rotation=45)
plt.title('Educational Variance by Region (2015)')
plt.tight_layout()
plt.savefig("/Users/alibashirzade/Downloads/4_regional_boxplot.png")
plt.show()

# --- 6. CORRELATION MATRIX (HEATMAP) ---
plt.figure(figsize=(8, 6))
sns.heatmap(df[['No_Schooling', 'Primary_Total', 'Secondary_Total', 'Tertiary_Total', 'Avg_Years_Total']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig("/Users/alibashirzade/Downloads/5_correlation_heatmap.png")
plt.show()

# --- 7. REGRESSION (FIXED EFFECTS) ---
df_reg = pd.get_dummies(df, columns=['Region'], drop_first=True)
features = ['Year'] + [col for col in df_reg.columns if 'Region_' in col]
X = sm.add_constant(df_reg[features].astype(float))
y = df_reg['Avg_Years_Total']
print("\n" + "="*60 + "\nREGRESSION SUMMARY\n" + "="*60)
print(sm.OLS(y, X).fit().summary())
