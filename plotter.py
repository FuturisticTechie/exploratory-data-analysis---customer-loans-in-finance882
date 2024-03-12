
import pandas as pd
import missingno as msno
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt 


class Plotter:


    def missing_matrix(self, df):
        return msno.matrix(df)
    

    def facet_grid_histogram(self, df):
        # Reshape the DataFrame into long format
        melted_df = df.melt()

        # Create a FacetGrid with Seaborn
        g = sns.FacetGrid(melted_df, col='variable', col_wrap=3, sharex=False, sharey=False)

        # Map histogram plot to each variable
        g.map(sns.histplot, 'value')

        # Set titles for each subplot based on the variable name
        for ax, title in zip(g.axes.flat, df.columns):
            ax.set_title(title)

        # Adjust layout
        plt.tight_layout()

        # Show plot
        plt.show()


# plot = Plotter()
