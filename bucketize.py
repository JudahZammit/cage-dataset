import pandas
import matplotlib.pyplot as plt
import shutil
import os


metadata = pandas.read_csv('./metadata.csv')
prog = metadata['Progression (Days)']
prog_round = prog.round()
metadata['Progression (Days)'] = prog_round

def new_path(row):
      out = '/home/judah/Desktop/Bucket_Flagship/ncp/day'
      out += str(int(row['Progression (Days)']))
      out += '/'
      out += str(int(row['scan_id']))
      out += '/'
      out += str(int(row['patient_id']))
      return out

def old_path(row):
      out = '/home/judah/Desktop/Cleaned_Flagship/ncp/'
      out += str(int(row['scan_id']))
      out += '/'
      out += str(int(row['patient_id']))
      return out

metadata['new_path'] = metadata.apply(new_path,axis = 1)
metadata['old_path'] = metadata.apply(old_path,axis = 1)


def func(row):
    os.makedirs(row['new_path'],exist_ok = True)
    try:
      for path in os.listdir(row['old_path']):
          os.rename(row['old_path']+'/'+path,row['new_path']+'/'+path)
    except:
      print(row)
metadata.apply(func,axis = 1)
