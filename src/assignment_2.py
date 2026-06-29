import pandas as pd
import numpy as np

def calculate_total_spending(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a new column 'TotalSpending' by summing up:
    'RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', and 'VRDeck'.
    Handle missing values by treating them as 0 before summing.
    Should return the modified DataFrame.

    1. fillnan 0
    2. totalspending = roomservice + foodcourt + shoppingmall + spa + vrdeck
    """
    cols='RoomService FoodCourt ShoppingMall Spa VRDeck'.split()
    df[cols]=df[cols].fillna(0)
    # print(df.isnull().sum())
    df['TotalSpending']=df[cols].sum(axis=1)
    # print(df.head())
    return df
    # # TODO: Implement this function
    # pass

def parse_cabin(df: pd.DataFrame) -> pd.DataFrame:
    """
    The 'Cabin' column is in the format 'Deck/Num/Side' (e.g., 'B/0/P').
    Split this into three new columns: 'Deck', 'CabinNum', and 'Side'.
    If 'Cabin' is NaN, these new columns should also be NaN.
    'CabinNum' should be converted to numeric (float or int).
    Should return the modified DataFrame.
    
    if cabin.isna:
        deck, cabinnum, side = NaN, NaN, NaN
    else:
        deck, cabinnum, side = cabin.split("/")
    convert cabinnum to int
    slow
    """
    # print(df["Cabin"].dtype)
    df["Deck CabinNum Side".split()]=df["Cabin"].str.split("/",expand=True)
    df["CabinNum"] = pd.to_numeric(df["CabinNum"])
    
    #debug
    # print(df[['Cabin', 'Deck', 'CabinNum', 'Side']].head(10))
    # print(df[df['Cabin'].isna()][['Cabin', 'Deck', 'CabinNum', 'Side']].head())
    # print(df['CabinNum'].dtype)
    # TODO: Implement this function
    return df

def filter_outliers_iqr(df: pd.DataFrame, column_name: str) -> pd.Series:
    """
    make copy of df
    Identify and remove outliers in the specified column using the IQR method.
    - Calculate Q1 (25th percentile) and Q3 (75th percentile).
    - Calculate IQR = Q3 - Q1.
    - Define bounds: Lower = Q1 - 1.5 * IQR, Upper = Q3 + 1.5 * IQR.
    - Keep only rows where the column value is within [Lower, Upper].
    Should return a Series containing the filtered column values.
    
    """

    ##TODO (Theoretical): implement error if column not in df, implement error if not numeric
    copy = df.copy()
    #calc percentiles
    q25 = copy[column_name].quantile(0.25)
    q75 = copy[column_name].quantile(0.75)
    #calc iqr
    iqr = q75-q25
    #define bounds
    lower = q25-1.5*iqr
    upper = q75+1.5*iqr
    #kick outliers
    copy = copy[(copy[column_name] >= lower) & (copy[column_name] <= upper)]
    
    return copy

    pass

if __name__ == "__main__":
    # Test your logic here
    data = pd.read_csv("data/train.csv")
    filtered=filter_outliers_iqr(df=data, column_name="Spa")

    print("Originalgröße:", len(data))
    print("Nach Outlier-Removal:", len(filtered))
    print("Min:", filtered.min(), "| Max:", filtered.max())


    try:
        # Assuming assignment_1.py functions are used or mock data is loaded
        print("Assignment 2 template ready for implementation.")
    except Exception as e:
        print(f"Error: {e}")
