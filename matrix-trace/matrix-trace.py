import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    rows = len(A)
    if rows == 0:
        raise ValueError("Matrix A is empty")

    cols = len(A[0])

    if rows != cols:
        raise ValueError("Matrix A is not-square")

    trace = 0.0
    for i in range(rows):
        trace += A[i][i]

    return trace