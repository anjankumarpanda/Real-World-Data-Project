def clean_data(data):

    # Remove duplicates
    data = data.drop_duplicates()

    # Fill missing values
    data = data.fillna(0)

    return data