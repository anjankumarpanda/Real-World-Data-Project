def analyze_data(data):

    print("\n===== FIRST 5 ROWS =====")
    print(data.head())

    print("\n===== DATASET INFO =====")
    print(data.info())

    print("\n===== STATISTICAL SUMMARY =====")
    print(data.describe())

    print("\n===== TOTAL SALES =====")
    print(data["Sales"].sum())

    print("\n===== TOTAL PROFIT =====")
    print(data["Profit"].sum())