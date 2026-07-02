from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

app = Flask(__name__)

CORS(app)

model = load_model("sign_language_cnn.keras")

# Home route
@app.route('/')
def home():
    return "Flask Backend Running Successfully!"

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    return jsonify({
        "username": data["username"]
    })

# Predict route
@app.route('/predict', methods=['POST'])
def predict():

    try:

        file = request.files['image']

        image = Image.open(file)

        image = image.convert('L')

        image = image.resize((28, 28))

        image = np.array(image)

        image = 255 - image   # invert colors

        image = image / 255.0

        image = image.reshape(1, 28, 28, 1)

        prediction = model.predict(image)

        predicted_class = np.argmax(prediction)

        labels = {
                0: "A", 
                1: "B",
                2: "C",
                3: "D",
                4: "E",
                5: "F",
                6: "G",
                7: "H",
                8: "I",
                9: "K",
                10: "L",
                11: "M",
                12: "N",
                13: "O",
                14: "P",
                15: "Q",
                16: "R",
                17: "S",
                18: "T",
                19: "U",
                20: "V",
                21: "W",
                22: "X",
                23: "Y"
            }

        print("Predicted Class:", predicted_class)

        return jsonify({
             "prediction": labels[predicted_class]
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


        
if __name__ == '__main__':
    app.run(debug=True)


