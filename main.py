# 1

# def sum(list):
#     count = 1
#     for num in list:
#         count *= num
#     return count
#
# print(sum([1, 2, 3, 4]))

# 2

# def minimum(list):
#     x = min(list)
#     return x
#
# print(minimum([2, 3, 4, 9, 1]))


# 3

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def count_primes_in_list(lst):
#     count = 0
#     for num in lst:
#         if is_prime(num):
#             count += 1
#     return count
#
# my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# prime_count = count_primes_in_list(my_list)
# print(prime_count)


# 4


# def remove_number_from_list(lst, num_to_remove):
#     count_removed = 0
#     while num_to_remove in lst:
#         lst.remove(num_to_remove)
#         count_removed += 1
#     return count_removed
#
#
# my_list = [1, 2, 3, 4, 3, 5, 6, 3]
# number_to_remove = 3
# removed_count = remove_number_from_list(my_list, number_to_remove)
# print(removed_count)

# 5



# def sum_list(list1, list2):
#     list3 = list1 + list2
#     return list3
#
# print(sum_list([2, 4, 6, 9], [5, 4, 8, 2, 1]))


# 6


# def calculate(list, power):
#     powered_list = [num ** power for num in list]
#     return powered_list
#
# my_list = [2, 3, 4, 5]
# power = 3
# result_list = calculate(my_list, power)
# print(result_list)