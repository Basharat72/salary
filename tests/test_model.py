import os
import pickle
import numpy as np

def test_model_file_exists():
    assert os.path.exists('model.pkl'), "Model file 'model.pkl' missing. Run model_trainer.py."

def test_model_prediction_range():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    # Test prediction with 5 years experience
    pred = model.predict(np.array([[5]]))[0]
    assert 20000 < pred < 100000, f"Prediction {pred} out of expected salary range."
