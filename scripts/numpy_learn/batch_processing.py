import numpy as np

def batch_generator(X: np.ndarray, y: np.ndarray, batch_size: int):
    """Generate mini-batches of data."""
    for i in range(0, len(X), batch_size):
        yield X[i:i + batch_size], y[i:i + batch_size]

def main():
    # example data
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) # data
    y = np.array([1, 0, 1, 0, 1]) # labels

    print(f'Data:\n{X}\n')
    print(f'Labels:\n{y}\n')

    batch_size = 3 # batch_size is the number of samples processed together in one pass through the model during training.

    for i, (X_batch, y_batch) in enumerate(batch_generator(X, y, batch_size), start=1):
        print(f'Batch {i}:')
        print(f'Batch of data:\n{X_batch}')
        print(f'Batch of labels:\n{y_batch}\n')

if __name__ == "__main__":
    main()
