
import psycopg2
import yaml
from sqlalchemy import create_engine, inspect
import pandas as pd


def load_yaml_file():                           #loads yaml file
    with open('credentials.yaml', 'r') as file:
        credentials = yaml.safe_load(file)
        return credentials

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials          #to extract credentials 
        
    def init_db_engine(self):                               
        engine = create_engine(f"postgresql+psycopg2://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}")
        return engine

    def load_table(self): 
        self.engine = self.init_db_engine()                              #initialises db connection and loads payment table
        with self.engine.begin() as conn:
            self.loan_payments_df = pd.read_sql_table('loan_payments', conn)    #Loads it as dataframe
        return self.loan_payments_df   

    def save_dataframe_to_csv(self, df, output_file):                    #loads remote yaml table from df to local csv
        df.to_csv(output_file, index=False)

    def load_loan_data(self, file_path):                                #loads table from local csv to local pf 
            return pd.read_csv(file_path)

if __name__ == '__main__':
    def main():
        credentials = load_yaml_file()  # Load credentials from YAML file
        dc = RDSDatabaseConnector(credentials)  # Create an instance of DatabaseConnector
        table = dc.load_table()  # Call the instance method on the created instance
        # dc.save_dataframe_to_csv(table, 'loan_payments.csv')
        # loan_data = dc.load_loan_data('loan_payments.csv')
main()