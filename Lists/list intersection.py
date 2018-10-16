
def intersection1(list1,list2):
	return list(set(list1)&set(list2))

def intersection2(list1,list2):
 """Duplicates elements that's duplicated in list2"""
	return [x for x in list1 if x in list2]

def intersection3(list1,list2):
"""This is fastest and most memory efficient one for long lists"""
	short, long = (list1, list2) if len(list1) < len(list2) else (list2, list1)
	return list(set(short).intersection(long))
