#   Quantum Phase Change (Z Gate Effect)

from qiskit import QuantumCircuit
qc = QuantumCircuit(1)
qc.h(0)
qc.z(0)
qc.h(0)
qc.measure_all()
fig=qc.draw('mpl')
fig.savefig('Prg7.9.png')
