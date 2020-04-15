import random
import time
import argparse

# define the argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--listA", nargs="*", type=int, default=[3, 2, 1])
parser.add_argument("--listB", nargs="*", type=int, default=[1, 2, 3])


# bogosort function
def bogo_sort(A, B):
    sorted = A == B
    while not sorted:
        if A == B:
            return A
        random.shuffle(lst)


# initialise the inputs
args = parser.parse_args()
lst = args.listA
lst_sorted = args.listB

# time start
start_time = time.time()

# perform bogo sort
sorted_list = bogo_sort(lst, lst_sorted)

# time end
end_time = time.time()

print("This sort took %s seconds" % (end_time - start_time))
