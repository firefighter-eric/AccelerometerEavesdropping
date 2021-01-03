from util import *

WINDOW_SIZE = 16
OVERLAP = 8
SAMPLE_RATE = 500
SAMPLE_NUM = 300
PAD_LENGTH = 38

# WINDOW_SIZE = 32
# OVERLAP = 30
# SAMPLE_RATE = 500
# SAMPLE_NUM = 300
# PAD_LENGTH = 151

# WINDOW_SIZE = 64
# OVERLAP = 60
# SAMPLE_RATE = 500
# SAMPLE_NUM = 300
# PAD_LENGTH = 76

# WINDOW_SIZE = 128
# OVERLAP = 120
# SAMPLE_RATE = 500
# SAMPLE_NUM = 300
# PAD_LENGTH = 38

util = Util(WINDOW_SIZE, SAMPLE_RATE, SAMPLE_NUM, OVERLAP)
raw, label, time = read_acc_file('accelerometer_data')

wave = util.cut(raw)
# plt.plot(time[0])
# plt.show()

util.show_wave(wave[0, :, 0])
util.show_wave(wave[0, :, 1])
util.show_wave(wave[0, :, 2])

spec = util.ft(wave)

# util.length_hist(spec_raw_x)
spec = np.log2(spec)

util.show_spec(spec[0, :, :, 0])
util.show_spec(spec[0, :, :, 1])
util.show_spec(spec[0, :, :, 2])
