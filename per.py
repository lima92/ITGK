def spm():
	x=str(input("Er du feit? "))
	if(x=="ja"):
		print("Din feite ku!\n")
	elif(x=="nei"):
		print("Se deg i speilet en gang til\n")
		spm()
	else:
		print("Svar ja eller nei!\n")
		spm()
		
spm()