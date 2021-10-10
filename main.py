def numbers_with_max_dividers(a, b):
    max_count_of_dividers = 0
    numbers_and_dividers = list()
    numbers_with_max_dividers_list = list()
    for number in range(a, b + 1, 1):
        count_of_dividers = 0
        for i in range(number, 1, -1):
            if number % i == 0:
                count_of_dividers += 1
        numbers_and_dividers.append([number, count_of_dividers])
        if count_of_dividers > max_count_of_dividers:
            max_count_of_dividers = count_of_dividers
    for number in numbers_and_dividers:
        if number[1] == max_count_of_dividers:
            numbers_with_max_dividers_list.append(number[0])
    numbers_with_max_dividers_list = tuple(numbers_with_max_dividers_list)
    return numbers_with_max_dividers_list


def ex4():
    print("Номер 4")
    while True:
        try:
            a = int(input("Введите число a: "))
            break
        except ValueError:
            print("Вы ввели не число. Попробуйте снова: ")
    while True:
        try:
            b = int(input("Введите число b: "))
            break
        except ValueError:
            print("Вы ввели не число. Попробуйте снова:")
    numbers_with_max_dividers_tuple = numbers_with_max_dividers(a, b)
    print("Числа с наибольшим количеством делителей:")
    for i in numbers_with_max_dividers_tuple:
        print(str(i))


def is_unique_list(entered_list):
    arr = set(entered_list)
    if len(arr) == len(entered_list):
        return True
    else:
        return False


def ex5():
    print("Номер 5")
    my_list = input("Введите данные списка:").split()
    unique_list = is_unique_list(my_list)
    if unique_list:
        print("Список уникальный")
    else:
        print("Есть повторы")


def intersection_of_lists(*lists):
    print(lists)
    my_sets = list()
    for my_list in lists:
        my_sets.append(set(my_list))
    is_intersection = False
    print(my_sets[0].intersection(*my_sets[:]))
    if len(my_sets[0].intersection(*my_sets[:])) != 0:
        is_intersection = True
    return is_intersection


def ex6():
    print("Номер 6")
    while True:
        try:
            amount_of_lists = int(input("Введите нужное количество листов:"))
            break
        except ValueError:
            print("Вы ввели не число. Попробуйте снова: ")
    my_lists = list()
    for i in range(amount_of_lists):
        my_lists.append(input("Введите данные для {:d} списка".format(i + 1)).split())
        print(my_lists[i])
    is_intersection = intersection_of_lists(*my_lists[:])
    if is_intersection:
        print("Списки пересекаются")
    else:
        print("Списки не пересекаются")


def main():
    ex4()
    ex5()
    ex6()


if __name__ == '__main__':
    main()

