import numpy as np

def compute_weights(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Formula: (X.T @ X)^-1 @ X.T @ y
    Computes the weights for linear regression using the normal equation.
    Args:
        X (np.ndarray): Feature matrix (including bias term if needed).
        y (np.ndarray): Target vector.
    Returns:
        np.ndarray: Weight vector.
    """
    return np.linalg.inv(X.T @ X) @ X.T @ y

def main():
    # Example data for linear regression
    features = np.array([[1, 4], [1, 2], [1, 3]])  # Feature matrix with a bias term
    targets = np.array([1, 2, 3])  # Target values

    # Compute weights
    weights = compute_weights(features, targets)

    print(f'Feature matrix:\n{features}\n')
    print(f'Target vector:\n{targets}\n')
    print(f'Weights:\n{weights}')

if __name__ == "__main__":
    main()
