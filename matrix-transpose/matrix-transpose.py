import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    rows = len(A)
    if rows == 0:
        raise ValueError("Matrix A is empty")
        
    cols = len(A[0])
    AT = [[0 for _ in range(rows)] for _ in range(cols) ]
    
    for i in range(rows):
        for j in range(cols):
            AT[j][i] = A[i][j]

    return np.array(AT)
            
