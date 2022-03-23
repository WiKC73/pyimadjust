import numpy as np

def imadjust(img, low_in, high_in, low_out, high_out, gamma):

    out = np.power((img - low_in) / (high_in - low_in), gamma) * (high_out - low_out) + low_out
    out = np.where(out < low_out, low_out, out)
    out = np.where(out > high_out, high_out, out)

    return out