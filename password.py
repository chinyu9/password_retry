password = 'a123456'
i = 3 # sign in times
while True:
	pwd = input('enter your password')
	if pwd == password:
		print('sign in')
		break #salir de loop
	else:
		i = i -1 
		print('password error', 'remain', i , 'time to try')
		if i == 0:
			break 