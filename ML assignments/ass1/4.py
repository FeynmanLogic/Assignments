import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  


model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),       
    layers.Dense(128, activation='relu'),       
    layers.Dropout(0.2),                        
    layers.Dense(10, activation='softmax')       
])


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',  
              metrics=['accuracy'])


model.fit(x_train, y_train, epochs=10, validation_split=0.2)


test_loss, test_acc = model.evaluate(x_test, y_test)
print("Test accuracy:", test_acc)
