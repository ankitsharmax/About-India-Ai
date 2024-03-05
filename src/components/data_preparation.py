import os
import sys
import pandas
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
        pass
