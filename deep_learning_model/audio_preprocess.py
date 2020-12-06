from util import *

WINDOW_SIZE = 256
SAMPLE_RATE = 8000
SAMPLE_NUM = 5120
OVERLAP = WINDOW_SIZE // 2

util = Util(WINDOW_SIZE, SAMPLE_RATE, SAMPLE_NUM, OVERLAP)
raw, label = read_radio_file('recordings')
wave = util.cut(raw)
spec = util.ft(wave)

# util.length_hist(spec_raw_x)
# spec = np.log2(spec)

util.show_wave(wave[0, :, 0])
util.show_spec(spec[0, :, :, 0])
