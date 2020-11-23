from sklearn.model_selection import train_test_split

from util import *
import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.utils import shuffle
from sklearn.metrics import confusion_matrix
from tensorflow.keras import layers
from tensorflow.keras import models

WINDOW_SIZE = 64
SAMPLE_RATE = 500
SAMPLE_NUM = 300
PAD_LENGTH = 11

util = Util(WINDOW_SIZE, SAMPLE_RATE, SAMPLE_NUM)
wave_raw, label, time = read_acc_file('accelerometer_data')

spec_raw_x = list(map(util.ft, wave_raw[0]))
spec_raw_y = list(map(util.ft, wave_raw[1]))
spec_raw_z = list(map(util.ft, wave_raw[2]))

spec_x = util.pad_and_merge(spec_raw_x, PAD_LENGTH)
spec_y = util.pad_and_merge(spec_raw_y, PAD_LENGTH)
spec_z = util.pad_and_merge(spec_raw_z, PAD_LENGTH)

n_data, spec_length, time_length = spec_x.shape
spec = np.empty(shape=(n_data, spec_length, time_length, 3))
spec[:, :, :, 0] = spec_x
spec[:, :, :, 1] = spec_y
spec[:, :, :, 2] = spec_z
spec = spec[:, 2:, :, :]
n_data, spec_length, time_length, channel_num = spec.shape
spec = np.log2(spec)

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
