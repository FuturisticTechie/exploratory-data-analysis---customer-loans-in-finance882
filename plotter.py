
import pandas as pd
import missingno as msno
import plotly.express as px


class Plotter:


    def missing_matrix(self, df):
        return msno.matrix(df)
    


# plot = Plotter()
