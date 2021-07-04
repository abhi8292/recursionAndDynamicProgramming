# Python3 program to find repeating
# sequence in a fraction

# This function returns repeating sequence
# of a fraction.If repeating sequence doesn't
# exits, then returns empty string


def fractionToDecimal(numr, denr):

	# Initialize result
	res = ""

	# Create a map to store already seen
	# remainders. Remainder is used as key
	# and its position in result is stored
	# as value. Note that we need position
	# for cases like 1/6. In this case,
	# the recurring sequence doesn't start
	# from first remainder.
	mp = {}

	# Find first remainder
	rem = numr % denr

	# Keep finding remainder until either
	# remainder becomes 0 or repeats
	while ((rem != 0) and (rem not in mp)):

		# Store this remainder
		mp[rem] = len(res)

		# Multiply remainder with 10
		rem = rem * 10

		# Append rem / denr to result
		res_part = rem // denr
		res += str(res_part)

		# Update remainder
		rem = rem % denr

	if (rem == 0):
		return ""
	else:
		return res[mp[rem]:]


# Driver code
numr, denr = 50, 22
res = fractionToDecimal(numr, denr)

if (res == ""):
	print("No recurring sequence")
else:
	print("Recurring sequence is", res)

# This code is contributed by divyeshrabadiya07
