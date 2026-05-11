# Quantum Random Number Generator (QRNG) vs Classical RNG

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import random
import matplotlib.pyplot as plt


# -------------------------------
# STEP 1: Quantum RNG Function
# -------------------------------

def quantum_random_bits(num_bits=512):
    backend = Aer.get_backend("aer_simulator")

    qc = QuantumCircuit(1, 1)

    bits = []

    for _ in range(num_bits):
        qc.h(0)
        qc.measure(0, 0)

        qc_transpiled = transpile(qc, backend)
        job = backend.run(qc_transpiled, shots=1)
        result = job.result()

        counts = result.get_counts()
        bit = list(counts.keys())[0]  # '0' or '1'

        bits.append(int(bit))

        qc.reset(0)  # reset for next iteration

    return bits


# -------------------------------
# STEP 2: Classical RNG Function
# -------------------------------

def classical_random_bits(num_bits=512):
    return [random.randint(0, 1) for _ in range(num_bits)]


# -------------------------------
# STEP 3: Generate Data
# -------------------------------

num_bits = 512

quantum_bits = quantum_random_bits(num_bits)
classical_bits = classical_random_bits(num_bits)


# -------------------------------
# STEP 4: Basic Statistical Comparison
# -------------------------------

def analyze(bits):
    zeros = bits.count(0)
    ones = bits.count(1)
    return zeros, ones


q_zeros, q_ones = analyze(quantum_bits)
c_zeros, c_ones = analyze(classical_bits)


print("\n===== Randomness Comparison =====")
print(f"Quantum RNG   → 0s: {q_zeros}, 1s: {q_ones}")
print(f"Classical RNG → 0s: {c_zeros}, 1s: {c_ones}")


# -------------------------------
# STEP 5: Plot Comparison
# -------------------------------

labels = ['0s', '1s']

plt.figure()
plt.bar(labels, [q_zeros, q_ones])
plt.title("Quantum RNG Distribution")

plt.figure()
plt.bar(labels, [c_zeros, c_ones])
plt.title("Classical RNG Distribution")

plt.show()