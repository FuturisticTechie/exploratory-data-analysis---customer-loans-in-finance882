
import pandas as pd
import missingno as msno
import plotly.express as px
import plotly.offline as py
import plotly.io as pio
import seaborn as sns
import matplotlib.pyplot as plt 
from matplotlib import pyplot
from statsmodels.graphics.gofplots import qqplot



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
    
    def box_and_whiskers_plot(self, df, column=None):
        if column:
            box_plot = px.box(df, y=column, width=600, height=500)
        else:
            box_plot = px.box(df, width=600, height=500)
        pio.show(box_plot)

    def violin_plot (self, df, column=None):
        if column:
            violin_plot = sns.violinplot(data = df, y = column)
        else:
            violin_plot = sns.violinplot(data = df, y = column)
        sns.despine()
        plt.show()
        return violin_plot
    
    # Check entire dataframe correlation
    def correlation_heatmap(self, df):
        df = df.select_dtypes(include = "number")
        selected_corr = df.corr()
        fig, ax = plt.subplots(figsize=(20, 20))
        return sns.heatmap(selected_corr, annot = True, cmap = "coolwarm", ax=ax)
    
    # TEST THIS IS CLEANLY WORKING (YOU WILL NEED TO RESTART VSCODE)
    def qq_plotter (self, df, column=None):
        qq_plot = qqplot(df[column], scale = 1, line = "q", fit = True)
        return pyplot.show()


    

    #DELETE THIS!!!!!!!!!!!
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


    #Code to visulaise skewness acorss all the data
    def visualise_skewness(self, df):
        '''This method plots the data to visualise the skew. It uses Seaborn's Histogram with KDE line plot to achieve this.       
              
        Returns:
        --------
        plot
            Seaborn's Histogram with KDE line plot.
        '''  
        #select only the numeric columns in the DataFrame
        # df = self.df.select_dtypes(include=['float64'])
        df = df.select_dtypes(include=['number'])
        plt.figure(figsize=(18,14))

        for i in list(enumerate(df.columns)):
            fig_cols = 4
            fig_rows = int(len(df.columns)/fig_cols) + 1
            plt.subplot(fig_rows, fig_cols, i[0]+1)
            sns.histplot(data = df[i[1]], kde=True)

        # Show the plot
        plt.tight_layout()
        return plt.show()

# plot = Plotter()
