def remove_duplicate(string):
	new_string = ""
	count =0
	for i in string.lower():
		if i not in new_string:
			new_string +=i
		else:
			count +=1
		result =(''.join(sorted(new_string)), count)
	return result