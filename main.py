import pandas as pd

# Change directory if the file is in a different location
import os
os.chdir('C:/Users/Siris/Desktop/GitHub Projects 100 Days NewB/_24_0076__Day72_Data Exploration with Pandas_College Major__240807/NewProject/r00-r09 START/r00_env_START')

# Now read the CSV file
df = pd.read_csv('salaries_by_college_major.csv')

# Display the first few rows
#df.tail()

clean_df = df.dropna()
#clean_df.tail()

#clean_df['Mid-Career Median Salary'].idxmin()
#clean_df['Starting Median Salary'].idxmax()
#clean_df.loc[18]
#clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]
#clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

#low_risk = clean_df.sort_values('Spread')
#low_risk[['Undergraduate Major', 'Spread']].head()

#high_risk = clean_df.sort_values('Spread')
#high_risk[['Undergraduate Major', 'Spread']].head()

#top_5_degrees = clean_df.sort_values(by='Mid-Career 90th Percentile Salary', ascending=False).head(5)
#print(top_5_degrees)

#greatest_spread = clean_df.sort_values(by='Mid-Career 90th Percentile Salary', ascending=False).head(5)
#print(top_5_degrees)

#largest_spread_degrees = clean_df.sort_values(by='Spread', ascending=False).head(5)
#print(largest_spread_degrees)

#clean_df.groupby('Group').count()
#mean_group = clean_df.groupby('Group').mean()
#print(mean_group)

# Select only numeric columns for the mean calculation
numeric_columns = clean_df.select_dtypes(include='number')

# Group by 'Group' and calculate the mean for numeric columns
pd.options.display.float_format = '{:,.2f}'.format
mean_group = clean_df.groupby('Group')[numeric_columns.columns].mean()

print(mean_group)