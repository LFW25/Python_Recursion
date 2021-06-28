# Herbert the Heffalump is trying to climb up a scree slope.
# He finds that the best approach is to rush up the slope until he's exhausted, then pause to get his breath back.
# However, while he pauses each time, the slope settles underneath him, carrying him back down part of the slope he just climbed.
# The function num_rushes(slope_height, rush_height_gain, back_sliding)
# calculates how many rushes it takes Herbert to climb up a slope of height slope_height metres,
# given that each rush gains him rush_height_gain metres before he slides back back_sliding metres during the pause before the next rush.
# The final rush will still be counted as 1 rush, even though it may be of shorter duration than the previous rushes.

def num_rushes(slope_height, rush_height_gain, back_sliding):
    """ Herbert the Heffalump, recursively
        Inputs:
        - slope_height: the total height of the slope Herbert is trying to climb
        - rush_height_gain: the height Herbert gains with each rush
        - back_sliding: the height Herbert loses with each rest
        Ouputs:
        The number of rushes required for Herbert to reach the top of the slope
    """
    if slope_height <= rush_height_gain:
        return 1
    else:
        slope_height = slope_height - rush_height_gain + back_sliding
        return 1 + num_rushes(slope_height, 0.95*rush_height_gain, 0.95*back_sliding)
