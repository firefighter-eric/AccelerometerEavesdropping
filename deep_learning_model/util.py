import os

import numpy as np
import matplotlib.pyplot as plt

from scipy.io import wavfile
from scipy.signal import stft


class Util:
    def __init__(self, window_size, sample_rate, sample_num):
        self.WINDOW_SIZE = window_size
        self.SAMPLE_RATE = sample_rate
        self.SAMPLE_NUM = sample_num

    def cut(self, wave):
        return wave[:self.SAMPLE_NUM]

    def ft(self, wave):
        _, _, spec = stft(wave, nperseg=self.WINDOW_SIZE, padded=True)
        return np.abs(spec)

    @staticmethod
    def show_wave(wave):
        plt.plot(wave)
        plt.show()

    @staticmethod
    def show_spec(spec):
        plt.imshow(spec)
        plt.show()

    @staticmethod
    def length_hist(spec):
        ans = []
        for s in spec:
            ans.append(s.shape[1])
        plt.hist(ans, bins=20, range=(0, 100))
        plt.show()

    def pad_and_merge(self, spec, pad_length):
        out = np.zeros(shape=(len(spec), self.WINDOW_SIZE // 2 + 1, pad_length))
        for i, s in enumerate(spec):
            if s.shape[1] < pad_length:
                out[i, :, :s.shape[1]] = s[:, :]
            else:
                out[i] = s[:, :pad_length]
        return out


def read_radio_file(path):
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


def read_acc_file(path):
    def line2array(line):
        return np.array(list(map(float, line.split(',')[:-1])))

    sub_paths = os.listdir(path)
    time = []
    data = [[], [], []]
    label = []
    for sub_path in sub_paths:
        files = os.listdir(path + '/' + sub_path)
        for file in files:
            f = open(path + '/' + sub_path + '/' + file).read().split()
            if not f or f[0].startswith('\n'):
                continue
            time.append(line2array(f[0]))
            data[0].append(line2array(f[1]))
            data[1].append(line2array(f[2]))
            data[2].append(line2array(f[3]))
            label.append(int(sub_path))
    return data, np.array(label), time
