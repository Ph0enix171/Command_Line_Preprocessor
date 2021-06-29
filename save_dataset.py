import pandas as pd

def saveHere(dataSet):
    name=input("\nEnter name of dataset\n:")
    try:
        dataSet.to_csv(name+'.csv')
        print("\nDataset saved successfully in the same directory")
    except:
        print("\nError: Could not save dataset\n")

def saveToFilePath(dataSet):
    filepath=input("\nEnter location where dataset is to be saved\n:")
    name=input("\nEnter name of dataset\n:")
    try:
        dataSet.to_csv(filepath+'/'+name+'.csv')
        print("\nDataset saved successfully in the specified filepath")
    except:
        print("\nThere was an error in saving the dataset, please check whether filepath is correct\n")
        
def main(dataSet):
     while True:
        print("\n\nSave dataset:\n\n1. Save to same directory\n2. Save to different directory")
        opt=input("\n\nSelect an option, select 0 to go back\n:")
        if opt=='1':
            saveHere(dataSet)
        elif opt=='2':
            saveToFilePath(dataSet)
        elif opt=='0':
            break
        else:
            print("\nInvalid option, try again\n")