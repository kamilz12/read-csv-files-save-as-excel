import pandas as pd

dataFromFile = pd.read_csv ("file.csv", encoding='utf-8', na_filter=False, index_col=0)
dataFromFile ['Totaly new column']="New data" 
dataFromFile.insert (1, column="Col in middle", value="Good morning son")
print (dataFromFile)
dataFromFile.to_excel ('data.xlsx') #save our data's as excel file
dataFromFile.to_csv ('new.csv') #save our data's as csv file