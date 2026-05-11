# QML Comparison: VQC vs Logistic Regression (WORKING VERSION)

import numpy as np

# Qiskit ML
from qiskit_machine_learning.algorithms import VQC
from qiskit_machine_learning.datasets import ad_hoc_data
from qiskit.primitives import StatevectorSampler
from qiskit.circuit.library import zz_feature_map, real_amplitudes
from qiskit_algorithms.optimizers import COBYLA

# Classical ML
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# -------------------------------
# STEP 1: Dataset
# -------------------------------

train_features, train_labels, test_features, test_labels = ad_hoc_data(
    training_size=30,
    test_size=15,
    n=2,
    gap=0.3,
    plot_data=False
)

# -------------------------------
# STEP 2: Prepare Labels
# -------------------------------

# Save original labels for VQC (one-hot)
train_labels_vqc = train_labels.copy()
test_labels_vqc = test_labels.copy()

# Convert to 1D labels for classical ML
train_labels_clf = np.argmax(train_labels, axis=1)
test_labels_clf = np.argmax(test_labels, axis=1)


# -------------------------------
# STEP 3: Classical Model
# -------------------------------

clf = LogisticRegression(max_iter=200)
clf.fit(train_features, train_labels_clf)

pred_classical = clf.predict(test_features)
acc_classical = accuracy_score(test_labels_clf, pred_classical)


# -------------------------------
# STEP 4: Quantum Model (VQC)
# -------------------------------

feature_map = zz_feature_map(feature_dimension=2, reps=2)
ansatz = real_amplitudes(num_qubits=2, reps=2)

sampler = StatevectorSampler()
optimizer = COBYLA(maxiter=100)

vqc = VQC(
    feature_map=feature_map,
    ansatz=ansatz,
    optimizer=optimizer,
    sampler=sampler
)

# Train VQC (uses one-hot labels)
vqc.fit(train_features, train_labels_vqc)

# Predict
pred_quantum = vqc.predict(test_features)

# Convert VQC predictions → class labels
pred_quantum = np.argmax(pred_quantum, axis=1)

acc_quantum = accuracy_score(test_labels_clf, pred_quantum)


# -------------------------------
# STEP 5: Results
# -------------------------------

print("\n===== QML Comparison =====")
print(f"Logistic Regression Accuracy : {acc_classical:.3f}")
print(f"VQC Accuracy                : {acc_quantum:.3f}")