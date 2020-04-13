import random
import sys
import time
import argparse

# define the argument parser
parser = argparse.ArgumentParser()
parser.add_argument(
	"--listA",
	nargs="*",
	type=int,
	default = [3,2,1]
)
parser.add_argument(
	"--listB",
	nargs="*",
	type=int,
	default = [1,2,3]
)

# initialise the inputs
args = parser.parse_args()
lst = args.listA
lst_sorted = args.listB
sorted = (lst==lst_sorted)

# time
start_time = time.time()

# ACTUAL SORTING ALGORITHM
while(not sorted):
	if (lst==lst_sorted):
		break
	random.shuffle(lst)

end_time = time.time()

print("This sort took %s seconds" %(end_time-start_time))
