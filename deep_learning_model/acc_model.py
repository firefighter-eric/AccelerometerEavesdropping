from sklearn.model_selection import train_test_split

from util import *
import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.utils import shuffle
from sklearn.metrics import confusion_matrix
from tensorflow.keras import layers
from tensorflow.keras import models

WINDOW_SIZE = 16
OVERLAP = 8
SAMPLE_RATE = 500
SAMPLE_NUM = 300
# PAD_LENGTH = 38

util = Util(WINDOW_SIZE, SAMPLE_RATE, SAMPLE_NUM, OVERLAP)
raw, label, time = read_acc_file('accelerometer_data')

wave = util.cut(raw)
spec = util.ft(wave)
spec = np.log2(spec)

spec = spec[:, 2:, 1:-1, :]
n_data, spec_length, time_length, channel_num = spec.shape

BATCH_SIZE = 64

data, label = shuffle(spec, label)
X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.2)

input_shape = (spec_length, time_length, channel_num)
num_labels = len(set(label))

model = models.Sequential([
    layers.Input(shape=input_shape),
    # preprocessing.(32, 32),
    layers.BatchNormalization(),
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

model.fit(x=X_train, y=y_train,
          batch_size=BATCH_SIZE, epochs=200,
          validation_data=(X_test, y_test),
          verbose=1)

y_pred = np.argmax(model.predict(X_test), axis=1)
confusion_mtx = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 8))
plt.imshow(confusion_mtx)
plt.xlabel('Prediction')
plt.ylabel('Label')
plt.show()
