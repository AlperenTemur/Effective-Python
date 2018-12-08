
def intersection1(list1,list2):
"""That's shortest and most pratical way for get intersection of two lists."""
	return list(set(list1)&set(list2))

def intersection2(list1,list2):
 """Duplicates elements that's duplicated in list2"""
	return [x for x in list1 if x in list2]

def intersection3(list1,list2):
"""This is right way to get intersection of 2 lists if duplicated elements aren't wanted and speed matters.
It's fastest and most memory efficient way for long lists"""
	short, long = (list1, list2) if len(list1) < len(list2) else (list2, list1)
	return list(set(short).intersection(long))
