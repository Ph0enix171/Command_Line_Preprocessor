import pandas as pd

def dataDescription(dataSet):
	print(dataSet.describe(include='all'),"\n")
	print(dataSet.info(),"\n")

def dataDescriptionCol(dataSet):
    columnName=input("\nEnter column name\n:")
    try:
        print(dataSet[columnName].describe(),"\n")
    except:
        print("\n\nError: column does not exist\n\n")

def showData(dataSet):
    l=len(dataSet.index)
    rows=int(input("\nEnter number of rows to be displayed(max rows="+str(l)+")\n:"))
    while type(rows)!=int:
        print("\nPlease enter an integer value\n")
        rows=input("\nEnter number of rows to be displayed(max rows="+str(l)+")\n:")
    if l<=rows:
        print(dataSet.head(l),"\n")
    else:
        print(dataSet.head(rows),"\n")

def main(dataSet):
    while True:
        print("\n\nData description options:\n\n1. Describe dataset\n2. Describe a column\n3. Show specific number of rows")
        opt=input("\n\nSelect an option, select 0 to go back\n:")
        if opt=='1':
            dataDescription(dataSet)
        elif opt=='2':
            dataDescriptionCol(dataSet)
        elif opt=='3':
            showData(dataSet)
        elif opt=='0':
            return dataSet
        else:
            print("\nInvalid option, try again\n")

