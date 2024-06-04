
import pandas as pd
import numpy as np
from plotter import Plotter
from scipy import stats

class DataTransform:
    def __init__(self):
            self.plotter = Plotter()  # Instantiate the Plotter class
    
    def string_to_date(self, df, date_column):
        df[date_column] = pd.to_datetime(df[date_column], errors='coerce').dt.to_period('M')
        return df
    

    def log_transform(self, df, column):
        # Calculate skewness of the original column
        original_skewness = df[column].skew()

        # Plot original data
        print("Before the log transformatrion, the skewness is", original_skewness)
        self.plotter.kernel_density_estimate_plot(df[column])  # Use the plotter instance
        self.plotter.qq_plotter(df, column)  # Pass the DataFrame and column name

        # Apply log transformation
        log_column = df[column].map(lambda i: np.log(i) if i > 0 else 0)
        
        # Calculate skewness of the log-transformed column
        log_skewness = log_column.skew()
        print("After log transformation, the skewness is:", log_skewness)
        
        # Plot transformed data
        self.plotter.kernel_density_estimate_plot(log_column)  # Use the plotter instance
        self.plotter.qq_plotter(df, column)  # Pass the DataFrame and column name
        
         
        return log_skewness

    def box_cox_transform(self, df, column):
        # Calculate skewness of the original column
        original_skewness = df[column].skew()

        # Plot original data
        print("Pre Box transformation, the skewness is", original_skewness)
        self.plotter.kernel_density_estimate_plot(df[column])  # Use the plotter instance
        self.plotter.qq_plotter(df, column)  # Pass the DataFrame and column name

        #Apply the transformation
        # boxcox_transform = self.df[column]
        boxcox_transform = df[column]
        boxcox_transform = stats.boxcox(boxcox_transform)
        boxcox_transform = pd.Series(boxcox_transform[0])

                # Calculate skewness of the log-transformed column
        log_skewness = boxcox_transform.skew()
        print("After Box-Cox transformation, the skewness is:", log_skewness)
        
        # Plot transformed data
        self.plotter.kernel_density_estimate_plot(boxcox_transform)  # Use the plotter instance
        self.plotter.qq_plotter(df, column)  # Pass the DataFrame and column name

        return boxcox_transform.skew()
    
    #CURRENTLY WORKING ON THIS TO MASS TRANSFORM DATA--- HAS NOT BEEN STARTED TESTING YET!!!!!!!!!!!!!!
    def transform_columns(self):
        '''This method transforms to identified columns of the DataFrame to reduce skewness.
              
        Returns:
        --------
        dataframe
            A Pandas DataFrame
        '''  
        #select only the numeric columns in the DataFrame
        df = self.impute_null_values().select_dtypes(include=['float64']) # include=np.number
        
        # Model Creation
        p_scaler = PowerTransformer(method='yeo-johnson')
        # yeojohnTr = PowerTransformer(standardize=True)   # not using method attribute as yeo-johnson is the default

        # fitting and transforming the model
        df_yjt = pd.DataFrame(p_scaler.fit_transform(df), columns=df.columns)

        return df_yjt   
    


    # def yeo_johnson_transform(self, column):
    #     yeojohnson_transform = self.df[column]
    #     yeojohnson_transform = stats.yeojohnson(yeojohnson_transform)
    #     yeojohnson_transform = pd.Series(yeojohnson_transform[0])
    #     return yeojohnson_transform.skew()
    
    
    # def yeo_johnson_transform_df(self, column):
    #     column_data = self.df[column].values.reshape(-1, 1)

    #     power_transformer = PowerTransformer(method="yeo-johnson", standardize = True)
    #     self.df[column] = power_transformer.fit_transform(column_data)

    #     print(f"Transformed column '{column}':\n{self.df[column]}")
    #     return self.df
    

    # def box_cox_transform_df(self, column):
    #     column_data = self.df[column].values.reshape(-1, 1)

    #     power_transformer = PowerTransformer(method="box-cox", standardize = True)
    #     self.df[column] = power_transformer.fit_transform(column_data)

    #     print(f"Transformed column '{column}':\n{self.df[column]}")
    #     return self.df
    
    
    # def log_transform_df(self, column):        
    #     self.df[column] = self.df[column].map(lambda i: np.log(i) if i > 0 else 0)
    #     return self.df
    
    # def z_scores(self, column, threshold = 3):
    #     mean_column = np.mean(self.df[column])
    #     std_column = np.std(self.df[column])
    #     z_scores = np.abs((self.df[column] - mean_column) / std_column)
    #     self.df.loc[z_scores > threshold, column] = mean_column
            