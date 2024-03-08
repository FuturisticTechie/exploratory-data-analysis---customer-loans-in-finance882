
import pandas as pd


class DataFrameTransform:
    pass


    def drop_column(self, df, column):
        df.drop(column, axis=1, inplace=True)
        return df