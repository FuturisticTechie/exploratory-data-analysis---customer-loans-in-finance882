
import pandas as pd
import missingno as msno
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt 


class Plotter:


    def missing_matrix(self, df):
        return msno.matrix(df)
    

    def histogram_plot (self, df, column=None):
        if column:
            df[column].hist(bins=50)
            return plt.show()
        else:
            df.hist(bins=50)
            return plt.show()


    def kernel_density_estimate_plot(self, df, column=None):
        if column:
            plot = sns.histplot(data=df, x=column, kde=True)
        else:
            plot = sns.histplot(data=df, kde=True)
        sns.despine()
        return plot
    
    #This section is being edited --- THIS NEEDS TESTING
    def box_and_whiskers_plot (self, df, column=None):
        if column:
            box_plot = px.box(df, y = column, width = 600, height = 500)
        else:
            box_plot = px.box(df, width = 600, height = 500)
        return box_plot.show()

# WORK ON THIS CODE NEXT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # def violin_plot (self, column, df):

    #     sns.violinplot(data = df, y = column)
    #     return sns.despine()


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
