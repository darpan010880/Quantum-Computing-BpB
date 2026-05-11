# GHZ State (3-Qubit Entanglement)
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


qc = QuantumCircuit(3, 3)		# Create a 3-qubit circuit
qc.h(0)				# Step 1: Superposition on the first qubit
qc.cx(0, 1)				# Step 2: Entangle 1st → 2nd and 2nd → 3rd
qc.cx(1, 2)
qc.measure([0, 1, 2], [0, 1, 2])	# Step 3: Measure all qubits
fig=qc.draw("mpl")			# Draw the circuit
fig.savefig('circuit_Prg7.12.png')


sim = AerSimulator()		# Simulate
compiled = transpile(qc, sim)
result = sim.run(compiled, shots=1024).result()
counts = result.get_counts()
print(counts)
plot_histogram(counts)
plt.savefig('histogram_Prg7.12.png')