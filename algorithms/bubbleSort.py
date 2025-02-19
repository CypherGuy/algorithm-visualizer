from main import draw_list


def bubbleSortAlgorithm(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(
                    draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True  # Lets you pause the code midway, and store the code, ready for you to resume anytime
    return lst
