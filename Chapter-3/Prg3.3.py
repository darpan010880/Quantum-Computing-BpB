# Create an entangled state between two qubits such that measuring one instantly 
# determines the state of the other.


#Step 1:-Import libraries
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector
import matplotlib.pyplot as plt


#Step 2:- Create a 2-qubit quantum circuit with 2 classical bits
qc = QuantumCircuit(2, 2)


#Step 3:- Apply Hadamard gate to qubit 0 and CNOT to entangle with qubit 1
qc.h(0)
qc.cx(0, 1)


#Step 4:- Get the statevector BEFORE measurement
qc.measure(0, 0)
qc.measure(1, 1)


#Step 5:- Simulate with AerSimulator
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(qc, shots=1024)
result = job.result()


#Step 6:- Get measurement counts
result = simulator.run(compiled_circuit).result()
counts = result.get_counts(qc)
print("Measurement counts:", counts)

#Step 7:- Plot histogram
hist = plot_histogram(counts)
hist.savefig('Prg3.3_histogram.png')

#Step 8:- Plot Circuit
qc.draw('mpl')
plt.savefig('Prg3.3_circuit.png')

