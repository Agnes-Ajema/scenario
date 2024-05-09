class User:
    def __init__(self,username):
        self.username = username
        self.id_no = None

class UserApp:
    def __init__(self):
        self.users = []
        self.id_no_count = 1

def add_user(self,username):
    user = User(username)
    user.id_no = self.id_no
    self.id_no += 1
    self.users.append(user)

user_app = UserApp()
user_app.add_user("Agnes")
user_app.add_user("Ajema")

print(f"User {Ajema.username}has ID {Ajema_id}")
print(f"User {Agnes.username} has ID {Agnes_id}")

user_followers =[
    {"username": "user1","followers":["follower1","follower2","follower3"]},
    {"username": "user2","followers":["follower5","follower6","follower7"]}
]
def get_followers(username):
    for user in user_followers:
        if user["username"] == username:
            return user["followers"]
    return[]
print(get_followers("user1"))
print(get_followers("user3"))
