def sorted_search(elements,target):
	if not elements or len(elements) <= 0:
		return -1
	left = 0
	right = len(elements) - 1

	while left < right:
		middle = (left + right)/2

		if elements[middle] > target:
			right = middle - 1
		else:
			left = middle + 1
	if elements[right] == target:
		return right
	return -1


def check():
    l = [1, 2, 3]
    target = 0
    ans = target in l
    if ((sorted_search(l,target) == target) == ans):
        print "CORRECT"
    else:
        print len(l)
        print l
        print target

check()