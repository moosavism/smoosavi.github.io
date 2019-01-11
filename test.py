import numpy as np

l_o_o = list(np.random.randn(0))#list_of_objects is a list

l_o_o_b = l_o_o.copy()

for i in range(len(l_o_o)//2):
    temp = l_o_o[i]
    l_o_o[i] = l_o_o[-(i+1)]
    l_o_o[-(i+1)] = temp

class node:
    def __init__(self, x):
        self.val = x
        self.next = None
    def add(self, x):
        self.next = node(x)
        return self.next

def approx_pi(num_points):
    random_points = 2*(np.random.rand(2,num_points)-0.5)
    return np.sum(np.sqrt(random_points[0]**2 + random_points[1]**2)<=1)/float(num_points)*4
        

def quicksort(x):
	
	if len(x)<2:
		return x
	pivot = x[0:1]
				
	low_array = []
	high_array = []

	for a in x[1:]:
		if a<pivot[0]:
			low_array.append(a)
		else:
			high_array.append(a)
	out = quicksort(low_array) + pivot + quicksort(high_array)
	#print(quicksort(low_array))
	#print(len(out))
	return out

import heapq
def find_median(x):
	max_h = []
	min_h = []
	
	heapq.heappush(max_h, -x[0])
	for a in x[1:]:
		if a<=-max_h[0]:
			heapq.heappush(max_h, -a)
		else:
			heapq.heappush(min_h, a)
		print(len(max_h), len(min_h))
		if len(max_h)<len(min_h)-1:
			t = heapq.heappop(min_h)
			heapq.heappush(max_h, -t)			
		elif len(min_h)<len(max_h)-1:
			t = -heapq.heappop(max_h)
			heapq.heappush(min_h, t)
		print(len(max_h), len(min_h))
	return max_h, min_h

