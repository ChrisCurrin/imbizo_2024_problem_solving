from __future__ import annotations
import numpy as np
import functools


def heaviside(x):
    """Heaviside step function which returns True when x is 0 or greater, and
    False otherwise"""
    return x >= 0


def g_syn(t, spks, g_max=50, tau=5):
    """Single exponential conductance decay using equation 6.

    :param t: time point at which to evaluate (ms)
    :param spks: list of time points (ms) of incoming signals (presynaptic action potentials)
    :param g_max: maximum synaptic conductance (nS) [default: 50]
    :param tau: synapse time constant (ms) [default: 5]
    :return: value of synaptic conductance (nS) at time t

    Tests
    ------
    >>> g_syn(1,[1],50,5) # command starting with '>>>' and expected output below
    50.0
    >>> g_syn(1,1,50,5) # a number instead of list is passed
    50.0
    >>> g_syn(1,2,50,5) # a number instead of list is passed
    0.0
    >>> g_syn(1,np.array([1]),50,5) # a numpy array
    50.0
    >>> g_syn(1,[10000],50,5) # a spk is waaaay ahead of t
    0.0
    >>> g_syn(1,[1,10000],50,5) # a spk is waaaay ahead of t
    50.0
    >>> g_syn(10000,[1],50,5) # t is waaaay after spk
    0.0
    """
    total = 0.0  # we iterate from 0 until the length of the spks list (e.g. 100)
    for i in range(len(spks)):
        total += g_max * np.e ** (-(t - spks[i]) / tau) * heaviside(t - spks[i])
    return total


def I_single_exp(
    t: float,
    V_t: float,
    spks: list[float] | np.ndarray,
    g_max: float,
    tau: float,
    E: float,
):
    """
    Calculate the current generated by a single exponential synapse.

    Parameters:
        t (float): The time point at which to calculate the current (ms).
        V_t (float): The membrane potential at time t (mV).
        spks (list[float]): The list of spike times (ms).
        g_max (float): The maximum conductance of the synapse (nS).
        tau (float): The time constant of the synapse (ms).
        E (float): The reversal potential of the synapse (mV).

    Returns:
        float: The current generated by the synapse at time t (mA).
    """
    return 1e-3 * g_syn(t, spks, g_max, tau) * (V_t - E)


# Excitatory synapse
I_AMPA = functools.partial(I_single_exp, g_max=50, tau=4, E=0)
# Inhibitory synapse
I_GABA = functools.partial(I_single_exp, g_max=50, tau=8, E=-70)
