import numpy as np

def load_txt(file_path: str, delimiter: str = ",") -> np.ndarray:
    """
    Load data from a text file.
    :param file_path: Path to the text file.
    :param delimiter: Delimiter used in the text file (default: ',').
    :return: NumPy array with the loaded data.
    """
    return np.loadtxt(file_path, delimiter=delimiter)

def save_txt(data: np.ndarray, file_path: str, delimiter: str = ",") -> None:
    """
    Save a NumPy array to a text file.
    :param data: NumPy array to save.
    :param file_path: Path to save the text file.
    :param delimiter: Delimiter to use in the text file (default: ',').
    """
    np.savetxt(file_path, data, delimiter=delimiter)

def load_npy(file_path: str) -> np.ndarray:
    """
    Load data from a binary NumPy .npy file.
    :param file_path: Path to the .npy file.
    :return: NumPy array with the loaded data.
    """
    return np.load(file_path)

def save_npy(data: np.ndarray, file_path: str):
    """
    Save a NumPy array to a binary .npy file.
    :param data: NumPy array to save.
    :param file_path: Path to save the .npy file.
    """
    np.save(file_path, data)

def main():
    """
    Example of loading, processing, and saving data using NumPy.
    """
    # paths to datas
    path_txt_data = 'data/txts/numbers_example.txt'
    path_npy_data = 'data/npys/numbers_example.npy'

    # example: save and load a text file
    data = np.array([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0]
    ])

    save_txt(data, path_txt_data)
    loaded_txt_data = load_txt(path_txt_data)

    print(f'Loaded from .txt:\n{loaded_txt_data}\n')

    # example save and load a binary NumPy file
    save_npy(data, path_npy_data)
    loaded_npy_data = load_npy(path_npy_data)
    print(f'Loaded from .npy:\n{loaded_npy_data}')

if __name__ == '__main__':
    main()
