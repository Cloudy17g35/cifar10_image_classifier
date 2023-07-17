
# Cifar10 Image Classifier

This project contains two scripts: `model.py` and `main.py`. The `model.py` script is responsible for training a CIFAR-10 image classification model using TensorFlow and saving the trained model. The `main.py` script uses the trained model to classify images uploaded by the user through a Streamlit web application.

## Installation

1. Clone the repository:

> `git clone https://github.com/Cloudy17g35/cifar10_image_classifier.git`

2. Install the required dependencies:

> `pip install -r requirements.txt`


## Usage  1. Train the model by running the `model.py` script:

    python model_training/model.py


This script will download the CIFAR-10 dataset, preprocess the data, train the model, and save the trained model as `cifar10_model.h5`.

2. Run the web application using the `main.py` script:

    streamlit run app/main.py


This will start the web application, and you can access it by opening the provided URL in your web browser.

3. Upload an image through the web application and see the predictions made by the trained model.

## File Structure

- `app/`: Contains the `main.py` script for the web application.
- `model_training/`: Contains the `model.py` script for training the model.

## Dependencies

- TensorFlow
- Keras
- NumPy
- Streamlit
- Matplotlib
- PIL

You can find the complete code in the corresponding script files: [model.py](model_training/model.py) and [main.py](app/main.py).
