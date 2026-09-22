import pandas as pd

df=pd.read_csv('startup_growth_investment_data.csv',delimiter=',')
print(df)

print(df.dtypes)
print(df.describe)
print()

print(len(df))
print()

print(df.shape)
print(df.info())
print()

print(df.head(70))
print(df.tail(80))
print()

Country=df['Country']
print('Access of the name of the colums :')
print(Country)
print()

Country_Year=df[['Country','Year Founded']]
print('Access the multiple colums using df:')
print(Country_Year)
print()




first_row=df.loc[2:5]
print('selecting a slice of rows using .loc :')
print(first_row)
print()


first_row2=df.loc[[2,8]]
print('Slecting a multiple rows using .loc : ')
print(first_row2)
print()

first_row3=df.loc[1]
print('Select a single row using .loc :')
print(first_row3)
print()

first_row4=df.loc[df['Country']=='UK']
print('Conditional slection of rows using .loc :')
print(first_row4)
print()


first_row5=df.loc[df['Country']=='UK','Funding Rounds':'Country']
print('selecting a slice of colums using .loc:')
print(first_row5)
print()

first_row6=df.loc[:1,'Country']
print('Selecgting  a single colums using .loc :')
print(first_row6)
print()

first_row7=df.loc[:,['Country','Funding Rounds']]
print('selecting a multiple colums using .loc')
print(first_row7)
print()

first_row8=df.loc[:80,'Funding Rounds':'Growth Rate (%)']
print('selecting a slice of colums using .loc :')
print(first_row8)
print()


df_index_col=pd.read_csv('startup_growth_investment_data.csv',delimiter=',')
print(df_index_col)

print(df_index_col.shape)
print(df_index_col.describe)
print(df_index_col.dtypes)


second_row=df_index_col.loc[2]
print('select a row using .loc')
print(second_row)
print()

second_row2=df_index_col.loc[[1,4]]
print('Select a multiple rows using .loc :')
print(second_row2)
print()

second_row3=df_index_col.loc[1:9]
print('slect a slice of rows using .loc :')
print(second_row3)
print()


second_row4=df_index_col.loc[df_index_col['Growth Rate (%)']==104.98]
print('select a single colum using .loc :')
print(second_row4)

second_row5=df_index_col.loc[df_index_col['Growth Rate (%)']==104.98,'Industry':'Country']
print('select a combination of colum and row uain .loc :')
print(second_row5)
print()

second_row6=df_index_col.loc[:345,'Industry':'Country']
print('select a slice of colums using .loc :')
print(second_row6)
print()

second_row7=df_index_col.loc[:123,['Country','Industry']]
print('select a muliple colms using .loc')
print(second_row7)
print()

second_row8=df_index_col.loc[:345,['Country']]
print('select a single colums using .loc')
print(second_row8)
print()

print('\n')
print('start the .iloc ')

second_row=df_index_col.iloc[0]
print('select a single row using .iloc')
print(second_row)
print()

second_row2=df_index_col.iloc[1:9]
print('select a slice of rows using .iloc')
print(second_row2)

second_row3=df_index_col.iloc[[1,5,9]]
print('select a multipl rows using .iloc :')
print(second_row3)
print()

second_row4=df_index_col.iloc[df_index_col['Year Founded']==2011]
print('select a single colum using .iloc')
print(second_row4)
print()

second_row5=df_index_col.iloc[:234,3:9]
print('select a slice of colums using .iloc')
print(second_row5)
print()

second_row6=df_index_col.iloc[:67,[5,8]]
print('select a multiple couls using .iloc :')
print(second_row6)
print()

second_row7=df_index_col.iloc[df_index_col['Year Founded']==2011,3:6]
print('select a combination of rows and colums using .iloc :')
print(second_row7)
print()


second_row8=df_index_col.iloc[:7890,1:5]
print('select a slice of colums using .iloc')
print(second_row8)


""""Pandas DataFrame Manipulation
DataFrame manipulation in Pandas involves editing and modifying existing DataFrames. Some common DataFrame manipulation operations are:

Adding rows/columns
Removing rows/columns
Renaming rows/columns"""

#Add a New Row to a Pandas DataFrame
# add a new row
# Copy array from list and add to DataFrame
# 3477952;82;"https://www.zameen.com/Property/lahore_model_town_6_kanal_excellent_house_for_sale_in_model_town-347795-8-12.html";"House2";2200000002;"Model Town2";"Lahore2";"Punjab2";312.483868658082;742.325685501099;02;"6 Kanal2";"For Sale2";02;"07-17-2019";"Real Biz International2";"Usama Khan2"

#add new line
df.loc[len(df.index)]=[1,2,3,4,5,6,7,8,9]
print(df)
print()

df.drop(1,axis=0,inplace=True)
print(df)
print()

df.drop(index=2,inplace=True)
print(df)
print()

df.drop([3,5],axis=0,inplace=True)
print(df)
print()

df.drop('Industry',axis=1,inplace=True)
print(df)
print()

df.drop(['Funding Rounds'],axis=1,inplace=True)
print(df)
print()

df.rename(columns={'Startup Name':'changed_startup_Name'},inplace=True)
print(df)
print()

df.rename(mapper={'Growth Rate (%)':'Changed_Growth Rate (%)','Year Founded':'changed_Year_Founded'},axis=1,inplace=True)
print(df)
print()

df.rename(index={0:7},inplace=True)
df.rename(mapper={9:10,10:11},axis=0,inplace=True)
print(df)
print()
#df['Country'] = pd.to_numeric(df['Country'], errors='coerce')
df['changed_Year_Founded'] = pd.to_numeric(df['changed_Year_Founded'], errors='coerce')
selected_rows=df.query('Country==\'India\' or changed_Year_Founded>2011')
print(selected_rows)

print(selected_rows.to_string())
print(len(selected_rows))


sorted_df=df.sort_values(by='changed_Year_Founded')
print(sorted_df.to_string(index=False))


df1=df.sort_values(by=['Investment Amount (USD)','Valuation (USD)'])
print(df1.to_string(index=False))

"""
Reference: https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/
Explanation: This code creates a DataFrame from a dictionary with three columns (Weight, Name, Age), structures it into a tabular format using pd.DataFrame() and converts it into a fully visible string representation with df.to_string().

Syntax
DataFrame.to_string(buf=None, columns=None, col_space=None, header=True, index=True, na_rep=’NaN’, formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, max_cols=None, show_dimensions=False, decimal=’.’, line_width=None)


Parameters:

buf: Buffer to write the output string to (e.g., a file). Defaults to None, which means the output is returned as a string.
columns: Specifies a subset of columns to include in the output. If None, all columns are printed.
col_space: Defines the minimum width of each column.
header: Whether to print column names. Can also accept a list of column name aliases.
index: Whether to include index labels. Default is True.
na_rep: String representation for missing values (NaN). Default is ‘NaN’.
formatters: Dictionary or list of functions to apply to columns for formatting their output.
float_format: Formatter function to apply specifically to floating-point numbers.
sparsify: Controls hierarchical index formatting. If False, prints every multi-index key at each row.
index_names: Whether to print index names. Default is True.
justify: Alignment of column headers (‘left’, ‘right’, ‘center’, ‘justify’ or ‘justify-all’).
max_rows: Maximum number of rows to display. If exceeded, truncates output.
max_cols: Maximum number of columns to display. If exceeded, truncates output.
show_dimensions: If True, displays the shape (rows x columns) of the DataFrame.
decimal: Specifies the character for decimal separation (e.g., ‘,’ for European formatting).
line_width: Defines the maximum character width of a row before wrapping text."""



#Pandas groupby
#In Pandas, the groupby operation lets us group data based on specific columns. This means we can divide a DataFrame into smaller groups based on the values in these columns.

# group the DataFrame by the location_id column and
# calculate the sum of price for each category


grouped=df.groupby('changed_Year_Founded')['Country'].sum()
print(grouped.to_string())
print(len(grouped))

df_cleaned=df.dropna()
print('Cleaned Data :\n',df_cleaned)

df.fillna(0,inplace=True)

print("\nData after filling NaN with 0:\n",df_cleaned)

data = [2, 4, 6, 8]
# create Pandas array using data
array1 = pd.array(data)
print(array1)
"""<IntegerArray>
[2, 4, 6, 8]
Length: 4, dtype: Int64"""


# creating a pandas.array of integers
int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()

int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()

#Pandas Reshape
#In Pandas, reshaping data refers to the process of converting a DataFrame from one format to another for better data visualization and analysis.
#Pandas provides multiple methods like pivot(), pivot_table(), stack(), unstack() and melt() to reshape data. We can choose the method based on our analysis requirement.

