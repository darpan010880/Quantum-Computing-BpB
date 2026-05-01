#   Compute Von Neumann Entropy of a Given Density Matrix
#   Task: Write a function that calculates the von Neumann entropy of a 2×2 density matrix using its eigenvalues.
# Compute Von Neumann Entropy of a Given Density Matrix

import numpy as np

# Example 2x2 density matrix
rho = np.array([[0.5, 0.0],
                [0.0, 0.5]])

# Function to calculate von Neumann entropy
def von_neumann_entropy(rho):
    
    # Find eigenvalues
    eigenvalues = np.linalg.eigvals(rho)
    
    # Remove very small numerical errors
    eigenvalues = np.real(eigenvalues)
    
    # Keep only positive eigenvalues
    eigenvalues = eigenvalues[eigenvalues > 1e-12]
    
    # Compute entropy: S = -Tr(rho log2 rho)
    entropy = -np.sum(eigenvalues * np.log2(eigenvalues))
    
    return entropy

# Calculate entropy
S = von_neumann_entropy(rho)

# Print results
print("Density Matrix:")
print(rho)

print("\nEigenvalues:", np.linalg.eigvals(rho))
print("Von Neumann Entropy =", S)