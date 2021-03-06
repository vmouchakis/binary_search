def binary_search(sequence, item):
	begin_index = 0
	end_index = len(sequence) - 1

	while begin_index <= end_index:
		midpoint = begin_index + (end_index - begin_index) // 2
		midpoint_value = sequence[midpoint]

		if midpoint_value == item:
			return midpoint + 1				# because we start counting from 0
		elif item < midpoint_value:
			end_index = midpoint - 1
		else:
			begin_index = midpoint + 1

	return None 


sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
item = 6

print(binary_search(sequence, item))

# Complexity: O(logn)
