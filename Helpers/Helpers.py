import os
import itertools
import pandas as pd
from fuzzywuzzy import fuzz


def save_as_csv(df, filename):
    path = os.path.join(os.getcwd(), 'Data', filename)
    df.to_csv(path)


def remove_duplicates(df):
    potential_duplicates = pd.DataFrame(itertools.combinations(df["Name"].values, 2)).assign(
        ratio=lambda x: x.apply(lambda t: fuzz.ratio(t[0], t[1]), axis=1)
    ).query("ratio > 60")

    potential_duplicates["copy1"] = potential_duplicates[0].str.split().str[:5]
    potential_duplicates["copy2"] = potential_duplicates[1].str.split().str[:5]
    potential_duplicates = potential_duplicates.query("copy1 == copy2")
    
    return df[~df["Name"].isin(potential_duplicates[1])]


def camera_formatting(df, camera_categories):
    """
    Format and extract relevant features from a dataframe of camera data.
    
    Parameters:
    - df (pd.DataFrame): The input dataframe containing camera information.
        It should have at least the columns 'Price' and 'Name'.
    - camera_categories (list of str): A list of categories to which cameras can be classified.
    
    Returns:
    - pd.DataFrame: The formatted dataframe with new columns 'brand', 'category', and 'Type'.
    
    Notes:
    - 'brand': Extracted from the first word in the 'Name' column.
    - 'category': Extracted based on matching substrings in 'Name' column to the provided categories.
    - 'Type': Categorized into 'B', 'BL', or 'Other' based on the presence of substrings 'body' and 'lens' in the 'Name' column.
    """

    # Formatting price column from string to float
    df['Price'] = df['Price'].replace(r"[\£,]", '', regex=True).astype(float)
    
    # Brand extraction
    df['brand'] = df['Name'].str.split().str[0]
    
    # Category extraction
    df['category'] = df['Name']
    
    # Assign categories
    for category in camera_categories:
        df.loc[df['category'].str.contains(category, regex=False, case=False), 'category'] = category
        
    df.loc[df['category'].str.len() > 10, 'category'] = "Other or Not Specified"
    
    # Type extraction
    df['Type'] = 'Other'
    
    # "Body" only products
    df.loc[df['Name'].str.contains('body', case=False) & ~df['Name'].str.contains('lens', case=False), 'Type'] = 'B'
    
    # "Lens" only products
    df.loc[~df['Name'].str.contains('body', case=False) & df['Name'].str.contains('lens', case=False), 'Type'] = 'BL'
    
    return df