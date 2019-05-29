import sys
from PTTLibrary import PTT
import MySQLdb

def GetPttData():

    print('Input your ID')
    ID = input()
    print('Input your password')
    Password = input()
    PTTBot = PTT.Library()

    ErrCode = PTTBot.login(ID, Password)
    if ErrCode != PTT.ErrorCode.Success:
        PTTBot.Log('登入失敗')
    sys.exit()
    
    # return a datatype with various information
    # getPost( board, article index)
    ErrCode, Post = PTTBot.getPost('Gossiping', PostIndex=44444)

    title = Post.getTitle()
    content = Post.getContent()
    author = Post.getAuthor()
    #PTTBot.Log('標題: ' + Post.getTitle())
    #PTTBot.Log('內文:\n' + Post.getContent())
    #PTTBot.Log('作者: ' + Post.getAuthor())
    print(title)
    print(content)
    print(author)
    
    return Post
    PTTBot.logout()
"""
ID = 'costorica'
Password = '6buqe25mgk'

PTTBot = PTT.Library()

ErrCode = PTTBot.login(ID, Password)
if ErrCode != PTT.ErrorCode.Success:
    PTTBot.Log('登入失敗')
    sys.exit()
    
# return a datatype with various information
# getPost( board, article index)
ErrCode, Post = PTTBot.getPost('Gossiping', PostIndex=44444)

title = Post.getTitle()
content = Post.getContent()
author = Post.getAuthor()
#PTTBot.Log('標題: ' + Post.getTitle())
#PTTBot.Log('內文:\n' + Post.getContent())
#PTTBot.Log('作者: ' + Post.getAuthor())
print(title)
print(content)
print(author)

PTTBot.logout()

#connect to mysql
db = MySQLdb.connect(host="localhost"
                     ,user="costorica"
                     , passwd="6buqe25mgk"
                     , db="ptt"
                     , charset="utf8")
print(db)
cursor = db.cursor()
command = 'INSERT INTO article(title,content,author) VALUES ('
command += "\"" + title + "\","
command += "\"" + "空" + "\","
command += "\"" + author + "\");"
#command = "INSERT INTO article(title,content,author) VALUES('a','b','c');"
cursor.execute(command)

results = cursor.fetchall()
for record in results:
  col1 = record[0]
  print(col1)
db.commit()
db.close()
"""
