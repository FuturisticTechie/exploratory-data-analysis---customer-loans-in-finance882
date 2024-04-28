
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
    

    # def box_plot_tranform(self,df,column=None):
    #     numeric_data = ['loan_amount',
    #                 'funded_amount', 
    #                 'funded_amount_inv',
    #                 'instalment',
    #                 'annual_inc',
    #                 'open_accounts',
    #                 'out_prncp',
    #                 'out_prncp_inv',
    #                 'total_payment',
    #                 'total_payment_inv',
    #                 'total_rec_prncp',
    #                 'total_rec_int'
    #                 ]
    #     boxcox_column = stats.boxcox(numeric_data)
    #     boxcox_column = pd.Series(numeric_data[0])
    #     return boxcox_column
    

    def box_plot_transform(self, df, columns=None):
        if columns is None:
            columns = ['loan_amount', 'funded_amount', 'funded_amount_inv', 'instalment', 'annual_inc', 'open_accounts', 'out_prncp', 'out_prncp_inv', 'total_payment', 'total_payment_inv', 'total_rec_prncp', 'total_rec_int']

        transformed_data = pd.DataFrame(index=df.index)

        for col in columns:
            if col in df.columns:
                data = df[col].dropna()  # Drop missing values
                data = data[data > 0]  # Filter out zero or negative values
                transformed_column, lambda_value = stats.boxcox(data)
                transformed_data[col] = transformed_column
            else:
                print(f"Column '{col}' not found in DataFrame.")

        return transformed_data
    
    # def yeojohnson_transform(self, df, column=None):
    #     if column is not None and isinstance(column, str):
    #         transformed_data, _ = stats.yeojohnson(df[column])
    #         transformed_data = pd.Series(transformed_data)
    #         t = sns.histplot(transformed_data, label="Skewness: %.2f" % transformed_data.skew())
    #         return t
    #     else:
    #         return None

        

    def yeojohnson_transform(self, df, column=None):
        if column is not None and isinstance(column, (list, pd.Series)):
            transformed_data = pd.DataFrame()
            for col in column:
                if col in df.columns:
                    transformed_col, _ = stats.yeojohnson(df[col])
                    transformed_data[col] = transformed_col
                    sns.histplot(transformed_col, label=f"Skewness: {transformed_col.skew():.2f}")
                    plt.legend()
                else:
                    print(f"Column '{col}' not found in DataFrame.")
            return transformed_data
        else:
            return None
