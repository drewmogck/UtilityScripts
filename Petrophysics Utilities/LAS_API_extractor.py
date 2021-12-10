"""
Utility script to create a csv containing API# and file names of all log (.las) files in a directory. 

Utilizes the lasio package. https://github.com/kinverarity1/lasio

"""
import lasio
import glob
import os
import pandas as pd

path = os.getcwd() #file path for LAS files - Defaults to current working directory

path_las=glob.glob(path+'*.las') #gets paths to all .las files in directory

#file path for export
export_path = path #modify as needed

#initialize blank dataframe for storing data
df = pd.DataFrame(columns=['API', 'filename'])

#loop through LAS files and extract API and filename to dataframe
for las in path_las:
    las_data = lasio.read(las) #read las file
    API = las_data.well.API.value #extract API# from file
    filename=os.path.basename(las) #get filename
    
    las_df = {'API': API, 'filename': filename} 
    df = df.append(las_df, ignore_index = True) 
    
df.to_csv(export_path+'LAS_directory.csv') #export data to final list