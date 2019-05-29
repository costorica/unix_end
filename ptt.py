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
