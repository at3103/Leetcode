from collections import defaultdict

def check_strings(a,b):
	if len(a) != len(b):
		return False

	#a=set(a)
	#b=set(b)
	d=defaultdict()

	for s in a:
		if not d.get(s):
			d[s] = 1
		else:
			d[s]+=1

	for s in b:
		if not d.get(s):
			return False
		else:
			d[s]-=1
			if d[s] == 0:
				del d[s]

	return len(d) == 0


print check_strings('ddddddsajjkdshkjdahkjhadkjhdfkjhadkjhadkj','ddddddasdbsbhsdfkbda')