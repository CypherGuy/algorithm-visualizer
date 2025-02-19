from main import draw_list

# Selection sortworks by finding the minimum element in the unsorted part of the list and swapping it with the first element of the unsorted part of the list


def selectionSortAlgorithm(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if (lst[min_index] > lst[j] and ascending) or (lst[min_index] < lst[j] and not ascending):
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
        draw_list(draw_info, {i: draw_info.GREEN,
                  min_index: draw_info.RED}, True)
        yield True

    return lst
