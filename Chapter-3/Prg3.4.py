# Qiskit Program to Illustrate Decoherence:- 

#Step 1:-Import libraries
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, amplitude_damping_error, phase_damping_error
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


#Step 2:- Create a simple quantum circuit
qc = QuantumCircuit(1, 1)
qc.h(0)          # Put qubit in superposition (|+⟩ state)
qc.barrier()
qc.id(0)         # Identity gate to simulate idle decoherence time
qc.measure(0, 0)


#Step 3:- Create noise model with amplitude and phase damping
noise_model = NoiseModel()
amp_error = amplitude_damping_error(0.3)   # Amplitude damping (T1-like)
phase_error = phase_damping_error(0.4)     # Phase damping (T2-like)


# Apply both errors to the 'id' (identity) gate on qubit 0
noise_model.add_quantum_error(amp_error, ['id'], [0])
noise_model.add_quantum_error(phase_error, ['id'], [0])


#Step 4:- Simulate the noisy circuit
simulator = AerSimulator(noise_model=noise_model)
result = simulator.run(qc, shots=1000).result()
counts = result.get_counts()

#Step 5:- Visualize results
print("Measurement outcomes with decoherence noise:", counts)
fig= qc.draw('mpl')
fig.savefig('Prg3.4_circuit.png')

fig= plot_histogram(counts, title="Effect of Decoherence on |+⟩ State")
fig.savefig('Prg3.4_histogram.png')
