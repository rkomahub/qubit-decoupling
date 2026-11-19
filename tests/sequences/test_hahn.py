import numpy as np
import pytest

from qubit_decoupling.sequences.hahn import hahn_pulse_times


def test_hahn_pulse_is_at_midpoint():
    """Check that a two-second sequence has one pulse at one second."""
    pulse_times = hahn_pulse_times(duration=2.0)

    np.testing.assert_allclose(pulse_times, [1.0])
    

@pytest.mark.parametrize("duration", [0.0, -1.0])
def test_hahn_rejects_non_positive_duration(duration):
    """Check that a Hahn sequence requires a positive duration."""
    with pytest.raises(ValueError, match="duration must be positive"):
        hahn_pulse_times(duration)