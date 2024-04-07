from enum import Enum
import ctypes


# Range Settings
class opt4048RangeT(Enum):
    RANGE_2KLUX2 = 0x00
    RANGE_4KLUX5 = 0x01
    RANGE_9LUX = 0x02
    RANGE_18LUX = 0x03
    RANGE_36LUX = 0x04
    RANGE_72LUX = 0x05
    RANGE_144LUX = 0x06
    RANGE_AUTO = 0x0C


# Conversion Settings
class opt4048ConversionTimeT(Enum):
    CONVERSION_TIME_600US = 0x00
    CONVERSION_TIME_1MS = 0x01
    CONVERSION_TIME_1MS8 = 0x02
    CONVERSION_TIME_3MS4 = 0x03
    CONVERSION_TIME_6MS5 = 0x04
    CONVERSION_TIME_12MS7 = 0x05
    CONVERSION_TIME_25MS = 0x06
    CONVERSION_TIME_50MS = 0x07
    CONVERSION_TIME_100MS = 0x08
    CONVERSION_TIME_200MS = 0x09
    CONVERSION_TIME_400MS = 0x0A
    CONVERSION_TIME_800MS = 0x0B


# Operation mode settings
class opt4048OperationModeT(Enum):
    OPERATION_MODE_POWER_DOWN = 0x00
    OPERATION_MODE_AUTO_ONE_SHOT = 0x01
    OPERATION_MODE_ONE_SHOT = 0x02
    OPERATION_MODE_CONTINUOUS = 0x03


# Fault count settings
class opt4048FaultCountT(Enum):
    FAULT_COUNT_1 = 0x00
    FAULT_COUNT_2 = 0x01
    FAULT_COUNT_3 = 0x02
    FAULT_COUNT_8 = 0x03


# Threshold channel settings
class opt4048ThresholdChannelT(Enum):
    THRESH_CHANNEL_CH0 = 0x00
    THRESH_CHANNEL_CH1 = 0x01
    THRESH_CHANNEL_CH2 = 0x02
    THRESH_CHANNEL_CH3 = 0x03


# Interrupt settings
class opt4048IntCFGT(Enum):
    INT_SMBUS_ALERT = 0x00
    INT_DR_NEXT_CHANNEL = 0x01
    INT_DR_ALL_CHANNELS = 0x03


# Register for Exponent and Result (MSB) for Channel 0
SFE_OPT4048_REGISTER_EXP_RES_CH0 = 0x00


class opt4048_reg_exp_res_ch0_bits_t(ctypes.LittleEndianStructure):
    _fields_ = [
        ("result_msb_ch0", ctypes.c_uint16, 12),
        ("exponent_ch0", ctypes.c_uint8, 4),
    ]


class opt4048_reg_exp_res_ch0_t(ctypes.Union):
    _fields_ = [
        ("bits", opt4048_reg_exp_res_ch0_bits_t),
        ("word", ctypes.c_uint16, 16),
    ]


# Register for Result (LSB), Counter, and CRC for Channel 0
SFE_OPT4048_REGISTER_RES_CNT_CRC_CH0 = 0x01


class opt4048_reg_res_cnt_crc_ch0_bits_t(ctypes.LittleEndianStructure):
    _fields_ = [
        ("crc_ch0", ctypes.c_uint8, 4),
        ("counter_ch0", ctypes.c_uint8, 4),
        ("result_lsb_ch0", ctypes.c_uint8, 8),
    ]


class opt4048_reg_res_cnt_crc_ch0_t(ctypes.Union):
    _fields_ = [
        ("bits", opt4048_reg_res_cnt_crc_ch0_bits_t),
        ("word", ctypes.c_uint16, 16),
    ]


# Register for Exponent and Result (MSB) for Channel 1
SFE_OPT4048_REGISTER_EXP_RES_CH1 = 0x02


class opt4048_reg_exp_res_ch1_bits_t(ctypes.LittleEndianStructure):
    _fields_ = [
        ("result_msb_ch1", ctypes.c_uint16, 12),
        ("exponent_ch1", ctypes.c_uint8, 4),
    ]


class opt4048_reg_exp_res_ch1_t(ctypes.Union):
    _fields_ = [
        ("bits", opt4048_reg_exp_res_ch1_bits_t),
        ("word", ctypes.c_uint16, 16),
    ]


# Register for Result (LSB), Counter, and CRC for Channel 1
SFE_OPT4048_REGISTER_RES_CNT_CRC_CH1 = 0x03


class opt4048_reg_res_cnt_crc_ch1_bits_t(ctypes.LittleEndianStructure):
    _fields_ = [
        ("crc_ch1", ctypes.c_uint8, 4),
        ("counter_ch1", ctypes.c_uint8, 4),
        ("result_lsb_ch1", ctypes.c_uint8, 8),
    ]


class opt4048_reg_res_cnt_crc_ch1_t(ctypes.Union):
    _fields_ = [
        ("bits", opt4048_reg_res_cnt_crc_ch1_bits_t),
        ("word", ctypes.c_uint16, 16),
    ]


# Register for Exponent and Result (MSB) for Channel 2
SFE_OPT4048_REGISTER_EXP_RES_CH2 = 0x04


class opt4048_reg_exp_res_ch2_bits_t(ctypes.LittleEndianStructure):
    _fields_ = [
        ("result_msb_ch2", ctypes.c_uint16, 12),
        ("exponent_ch2", ctypes.c_uint8, 4),
    ]


class opt4048_reg_exp_res_ch2_t(ctypes.Union):
    _fields_ = [
        ("bits", opt4048_reg_exp_res_ch2_bits_t),
        ("word", ctypes.c_uint16, 16),
    ]


# Register for Result (LSB), Counter, and CRC for Channel 2
SFE_OPT4048_REGISTER_RES_CNT_CRC_CH2 = 0x05


class opt4048_reg_res_cnt_crc_ch2_bits_t(ctypes.LittleEndianStructure):
    _fields_ = [
        ("crc_ch2", ctypes.c_uint8, 4),
        ("counter_ch2", ctypes.c_uint8, 4),
        ("result_lsb_ch2", ctypes.c_uint8, 8),
    ]


class opt4048_reg_res_cnt_crc_ch2_t(ctypes.Union):
    _fields_ = [
        ("bits", opt4048_reg_res_cnt_crc_ch2_bits_t),
        ("word", ctypes.c_uint16, 16),
    ]


# Register for Exponent and Result (MSB) for Channel 3
SFE_OPT4048_REGISTER_EXP_RES_CH3 = 0x06


class opt4048_reg_exp_res_ch3_bits_t(ctypes.LittleEndianStructure):
    _fields_ = [
        ("result_msb_ch3", ctypes.c_uint16, 12),
        ("exponent_ch3", ctypes.c_uint8, 4),
    ]


class opt4048_reg_exp_res_ch3_t(ctypes.Union):
    _fields_ = [
        ("bits", opt4048_reg_exp_res_ch3_bits_t),
        ("word", ctypes.c_uint16, 16),
    ]


# Register for Result (LSB), Counter, and CRC for Channel 3
SFE_OPT4048_REGISTER_RES_CNT_CRC_CH3 = 0x07


class opt4048_reg_res_cnt_crc_ch3_bits_t(ctypes.LittleEndianStructure):
    _fields_ = [
        ("crc_ch3", ctypes.c_uint8, 4),
        ("counter_ch3", ctypes.c_uint8, 4),
        ("result_lsb_ch3", ctypes.c_uint8, 8),
    ]


class opt4048_reg_res_cnt_crc_ch3_t(ctypes.Union):
    _fields_ = [
        ("bits", opt4048_reg_res_cnt_crc_ch3_bits_t),
        ("word", ctypes.c_uint16, 16),
    ]


# Register for Threshold  Exponent and Result - Low
SFE_OPT4048_REGISTER_THRESH_L_EXP_RES = 0x08


class opt4048_reg_thresh_exp_res_low_bits_t(ctypes.LittleEndianStructure):
    _fields_ = [
        ("thresh_result", ctypes.c_uint16, 12),
        ("thresh_exp", ctypes.c_uint8, 4),
    ]


class opt4048_reg_thresh_exp_res_low_t(ctypes.Union):
    _fields_ = [
        ("bits", opt4048_reg_thresh_exp_res_low_bits_t),
        ("word", ctypes.c_uint16, 16),
    ]


# Register for Threshold Exponent and Threshold Result - High
SFE_OPT4048_REGISTER_THRESH_H_EXP_RES = 0x09


class opt4048_reg_thresh_exp_res_high_bits_t(ctypes.LittleEndianStructure):
    _fields_ = [
        ("thresh_result", ctypes.c_uint16, 12),
        ("thresh_exp", ctypes.c_uint8, 4),
    ]


class opt4048_reg_thresh_exp_res_high_t(ctypes.Union):
    _fields_ = [
        ("bits", opt4048_reg_thresh_exp_res_high_bits_t),
        ("word", ctypes.c_uint16, 16),
    ]


# Register that controls the main functions of the device.
SFE_OPT4048_REGISTER_CONTROL = 0x0A


class opt4048_reg_control_bits_t(ctypes.LittleEndianStructure):
    _fields_ = [
        ("fault_count", ctypes.c_uint8, 2),
        ("int_pol", ctypes.c_uint8, 1),
        ("latch", ctypes.c_uint8, 1),
        ("op_mode", ctypes.c_uint8, 2),
        ("conversion_time", ctypes.c_uint8, 4),
        ("range", ctypes.c_uint8, 4),
        ("reserved", ctypes.c_uint8, 1),
        ("qwake", ctypes.c_uint8, 1),
    ]


class opt4048_reg_control_t(ctypes.Union):
    _fields_ = [
        ("bits", opt4048_reg_control_bits_t),
        ("word", ctypes.c_uint16, 16),
    ]


# Register with settings for the interrupt pin.
SFE_OPT4048_REGISTER_INT_CONTROL = 0x0B


class opt4048_reg_int_control_bits_t(ctypes.LittleEndianStructure):
    _fields_ = [
        ("i2c_burst", ctypes.c_uint8, 1),
        ("reserved_two", ctypes.c_uint8, 1),
        ("int_cfg", ctypes.c_uint8, 2),
        ("int_dir", ctypes.c_uint8, 1),
        ("threshold_ch_sel", ctypes.c_uint8, 2),
        ("reserved_one", ctypes.c_uint16, 9),
    ]


class opt4048_reg_int_control_t(ctypes.Union):
    _fields_ = [
        ("bits", opt4048_reg_int_control_bits_t),
        ("word", ctypes.c_uint16, 16),
    ]


# Register containing various status flags.
SFE_OPT4048_REGISTER_FLAGS = 0x0C


class opt4048_reg_flags_bits_t(ctypes.LittleEndianStructure):
    _fields_ = [
        ("flag_low", ctypes.c_uint8, 1),
        ("flag_high", ctypes.c_uint8, 1),
        ("conv_ready_flag", ctypes.c_uint8, 1),
        ("overload_flag", ctypes.c_uint8, 1),
        ("reserved", ctypes.c_uint16, 12),
    ]


class opt4048_reg_flags_t(ctypes.Union):
    _field_ = [
        ("bits", opt4048_reg_flags_bits_t),
        ("word", ctypes.c_uint16, 16),
    ]


# Register containing the device ID.
SFE_OPT4048_REGISTER_DEVICE_ID = 0x11


class opt4048_reg_device_id_bits_t(ctypes.LittleEndianStructure):
    _fields_ = [
        ("DIDH", ctypes.c_uint16, 12),
        ("DIDL", ctypes.c_uint8, 2),
        ("reserved", ctypes.c_uint16, 2),
    ]


class opt4048_reg_device_id_t(ctypes.Union):
    _fields_ = [
        ("bits", opt4048_reg_device_id_bits_t),
        ("word", ctypes.c_uint16, 16),
    ]
