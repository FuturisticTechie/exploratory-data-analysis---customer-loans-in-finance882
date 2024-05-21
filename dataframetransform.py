
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns




class DataFrameTransform:
    pass

    def drop_column(self, df, column):
        df.drop(column, axis=1, inplace=True)
        return df
    

    def impute_categorical_nulls(self, df, column=None):
        if column:
            if df[column].dtype == 'object':
                df[column].fillna(df[column].mode()[0], inplace=True)
            else:
                return None
        return df

    
    def impute_boolean_nulls(self, df, column=None):
        if column:
            if df[column].dtype == 'bool':
                df[column].fillna(df[column].mode()[0], inplace=True)
            else:
                return None
        return df
        

    def columns_with_sparse_nulls(self, df, lower_threshold=0.000129, upper_threshold=0.01):
        null_percentage = df.isnull().sum() / len(df)
        cols_to_consider = null_percentage[(null_percentage >= lower_threshold) & (null_percentage <= upper_threshold)].index.tolist()
        return cols_to_consider