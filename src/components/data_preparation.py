import os
import sys
import pandas as pd
from dataclasses import dataclass

@dataclass
class DataPreparationConfig:
    data_path = os.path.join('data',"indian_cities.csv")

class DataPreparation:
    def __init__(self):
        self.ingestion_config = DataPreparationConfig()

    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv('data\worldcities.csv')

            return df
        except:
            pass

    def data_transformation(self,df):
        try:
            df = df[df["country"]=='India']
            # return df
            df.to_csv(self.ingestion_config.data_path,index=False,header=True)
        except:
            pass

if __name__ == '__main__':
    data_obj = DataPreparation()
    df = data_obj.initiate_data_ingestion()
    data_obj.data_transformation(df)