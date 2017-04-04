"""
Author: Delvin Low Zheng Yang
Date: 4 April 2017
Pre-Interview Test - iGRAD- SP Group

How to Run the Program
- Install Python 2.7
- Place this file main.py and given WordsRTF.RTF in the same folder
- Open a terminal console
- Type "python main.py"
- Key in the four inputs

Explanation of your technical choices:
- I chose to implement my solution in Python as string manipulations in python are significantly easier since python strings are iterable. Furthermore, python also has built in dictionaries types and also list comprehensions that can greatly simplify the code.

- I used two python dictionaries to represent the data structures for the keypad (digit - > letters) and inverse mapping of the keypad (letter -> digit).This is because some of the questions like Q2 can be solved faster with the inverse mapping, while Q3 and Q4 is faster using the normal mapping keypad.

- I considered the additional memory required to hold the additional data structure which is likely not a problem for this particular problem as the size of the problem is small containing 10 digits and 26 alphabets.

- Although there is no time limit for this particular problem, I tried to optimise my code in terms of time complexity. The currently developed algorithm should be fast enough to run quickly even if the input grows in size.

- I believe there are other ways to tackle this problem like using more complex data structures. Such approaches may be more efficient but might be an overkill and will not yield much noticable performance gain since the given problem is small. I believe we need to consider trade off in terms of more development time vs the increase in performance.
"""

import itertools

def build_keypads():
	"""Returns two python dictionaries that represent the data structures for the key pad (digit -> letters) and inverse mapping of the keypad (letter -> digit)

	Returns:
		keypad(dict of 'int':'str'): python dictionary that maps digits to letters
		inv_keypad(dict of 'str':'str'): python dictionary with inverse mapping of the keypad (letter -> digit) 

	"""
	keypad = { 1: "", 2: "abc", 3: "def", 4:"ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8:"tuv", 9: "wxyz", 0: ""  } # Only this needs to be changed if keypad arrangement changes
	inv_keypad = {}
	for digit, string in keypad.iteritems():
		for char in string: # split into individual characters so that can use for faster lookup in dictionary e.g dict['c']
			inv_keypad[char] = str(digit)

	return keypad, inv_keypad


def get_num_key_presses(word, keypad, inv_keypad):
	"""Q1. Given a word, return the total number of key presses required to spell the word using the keypad

	Args:
		word(str): the word to spell
		keypad(dict of 'int':'str'): python dictionary that maps digits to letters
		inv_keypad(dict of 'str':'str'): python dictionary with inverse mapping of the keypad (letter -> digit) 

	Returns:
		total number of key presses to spell the word

	"""
	num_keypresses = 0
	for letter in word:
		# Find which digit the letter is on keypad first
		digit = int(inv_keypad[letter])
		# Find how many times to press to get that letter
		letters_on_digit = keypad[digit]
		num_keypresses += letters_on_digit.index(letter) + 1 # add one because of zero-based indexing
	return num_keypresses


def get_num_from_word(word, inv_keypad):
	"""Q2. Given a word, return the number that the word could represent

	Args:
		word(str): the word to change to number
		inv_keypad(dict of 'str':'str'): python dictionary with inverse mapping of the keypad (letter -> digit) 

	Returns:
		The string form of the number that the word represents

	"""
	number = "" # Define as string so can concatenate instead of add
	for letter in word:
		number += inv_keypad[letter] # Get the digit for each letter and concat them
	return number


def get_letter_combinations(number, keypad):
	"""Q3. Given a number, return all possible letter combinations that the number could represent.
	
	Args:
		number(str): the number to generate words for
		keypad(dict of 'int':'str'): python dictionary that maps digits to letters

	Returns:
		A list of possible letters combinations for that number

	"""
	digits = []
	# Split number into its constituent digits
	for digit in number:
		digits.append(list(keypad[int(digit)])) # get letters e.g. 'abc' for that digit. list() converts a string to a list of characters ['a, 'b', 'c']

	# Use Python itertools.product to get combinations of a list of lists of characters to generate possible combinations. As number could be more than two digits so a double for-loop will not suffice. We can also program a recursive function to do this and get combinations of all the letters.
	possible_combinations = list(itertools.product(*digits)) # Will give a list of tuples for all combinations
	ans = []
	for combi in possible_combinations:
		ans.append("".join(combi)) # Join the letters in the tuple into one word

	return ans


def get_words_combinations(number, keypad):
	"""Q4. Given a number, return all possible word combinations from given dictionary that the number could represent

	Args:
		number (str): the number to generate words for
		keypad (dict of 'int':'str'): python dictionary that maps digits to letters

	Returns:
		A list of possible words for that number that are also found in the real dictionary

	"""
	# Read in the real dictionary from given file first
	real_dictionary = []
	file_real_dictionary = open("WordsRTF.RTF", "r")
	for real_word in file_real_dictionary:
		real_word = real_word.strip() # Remove white space
		real_word = real_word[:-1] # Remove trailing slash /
		real_dictionary.append(real_word)
	file_real_dictionary.close()

	# Use function in Q3 to get all possible letter combinations
	possible_combinations = get_letter_combinations(number, keypad)
	
	# Filter the combinations if they are also words from the real dictionary
	results = [word for word in possible_combinations if word in real_dictionary] # Slight performance consideration: the for-part in the list comprehension is done on possible_combinations not the other way round, because len(possible_combinations) should be shorter than len (real_dictionary). Might matter if real_dictionary is really long.
	return results


def main():
	keypad, inv_keypad = build_keypads()

	word_q1 = raw_input("Input: ")
	print "Output: " + str(get_num_key_presses(word_q1, keypad, inv_keypad))

	word_q2 = raw_input("Input: ")
	print "Output: " + get_num_from_word(word_q2, inv_keypad)

	number_q3 = raw_input("Input: ")
	possible_combinations = get_letter_combinations(number_q3, keypad)
	print "Output: " + str(possible_combinations)

	number_q4 = raw_input("Input: ")
	print "Output: " + str(get_words_combinations(number_q4, keypad))


if __name__ == '__main__':
	main()
