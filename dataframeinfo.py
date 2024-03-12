
import pandas as pd

class DataFrameInfo:
    def __init__(self):
        self.__private_variable = None
    
#Describe all columns in the DataFrame to check their data types
    def describe_all_column(self, df):
        desc = df.describe()
        return desc

# Extract statistical values: median, standard deviation and mean from the columns and the DataFrame
    
    def median(self, df, column=None):
        if column:
            if pd.api.types.is_numeric_dtype(df[column]):   #filter the DataFrame to include only numeric columns before calculating the median
                return df[column].median()
            else:
                return None 
        else:
            numeric_cols = df.select_dtypes(include=['number']).columns
            return df[numeric_cols].median()


    def std(self, df, column=None):
        if column:
            if pd.api.types.is_numeric_dtype(df[column]):
                return df[column].std()
            else:
                return None
        else:
            numeric_cols = df.select_dtypes(include=['number']).columns
            return df[numeric_cols].std()


    def mean(self, df, column=None):
        if column:
            if pd.api.types.is_numeric_dtype(df[column]):
                return df[column].mean()
            else:
                return None
        else:
            numeric_cols = df.select_dtypes(include=['number']).columns
            return df[numeric_cols].mean()
        
    def mode(self, df, column=None):
        if column: 
            return df[column].mode()
        else:
            return df.mode()

        
    def distinct_count(self, df, column):
        dist = df[column].nunique()
        return dist 

# Print out the shape of the DataFrame
    def shape_print(self, df):
        shaped = df.shape
        return shaped

# Generate a count/percentage count of NULL values in each column
    def null_count(self, df, column=None):
        if column:
           return df[column].isnull().sum()
        else:
            return df.isnull().sum()
    
    def null_percentage(self, df):
        return df.isnull().sum()/len(df)

# Any other methods you may find useful
    
    def calculate_skew(self, df):
        # Filter numeric columns
        numeric_columns = df.select_dtypes(include=['number'])
        # Calculate skewness for numeric columns
        skewed_data = numeric_columns.skew()
        return skewed_data
