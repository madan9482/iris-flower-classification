from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load the trained model
model_path = r'C:\Users\dell\OneDrive\Desktop\irisflower-demo\folwermodel.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Create Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract the data from the form
    int_features = [float(x) for x in request.form.values()]
    final_features = np.array([int_features])
    
    # Make prediction
    prediction = model.predict(final_features)
    output = prediction[0]
    
    # Map prediction to class name
    class_names = {0: 'Iris Setosa', 1: 'Iris Versicolor', 2: 'Iris Virginica'}
    flower_class = class_names.get(output, "Unknown Class")
    
    return render_template('index.html', prediction_text=f'Predicted Iris Flower Class: {flower_class}')

if __name__ == "__main__":
    app.run(debug=True)
