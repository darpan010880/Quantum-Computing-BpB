# Simulate Entanglement Between Two Qubits
#Task: Create a Bell state using a Hadamard gate and a CNOT gate. Measure both qubits and show that they are correlated.


from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator

# Create circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Step 1: Apply Hadamard gate on qubit 0
qc.h(0)

# Step 2: Apply CNOT gate
qc.cx(0, 1)

# Draw circuit
print("Quantum Circuit:")
print(qc)
fig=qc.draw(output='mpl')
fig.savefig('Prg1.4_circuit.png')

# Measure both qubits
qc.measure([1, 0], [1, 0])

# Simulate circuit
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()

# Get measurement counts
counts = result.get_counts()

# Print results
print("Measurement Counts:")
print(counts)

# Plot histogram
fig=plot_histogram(counts)
fig.savefig('Prg1.4histogram.png')