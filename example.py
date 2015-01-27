# encoding: utf-8

from evernote.api.client import EvernoteClient
import thrift.protocol.TBinaryProtocol as TBinaryProtocol
import thrift.transport.THttpClient as THttpClient
import evernote.edam.userstore.UserStore as UserStore
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.notestore.NoteStore as NoteStore
import evernote.edam.type.ttypes as Types
import evernote.edam.error.ttypes as Errors


dev_token = "S=s1:U=8fec4:E=152811003ee:C=14b295ed600:P=1cd:A=en-devtoken:V=2:H=39abc9fb82991f988f974fe875438c09"
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()
print user.username

# UserStore
#client = EvernoteClient(token=auth_token)
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()

# 获取所有的笔记本的名称
noteStore = client.get_note_store()
notebooks = noteStore.listNotebooks()
for n in notebooks:
		print n.name

# 新建笔记本
# CreateNotebook
#noteStore = client.get_note_store()
#notebook = Types.Notebook()
#notebook.name = "kindle_books"
#notebook = noteStore.createNotebook(notebook)
#print notebook.guid

# 新建笔记
noteStore = client.get_note_store()
note = Types.Note()
note.title = "I'm a test note!"
note.notebookGuild="kindle_books"
note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
note.content += '<en-note>Hello, world!</en-note>'
note = noteStore.createNote(note)

