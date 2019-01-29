"""Reads in data from a file, and generates a 2D array of values by iterating through every byte in the file and using
raw byte values as coordinates, and incrementing the value at that location."""

from matplotlib import pyplot as plot

import math
import numpy  # using numpy just because i've never used it, i could use lists also
import time

file = "Darkness.flac"
dataset = numpy.zeros((256, 256), dtype=numpy.float64)

source = bytearray(open(f"test_files/{file}", "rb").read())

start = time.perf_counter()
index = 0
for _ in source[:-1]:
	x = source[index]
	y = source[index+1]
	dataset[x][y] += 1
	index += 1

end = time.perf_counter()
print(f"Execution time {end-start:.3f} seconds")
print(f"Time per byte: {((end-start)*1_000_000)/len(source[:-1])} us")

for index, x in numpy.ndenumerate(dataset):
	if x != 0:
		dataset[index] = math.log2(x)

plot.figure(figsize=(10, 10))
plot.imshow(dataset)
plot.savefig(f"output/{file}.png", bbox_inches="tight")
plot.show()