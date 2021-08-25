password = 'a123456'
i = 3 # sign in times
while i > 0:
	i = i -1 
	pwd = input('enter your password')
	if pwd == password:
		print('sign in')
		break #salir de loop
	else:
		print('password error')
		if i > 0:
			print('remain', i , 'time to try')
		else:
			print('account has been blocked')