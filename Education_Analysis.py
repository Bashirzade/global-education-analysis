import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import os

# --- 1. DATA LOADING & CLEANING ---
path = "/Users/alibashirzade/Downloads/BL_v3_MF1564.csv"
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
    print("✓ Data successfully loaded and cleaned.")

# --- 2. REGIONAL CONVERGENCE ANALYSIS ---
regional_trends = df.groupby(['Region', 'Year'])['Avg_Years_Total'].mean().reset_index()
plt.figure(figsize=(14, 8))
sns.set_style("whitegrid")
sns.lineplot(data=regional_trends, x='Year', y='Avg_Years_Total', hue='Region', marker='o')
plt.title('Global Human Capital Accumulation: Regional Comparison (1950-2015)', fontsize=14, fontweight='bold')
plt.ylabel('Average Years of Schooling')
plt.legend(title='Regions', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("/Users/alibashirzade/Downloads/regional_convergence.png")
plt.show()

# --- 3. TURKEY VS BENCHMARKS ---
comparison_list = ['Advanced Economies', 'Europe and Central Asia']
df_filtered = regional_trends[regional_trends['Region'].isin(comparison_list)].copy()
turkey_trend = df[df['Country'] == 'Turkey'][['Year', 'Avg_Years_Total']].copy()
turkey_trend['Region'] = 'Turkey (Country)'
final_comp = pd.concat([df_filtered, turkey_trend])

plt.figure(figsize=(12, 7))
sns.lineplot(data=final_comp, x='Year', y='Avg_Years_Total', hue='Region', style='Region', markers=True, linewidth=3)
plt.title('Turkey vs. World Benchmarks: Educational Attainment', fontsize=14, fontweight='bold')
plt.savefig("/Users/alibashirzade/Downloads/turkey_benchmark.png")
plt.show()

# --- 4. TURKEY EDUCATION STRUCTURE (STACKED) ---
edu_levels = ['No_Schooling', 'Primary_Total', 'Secondary_Total', 'Tertiary_Total']
tr_edu = df[df['Country'] == 'Turkey'][['Year'] + edu_levels].copy()
plt.figure(figsize=(12, 7))
plt.stackplot(tr_edu['Year'], tr_edu['No_Schooling'], tr_edu['Primary_Total'], tr_edu['Secondary_Total'], tr_edu['Tertiary_Total'],
              labels=['No Schooling', 'Primary', 'Secondary', 'Tertiary'], colors=['#e74c3c', '#f1c40f', '#2ecc71', '#3498db'], alpha=0.8)
plt.title('Turkey: Structural Transformation of Education (1950-2015)', fontsize=14, fontweight='bold')
plt.ylabel('Percentage of Population (%)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.savefig("/Users/alibashirzade/Downloads/turkey_structure.png")
plt.show()

# --- 5. CORRELATION & BOXPLOT ---
plt.figure(figsize=(10, 8))
sns.heatmap(df[['No_Schooling', 'Primary_Total', 'Secondary_Total', 'Tertiary_Total', 'Avg_Years_Total']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Education Indicators')
plt.show()

df_2015 = df[df['Year'] == 2015]
plt.figure(figsize=(14, 8))
sns.boxplot(data=df_2015, x='Region', y='Avg_Years_Total')
plt.xticks(rotation=45)
plt.title('Regional Variation in Education Levels (2015)')
plt.show()

# --- 6. ECONOMETRIC REGRESSION (FIXED EFFECTS) ---
df_reg = pd.get_dummies(df, columns=['Region'], drop_first=True)
features = ['Year'] + [col for col in df_reg.columns if 'Region_' in col]
X = sm.add_constant(df_reg[features].astype(float))
y = df_reg['Avg_Years_Total']
model = sm.OLS(y, X).fit()

print("\n" + "="*60)
print("ECONOMETRIC RESULTS: TIME TREND & REGIONAL FIXED EFFECTS")
print("="*60)
print(model.summary())