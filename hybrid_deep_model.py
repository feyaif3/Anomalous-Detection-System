import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Load CSV data
data = pd.read_csv('your_data.csv')

# Preprocess data (excluding 'label' column)
features = data.drop(columns=['label']).values
labels = data['label'].values

# Define LSTM Component
lstm_input = keras.Input(shape=(features.shape[1],), name='lstm_input')
lstm_layer = layers.LSTM(64)(lstm_input)

# Define CNN Component
cnn_input = keras.Input(shape=(features.shape[1],), name='cnn_input')
cnn_layer = layers.Dense(32, activation='relu')(cnn_input)

# Define Autoencoder Component
autoencoder_input = keras.Input(
    shape=(features.shape[1],), name='autoencoder_input')
encoded = layers.Dense(128, activation='relu')(autoencoder_input)
decoded = layers.Dense(features.shape[1], activation='sigmoid')(encoded)

autoencoder = keras.Model(inputs=autoencoder_input, outputs=decoded)
autoencoder.compile(optimizer='adam', loss='mean_squared_error')

# Train the Autoencoder on normal data
normal_data = features[labels == 0]
autoencoder.fit(normal_data, normal_data, epochs=10, batch_size=32)

# Define the anomaly detection threshold (adjust as needed)
threshold = 0.1

# Detect anomalies using the autoencoder
reconstruction_errors = np.mean(
    np.square(features - autoencoder.predict(features)), axis=1)
anomalies = (reconstruction_errors > threshold).astype(int)

# Combine Components
combined_input = layers.concatenate(
    [lstm_layer, cnn_layer, autoencoder.output])

# Create the Output Layer for Anomaly Detection
output_layer = layers.Dense(1, activation='sigmoid')(combined_input)

# Create the Hybrid Model
model = keras.Model(inputs=[lstm_input, cnn_input,
                    autoencoder_input], outputs=output_layer)

# Compile the Model
model.compile(optimizer='adam', loss='binary_crossentropy',
              metrics=['accuracy'])
