# Decline of Biodiversity in Nearby Forest and Wetland Areas: A Climate Action Perspectiv

from qiskit import QuantumCircuit	#Library to create Quantum Circuit
import matplotlib.pyplot as plt		#Library to plot
qc = QuantumCircuit(1, 1)		#Define single Qubit
qc.h(0)
qc.measure(0, 0)				# Measurement of the qubit
fig=qc.draw('mpl')				# Draw the circuit using matplotlib
fig.savefig('Prg7.2.png')			# Save the figure as Prg7.2.png
