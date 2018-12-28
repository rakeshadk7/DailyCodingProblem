""""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

from operator import mul
from functools import reduce


def product_except_i(lst):

    # Simple solution is to calculate the product of entire array and then divide product by each element at i
    product = reduce(mul, lst, 1)
    results = []

    for i in range(len(lst)):
        results.append(int(product/lst[i]))

    return results

def bonus_product_except_i(lst):


    prior_products = []
    post_products = []
    results = []

    for i in range(0, len(lst)):
        if prior_products:
            prior_products.append(prior_products[-1] * lst[i-1])
        else:
            prior_products.append(1)

    for i in range(len(lst), 0,-1):
        if post_products:
            post_products.append(post_products[-1] * lst[i])
        else:
            post_products.append(1)
    post_products = list(reversed(post_products))

    for i in range(len(lst)):
        prod = prior_products[i] * post_products[i]
        results.append(prod)

    return results

if __name__ == "__main__":

    nums = [1, 2, 3, 4, 5]
    print(product_except_i(nums))
    print(bonus_product_except_i(nums))