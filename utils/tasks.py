# from scrap import *
import pandas as pd
from datetime import datetime

class Sheet:
    def __init__(self, sheet):
        self.sheet = sheet

    def working_df(self):
        return pd.read_excel(self.sheet, header=None)

    def url_collumn(self):
        return self.working_df()[1]
    
    def price_append(self, list):
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.working_df()(columns=[timestamp])
        self.working_df()[timestamp] = list
        return self.working_df()

    
    

    

planilha = Sheet('Links.xlsx')


