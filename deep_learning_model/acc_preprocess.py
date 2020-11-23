from util import *

# WINDOW_SIZE = 32
# SAMPLE_RATE = 500
# SAMPLE_NUM = 400
# PAD_LENGTH = 17

WINDOW_SIZE = 64
SAMPLE_RATE = 500
SAMPLE_NUM = 300
PAD_LENGTH = 11

util = Util(WINDOW_SIZE, SAMPLE_RATE, SAMPLE_NUM)
wave_raw, label, time = read_acc_file('accelerometer_data')
plt.plot(time[0])
plt.show()

wave_x = list(map(util.cut, wave_raw[0]))
wave_y = list(map(util.cut, wave_raw[1]))
wave_z = list(map(util.cut, wave_raw[2]))

util.show_wave(wave_x[0])
util.show_wave(wave_y[0])
util.show_wave(wave_z[0])

spec_raw_x = list(map(util.ft, wave_x))
spec_raw_y = list(map(util.ft, wave_y))
spec_raw_z = list(map(util.ft, wave_z))

util.length_hist(spec_raw_x)

spec_x = util.pad_and_merge(spec_raw_x, PAD_LENGTH)
spec_y = util.pad_and_merge(spec_raw_y, PAD_LENGTH)
spec_z = util.pad_and_merge(spec_raw_z, PAD_LENGTH)

spec_x = np.log2(spec_x)
spec_y = np.log2(spec_y)
spec_z = np.log2(spec_z)

util.show_spec(spec_x[1])
util.show_spec(spec_y[1])
util.show_spec(spec_z[1])
