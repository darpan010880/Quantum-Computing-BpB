#   Entanglement Detection
#   Task: Create a 2-qubit circuit. Apply Hadamard to qubit 0, then CNOT(0,1). Use Statevector to display the final state and verify entanglement.
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace, entropy
import numpy as np

# Create 2-qubit quantum circuit
qc = QuantumCircuit(2)

# Apply Hadamard gate on qubit 0
qc.h(0)

# Apply CNOT gate (control=0, target=1)
qc.cx(0, 1)

# Display circuit
print("Quantum Circuit:")
print(qc.draw())
fig= qc.draw('mpl')
fig.savefig('Ex_Prg3.8_circuit.png')

# Get final statevector
state = Statevector.from_instruction(qc)

# Display final quantum state
print("\nFinal Statevector:")
print(state)

print("\nStatevector Amplitudes:")
print(state.data)

# Expected Bell state:
# (|00> + |11>) / sqrt(2)

# -------------------------------
# Verify Entanglement
# -------------------------------

# Trace out qubit 1 and get reduced state of qubit 0
reduced_state = partial_trace(state, [1])

print("\nReduced Density Matrix of Qubit 0:")
print(reduced_state)

# Compute Von Neumann entropy
ent = entropy(reduced_state)

print("\nEntropy =", ent)

# If entropy > 0, state is entangled
if ent > 0.9:
    print("\nResult: The two qubits are ENTANGLED.")
else:
    print("\nResult: The state is NOT entangled.")