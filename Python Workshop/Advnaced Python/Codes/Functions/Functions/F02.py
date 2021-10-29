'''
Pass by reference in Python functions
'''
def test_pass_by_reference(arg_fruits, arg_monthDict):

    print("id of arg_fruits", id(arg_fruits))
    print("id of arg_monthDict", id(arg_monthDict))
    return 

def main():

    fruits = ["apple", "banana", "cherry"]
    monthDict  = {1: "Jan", 2: "Feb", 3:"Mar", \
                  4:"Apr", 5: "May", 6: "Jun", \
                  7:"Jul", 8:"Aug", 9:"Sep", \
                  10:"Oct", 11:"Nov",12:"Dec"} 
    print("id of fruits", id(fruits))
    print("id of monthDict", id(monthDict))

    # different manners to call a function
    # option 1
    test_pass_by_reference(fruits, monthDict)
	
	# option 2
    #test_pass_by_reference(arg_fruits=fruits,
    #				arg_monthDict=monthDict)

    # option 3
    #test_pass_by_reference(arg_monthDict=monthDict,
    #					 arg_fruits=fruits)
    return

main()