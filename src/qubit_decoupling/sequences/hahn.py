import numpy as np


def hahn_pulse_times(duration):
    """Return the Hahn echo pulse time in seconds for a positive duration."""
    if duration <= 0:
        raise ValueError("duration must be positive")

    return np.array([duration / 2])