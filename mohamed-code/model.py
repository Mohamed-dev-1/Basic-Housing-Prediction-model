from TreatData import load_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# load the clean dataframe
df = load_data()

def model_predict(df):
    # separate Features and Target
    X = df.drop("median_house_value", axis=1)
    y = df["median_house_value"]    

    # we split the data into train data and test data (we dont give the whole dataset to the model) we leave 20% of the data for the testing to test model prediction on a unseen data 
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

def model_evaluate_score(y_test, y_pred):
    
    score = r2_score(y_test, y_pred)
    return score    



