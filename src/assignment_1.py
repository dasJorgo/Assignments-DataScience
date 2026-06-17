import pandas as pd
import numpy as np

def load_data(file_path: str) -> pd.DataFrame:
    """
    #Load the CSV file using pandas.
    Return the loaded DataFrame.
    """
    
    return pd.read_csv(file_path)
    # TODO: Implement this function
    

def clean_age(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values in the 'Age' column by filling them with the median age.
    Should return the modified DataFrame.
    """
    median  = df["Age"].median()
    df["Age"] = df["Age"].fillna(median)
    
    # TODO: Implement this function
    return df

def convert_types(df:pd.DataFrame) -> pd.DataFrame:
    """
    Convert 'CryoSleep' and 'VIP' columns to boolean types.
    Missing values in these columns should be treated as False before conversion.
    Should return the modified DataFrame.
    """
    #fill false
    df["VIP"] = df["VIP"].fillna("False")
    df["CryoSleep"] = df["CryoSleep"].fillna("False")
    #convert
    df["VIP"] = df["VIP"].map({"True":True,"False":False}).astype(bool)
    df["CryoSleep"] = df["CryoSleep"].map({"True":True,"False":False}).astype(bool)
    
    
    # print(df["VIP"].isnull().sum())

    # TODO: Implement this function
    return df

if __name__ == "__main__":
    # This block allows students to test their code locally
    try:
        data = load_data("data/train.csv")

        data = clean_age(data)
        data = convert_types(data)
        print("Basic cleaning successful!")
        print(data.head())
    except Exception as e:
        print(f"Error during execution: {e}")
