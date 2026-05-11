#   Initialize and Measure a Qubit

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


qc = QuantumCircuit(1, 1)
qc.measure(0, 0)


sim = AerSimulator()
result = sim.run(qc, shots=1024).result()
print(result.get_counts())
fig=qc.draw('mpl')
fig.savefig('Prg7.3.png')