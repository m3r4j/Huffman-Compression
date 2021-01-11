
def turn_left(i):
	return 2 * i + 1


def turn_right(i):
	return 2 * i + 2


def go_back(i):
	i = i + 1
	i = (i // 2) - 1
	return i


def is_root(i):
	return i == 0


def is_leaf(i, arr):
	return turn_left(i) > len(arr) - 1


def is_node(i, arr):
	return ((not is_leaf(i, arr)) and (not is_root(i)))


def swap_elem(a, b, arr):
	if a < len(arr) and b < len(arr):
		c = arr[a]
		d = arr[b]

		arr[b] = c
		arr[a] = d


def delete_elem(arr):
	swap_elem(0, len(arr) - 1, arr)
	del arr[-1]


def insert_elem(elem, arr):
	arr.insert(len(arr) , elem)
	index = len(arr) - 1

	for x in range(len(arr)):
		back = go_back(index)

		if arr[index] > arr[back]:
			swap_elem(index, back, arr)
			index = back

		if index <= 0:
			break




def heap_sort(arr):
	index = 0

	for x in range(len(arr)):
		left = turn_left(index)
		right = turn_right(index)

		if left < len(arr) and right < len(arr):
			if arr[index] < arr[left]:
				swap_elem(index, left, arr)
				index = left

			elif arr[index] < arr[right]:
				swap_elem(index, right, arr)
				index = right



