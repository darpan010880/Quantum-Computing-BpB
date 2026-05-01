# 1. Superposition Simulation
# Task: Write a Qiskit program to apply a Hadamard gate to a single qubit initialized in state |0⟩. Display the histogram of the measurement results.

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create circuit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate
qc.h(0)

# Measure qubit
qc.measure(0, 0)

# Print circuit
print(qc.draw())

# Use Aer Simulator
simulator = AerSimulator()

# Transpile circuit for simulator
compiled_circuit = transpile(qc, simulator)

# Run simulation
job = simulator.run(compiled_circuit, shots=1024)

# Get result
result = job.result()
counts = result.get_counts()

# Print output
print("Measurement Results:", counts)

# Show histogram
fig=plot_histogram(counts)
fig.savefig('Ex_Prg3.5_histogram.png')


fig= qc.draw('mpl')
fig.savefig('Ex_Prg3.5_circuit.png')    