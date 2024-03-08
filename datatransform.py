
import pandas as pd

class DataTransform:
    pass
    
    def string_to_date(self, df, date_column):
        df[date_column] = pd.to_datetime(df[date_column], errors='coerce').dt.to_period('M')
        return df
    
