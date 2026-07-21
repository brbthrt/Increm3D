import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('../dataset.csv')

# compute correlation martix for numerical features
corr=df.drop(columns=['width', 'height']).corr(numeric_only=True)

plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, fmt='.2f')
plt.title('correlation matrix')
plt.tight_layout()
plt.savefig('results/correlation_matrix.png')
plt.show()