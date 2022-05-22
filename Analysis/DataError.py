import numpy as np


def Radial_Error(x_ideal, x_meas, y_ideal, y_meas):
    """

    :param x_ideal:
    :param x_meas:
    :param y_ideal:
    :param y_meas:
    :return:
    """
    # Create List of error b/w points
    x_ideal = np.asarray(x_ideal)
    x_meas = np.asarray(x_meas)
    y_ideal = np.asarray(y_ideal)
    y_meas = np.asarray(y_meas)
    radial_error = np.sqrt(((x_meas - x_ideal) ** 2 + (y_meas - y_ideal) ** 2))
    # Calculate Max, average, 3-sigma limit
    try:
        radial_error_max = np.max(radial_error)
        radial_error_ave = np.mean(radial_error)
        radial_error_3sig = radial_error.mean() + 3 * radial_error.std()
    except ValueError:
        radial_error_max = 0
        radial_error_ave = 0
        radial_error_3sig = 0

    return radial_error, radial_error_ave, radial_error_max, radial_error_3sig
