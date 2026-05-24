import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(data):

    # Sales by Product
    plt.figure(figsize=(6,4))

    sns.barplot(x="Product", y="Sales", data=data)

    plt.title("Sales by Product")

    plt.show()


    # Profit by Region
    plt.figure(figsize=(6,4))

    sns.barplot(x="Region", y="Profit", data=data)

    plt.title("Profit by Region")

    plt.show()


    # Quantity Distribution
    plt.figure(figsize=(6,4))

    sns.histplot(data["Quantity"], bins=5)

    plt.title("Quantity Distribution")

    plt.show()


    # Correlation Heatmap
    plt.figure(figsize=(6,4))

    sns.heatmap(
        data.corr(numeric_only=True),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")

    plt.show()