import pytest

from qubit_decoupling.evolution import free_evolution_phase


def test_free_evolution_phase_matches_constant_detuning():
    """Check the phase against an independently calculated constant-detuning result."""
    phase = free_evolution_phase(detuning=2.0, duration=0.5)

    assert phase == pytest.approx(1.0)
    

def test_free_evolution_phase_is_zero_at_zero_duration():
    """Check that no phase accumulates when no time elapses."""
    phase = free_evolution_phase(detuning=2.0, duration=0.0)

    assert phase == pytest.approx(0.0)
    

def test_free_evolution_phase_allows_negative_detuning():
    """Check that negative detuning reverses the accumulated phase."""
    phase = free_evolution_phase(detuning=-2.0, duration=0.5)

    assert phase == pytest.approx(-1.0)
    

def test_free_evolution_phase_rejects_negative_duration():
    """Check that a negative evolution duration is rejected."""
    with pytest.raises(ValueError, match="duration must be non-negative"):
        free_evolution_phase(detuning=2.0, duration=-0.5)