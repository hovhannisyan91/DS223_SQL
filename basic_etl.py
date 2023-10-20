# from etl.data_preperation.schema import *
from etl.data_preperation import SqlHandler
from etl.logger import CustomFormatter

Inst=SqlHandler('temp', 'employees')


import pandas as pd
data=pd.read_csv('employee.csv')

print(data.head())
Inst.insert_many(data)


Inst.close_cnxn()