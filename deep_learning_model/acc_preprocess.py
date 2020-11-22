from util import *

WINDOW_SIZE = 32
SAMPLE_RATE = 500
SAMPLE_NUM = 400

util = Util(WINDOW_SIZE, SAMPLE_RATE, SAMPLE_NUM)
wave_raw, label, time = read_acc_file('accelerometer_data')
plt.plot(time[0])

util.show_wave(wave_raw[0][0])
util.show_wave(wave_raw[1][0])
util.show_wave(wave_raw[2][0])

spec_raw_x = list(map(util.ft, wave_raw[0]))
spec_raw_y = list(map(util.ft, wave_raw[1]))
spec_raw_z = list(map(util.ft, wave_raw[2]))

util.length_hist(spec_raw_x)
PAD_LENGTH = 17
spec_x = util.pad_and_merge(spec_raw_x, PAD_LENGTH)
spec_y = util.pad_and_merge(spec_raw_y, PAD_LENGTH)
spec_z = util.pad_and_merge(spec_raw_z, PAD_LENGTH)
util.show_spec(spec_x[1])
util.show_spec(spec_y[1])
util.show_spec(spec_z[1])
