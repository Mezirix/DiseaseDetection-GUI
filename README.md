# Disease Detection GUI

## Overview
This project was part of my final year at Saskatchewan Polytechnic, completed in collaboration with my teammates Idongesit Utah and Evelyn Emoedume.
This repository contains a project for detecting diseases in various plant leaves using a Convolutional Neural Network (CNN). The project includes a Flask-based graphical user interface (GUI) that allows users to upload images of plant leaves and receive predictions on the type of disease affecting the plant.

The goal of this project is to leverage deep learning to assist farmers and agricultural experts in diagnosing plant diseases, thereby promoting timely intervention and improving crop yields.

## Features
- **Image Upload**: Users can upload images of plant leaves through a simple web interface.
- **Disease Classification**: The model predicts the disease type with a confidence score.
- **Model Architecture**: Built using a pre-trained DenseNet model fine-tuned for plant disease classification.

## Project Structure
- **app.py**: The Flask application that serves the web interface.
- **model**: The directory contains the trained model files.
- **templates**: Contains HTML files (`upload.html` and `result.html`) used by Flask to render the user interface.
- **static**: This folder is used for storing static files like images, CSS, and JavaScript.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Mezirix/DiseaseDetection-GUI.git
   ```
2. Navigate to the project directory:
   ```bash
   cd DiseaseDetection-GUI
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure you have the trained model file (`my_Updated_DenseNet_Model_best.keras`) placed in the appropriate directory (`./model`).

## Running the Application
To run the Flask application, execute the following command:
```bash
python app.py
```
After running this command, you should be able to access the application at `http://127.0.0.1:5000/` in your web browser.

## Usage
1. **Upload an Image**: Click on "Choose File" and upload an image of a plant leaf.
2. **View Prediction**: Click the "Submit" button to receive the disease classification and its confidence score.

## Technologies Used
- **TensorFlow/Keras**: For building and training the deep learning model.
- **Flask**: To create the web interface.
- **HTML/CSS**: For front-end development.

## Model Information
The disease detection model is a custom fine-tuned version of the DenseNet architecture. It has been trained on a dataset of plant leaves affected by different diseases, covering multiple classes like **Bacterial Spot**, **Apple Scab**, **Black Rot**, etc.

## Contributing
Feel free to open issues or submit pull requests if you would like to contribute to the project.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
If you have any questions or suggestions, feel free to reach out to me at [Mezirix](https://github.com/Mezirix).

---

We welcome feedback and contributions! Let us know if you found this project useful or if you have ideas for improvement.

