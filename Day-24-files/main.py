"""
file=open('my_file.txt')
content=file.read()
print(content)
file.close()

with open('my_file.txt') as f:
    content=f.read()
    print(content)


with open('my_file.txt', mode="a") as f:
    f.write("Hello, this is entry via python")
"""
with open('C:\\Users\\dipeshkumar.gupta\\Desktop\\testfile.txt',mode='w') as f:
    f.write("Hello this is first entry via python")







