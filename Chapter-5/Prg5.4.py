#   Qiskit code for Quantum Machine Learning Algorithm

import numpy as np
from qiskit import QuantumCircuit
from qiskit_machine_learning.algorithms import VQC
from qiskit_machine_learning.datasets import ad_hoc_data
from qiskit_algorithms.optimizers import COBYLA
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes
from qiskit.primitives import Sampler


# Step 1. Load sample dataset ( Generate 2D classification dataset (20 training, 10 testing))
train_features, train_labels, test_features, test_labels = ad_hoc_data(
    training_size=20, test_size=10, n=2, gap=0.3, plot_data=True
)

# Step 2. Define feature map (data encoding)
feature_map = ZZFeatureMap(feature_dimension=2, reps=2)

# Step 3. Define ansatz (parameterized circuit)
ansatz = RealAmplitudes(num_qubits=2, reps=2)

# Step 4. Classical optimizer
optimizer = COBYLA(maxiter=100)

# Step 5. Sampler backend (simulator)
sampler = Sampler()

#Step 6. Build Variational Quantum Classifier (VQC) model
vqc = VQC( feature_map=feature_map,  ansatz=ansatz,  optimizer=optimizer,  sampler=sampler)

#Step 7.  Train the model
vqc.fit(train_features, train_labels)

#Step 8. Test the model
accuracy = vqc.score(test_features, test_labels)

print("Hello World")
