import pickle
import joblib
import sys

# Add UniKP_lib to path if needed, though unpickling usually needs classes to be importable
sys.path.append('.')

model_path = 'UniKP_model/UniKP for kcat.pkl'
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print(f"Loaded model type: {type(model)}")
    print(model)
except Exception as e:
    print(f"Error loading pickle: {e}")
