import numpy as np

from constants import c, G


def tov_const_density(big_r: np.float64, big_m: np.ndarray, rho: np.ndarray, r: np.ndarray):

    return np.real((c ** 2 * rho * ((big_r * np.sqrt(big_r - 2 * G * big_m[-1] / c ** 2)
                 - np.emath.sqrt(big_r ** 3 - 2 * G * big_m[-1] * r ** 2 / c ** 2)) /
                (np.emath.sqrt(big_r ** 3 - 2 * G * big_m[-1] * r ** 2 / c ** 2) - 3 * big_r *
                 np.sqrt(big_r - 2 * G * big_m[-1] / c ** 2))) * (r < big_r)))
