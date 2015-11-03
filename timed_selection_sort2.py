import random
import datetime

x=[]
def create_list():
	for i in range(0,100):
		random_num = random.randint(0,10000)
		x.append(random_num)

def print_pretty():
	for i in range(0,10):
		for j in range(0,10):
			print '{0:5d}'.format(x[j+i*10]),
		print

def selection_sort():
	print 'half size: ' + str(len(x)//2)
	for i in range(0,len(x)//2):
		min_index = i
		min_value = x[i]

		max_index = len(x) - 1 - i
		max_value = x[max_index]
		
		for j in range(i+1,len(x)-i):
			if min_value > x[j]:
				min_index = j
				min_value = x[j]
			elif max_value < x[j]:
				max_index = j
				max_value = x[j]
		temp = x[i]
		x[i] = min_value
		x[min_index] = temp
		temp = x[j]
		x[j] = max_value
		x[max_index] = temp

create_list()
print '.......Unsorted List.....'
print_pretty()
start_time = datetime.datetime.now()
selection_sort()
print '.......Sorted List.....'
print_pretty()
end_time = datetime.datetime.now()
duration = end_time - start_time
print 'Time for selection_sort with both min and max value (hrs, mins, seconds): '
print duration

