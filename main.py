from src.load_data import load_dataset
from src.cleaning import clean_data
from src.analysis import analyze_data
from src.visualization import visualize_data
from src.prediction import predict_sales


# STEP 1 → Load Dataset
data = load_dataset()

# STEP 2 → Clean Data
data = clean_data(data)

# STEP 3 → Analyze Data
analyze_data(data)

# STEP 4 → Visualize Data
visualize_data(data)

# STEP 5 → Predict Sales
predict_sales(data)