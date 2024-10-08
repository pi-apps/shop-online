# product_recommender.py
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class ProductRecommender:
    def __init__(self, user_id, product_id):
        self.user_id = user_id
        self.product_id = product_id
        self.model = RandomForestRegressor()

    def train_model(self, user_data, product_data):
        X_train, X_test, y_train, y_test = train_test_split(user_data, product_data, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

    def get_recommendations(self):
        recommendations = self.model.predict(self.user_id, self.product_id)
        return recommendations
