def pigeonhole_sort(array):
    final_array = array.copy()
    my_min = min(final_array)
    my_max = max(final_array)
    size = my_max - my_min + 1
    holes = [0] * size
    for x in final_array:
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            final_array[i] = count + my_min
            i += 1
    return final_array
