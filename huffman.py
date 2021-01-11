import heap
import sys
import ast


special_char = chr(0)

# Usage: huffman.py [-e[-d]] [file]
def usage():
	print('Usage: huffman.py [-e[-d]] [file]')
	sys.exit()


# Calculate the frequencies
def cal_freqs(text, dictionary):
	for x in text:
		if dictionary.get(x):
			dictionary[x] += 1
		else:
			dictionary[x] = 1



# Sort the dictionary in ascending order
def sort(dictionary):
	new_dict = {}
	res = sorted(dictionary.items(), key=lambda x: x[1])

	for items in res:
		new_dict[items[0]] = items[1]

	return new_dict



# Combine pairs / frequencies
def comb_pairs(dictionary):
	new_dict = {}

	for keys, values in dictionary.items():
		new_dict[keys] = values

	smallest_pair = []

	smallest_pair.append(list(dictionary.items())[0])
	smallest_pair.append(list(dictionary.items())[1])

	new_dict.pop(smallest_pair[0][0])
	new_dict.pop(smallest_pair[1][0])

	new_dict[f'{smallest_pair[0][0]}{smallest_pair[1][0]}'] = smallest_pair[0][1] + smallest_pair[1][1]

	return new_dict


# Get the files text
def get_file(filename):
	filename = open(str(filename), 'r')
	res = filename.readlines()
	filename.close()
	return res


# Save changes to the file
def save_changes(text, filename):
	filename = open(str(filename), 'w')
	filename.write(str(text))
	filename.close()



# Encode a string (text)
def encode(text):
	# Building the tree
	global arr

	arr = []
	freq_table = {}
	dict_list = []
	res = ''

	cal_freqs(text, freq_table)
	arr = []

	freq_table = sort(freq_table)
	dict_list.append(freq_table)

	while len(freq_table) != 1:
		freq_table = comb_pairs(freq_table)
		dict_list.append(freq_table)




	for x in dict_list:

		for keys, values in x.items():
			arr.append(str(values) + special_char + str(keys))

	arr = list(dict.fromkeys(arr))
	arr = arr[::-1]



	# Encoding the text with the tree
	unique_arr = []
	codes = {}

	for keys, values in dict_list[0].items():
		unique_arr.append(keys)


	for x in unique_arr:
		res = ''
		index = 0


		while True:
			left = heap.turn_left(index)
			right = heap.turn_right(index)

			if x in arr[left]:
				index = left
				res += '0'

			else:
				index = right
				res += '1'





			if heap.is_leaf(index, arr):
				codes[x] = res
				break


	# Save and return
	res = ''
	for x in text:
		res += codes[x]

	return res


# Decode a string (text) with the tree (heap)
def decode(result, tree):
	decoded_message = ''
	index = 0

	for x in result:
		if x == '0':
			# Turn left
			index = heap.turn_left(index)

		elif x == '1':
			# Turn right
			index = heap.turn_right(index)

		# If hits a leaf node then add the decoded character to decoded message
		if heap.is_leaf(index, tree):
			find = tree[index].find(special_char)
			res = tree[index][find+1:]
			decoded_message += res 
			index = 0


	return decoded_message


# Encoding files
def encode_file(file):
	result = get_file(file)
	result = ''.join(result)
	original_bits = len(result) * 8
	result = encode(result)
	compressed_bits = len(result)
	space_saving = round(100 -((compressed_bits/original_bits)*100), 2)
	print(f"The Orginal Number of Bits: {original_bits}")
	print(f"The Compressed Number of Bits: {compressed_bits}")
	print(f"Space Saving Percentage: {space_saving}")
	save = f'{arr}\n\n{result}'
	save_changes(save, file)


# Decoding files
def decode_file(file):
	result = get_file(file)
	tree = result[0].rstrip('\n')
	tree = ast.literal_eval(tree)
	text = result[2]
	text = text.rstrip('\n')
	save = f'{decode(text, tree)}'
	save_changes(save, file)




# Command Line stuff:

if len(sys.argv) == 3:
	file = sys.argv[2]
	option = sys.argv[1]

	if option not in ['-e', '-d']:
		usage()

else:
	usage()

if option == '-e':
	encode_file(file)

elif option == '-d':
	decode_file(file)


