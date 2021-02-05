import scratchapi2
user = input("Input your username.")
#Install with pip3 install scratchapi2
#Very very simple.
def get_messages(user):
  return(scratchapi2.User(user).unread_messages())
print(get_messages(user))
