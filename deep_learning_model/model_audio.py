from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

from util import *
import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.utils import shuffle
from tensorflow.keras import layers
from tensorflow.keras import models

WINDOW_SIZE = 256
SAMPLE_RATE = 8000
SAMPLE_NUM = 5120
PADDING_NUM = 50

util = Util(WINDOW_SIZE, SAMPLE_RATE, SAMPLE_NUM)
wave_raw, label = read_radio_file('recordings')
spec_raw = list(map(util.ft, wave_raw))
spec = util.pad_and_merge(spec_raw, PADDING_NUM)

n_data, spec_length, time_length = spec.shape

BATCH_SIZE = 32
spec = spec.reshape(n_data, spec_length, time_length, 1)

data, label = shuffle(spec, label)
X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.2)

input_shape = (spec_length, time_length, 1)
num_labels = len(set(label))

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

model.fit(x=X_train, y=y_train,
          batch_size=BATCH_SIZE, epochs=10,
          validation_data=(X_test, y_test))
y_pred = np.argmax(model.predict(X_test), axis=1)
confusion_mtx = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 8))
plt.imshow(confusion_mtx)
plt.xlabel('Prediction')
plt.ylabel('Label')
plt.show()
