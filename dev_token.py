import evernote-sdk-python
dev_token = "S=s1:U=8fec4:E=15235115189:C=14add6023a8:P=1cd:A=en-devtoken:V=2:H=e9302bc134149b2d3654f34729f050bc"
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()
print user.username
