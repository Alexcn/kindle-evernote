# 认证
dev_token = "put your dev token here"
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()
print user.username

# UserStore
## 获取当前用户的相关信息的对象 
client = EvernoteClient(token=auth_token)
userStore = client.get_user_store()
user = userStore.getUser()

# NoteStore
## 用来创建、更新和删除笔记、笔记本还有其他在用户帐户中可找到的印象笔记的数据的.
noteStore = client.get_note_store()
notebooks = noteStore.listNotebooks()
for n in notebooks:
		print n.name

