def typecheck(inputvalue, inputkind):
        if inputkind == "str":
                try:
                        int(inputvalue)/2
                        print('value is a number')
                        return True
                except:
                        print('value is a string')
                        return False
        elif inputkind == "int":
                try:
                        int(inputvalue)/2
                        print('value is a number')
                        return False
                except:
                        print('value is a string')
                        return True
        else:
                print('No valid input, please enter either "str" or "int"')
	

def inputcheck(inputvalue_test, kind):
	while typecheck(inputvalue_test, kind)==True:
		#typecheck(inputvalue_test)
		inputvalue_test = input('please enter {kind}:')
	return inputvalue_test

