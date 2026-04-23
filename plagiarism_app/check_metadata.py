import joblib
import os

metadata_path = r'c:\Users\Debasmita\Desktop\Mini Project\plagiarism_app\models\model_metadata.pkl'
if os.path.exists(metadata_path):
    try:
        metadata = joblib.load(metadata_path)
        print("Metadata loaded successfully:")
        for k, v in metadata.items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"Error loading metadata: {e}")
else:
    print("Metadata file not found.")
