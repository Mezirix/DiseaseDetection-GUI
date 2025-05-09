from flask import Flask, request, render_template
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

app = Flask(__name__)

# Load the saved model
model_path = "Models/my_Updated_DenseNet_Model_final.keras"
# model_path = "C:/Users/Chimeziri Anyanwu/OneDrive/Web Dev. Tools/AIDA Projects/DiseaseDetection GUI/my_Updated_DenseNet_Model_final.keras"
model = load_model(model_path)

# Define class labels (unified_class_indices)
unified_class_indices = {
    'Bacterial Spot': 0,
    'Healthy': 1,
    'Apple Scab': 2,
    'Black Rot': 3,
    'Cedar Apple Rust': 4,
    'Powdery Mildew': 5,
    'Esca (Black Measles)': 6,
    'Leaf Blight': 7,
    'Early Blight': 8,
    'Late Blight': 9
}

@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        img_file = request.files["file"]
        if img_file:
            # Ensure the uploads directory exists
            uploads_dir = os.path.join(os.getcwd(), 'uploads')
            if not os.path.exists(uploads_dir):
                os.makedirs(uploads_dir)
                
            img_path = os.path.join(uploads_dir, img_file.filename)
            img_file.save(img_path)

            # Preprocess the image
            img = image.load_img(img_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0

            # Make predictions
            prediction = model.predict(img_array)
            predicted_class_index = np.argmax(prediction, axis=1)[0]
            
            # Map the predicted class index to class label
            class_labels = list(unified_class_indices.keys())
            predicted_class_label = class_labels[predicted_class_index]
            probability = prediction[0][predicted_class_index] * 100

            return render_template("result.html", prediction=f"{predicted_class_label} ({probability:.2f}%)")

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
