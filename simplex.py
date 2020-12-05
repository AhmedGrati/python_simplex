import numpy as np

np.seterr(divide='ignore', invalid='ignore')


def hasPositiveValue(vector):
    for element in vector:
        if element > 0:
            return True

    return False


coeff_z_array = np.array([30, 50, 0, 0, 0])
matrix = np.array([[1, 0, 1, 0, 0, 4],
                   [0, 2, 0, 1, 0, 12],
                   [3, 2, 0, 0, 1, 18]
                   ], dtype=float)
vr_coeff_array = np.zeros(3, dtype=float)
zj = np.zeros(5, dtype=float)
cj_minus_zj = coeff_z_array - zj

# first iteration
while hasPositiveValue(cj_minus_zj):
    # find the index of the max element in the array
    max_index = int(np.where(cj_minus_zj == max(cj_minus_zj))[0])
    print('MAX INDEX : ', max_index)
    # extract the pivot fector and flatten it
    pivot_vector = matrix[:, max_index:max_index + 1]
    pivot_vector = pivot_vector.flatten()
    # extract bj values
    bj = matrix[:, -1]
    # extract sorted values by dividing bj by pivot vector
    vs = np.divide(bj, pivot_vector)
    # extract the index of the min element in the array so we know the pivot element
    min_index = int(np.where(vs == min(vs))[0])
    matrix[min_index] = matrix[min_index] / matrix[min_index, max_index]
    vr_coeff_array[min_index] = coeff_z_array[max_index]
    for index in range(len(matrix)):
        if index != min_index:
            coeff = matrix[index, max_index]
            if coeff != 0:
                matrix[index] = matrix[index] - matrix[min_index] * coeff
    # loop through each variable
    for index in range(len(matrix[0, :-1])):
        # scalar product
        n = np.dot(matrix[:, index], vr_coeff_array)
        zj[index] = n
    cj_minus_zj = coeff_z_array - zj

print("The maximum gain is: ", np.dot(vr_coeff_array, bj))
