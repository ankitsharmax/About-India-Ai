import os
import sys
import pandas as pd
from dataclasses import dataclass

@dataclass
class DataPreparationConfig:
    indian_cities = os.path.join('data',"indian_cities.csv")
    data_scrapper_site = 'https://en.wikipedia.org/wiki/'
    data_download_link = 'https://en.wikipedia.org/api/rest_v1/page/pdf/'
    crawler_data = os.path.join('data','crawler_data.csv')

class DataPreparation:
    def __init__(self):
        self.data_config = DataPreparationConfig()

    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv('data\worldcities.csv')
            df = df[df["country"]=='India']
            # df.to_csv(self.data_config.indian_cities,index=False,header=True)
            df.reset_index(inplace=True)
            return df
        except:
            pass

    def data_preprocessor(self,df):
        df["page_url"] = None
        df["download_url"] = None
        df["download_status"] = None
        print(df)
        for i in range(df.shape[0]):
            df.loc[i,"page_url"] = self.data_config.data_scrapper_site + df.loc[i,"city"]
            df.loc[i,"download_url"] = self.data_config.data_download_link + df.loc[i,"city"]
        # df.to_csv(self.data_config.crawler_data,index=False,header=True)
        return df
    # https://codereview.stackexchange.com/questions/160784/small-program-to-download-wikipedia-articles-to-pdf

if __name__ == '__main__':
    data_obj = DataPreparation()
    df = data_obj.initiate_data_ingestion()
    print(data_obj.data_preprocessor(df[["city"]]))