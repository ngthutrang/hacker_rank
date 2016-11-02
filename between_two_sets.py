def get_factor(number):
	factors = []
	for i in range(1,number+1):
		if number % i == 0: factors.append(i)
	return factors

a = sorted(a)
b = sorted(b)
factor_b_0 = get_factor(b[0])
factor_b = []

for f in factor_b_0:
	is_factor = True
	for bi in b:
		if bi % f != 0:
			is_factor = False
	if is_factor == False: continue
	else: factor_b.append(f)

factor_a = []

for f in factor_b:
	is_factor = True
	for ai in a:
		if f % ai != 0:
			is_factor = False
	if is_factor == False: continue
	else: factor_a.append(f)

print(len(factor_a))