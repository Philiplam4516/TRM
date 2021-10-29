'''
Pass by reference in Python functions
'''
def test_pass_by_reference(arg_fruits):

  print("id of arg_fruits", id(arg_fruits))

  #change the 0th element 
  arg_fruits[0] = "orange"
  print("id of arg_fruits", id(arg_fruits))

  #append a new element 
  arg_fruits.append("grape")
  print("id of arg_fruits", id(arg_fruits))

  return 

def main():

  fruits = ["apple", "banana", "cherry"]
  print("id of fruits", id(fruits))
  test_pass_by_reference(fruits)

  print(fruits)
  return

main()