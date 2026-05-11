# Simplified Shor’s Algorithm (Period Finding Demo for N=21)

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile
import numpy as np
import math


# -------------------------------
# CLASSICAL POST-PROCESSING
# -------------------------------

def classical_post_processing(r, a, N):
    if r % 2 != 0:
        return None

    x = pow(a, r // 2, N)

    factor1 = math.gcd(x - 1, N)
    factor2 = math.gcd(x + 1, N)

    if factor1 * factor2 == N and factor1 != 1 and factor2 != 1:
        return factor1, factor2

    return None


# -------------------------------
# SIMULATED PERIOD FINDING
# -------------------------------

def find_period_classically(a, N):
    for r in range(1, N):
        if pow(a, r, N) == 1:
            return r
    return None


# -------------------------------
# MAIN SHOR DRIVER
# -------------------------------

def shor_factor(N):
    print(f"\nFactoring N = {N}")

    # choose random 'a'
    for a in range(2, N):
        if math.gcd(a, N) != 1:
            return math.gcd(a, N), N // math.gcd(a, N)

        r = find_period_classically(a, N)

        if r is None:
            continue

        factors = classical_post_processing(r, a, N)

        if factors:
            return factors

    return None


# -------------------------------
# RUN FOR 21
# -------------------------------

factors_21 = shor_factor(21)
print("Factors of 21:", factors_21)