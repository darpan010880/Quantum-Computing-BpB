#   Quantum Teleportation

from qiskit import QuantumCircuit
qc = QuantumCircuit(3, 3)
qc.h(1)					    # Create Bell pair between qubit 1 and 2
qc.cx(1, 2)
qc.x(0)					    # Encode unknown state on qubit 0
qc.cx(0, 1)					# Bell measurement
qc.h(0)
qc.measure([0, 1], [0, 1])
qc.cx(1, 2)					# Conditional operations
qc.cz(0, 2)
qc.measure(2, 2)
fig=qc.draw('mpl')
fig.savefig('Prg7.10.png')
