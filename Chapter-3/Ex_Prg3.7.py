# Demonstrate Quantum Interference
# Task :Construct a quantum circuit with 1 qubit. Apply Hadamard → Z → Hadamard gates and measure the output. Explain the result based on interference.
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create 1-qubit circuit
qc = QuantumCircuit(1, 1)
#qc.measure(0, 0)
# Apply gates
qc.h(0)   # Hadamard
qc.z(0)   # Z gate (phase flip)
qc.h(0)   # Hadamard again

# Measure
qc.measure(0, 0)

# Show circuit
print(qc.draw())

# Simulator
simulator = AerSimulator()
compiled = transpile(qc, simulator)

# Run simulation
job = simulator.run(compiled, shots=1024)
result = job.result()

counts = result.get_counts()

print("Measurement Results:", counts)

# Plot histogram
fig=plot_histogram(counts)
fig.savefig('Ex_Prg3.7_histogram.png')    
fig= qc.draw('mpl')
fig.savefig('Ex_Prg3.7_circuit.png')