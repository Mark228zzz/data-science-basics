import numpy as np

def normalize_features(features: np.ndarray) -> np.ndarray:
    """
    Normalizes the features using z-score normalization.
    Args:
        features (np.ndarray): A 2D array where rows are samples and columns are features.
    Returns:
        np.ndarray: Normalized features.
    """

    # mean by axis 0
    mean = features.mean(axis=0)
    print(f'{mean = }\n')

    # std by axis 0
    std = features.std(axis=0)
    print(f'{std = }\n')

    print(f'features - mean =\n{features - mean}\n')

    return (features - mean) / std

if __name__ == '__main__':
    # Example feature data
    features = np.array([[10, 20], [30, 40], [50, 60]])

    # Normalize the features
    normalized_features = normalize_features(features)

    print(f'Features =\n{features}')
    print(f'Normalized features =\n{normalized_features}')
