import qutip as qt


def free_evolution_phase(detuning, duration):
    """Return phase in radians for constant detuning (rad/s) and duration (s)."""
    if duration < 0:
        raise ValueError("duration must be non-negative")

    return detuning * duration


def free_evolution_state(initial_state, detuning, duration):
    """Evolve a qubit state with detuning in rad/s and duration in seconds."""
    phase = free_evolution_phase(detuning, duration)
    propagator = (-0.5j * phase * qt.sigmaz()).expm()

    return propagator * initial_state