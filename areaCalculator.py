print("""In this project, we'll create a calculator that can compute the area of the following shapes:

Circle
Triangle""")

print("Calculator is starting up")

option = raw_input("Enter C for Circle or T for Triangle: ")

if option.upper() == "C":
  radius = float(raw_input("Input the radius: "))
  area = 3.14159*(radius**2)
  print("The circle area is " + str(area))
elif option.upper()== "T":
  base = float(raw_input("Input the base: "))
  height = float(raw_input("Input the height: "))
  area = (base * height)/2
  print("The triangle area is " + str(area))
else: 
	print("You have entered an invalid shape")

print("You are exiting the program")