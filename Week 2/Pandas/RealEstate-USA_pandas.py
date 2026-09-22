import pandas as pd

df=pd.read_csv('RealEstate-USA.csv',delimiter=",")
print(df)

print("dtypes value:",df.dtypes)
print("info is the file:", df.info())

print('first three lines:')
print(df.head(3))

print('last three lines:')
print(df.tail(3))

#Summary of Statistics of DataFrame using describe() method.
print('Summary of Statistics of DataFrame using describe() method:')
print(df.describe())

print('shape of the file:')
print(df.shape)
print()

status=df['status']
print('allow the access the status rows and clums:')
print(status)
print()

status_price=df[['status','price']]
print("value of the status or price :")
print(status_price)
print()

#case 1 using loc
second_row=df.loc[1]
print("Selecting a single row in the .loc:")
print(second_row)
print()

second_row2=df.loc[[1,3]]
print("Selecting a mulitple row :")
print(second_row2)
print()

second_row3=df.loc[[1,5]]
print("selecting a multiple rows:")
print(second_row3)
print()

conditional_row=df.loc[df['price']<50000]
print("rows with price greater than 50000:")
print(conditional_row)
print()

single_colum=df.loc[:1,'price']
print("single colum value are:")
print(single_colum)
print()

multi_colum=df.loc[:2,['price','bed']]
print('muliple colum value :')
print(multi_colum)
print()

#print (0,1) value only in the bed
single_colum=df.loc[:1,'bed']
print("single colum value are:")
print(single_colum)
print()

second_row4=df.loc[:,['price','bed']]
print('selecting a colum a multiple row:')
print(second_row4)

second_row5=df.loc[df['price']==50000,'street':'city']
print('seleting a multiple row in the value:')
print(second_row5)

second_row6=df.loc[df['bed']==4,'price':'bath']
print(second_row6)

#case 2 using loc in indexing
df_index_col=pd.read_csv('RealEstate-USA.csv',delimiter=",")
print(df_index_col)
print(type(df_index_col))
print(df_index_col.dtypes)
print(df_index_col.info())

second_row=df_index_col.loc[4]
print('selecting a single value usind loc')
print(second_row)
print()

second_row2=df_index_col.loc[[5,7]]
print('selecting a multiple colum usin this row')
print(second_row2)
print()

second_row3=df_index_col.loc[5:7]
print('select a pice of slice of rows using .loc')
print(second_row3)
print()

second_row4=df_index_col.loc[df_index_col['bed']==4]
print('condition selecting rows using .loc')
print(second_row4)
print()

second_row5=df_index_col.loc[:500000,['price']]
print('selecting a single colum using .loc')
print(second_row5)
print()

second_row6=df_index_col.loc[:2,['price','bath']]
print('selecting a multiple of colum of using .loc')
print(second_row6)
print()

second_row7=df_index_col.loc[:2,'price':'bath']
print('selectin a slice of colum of using .loc')
print(second_row7)
print()

second_row8=df_index_col.loc[df_index_col['price']==50000,'bed':'bath']
print('combined row and colum selecting .loc')
print(second_row8)
print()

# Case 3 : Using .iloc - starts here
print('start here from the using of iloc')
print()

second_row=df_index_col.iloc[0]
print('selectin a single row of using .iloc')
print(second_row)
print()

second_row2=df_index_col.iloc[[1,3,5]]
print("selecting a multipl colum")
print(second_row2)
print()

second_row3=df_index_col.iloc[2:5]
print("select a slice of the colum  using .iloc")
print(second_row3)
print()

second_row4=df_index_col.iloc[:,2]
print('selecting a single colum using .iloc')
print(second_row4)
print()

second_row5=df_index_col.iloc[:,[5,6]]
print('selecting mulitple colum using .iloc')
print(second_row5)
print()

second_row6=df_index_col.iloc[:,2:5]
print('Selectin a slice of colum using .iloc')
print(second_row6)
print()

second_row7=df_index_col.iloc[[1,3,7],1:4]
print('Selecting a rows or colums using .iloc')
print(second_row7)
print()

#case 3 :using .iloc -ends here

print('next Run')


#Add a New Row to a Pandas DataFrame
# add a new row
df.loc[len(df.index)]=[1590,'not_for_sale',239001,7,3,0.31,1551669,'Azhar','Puerto Rico',612,2715,'NaN']
print(df)
print()

#Remove Rows/Columns from a Pandas DataFrame

# delete row with index 1
df.drop(1,axis=0,inplace=True)
# delete row with index 2
df.drop(index=2,inplace=True)
# delete rows with index 3 and 5
df.drop([3,5],axis=0,inplace=True)
print("Modified DataFrame - Remove Rows:")
print(df)

# delete price column
df.drop('status',axis=1,inplace=True)

df.drop(columns='price',inplace=True)
# delete height and profession columns
df.drop(['bed','bath'],axis=1,inplace=True)
# display the modified DataFrame after deleting rows
print('Modified DataFrame -  delete page_url,price,bath,staus,bed')
print(df)

#Example: Rename Row Labels
df.rename(index={0:7},inplace=True)
#rename columns multiple index labels
df.rename(mapper={1:5,8:77},axis=0,inplace=True)
print('rename of the value using  mapper:')
print(df)

#query() to Select Data
#The query() method in Pandas allows you to select data using a more SQL-like syntax.

# select the rows where the age is greater than 25

selected_rows=df.query('zip_code==601 or street>331151')

print(selected_rows.to_string())
print(len(selected_rows))

sorted_df=df.sort_values(by='zip_code')
print(sorted_df.to_string(index=False))


#sorted multiple colums
df1=df.sort_values(by=['city','state'])

print("sorting of the program in the program assending or decesding")
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

grouped=df.groupby('city')['state'].sum()
print('grouped:', len(grouped))




df_cleaned=df.dropna()
print('cleaned Data:\n',df_cleaned)

df.fillna(0,inplace=True)
print("\nData after filling NaN with 0:\n", df)

data=[9,8,0,4]
array1=pd.array(data)
print(array1)


int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()
