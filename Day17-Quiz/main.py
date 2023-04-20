# class User:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("the New User got created",self.name,"having age is", self.age)
#
# User1=User("Angela","55")
# User2=User("Kanha","45")
# User1.address="Tajmahal"
# def function():
#     pass
# print("Hello World !!")
# print(User1.address)
# Instagram
import uuid
class User():
    def __init__(self,username,age):

        self.name=username
        self.id=uuid.uuid4()
        self.age=age
        self.followers=0
        self.followerlist=[]
        self.following=0
        self.followinglist=[]
        print("The id generated for-",self.name,"is", self.id, "with followers count is", len(self.followinglist))

    def follow(self,user):
        print("the User-", self.name," is following", user)
        user.followers +=1
        user.followerlist.append(self.name)
        self.following +=1
        self.followinglist.append(self.name)
        print("the list of followers of",user," are here ",self.followinglist)

User1=User("Radheshyam","30")
User2=User("Kanha","28")
User3=User("Kardashian",35)
User4=User("Christiano Ronaldo",33)

User1.follow(User3)
User2.follow(User3)
User4.follow(User3)
