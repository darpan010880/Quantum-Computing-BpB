#   Apply Pauli Gates (X, Y, Z)

from qiskit import QuantumCircuit
qc = QuantumCircuit(1, 1)
qc.x(0)  # NOT gate
qc.measure(0, 0)
fig=qc.draw('mpl')
fig.savefig('Prg7.5_X_gate.png')
qc = QuantumCircuit(1, 1)
qc.y(0)  # Y gate
qc.measure(0, 0)
fig=qc.draw('mpl')
fig.savefig('Prg7.5_Y_gate.png')