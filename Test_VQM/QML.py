# ============================================================
# HYBRID QUANTUM MACHINE LEARNING USING QISKIT
# VQC MODEL FOR TEEN MENTAL HEALTH PREDICTION
# ============================================================

# TARGET VARIABLES:
#   1. stress_level
#   2. anxiety_level
#   3. addiction_level
#   4. depression_label
#
# INPUT FEATURES:
#   daily_social_media_hours
#   platform_usage
#   sleep_hours
#   screen_time_before_sleep
#   academic_performance
#   physical_activity
#   social_interaction_level
#
# ============================================================

# REQUIRED INSTALLATION
# ============================================================
# pip install pandas numpy matplotlib scikit-learn
# pip install qiskit qiskit-machine-learning
# pip install qiskit-aer qiskit-algorithms

# ============================================================
# IMPORT LIBRARIES
# ============================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# ============================================================
# QISKIT IMPORTS
# ============================================================

from qiskit.primitives import StatevectorSampler

from qiskit.circuit.library import zz_feature_map
from qiskit.circuit.library import real_amplitudes

from qiskit_machine_learning.algorithms.classifiers import VQC

from qiskit_algorithms.optimizers import COBYLA

# ============================================================
# LOAD CSV DATASET
# ============================================================

csv_file = "Teen_Mental_Health_Dataset.csv"

df = pd.read_csv(csv_file)

# ============================================================
# DATASET INFORMATION
# ============================================================

print("\n================================================")
print("DATASET PREVIEW")
print("================================================")

print(df.head())

print("\n================================================")
print("DATASET SHAPE")
print("================================================")

print(df.shape)

print("\n================================================")
print("DATASET COLUMNS")
print("================================================")

print(df.columns)

# ============================================================
# REMOVE NULL VALUES
# ============================================================

df.dropna(inplace=True)

# ============================================================
# CONVERT TEXT TO LOWERCASE
# ============================================================

categorical_columns = [
    'platform_usage',
    'academic_performance',
    'physical_activity',
    'social_interaction_level'
]

for col in categorical_columns:

    df[col] = df[col].astype(str).str.lower().str.strip()

# ============================================================
# DISPLAY UNIQUE VALUES
# ============================================================

print("\n================================================")
print("UNIQUE VALUES")
print("================================================")

for col in categorical_columns:

    print(f"\n{col} :")
    print(df[col].unique())

# ============================================================
# LABEL ENCODING
# ============================================================

label_encoders = {}

all_categorical_columns = [
    'platform_usage',
    'academic_performance',
    'physical_activity',
    'social_interaction_level',
    'stress_level',
    'anxiety_level',
    'addiction_level',
    'depression_label'
]

for col in all_categorical_columns:

    le = LabelEncoder()

    df[col] = le.fit_transform(df[col])

    label_encoders[col] = le

# ============================================================
# INPUT FEATURES
# ============================================================

X = df[
    [
        'daily_social_media_hours',
        'platform_usage',
        'sleep_hours',
        'screen_time_before_sleep',
        'academic_performance',
        'physical_activity',
        'social_interaction_level'
    ]
]

# ============================================================
# FEATURE SCALING
# ============================================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# ============================================================
# REDUCE FEATURES FOR QUANTUM PROCESSING
# ============================================================

# Only first 4 features used due to qubit limitations

X_quantum = X_scaled[:, 0:4]

# ============================================================
# TARGET VARIABLES
# ============================================================

targets = [
    'stress_level',
    'anxiety_level',
    'addiction_level',
    'depression_label'
]

# ============================================================
# QUANTUM FEATURE MAP
# ============================================================

feature_map = zz_feature_map(
    feature_dimension=4,
    reps=2
)

# ============================================================
# QUANTUM ANSATZ
# ============================================================

ansatz = real_amplitudes(
    num_qubits=4,
    reps=2
)

# ============================================================
# OPTIMIZER
# ============================================================

optimizer = COBYLA(maxiter=20)

# ============================================================
# QUANTUM SAMPLER
# ============================================================

sampler = StatevectorSampler()

# ============================================================
# TRAIN MODEL FOR EACH TARGET
# ============================================================

trained_models = {}

for target in targets:

    print("\n================================================")
    print(f"TARGET : {target}")
    print("================================================")

    # Convert to numpy array
    y = df[target].values

    # ========================================================
    # TRAIN TEST SPLIT
    # ========================================================

    X_train, X_test, y_train, y_test = train_test_split(
        X_quantum,
        y,
        test_size=0.2,
        random_state=42
    )

    # ========================================================
    # CREATE VQC MODEL
    # ========================================================

    vqc = VQC(
        feature_map=feature_map,
        ansatz=ansatz,
        optimizer=optimizer,
        sampler=sampler
    )

    # ========================================================
    # TRAIN MODEL
    # ========================================================

    print("\nTraining Quantum Model...")

    vqc.fit(X_train, y_train)

    # Save model
    trained_models[target] = vqc

    # ========================================================
    # PREDICTION
    # ========================================================

    y_pred = vqc.predict(X_test)

    # ========================================================
    # EVALUATION
    # ========================================================

    accuracy = accuracy_score(y_test, y_pred)

    print(f"\nAccuracy : {accuracy:.4f}")

    print("\nClassification Report:\n")

    print(
        classification_report(
            y_test,
            y_pred,
            zero_division=0
        )
    )

# ============================================================
# NEW STUDENT DATA
# ============================================================

print("\n================================================")
print("NEW STUDENT PREDICTION")
print("================================================")

# IMPORTANT:
# Use ONLY values present in dataset unique values

new_student = pd.DataFrame({

    'daily_social_media_hours':[6],

    'platform_usage':['instagram'],

    'sleep_hours':[5],

    'screen_time_before_sleep':[3],

    'academic_performance':['good'],

    'physical_activity':['low'],

    'social_interaction_level':['medium']
})

# ============================================================
# LOWERCASE CONVERSION
# ============================================================

for col in categorical_columns:

    new_student[col] = (
        new_student[col]
        .astype(str)
        .str.lower()
        .str.strip()
    )

# ============================================================
# VALIDATE CATEGORY VALUES
# ============================================================

for col in categorical_columns:

    allowed_values = label_encoders[col].classes_

    value = new_student[col].iloc[0]

    if value not in allowed_values:

        print(f"\nERROR:")
        print(f"Invalid value '{value}' for column '{col}'")

        print(f"Allowed values are:")
        print(allowed_values)

        exit()

# ============================================================
# LABEL ENCODING
# ============================================================

for col in categorical_columns:

    new_student[col] = label_encoders[col].transform(
        new_student[col]
    )

# ============================================================
# FEATURE SCALING
# ============================================================

new_scaled = scaler.transform(new_student)

# ============================================================
# QUANTUM FEATURE SELECTION
# ============================================================

new_quantum = new_scaled[:, 0:4]

# ============================================================
# FINAL PREDICTIONS
# ============================================================

print("\n================================================")
print("PREDICTION RESULTS")
print("================================================")

for target in targets:

    model = trained_models[target]

    prediction = model.predict(new_quantum)

    prediction = prediction.astype(int)

    predicted_label = label_encoders[target].inverse_transform(
        prediction
    )

    print(f"{target} : {predicted_label[0]}")

# ============================================================
# PROGRAM COMPLETED
# ============================================================

print("\n================================================")
print("QUANTUM MACHINE LEARNING COMPLETED")
print("================================================")