import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import make_pipeline

def policy_1(offline_data: pd.DataFrame, online_data: pd.DataFrame):
    """
    Policy 1: Select the room that matches the maximum number of APs
    
    Parameters:
    offline_data (pd.DataFrame): A dataframe containing the offline data.
    online_data (pd.DataFrame): A dataframe containing the online data.

    Returns:
    str: A string representing the reference poin.
    """

    # Group data by room
    grouped = offline_data.groupby("room")["id"].unique()
    
    # Extract unique ids from online data
    online_ids = online_data["id"].unique()

    # Check which is the most similar group id wise
    rf = None
    max_count = 0
    for room, group in grouped.items():
        count = 0
        for id in group:
            if id in online_ids:
               count += 1 
        if count > max_count:
            max_count = count
            rf = room

    return rf

def policy_2(offline_data: pd.DataFrame, online_data: pd.DataFrame):
    """
    Policy 2: Select the RP that minimizes the RSS error
    
    Parameters:
    online_data (pd.DataFrame): A dataframe containing the online data.
    offline_data (pd.DataFrame): A dataframe containing the offline data.

    Returns:
    str: A string representing the reference point.
    """

    # Group offline data by room
    grouped = offline_data.groupby("room")

    # Compute mean RSS for each group
    mean_rss_off = grouped.mean().reset_index()

    # Compute mean RSS for each access point in online data
    mean_rss_on = online_data.mean(numeric_only=True)

    # Select the access points that minimize the error
    min = np.inf
    for i, row in mean_rss_off.iterrows():
        if abs(row["quality"] - mean_rss_on["quality"]) < min:
            min = abs(row["quality"] - mean_rss_on["quality"])
            rf = row["room"]

    return rf

def policy_3(offline_data: pd.DataFrame, online_data: pd.DataFrame):
    """
    Policy 3: Naive Bayes
    
    Parameters:
    online_data (pd.DataFrame): A dataframe containing the online data.
    offline_data (pd.DataFrame): A dataframe containing the offline data.

    Returns:
    str: A string representing the reference point.
    """

    def get_pipeline(clf=RandomForestClassifier(n_estimators=100, class_weight="balanced")):
        return make_pipeline(DictVectorizer(sparse=False), clf)

    # Train the model
    X = offline_data.drop(columns=["room"])
    y = offline_data["room"]
    model = get_pipeline()
    model.fit(X.to_dict(orient="records"), y)
    
    # Predict the room
    return model.predict(online_data.to_dict(orient="records"))[0]
