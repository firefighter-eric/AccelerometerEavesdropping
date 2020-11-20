from preprocess import *
import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.utils import shuffle
from tensorflow.keras import layers
from tensorflow.keras import models

wave_raw, label = read_file('recordings')
spec_raw = list(map(ft, wave_raw))
spec = pad_and_merge(spec_raw, 50)

n_data, spec_length, time_length = spec.shape

BATCH_SIZE = 32
spec = spec.reshape(n_data, spec_length, time_length, 1)
train_data, label = shuffle(spec, label)

input_shape = (spec_length, time_length, 1)
num_labels = 10

model = models.Sequential([
    layers.Input(shape=input_shape),
    # preprocessing.(32, 32),
    layers.Conv2D(32, 3, activation='relu'),
    layers.Conv2D(64, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Dropout(0.25),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(num_labels),
])
model.summary()

model.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy'],
)

model.fit(x=train_data, y=label, batch_size=BATCH_SIZE, epochs=10)
