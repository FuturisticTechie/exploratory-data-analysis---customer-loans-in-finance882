
import pandas as pd
import missingno as msno
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt 


class Plotter:


    def missing_matrix(self, df):
        return msno.matrix(df)
    

    # def facet_grid_histogram(self, df):
    #     # Filter numeric columns
    #     numeric_columns = df.select_dtypes(include=['number'])
    #     # Reshape the DataFrame into long format
    #     melted_df = numeric_columns.melt()
    #     # Create a FacetGrid with Seaborn
    #     g = sns.FacetGrid(melted_df, col='variable', col_wrap=3, sharex=False, sharey=False)
    #     # Map histogram plot to each variable
    #     g.map(sns.histplot, 'value')
    #     # Set titles for each subplot based on the variable name
    #     for ax, title in zip(g.axes.flat, numeric_columns.columns):
    #         ax.set_title(title)
    #     # Adjust layout
    #     plt.tight_layout()
    #     # Show plot
    #     plt.show()

    # def facet_grid_histogram(self, series):
    #     # Create a DataFrame with the series data
    #     df = pd.DataFrame(series, columns=['skewness'])
    #     # Reshape the DataFrame into long format
    #     melted_df = df.reset_index().melt(value_vars=['skewness'], var_name='variable', value_name='value')
    #     # Create a FacetGrid with Seaborn
    #     facet_grid = sns.FacetGrid(melted_df, col='variable', col_wrap=3, sharex=False, sharey=False)
    #     # Map histogram plot to each variable
    #     facet_grid.map(sns.histplot, 'value', kde=True, bins=20)
    #     # Set titles for each subplot based on the variable name
    #     facet_grid.set_titles("{col_name}")
    #     # Adjust layout
    #     plt.tight_layout()
    #     # Show plot
    #     plt.show()

    def skew_check(self, df):
        numeric_data = ['loan_amount',
                    'funded_amount', 
                    'funded_amount_inv',
                    'instalment',
                    'annual_inc',
                    'open_accounts',
                    'out_prncp',
                    'out_prncp_inv',
                    'total_payment',
                    'total_payment_inv',
                    'total_rec_prncp',
                    'total_rec_int'
                    ]

        categorical_data = [col for col in df.columns if col not in numeric_data]
        sns.set(font_scale=0.7)

        f = pd.melt(df, value_vars=numeric_data)
        g = sns.FacetGrid(f, col="variable",  col_wrap=3, sharex=False, sharey=False)
        g = g.map(sns.histplot, "value", kde=True)
        print(categorical_data)




# plot = Plotter()
