
class User:
	"""Models each Menu Item."""
	def __init__(self, user_id, username):
		self.id = user_id
		self.username = username
		self.followers = 0 # This initializes this value without it being an input to the class like username
		# whenever a new object is being created from this class, must contain these inputs
		self.following = 0
	def follow(self, user):
		user.followers += 1
		self.following += 1
user_1 = User('001', 'lily')
user_2 = User('001','butts')
user_1.follow(user_2)
print(user_1.followers)
print(f'user2 followers {user_2.followers}')
