import math

chars_readable = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
chars = list(range(0, 1000))

def convert_num_to_base(i, b):
	if i < 0:
		print("Error: Negative numbers not supported")
		return ""
	r = []
	power = int(math.floor(math.log(i, b)))
	processing = i
	while power >= 0:
		digit = 0
		while processing - pow(b, power) >= 0:
			processing -= pow(b, power)
			digit += 1
		r.append(chars[digit])
		power -= 1
	return r

def is_palindrome(s):
	le = len(s)
	if le == 1:
		return True
	for i, v in enumerate(s):
		if i >= (le/2):
			return True
		if v != s[-i-1]:
			break 
	return False


n = 1000
results = [None] * n
for b in range(2, len(chars)):		# loop through all bases
	pending = [i + 1 for i, v in enumerate(results) if v == None]
	found = [p for p in pending if is_palindrome(convert_num_to_base(p, b))]
	for i, f in enumerate(found):
		results[f - 1] = b
	if len([r for r in results if r is not None]) == 0:
		break

for i, r in enumerate(results):
	list_rep = (convert_num_to_base(i+1, r) if r is not None else "None")
	string_rep = ""
	for l in list_rep:
		if l < len(chars_readable):
			string_rep += chars_readable[l]
		else:
			string_rep += "?"
			print(len(chars_readable))
			print("Found one too long")
	print("{0}, {1}".format(str(i + 1), str(r)))
#print(len([r for r in results if r is None]))

#for i in range(2, 36):
#	print(convert_num_to_base(39, i))

import unittest

class TestPalindrome(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( multiply(3,4), 12)
 
    def test_strings_a_3(self):
        self.assertEqual( multiply('a',3), 'aaa')
 
if __name__ == '__main__':
    unittest.main()