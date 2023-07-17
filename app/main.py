import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import tensorflow as tf


def main():
    st.title('Cifar10 Image Classifier')
    st.write('Upload the image that you think fits in one of the classes and see if the prediction is correct')

    file = st.file_uploader(label='Please upload the files', type=['img', 'png'])

    if file:
        image = Image.open(file)
        st.image(image, use_column_width=True)
        resized_image = image.resize((32,32))
        image_array = np.array(resized_image) / 255
        image_array = image_array.reshape((1, 32, 32, 3))
        
        model = tf.keras.models.load_model('app/cifar10_model.h5')

        predictions = model.predict(image_array)
        cifar10_classes = [
            'airplane', 'automobile', 'bird', 'cat', 
            'deer', 'dog', 'frog', 'horse', 'ship', 'truck'
            ]
        fig, ax = plt.subplots()
        y_pos = np.arange(len(cifar10_classes))
        ax.barh(y_pos, predictions[0], align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(cifar10_classes)
        ax.invert_yaxis()
        ax.set_xlabel('Probability')
        ax.set_title('Cifar10 predicitons')  
        st.pyplot(fig)  

    else:
        st.write('You have not uploaded the file yet')


if __name__ == '__main__':
    main()