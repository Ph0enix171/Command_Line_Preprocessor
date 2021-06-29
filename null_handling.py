import pandas as pd

def nCount(dataSet):
    print("\nNull values in each column\n")
    for c in dataSet.columns.values:
        print(c,"=",dataSet[c].isna().sum())

def removeColumn(dataSet):
    print(dataSet.columns.values,'\n')
    print("\nEnter which column(s) needs to be removed? If entering multiple columns, type name of each in a new line, press enter when done\n")
    cols=[]
    while True:
        s=input(':')
        if s!='':
            cols.append(s)
        else:
            break
    try:
        dataSet.drop(cols,axis=1,inplace=True)
        print("These columns removed successfully:\n",cols)
    except:
        print("\n Error in removing columns: Please check if you have input the correct column name(s)\n")

def fillMean(dataSet):
    for i in dataSet.columns.values:
        if dataSet.dtypes[i]==object:
            continue
        mean=dataSet[i].mean()
        dataSet[i].fillna(value=mean,inplace=True)
    print("\nNaN values replaced with mean successfully\n")

def fillMedian(dataSet):
    for i in dataSet.columns.values:
        if dataSet.dtypes[i]==object:
            continue
        med=dataSet[i].median()
        dataSet[i].fillna(value=med,inplace=True)
    print("\nNaN values replaced with median successfully\n")
    
def fillMode(dataSet):
    for i in dataSet.columns.values:
        if dataSet.dtypes[i]==object:
            continue
        mode=dataSet[i].median()
        dataSet[i].fillna(value=mode,inplace=True)
    print("\nNaN values replaced with mode successfully\n")

def displayDataset(dataSet):
    pd.set_option("display.max_rows", None, "display.max_columns",None)
    print(dataSet)

def main(dataSet):
    while True:
        print("\n\nNull Handling options:\n\n1. Null count\n2. Remove column(s)\n3. Fill NaN with mean\n4. Fill NaN with median\n5. Fill NaN with mode\n6. Display dataset")
        opt=input("\n\nSelect an option, select 0 to go back\n:")
        if opt=='1':
            nCount(dataSet)
        elif opt=='2':
            removeColumn(dataSet)
        elif opt=='3':
            fillMean(dataSet)
        elif opt=='4':
            fillMean(dataSet)
        elif opt=='5':
            fillMode(dataSet)
        elif opt=='6':
            displayDataset(dataSet)
        elif opt=='0':
            return dataSet
        else:
            print("\nInvalid option, try again\n")
        

    