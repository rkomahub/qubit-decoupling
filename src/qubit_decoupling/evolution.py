def free_evolution_phase(detuning, duration):
    """Return phase in radians for constant detuning (rad/s) and duration (s)."""
    if duration < 0:
        raise ValueError("duration must be non-negative")

    return detuning * duration