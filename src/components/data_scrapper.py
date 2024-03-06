import os
import sys
import pandas as pd
import pdfkit
from dataclasses import dataclass

class DataCrawlerConfig:
    data_path = 'data'
    crawler_data = 'data\crawler_data.csv'

class DataCrawler:
    def __init__(self):
        self.data_configs = DataCrawlerConfig()

    def data_loader(self):
        try:
            df = pd.read_csv(self.data_configs.crawler_data)
        except:
            pass
    
    def data_downloader(self,data):
        pass
        
    
if __name__ == '__main__':
    data_obj = DataCrawler()
    df = data_obj.data_loader()