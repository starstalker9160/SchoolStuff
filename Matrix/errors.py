class InvalidMatrixSize(Exception):
    """Raised when matrix has size 0 on any axis"""
    def __init__(self):
        print("Matrix cannot have 0 size on any axis")

class NonMatchingMatrixSize(Exception):
    """Raised when matrices arent matching in size"""
    def __init__(self):
        print("Could not perform operation as matrices are not of same size")

