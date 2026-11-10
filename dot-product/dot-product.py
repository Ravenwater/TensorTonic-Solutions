import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    if len(x) != len(y):
        RaiseError("lists are not equal in length")

    return float(sum(x*y for x, y in zip(x, y)))