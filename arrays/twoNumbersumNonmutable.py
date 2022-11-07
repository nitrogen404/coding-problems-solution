# O(n) space
# (n) time
def twoSum(array, target):
	hashMapHuh = {}
	for idx, num in enumerate(array):
		diff = target - num
		if diff in hashMapHuh:
			return [idx, hashMapHuh[diff]]
		else:
			hashMapHuh.update({num: idx})
