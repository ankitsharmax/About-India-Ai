import os
import sys
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from urllib.request import urlretrieve
from dataclasses import dataclass

class DataCrawlerConfig:
    data_path = "data\pdfs\\"
    crawler_data = 'data\crawler_data.csv'
    batch_size = 10

class DataCrawler:
    def __init__(self):
        self.data_configs = DataCrawlerConfig()

    def data_loader(self):
        try:
            df = pd.read_csv(self.data_configs.crawler_data)
            return df
        except:
            pass

    def download(self,title,url):
        filename = title + '.pdf'
        print("Downloading Data {0}".format(filename))
        filepath = os.path.join(self.data_configs.data_path,filename)
        urlretrieve(url,filepath)
        print("File Downloaded Successfully")
    
    def data_downloader(self,data):
        print(data.loc[0])
        data = data[data["download_status"]==0]        
        data.reset_index(inplace=True)
        print("Data Ready for download")
        print("data size {0}".format(data.shape[0]))
        if data.shape[0] <= self.data_configs.batch_size:
            epochs = data.shape[0]
        else:
            epochs = self.data_configs.batch_size
        
        print("Ephoch size {0}".format(epochs))
        for i in range(epochs):
            title = data.loc[i,"city"]
            url = data.loc[i,"download_url"]
            try:
                self.download(title,url)
                data.loc[i,"download_status"] = 1
            except:
                data.loc[i,"download_status"] = -1 
        data.to_csv(self.data_configs.crawler_data,index=False,header=True)

        
    
if __name__ == '__main__':
    data_obj = DataCrawler()
    df = data_obj.data_loader()
    print(df.loc[0])
    data_obj.data_downloader(df)