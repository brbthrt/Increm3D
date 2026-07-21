import pandas as pd

df=pd.read_csv('../dataset.csv')
print('=================DATASET STATISTIC======================')

print('avg processing time: ', df['processing_time'].mean())

print('median processing time: ', df['processing_time'].median())

print('avg keypoints: ', df['keypoints'].mean())

print('median keypoints: ', df['keypoints'].median())

print('max matches: ', df['matches'].max())

print('min matches: ', df['matches'].min())

print('standard deviation of matches: ', df['matches'].std())

print('variance of matches: ', df['matches'].var())


print(df.quantile([0.25, 0.5, 0.75], numeric_only=True).to_string())