import pandas as pd
import matplotlib.pyplot as plt

def plot_feature_importance(model, features):
    importance = pd.Series(
        model.feature_importances_,
        index=features
    ).sort_values(ascending=True)

    plt.figure(figsize=(8, 5))
    importance.plot(kind="barh")
    plt.title("Feature Importance")
    plt.xlabel("Importance Score")
    plt.tight_layout()
    plt.show()

    return importance
