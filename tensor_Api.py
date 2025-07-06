# from flask import Flask, request, jsonify
# import tensorflow as tf
# import numpy as np
# from PIL import Image
# import os

# app = Flask(__name__)

# # Load your saved model (.keras or .h5)
# model = tf.keras.models.load_model('flowers_model.keras')

# # If you have saved your class names, load them here:
# class_names = sorted(['daisy', 'dandelion', 'rose', 'sunflower', 'tulip'])  # example

# # Image size
# IMG_SIZE = (180, 180)

# @app.route('/predict-multiple', methods=['POST'])
# def predict_multiple():
#     files = request.files.getlist("images")
#     if not files:
#         return jsonify({"error": "No images uploaded."}), 400

#     batch = []
#     filenames = []

#     for file in files:
#         img = Image.open(file.stream).resize(IMG_SIZE)
#         img_array = tf.keras.utils.img_to_array(img)
#         batch.append(img_array)
#         filenames.append(file.filename)

#     batch = np.stack(batch, axis=0)

#     predictions = model.predict(batch)

#     results = []
#     for i, pred in enumerate(predictions):
#         predicted_index = np.argmax(pred)
#         predicted_class = class_names[predicted_index]
#         results.append({
#             "filename": filenames[i],
#             "predicted_class": predicted_class
#         })

#     return jsonify(results)


# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the model
model = tf.keras.models.load_model('flowers_model.keras')

# Your class names
class_names = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if 'images' not in request.files:
        return jsonify({'error': 'No images part'}), 400

    files = request.files.getlist('images')
    results = []

    for file in files:
        img = Image.open(file).resize((180, 180))
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        prediction = model.predict(img_array)
        predicted_index = np.argmax(prediction[0])
        predicted_class = class_names[predicted_index]

        results.append({
            'filename': file.filename,
            'predicted_class': predicted_class
        })

    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)
