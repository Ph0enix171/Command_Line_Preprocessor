import pandas as pd
from sklearn.preprocessing import MinMaxScaler,StandardScaler

def normalizeData(dataSet,a,b):
    print("\n1. Normalize whole dataset\n2. Normalize column\n")
    type=input("\nSelect operation\n:")
    cols=dataSet.columns.values
    scaler=MinMaxScaler(feature_range=(a,b))
    
    if type=='1':
        for i in cols:
            if dataSet.dtypes[i]!=object:
                dataSet[i]=scaler.fit_transform(dataSet[i].values.reshape(-1,1))
            else:
                continue
        print("\nDataset normalized successfully\n")
    elif type=='2':
        print("\nEnter the columns to be normalized, press enter when done\n",cols,"\n")
        while True:
            s=input(':')
            if s!='':
                try:
                    dataSet[s]=scaler.fit_transform(dataSet[s].values.reshape(-1,1))
                    print("\nColumn ",s," normalized\n")
                except:
                    print("\nCould not normalize, please check column name or whether it is a numeric column\n")
            else:
                break
    else:
        print("\nInvalid option\n")
    return dataSet

def standardizeData(dataSet):
    print("\n1. Standardize whole dataset\n2. Standardize column\n")
    type=input("\nSelect operation\n:")
    cols=dataSet.columns.values
    scaler=StandardScaler()
    
    if type=='1':
        for i in cols:
            if dataSet.dtypes[i]!=object:
                dataSet[i]=scaler.fit_transform(dataSet[i].values.reshape(-1,1))
            else:
                continue
        print("\nDataset standardized successfully\n")
    elif type=='2':
        print("\nEnter the columns to be standardized, press enter when done\n",cols,"\n")
        while True:
            s=input(':')
            if s!='':
                try:
                    dataSet[s]=scaler.fit_transform(dataSet[s].values.reshape(-1,1))
                    print("\nColumn ",s," standardized\n")
                except:
                    print("\nCould not stanndardize, please check column name or whether it is a numeric column\n")
            else:
                break
    else:
        print("\nInvalid option\n")
    return dataSet

from null_handling import displayDataset
    
def main(dataSet):
    while True:
        print("\n\nFeature scaling options:\n\n1. Normalize dataset\n2. Standardize dataset\n3. Show dataset")
        opt=input("\n\nSelect an option, select 0 to go back\n:")
        if opt=='1':
            a=float(input("\nLower Limit?\n:"))
            b=float(input("\nHigher Limit?\n:"))
            dataSet=normalizeData(dataSet,a,b)
        elif opt=='2':
            standardizeData(dataSet)
        elif opt=='3':
            displayDataset(dataSet)
        elif opt=='0':
           return dataSet
        else:
            print("\nInvalid option, try again\n")
        