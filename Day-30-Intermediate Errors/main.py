try:
    file=open("file.txt")
    file.read()
    a_dictionary={"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file=open("file.txt",'w')
    file.write("something")
except KeyError as error_message:
    print(f"The Key  {error_message} doesn't exist")
else:
    content=file.read()
    print(content)
finally:
    file.close()
    print("file was closed")
    # raise KeyError
    # raise TypeError("error i made up")

height=float(input("Enter the height:"))
weight=int(input("Weight:"))
if height >3:
    raise ValueError("Human height should not be over 3 meters")
bmi=weight/height**2
print(bmi)