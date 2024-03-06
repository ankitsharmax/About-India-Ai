import os
import sys
import pandas as pd
from dataclasses import dataclass

class DataCrawlerConfig:
    data_path = 'data'
    indian_cities = 'data\indian_cities.csv'
    data_scrapper_site = 'https://en.wikipedia.org/wiki/'
    crawler_data = os.path.join('data','crawler_data.csv')

class DataCrawler:
    def __init__(self):
        self.data_configs = DataCrawlerConfig()

    def data_loader(self):
        try:
            df = pd.read_csv(self.data_configs.indian_cities)
            return df[['city']]
        except:
            pass
    
    def data_preprocessor(self,df):
        df['url'] = None
        for i in range(df.shape[0]):
            df.loc[i,"url"] = self.data_configs.data_scrapper_site + df.loc[i,"city"]
        df.to_csv(self.data_configs.crawler_data,index=False,header=True)
        return df
    
if __name__ == '__main__':
    data_obj = DataCrawler()
    df = data_obj.data_loader()
    print(data_obj.data_preprocessor(df))