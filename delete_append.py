new_s = ''
new_t = ''

for i in range(min(len(s), len(t))):
	if s[i] != t[i]:
		new_s = s[i:]
		new_t = t[i:]
		break
	new_s = s[i+1:]
	new_t = t[i+1:]

if k >= len(new_s) + len(new_t):
	print("Yes")
else:
	print("No")