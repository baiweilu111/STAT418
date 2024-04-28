import numpy as np
import io

def rows_greater_than_one(arr):
    """6.1 Returns a 2d array with rows of values > 1."""
    return arr[np.any(arr > 1, axis=1)]

def column_major_array(arr):
    """6.2 Returns a 1d array with all elements of the matrix in a column-major way."""
    return arr.flatten(order='F')

def replace_negatives_with_zero(arr):
    """6.3 Returns a 2d array with all the negative values replaced by zero."""
    return np.where(arr < 0, 0, arr)

def block_matrix(arr):
    """6.4 Returns a 3x4 Block Matrix (2d array) with each block as the input 2d array."""
    return np.tile(arr, (3, 4))

def round_to_nearest_hundred(arr):
    """6.5 Returns a 2d array with all elements of the input array rounded to the nearest hundred."""
    return np.round(arr / 100) * 100

def convert_to_string(arr):
    """6.6 Returns a 2d array with each number converted to a python string."""
    return np.vectorize(str)(arr)

def median_of_array(arr):
    """6.7 Returns the median of all entries in the array."""
    return np.median(arr)

def repeat_across_third_axis(arr):
    """6.8 Returns a 3d array with the numbers repeated across the 3rd axis 11 times."""
    return np.repeat(arr[:, :, np.newaxis], 11, axis=2)

def sorted_row_maxima(arr):
    """6.9 Returns a 1d array containing maximum values of each row, in sorted order."""
    return np.sort(np.max(arr, axis=1))

def array_to_file_object(arr):
    """6.10 Returns a file-like object on which np.save can be called to get back the input array."""
    file = io.BytesIO()
    np.save(file, arr)
    file.seek(0)
    return file

def zero_non_diagonal(arr):
    """6.11 Returns a 2d array with non-diagonal entries set to zero (given that it is square)."""
    return np.diag(np.diag(arr))

def rows_perfect_squares(arr):
    """6.12 Returns a 2d array with only rows whose row numbers are perfect squares."""
    indices = [i for i in range(arr.shape[0]) if int(np.sqrt(i))**2 == i]
    return arr[indices]
