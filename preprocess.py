import os
import pathlib
from scipy.io import wavfile
from scipy.signal import stft

import matplotlib.pyplot as plt
import numpy as np

WINDOW_SIZE = 256
SAMPLE_RATE = 8000
SAMPLE_LENGTH = 5120


def read_file(path):
    sub_paths = os.listdir(path)
    data = []
    label = []
    for sub_path in sub_paths:
        files = os.listdir(path + '/' + sub_path)
        for file in files:
            _, sig = wavfile.read(path + '/' + sub_path + '/' + file)
            data.append(sig)
            label.append(int(sub_path))
    return data, np.array(label)


def ft(wave):
    _, _, spec = stft(wave, nperseg=WINDOW_SIZE, padded=True)
    return np.abs(spec)


def show_spec(spec):
    plt.imshow(spec)
    plt.show()


def length_hist(spec):
    ans = []
    for s in spec:
        ans.append(s.shape[1])
    plt.hist(ans, bins=20, range=(0, 100))
    plt.show()


def pad_and_merge(spec, pad_length):
    out = np.zeros(shape=(len(spec), WINDOW_SIZE // 2 + 1, pad_length))
    for i, s in enumerate(spec):
        if s.shape[1] < 50:
            out[i, :, :s.shape[1]] = s[:, :]
        else:
            out[i] = s[:, :50]
    return out


if __name__ == '__main__':
    wave_raw, label = read_file('recordings')
    spec_raw = list(map(ft, wave_raw))
    length_hist(spec_raw)
    spec = pad_and_merge(spec_raw, 50)
    show_spec(spec[0])
