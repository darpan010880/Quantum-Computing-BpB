# 1. Create a Qubit in Superposition (Equal Probability of 0 and 1)
#Task: Use Qiskit to create a single qubit and apply a Hadamard gate to it. Visualize the result on a Bloch sphere.


from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

# Create 1-qubit circuit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate to create superposition:
# |0> --> (|0> + |1>) / √2
qc.h(0)

# Draw circuit
print(qc)
qc.draw(output='mpl')

# Get statevector
state = Statevector.from_instruction(qc)
print("Statevector:", state)

# Show Bloch Sphere
fig=plot_bloch_multivector(state)
fig.savefig('Prg1.2bloch_sphere.png')

# Measure qubit
qc.measure(0, 0)

# Simulate measurement
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

# Show results (approx. 50% 0 and 50% 1)
print("Measurement Counts:", counts)
fig =plot_histogram(counts)
fig.savefig('histogram.png')