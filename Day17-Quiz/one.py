class User:
    def __init__(self,name):
        self.name=name
        self.followers=0
        self.following=0

    def follow(self,user):
        user.followers+=1
        self.following+=1

user1=User("amit")
user2=User("Angelina Jolie")
print(user2.following,user2.followers)
print(user1.following,user1.followers)
print("=============================")
user1.follow(user2)
print(user2.following,user2.followers)
print(user1.following,user1.followers)
