# --- Kaggle dataset download ---
try:
    import kagglehub
except ImportError:
    raise ImportError("kagglehub is not installed. Please run 'pip install kagglehub' to use Kaggle dataset downloading.")

dataset_id = "shaz13/real-world-documents-collections"
print(f"Downloading Kaggle dataset: {dataset_id}")
dataset_path = kagglehub.dataset_download(dataset_id)
print("Dataset downloaded to:", dataset_path)

# List files in the dataset
import os
for root, dirs, files in os.walk(dataset_path):
    for file in files:
        print(os.path.join(root, file))
