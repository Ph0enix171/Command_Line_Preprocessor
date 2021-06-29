import pandas as pd

def categoricalColumn(dataSet):
    print("\nCategorical columns are:\n")
    for c in dataSet.columns.values:
        if dataSet.dtypes[c]==object:
            print(c)

def oneHotEncoding(dataSet):
    print("\nEnter the columns which need to be one hot encoded, each in a new line, press enter when done.\n")
    cols=[]
    while True:
        s=input(':')
        if s!='':
            cols.append(s)
        else:
            break
    try:
        return pd.get_dummies(dataSet,columns=cols)
        print("\n Successfully encoded these columns:\n",cols)
    except:
        print("\nThere was an error: check if you have input the correct column name(s)\n")

from null_handling import displayDataset

def main(dataSet):
    while True:
        print("\n\nCategorical Encoding options:\n\n1. List categorical columns\n2. Perform one hot encoding on a column\n3. Show dataset")
        opt=input("\n\nSelect an option, select 0 to go back\n:")
        if opt=='1':
            categoricalColumn(dataSet)
        elif opt=='2':
            dataSet=oneHotEncoding(dataSet)
        elif opt=='3':
            displayDataset(dataSet)
        elif opt=='0':
            return dataSet
        else:
            print("\nInvalid option, try again\n")