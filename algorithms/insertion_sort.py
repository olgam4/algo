def insertion_sort(array):
    final_array = array.copy()
    for index in range(1, len(final_array)):
        currentValue = final_array[index]
        currentPosition = index
        while currentPosition > 0 and final_array[currentPosition - 1] > currentValue:
            final_array[currentPosition] = final_array[currentPosition -1]
            currentPosition = currentPosition - 1
        final_array[currentPosition] = currentValue
    return final_array

