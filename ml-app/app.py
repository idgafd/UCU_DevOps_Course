from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import os
from flask import Flask, request, jsonify, render_template_string, url_for

app = Flask(__name__)

# Load the Iris dataset and train the model
iris = load_iris()
model = DecisionTreeClassifier()
model.fit(iris.data, iris.target)

# Flower names and their corresponding image filenames
flower_names = ["Setosa", "Versicolor", "Virginica"]
flower_images = ["iris_setosa.jpg", "iris_versicolor.jpg", "iris_virginica.jpg"]

# HTML template for the main page
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ML Prediction</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f9f9f9;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        form {
            display: inline-block;
            text-align: left;
            padding: 15px;
            border: 1px solid #ddd;
            background: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        label {
            font-weight: bold;
        }
        input[type="text"] {
            margin-bottom: 10px;
            padding: 8px;
            width: 100%;
            box-sizing: border-box;
        }
        button {
            padding: 10px 15px;
            font-size: 16px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        img {
            margin-top: 20px;
            max-width: 300px;
            border-radius: 10px;
        }
        .result {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Predict Iris Flower</h1>
    <form action="/predict-form" method="post">
        <label for="feature1">Feature 1:</label>
        <input type="text" id="feature1" name="feature1" required><br><br>
        <label for="feature2">Feature 2:</label>
        <input type="text" id="feature2" name="feature2" required><br><br>
        <label for="feature3">Feature 3:</label>
        <input type="text" id="feature3" name="feature3" required><br><br>
        <label for="feature4">Feature 4:</label>
        <input type="text" id="feature4" name="feature4" required><br><br>
        <button type="submit">Predict</button>
    </form>
    {% if prediction is not none %}
        <div class="result">
            <h2>Prediction: {{ prediction }}</h2>
            <img src="{{ image_url }}" alt="Flower Image" style="max-width: 300px;">
        </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    # Render the home page with no prediction initially
    return render_template_string(html_template, prediction=None, image_url=None)

@app.route("/predict-form", methods=["POST"])
def predict_form():
    try:
        # Retrieve features from the form input
        feature1 = float(request.form["feature1"])
        feature2 = float(request.form["feature2"])
        feature3 = float(request.form["feature3"])
        feature4 = float(request.form["feature4"])
        features = [feature1, feature2, feature3, feature4]

        # Make the prediction
        prediction_index = model.predict([features])[0]
        prediction_name = flower_names[prediction_index]
        prediction_image = flower_images[prediction_index]

        # Return the result with the corresponding image
        return render_template_string(
            html_template,
            prediction=prediction_name,
            image_url=url_for('static', filename=prediction_image)
        )
    except Exception as e:
        # Handle any errors and display the error message
        return render_template_string(html_template, prediction=f"Error: {str(e)}", image_url=None)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Retrieve JSON data from the request
        data = request.get_json()
        prediction_index = model.predict([data["features"]])[0]
        prediction_name = flower_names[prediction_index]
        return jsonify({"prediction": prediction_name})
    except Exception as e:
        # Return an error response in JSON format
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    # Run the Flask server on port 8050
    app.run(host="0.0.0.0", port=8050)
