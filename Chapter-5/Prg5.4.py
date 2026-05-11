# Updated Qiskit VQC Code (No deprecation issues)

import numpy as np
from qiskit_machine_learning.algorithms import VQC
from qiskit_machine_learning.datasets import ad_hoc_data
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import StatevectorSampler
from qiskit.circuit.library import zz_feature_map, real_amplitudes


# Step 1: Dataset
train_features, train_labels, test_features, test_labels = ad_hoc_data(
    training_size=20,
    test_size=10,
    n=2,
    gap=0.3,
    plot_data=False
)


# Step 2: Feature map (UPDATED)
feature_map = zz_feature_map(feature_dimension=2, reps=2)

# Step 3: Ansatz (UPDATED)
ansatz = real_amplitudes(num_qubits=2, reps=2)

# Step 4: Optimizer
optimizer = COBYLA(maxiter=100)

# Step 5: Sampler
sampler = StatevectorSampler()

# Step 6: VQC Model
vqc = VQC(
    feature_map=feature_map,
    ansatz=ansatz,
    optimizer=optimizer,
    sampler=sampler
)

# Step 7: Training
vqc.fit(train_features, train_labels)

# Step 8: Evaluation
accuracy = vqc.score(test_features, test_labels)

print("Hello World - Accuracy:", accuracy)