#   Apply a Quantum NOT Using CNOT
from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
qc = QuantumCircuit(2, 2)
qc.x(0)       				 # set control qubit to 1
qc.cx(0, 1)   				 # flip target qubit
qc.measure([0, 1], [0, 1])
plt=qc.draw('mpl')
plt.savefig('Prg7.8_circuit.png')