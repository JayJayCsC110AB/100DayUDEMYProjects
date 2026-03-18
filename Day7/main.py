class User:
    #set constructor to call atributes
    #init function
    def __init__(self, user_id, self_id ):
        self.id = user_id
        self.username = self_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers +=1
        self.following +=1


user_1 = User("1002", "Angela")
user_2 = User("2002", "Jack")

user_1.follow(user_2)

print(user_2.followers)
print(user_2.following)