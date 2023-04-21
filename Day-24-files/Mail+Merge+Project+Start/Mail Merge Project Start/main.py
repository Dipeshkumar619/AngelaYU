#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

name="[name]"
import random
data=[]
with open('Input\\Letters\\starting_letter.txt',mode='r') as template:
    content=template.read()


with open('Input\\Names\\invited_names.txt',mode='r') as names:
    guestlist=names.readlines()

for i in guestlist:
        stripped_named=i.strip()
        x=content.replace(name,stripped_named)
        data.append(x)
        with open(f"Output\\ReadyToSend\\letter_for_{stripped_named}.txt",mode='w') as myfile:
            myfile.write(x)

