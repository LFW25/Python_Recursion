def num_rushes(slope_height, rush_height_gain, back_sliding):
    """ Herbert the Heffalump
    recursively"""
    if slope_height <= rush_height_gain:
        return 1
    else:
        slope_height = slope_height - rush_height_gain + back_sliding
        return 1 + num_rushes(slope_height, 0.95*rush_height_gain, 0.95*back_sliding)