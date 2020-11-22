from util import *

WINDOW_SIZE = 256
SAMPLE_RATE = 8000
SAMPLE_NUM = 5120

util = Util(WINDOW_SIZE, SAMPLE_RATE, SAMPLE_NUM)
wave_raw, label = read_radio_file('recordings')
spec_raw = list(map(util.ft, wave_raw))
util.length_hist(spec_raw)
spec = util.pad_and_merge(spec_raw, 80)
util.show_spec(spec[50])
