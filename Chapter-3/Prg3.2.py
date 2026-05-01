# Import Qiskit components
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
# Create a quantum circuit with 4 qubits and 4 classical bits
qc = QuantumCircuit(4, 4)
# Apply Hadamard gate to all qubits to create superposition
qc.h(0)
qc.h(1)
qc.h(2)
qc.h(3)
# Measure all qubits
qc.measure([0,1,2,3], [0,1,2,3])
# Use Aer simulator


simulator = AerSimulator()
# Execute the circuit
job = simulator.run(qc, shots=1024)
result = job.result()
# Get counts
counts = result.get_counts(qc)
print("Measurement Results:")
print(counts)
# Plot the histogram
hist=plot_histogram(counts)
hist.savefig('Prg3.2_histogram.png')

# Display Circuit DIagram
circuit_diagram = qc.draw('mpl')
circuit_diagram.savefig('Prg3.2_circuit.png')
