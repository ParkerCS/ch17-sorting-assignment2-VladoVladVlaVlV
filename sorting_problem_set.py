# Problem 1 - Value Swap (2pts)
# Swap the values 18 and 38 in the list below
my_list = [27, 32, 18, 2, 11, 57, 14, 38, 19, 91]
my_list[2], my_list[7] = my_list[7], my_list[2]
print(my_list)
# Problem 2 - Selection Sort (8 pts)
# Make a selection sort FUNCTION which takes in 1 parameter (the list),
# sorts it and RETURNS the sorted list.  Then sort and print the result
# of the following list.
sort_me = [655, 722, 736, 314, 59, 778, 632, 477, 230, 556, 353, 769, 622, 731, 683, 233, 524, 186, 694, 507, 443, 833,
           270, 373, 567, 775, 34]


def selection_sort(my_list):
    k = 0
    s = 0
    for pos in range(len(my_list)):
        min_pos = pos
        k += 1
        for scan_pos in range(min_pos, len(my_list)):
            s += 1
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos

        temp = my_list[pos]
        my_list[pos] = my_list[min_pos]
        my_list[min_pos] = temp
    return s, k, my_list


print("With the selection sort, for the list,", selection_sort(sort_me)[2], "it takes", selection_sort(sort_me)[1],
      "times to go through the big loop and", selection_sort(sort_me)[0], "times to go through the small loop")

# Problem 3 - Insertion Sort (8 pts)
# Make an insertion sort FUNCTION which takes in 1 parameter (the list),
# sorts it and RETURNS the sorted list.  Then sort and print the result
# of the following list.
sort_me2 = [551, 138, 802, 954, 569, 372, 454, 366, 936, 959, 958, 202, 474, 658, 108, 424, 523, 611, 557, 0, 733, 903,
            788, 850, 11, 12, 975]


def insertion_sort(my_list):
    l = 0
    m = 0
    for pos in range(1, len(my_list)):
        l += 1
        key_pos = pos
        scan_pos = key_pos - 1
        key_val = my_list[key_pos]
        while scan_pos >= 0 and my_list[scan_pos] > key_val:
            m += 1
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1
        my_list[scan_pos + 1] = key_val

    return l, m, my_list


print("With the selection sor, for the list,", insertion_sort(sort_me2)[2], "it takes", insertion_sort(sort_me2)[1],
      "times to go through the big loop and", insertion_sort(sort_me2)[0], "times to go through the small loop")

# Problem 4 - Efficiency? (10 pts)
# Modify your two functions so that they track the number of times
# you iterate through the big loop, and the inner loop of the sort.
# Make the functions print each value.  Run the sorts on the list below.


sort_me3 = [77, 29, 59, 69, 86, 40, 47, 40, 74, 44, 58, 78, 9, 8, 13, 99, 3, 57, 19, 48, 55, 50, 94, 69, 98, 30, 37, 29,
            40, 29, 36, 32, 26, 85, 61, 51, 70, 96, 90, 89, 91, 88, 68, 4, 4, 74, 15, 72, 5, 91, 76, 6, 56, 80, 72, 87,
            63, 86, 48, 24, 17, 23, 30, 41, 7, 64, 16, 19, 40, 63, 14, 95, 44, 58, 1, 6, 45, 55, 52, 54, 44, 36, 50, 6,
            96, 66, 8, 46, 48, 48, 75, 25, 39, 30, 70, 44, 38, 90, 49, 70]
print("With the insertion sort, for the list, ", insertion_sort(sort_me3)[2], "it takes", insertion_sort(sort_me3)[1],
      "times to go through the big loop and", insertion_sort(sort_me2)[0], "times to go through the small loop")
print("With the selection sort, for the list,", selection_sort(sort_me3)[2], "it takes", selection_sort(sort_me3)[1],
      "times to go through the big loop and", selection_sort(sort_me2)[0], "times to go through the small loop")
