import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # Write code here
    rows = cols = len(v)
    A = [[ 0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        A[i][i] = v[i]

    return np.array(A)
            