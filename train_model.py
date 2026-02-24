from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
import joblib
import numpy as np

from sklearn.ensemble import GradientBoostingRegressor

def train_model(X_train, y_train):
    model = GradientBoostingRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=4,
        random_state=42
    )
    model.fit(X_train, y_train)
    return model



def evaluate(model, X_test, y_test):
    pred = model.predict(X_test)
    print("MAE:", mean_absolute_error(y_test, pred))
    print("R2:", r2_score(y_test, pred))
    rmse = np.sqrt(mean_squared_error(y_test, pred))
    print("RMSE:", rmse)

    mape = np.mean(np.abs((y_test - pred) / y_test)) * 100
    print("MAPE:", mape)


def save_model(model, path):
    joblib.dump(model, path)
