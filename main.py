import sys
import pandas as pd
from data_description import main as ddmain
from null_handling import main as nhmain
from categorical_encoding import main as cemain
from feature_scaling import main as fsmain
from save_dataset import main as sdmain

n=len(sys.argv)

def csvInput():
    if len(sys.argv)==1:
        print("\n\nUsage: main.py dataset_name.csv\n\n")
        exit()
    else:
        try:
            dataSet=pd.read_csv(sys.argv[1])
            print("Dataset ",sys.argv[1]," loaded successfully with the following columns\n")
            print(dataSet.columns.values,'\n')
            return dataSet
        except:
            print("\n\nAn error occured in loading the dataset:\nCheck whether you have input the correct dataset name in format dataset_name.csv or if the dataset is present in the working directory\n\n")
            exit()

def removeTarget(dataSet):
	
    targetColumnLock='n'

    while targetColumnLock=='n':
        targetColumn=input("\nEnter the target variable name\n")
        
        while targetColumn not in dataSet.columns.values:
            print("\nColumn ",targetColumn," does not exist, please try again\n")
            targetColumn=input("\nEnter the target variable name\n")
        targetColumnLock=input("\nSelected target variable is "+targetColumn+"?[y/n]:")

    while targetColumnLock!='y' and targetColumnLock!='n':
        print("\nPlease select from [y/n]")
        targetColumnLock=input("Selected target variable is "+targetColumn+"?[y/n]:")

    try:
    	dataSet.drop([targetColumn],axis=1,inplace=True)
    	print("\nRemoved selected target variable",targetColumn,"successfully\n")
    	return True
    except:
        print("\n\nThere was an error in removing the target variable: Please check if you have input the correct name\n\n")
        return False

def main(dataSet):
    while True:
        print("\n\nPreprocessing tasks\n\n1. Data Description\n2. Null handling\n3. Categorical encoding\n4. Feature Scaling the Dataset\n5. Save changes in Dataset")
        opt=input("\n\nSelect an option, select anything to exit\n:")
        if opt=='1':
            dataSet=ddmain(dataSet)
        elif opt=='2':
            dataSet=nhmain(dataSet)
        elif opt=='3':
            dataSet=cemain(dataSet)
        elif opt=='4':
            dataSet=fsmain(dataSet)
        elif opt=='5':
            dataSet=sdmain(dataSet)
        else:
            break
        
dataSet=csvInput()
r=False

while not r:
    r=removeTarget(dataSet)

main(dataSet)

