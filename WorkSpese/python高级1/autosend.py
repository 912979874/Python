# encoding = utf8
import itchat, time, re
from itchat.content import *


# 如果对方发的是文字，则我们给对方回复以下的东西
@itchat.msg_register([TEXT])
def text_reply(msg):
    match = re.search('在', msg['Text'])
    if match:
        itchat.send(('[自动回复] 主人不在，稍等一下'), msg['FromUserName'])

    # 如果对方发送的是图片，音频，视频和分享的东西我们都做出以下回复。


@itchat.msg_register([PICTURE, RECORDING, VIDEO, SHARING])
def other_reply(msg):
    #想给谁发信息
    users=itchat.search_friends(name='miki')
    user1=itchat.search_friends(userName='miki')
    #找到username
    userName=users[0]['UserName']
    itchat.send('[自动回复] 主人%s给你发语音或者文件了'%msg.fromUserName,toUserName=userName)

#itchat.auto_login(hotReload=False)
#itchat.run()
