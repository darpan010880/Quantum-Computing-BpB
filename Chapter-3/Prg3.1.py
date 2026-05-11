# Implementing Superposition using Qiskit in Python

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit_aer import AerSimulator

# Create quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard Gate
# |0> --> (|0> + |1>) / sqrt(2)
qc.h(0)

# Draw circuit
print("Quantum Circuit:")
print(qc)
fig=qc.draw(output='mpl')
fig.savefig('Prg3.1_circuit.png')

# Get statevector before measurement
state = Statevector.from_instruction(qc)

print("Statevector:")
print(state)

# Bloch Sphere representation
fig=plot_bloch_multivector(state)
fig.savefig('Prg3.1_state_bloch.png')

# Measure qubit
qc.measure(0, 0)

# Simulate measurement
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()

# Get counts
counts = result.get_counts()

print("Measurement Results:")
print(counts)

# Plot histogram
fig=plot_histogram(counts)
fig.savefig('Prg3.1_measurement.png')