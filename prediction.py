from sklearn.linear_model import LinearRegression

def predict_sales(data):

    X = data[["Quantity"]]

    y = data["Sales"]

    model = LinearRegression()

    model.fit(X, y)

    predicted_sales = model.predict([[9]])

    print("\nPredicted Sales for Quantity 9:")

    print(predicted_sales)