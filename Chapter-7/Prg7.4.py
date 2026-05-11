#   Apply a Hadamard Gate (Superposition)
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)


sim = AerSimulator()
result = sim.run(qc, shots=1024).result()
counts = result.get_counts()


print(counts)
fig=qc.draw('mpl')
fig.savefig('Prg7.4_circuit.png')
plt=plot_histogram(counts)
plt.savefig('Prg7.4_histogram.png')