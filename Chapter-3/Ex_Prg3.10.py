#   Compare Classical vs Quantum Coin Toss
#   Task: Simulate a classical random bit using Python and compare it to a quantum random bit generated via Hadamard + measurement. Plot and compare distributions.

import random
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Number of tosses
shots = 1000

# -----------------------------------
# Classical Coin Toss
# -----------------------------------
classical_results = [random.randint(0, 1) for _ in range(shots)]

classical_counts = {
    '0': classical_results.count(0),
    '1': classical_results.count(1)
}

print("Classical Coin Toss Results:")
print(classical_counts)

# -----------------------------------
# Quantum Coin Toss
# -----------------------------------
qc = QuantumCircuit(1, 1)

qc.h(0)              # Put qubit into superposition
qc.measure(0, 0)     # Measure

simulator = AerSimulator()
compiled = transpile(qc, simulator)

job = simulator.run(compiled, shots=shots)
result = job.result()

quantum_counts = result.get_counts()

print("\nQuantum Coin Toss Results:")
print(quantum_counts)

# -----------------------------------
# Plot Comparison
# -----------------------------------
fig, axes = plt.subplots(1, 2, figsize=(10,4))

# Classical Plot
axes[0].bar(classical_counts.keys(), classical_counts.values())
axes[0].set_title("Classical Coin Toss")
axes[0].set_xlabel("Outcome")
axes[0].set_ylabel("Counts")

# Quantum Plot
axes[1].bar(quantum_counts.keys(), quantum_counts.values())
axes[1].set_title("Quantum Coin Toss")
axes[1].set_xlabel("Outcome")
axes[1].set_ylabel("Counts")

fig=plt.tight_layout()

fig=qc.draw('mpl')
fig.savefig('Ex_Prg3.10_circuit.png')

fig=plot_histogram(quantum_counts)      
fig.savefig('Ex_Prg3.10_histogram.png')