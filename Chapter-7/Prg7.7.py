#    Create an Entangled Bell State
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0,1], [0,1])


sim = AerSimulator()
counts = sim.run(qc, shots=1024).result().get_counts()
print(counts)
fig=qc.draw('mpl')
fig.savefig('Prg7.7_circuit.png')
plot_histogram(counts)
plt.savefig('Prg7.7_histogram.png')