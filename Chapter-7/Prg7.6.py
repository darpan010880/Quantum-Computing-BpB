#Other version of the program to X flips |0⟩ → |1⟩.


from qiskit import QuantumCircuit
qc = QuantumCircuit(1, 1)
qc.y(0)  						# adds phase + rotation
qc.z(0)  						# adds phase only
value=qc.measure(0, 0)
fig=qc.draw('mpl')
fig.savefig('Prg7.6.png')