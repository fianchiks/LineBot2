# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()

kk = LINETCR.LINE()
kk.login(token="ElAA0BQG4kDryOSR6503.biRLhTNOFtsbwVm5XIYpiW.RI4jB5Adz6tvzopL9xaS7lK4tSqyA/E/32ofbSx+Tl8=")
kk.loginResult()

ki = LINETCR.LINE()
ki.login(token="ElJl9jEZ2a00PphlgyF4.rGnjiTwph3BZhrtJd0WtLa.p4VJrylI7vRtV/GCvWzDfz2aJFyOGR8u8zLRZpk1GGE=")
ki.loginResult()

kc = LINETCR.LINE()
kc.login(token="EluEVHqxj9iB8emn7z28.MinrOAgI3TOt5KJCXQX+Aa.LMn5dWRIOAzMj7he8g4KQbCc5n4dNf1FU0r0ina+whA=")
kc.loginResult()

cl

# adm = LineAlpha.LINE()
# adm.login(token="EkoRa4LbxQLepMyWmEMe.idD7rqcO/flZ+HSQWA/z7G.Z0Nd273uZOb1aD1eeTNA0FVr1/dN5ja7KuqCAyZlQFg=")
# adm.loginResult()

#client_id = '511abc94ee71658'
#client_secret = '948a2fcdbf566c04bcce5f990e349ce795ee7460'
#access_token = '30181acf5583ad6a215b4f69e6e5c7bc5c66efdb'
#refresh_token = '4a6b3f983b96714c2e9b581edf86f86e0d681938'

#client = ImgurClient(client_id, client_secret, access_token, refresh_token)

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

#album = None
#image_path = 'tmp/tmp.jpg'

# kk=ki=kc=cl

helpMessage ="""Ghoul Bot(s)
Use Prefix 「Ghoul」 to use the Bot(s)
Prefix is Case sensitive but the commands is not.
[Gid] - Show Group ID
[Mid all] - Show all the Bot(s) MID
[Bot 1/2/3/4/5] - Shows the specific Bot MID
[Bot all] - Show all the Bot(s) Contact
[Bot 1/2/3/4/5] - Shows the specific Bot Contact
[Yid] - Show your ID
[Contact 「mid」] - Give Contact by MID
[Join on/off] - Auto join group
[Leave on/off] - Allows the bot to leave the group
[*] Command in the groups [*]
[Ginfo] - Group Info
[Banlist] - Check Banlist
[Cancel] - Cancel all pending(s) invitation
[Stalk 「ID」] - Upload lastest instagram picture from ID
[*] Admin and Staff Commands [*]
[Bot Absen] - Check if bot is Online
[Auto Url On/Off] - Turn invitation link for group on/off
[Auto Cancel On/Off] - Turn auto cancel invite on/off 
[Gn 「group name」] - Change Group Name
[Speed] - Check bot response speed
[Gh Random:「A」] - Randomize group name A times
[Bc 「text」] - Let the bot send a text
[*] Admin only Commands [*]
[Clear group] - Clear all members in the group
[@Bye All] - Bot Leave
[@Bye Bot 1/2/3/4] - Bot Leave
[Ban 「@」] - Ban By Tag
[Unban 「@」] - Unban By Tag
[Ban] - By Sharing Contact
[Unban] - By Sharing Contact
[Kill ban] - Kick all banned contact(s)
[Staff add/remove @] - Add or Remove Staff By Tag
"""

KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = kk.getProfile().mid
Bmid = ki.getProfile().mid
Cmid = kc.getProfile().mid
Bots = [mid,Amid,Bmid,Cmid,]
admin = ["u6de2fd0d3f168038814531c1fb8fb7dc","u6de2fd0d3f168038814531c1fb8fb7dc","u6de2fd0d3f168038814531c1fb8fb7dc"]
staff = ["u6de2fd0d3f168038814531c1fb8fb7dc","u6de2fd0d3f168038814531c1fb8fb7dc","u6de2fd0d3f168038814531c1fb8fb7dc"]
adminMID = "u6de2fd0d3f168038814531c1fb8fb7dc"
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"Ghoul Vokster",
    "cName2":"Ghoul Berster",
    "cName3":"Ghoul Gifster",
    "cName4":"Ghoul Flipster",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

cancelinvite = {
    'autoCancel':True,
    'autoCancelUrl':True
}

#bot1_name = {
#    "1" : "[Ardh-]BOT1",
#    "2" : "Ardh-]BOT1[",
#    "3" : "rdh-]BOT1[A",
#    "4" : "dh-]BOT1[Ar",
#    "5" : "h-]BOT1[Ard",
#    "6" : "-]BOT1[Ardh",
#    "7" : "]BOT1[Ardh-",
#    "8" : "BOT1[Ardh-]",
#    "9" : "OT1[Ardh-]B",
#    "10" : "T1[Ardh-]BO",
#    "11" : "1[Ardh-]BOT"
#}
#bot2_name = {
#    "1" : "[Ardh-]BOT2",
#    "2" : "Ardh-]BOT2[",
#    "3" : "rdh-]BOT2[A",
#    "4" : "dh-]BOT2[Ar",
#    "5" : "h-]BOT2[Ard",
#    "6" : "-]BOT2[Ardh",
#    "7" : "]BOT2[Ardh-",
#    "8" : "BOT2[Ardh-]",
#    "9" : "OT2[Ardh-]B",
#    "10" : "T2[Ardh-]BO",
#    "11" : "2[Ardh-]BOT"
#}
#bot3_name = {
#    "1" : "[Ardh-]BOT3",
#    "2" : "Ardh-]BOT3[",
#    "3" : "rdh-]BOT3[A",
#    "4" : "dh-]BOT3[Ar",
#    "5" : "h-]BOT3[Ard",
#    "6" : "-]BOT3[Ardh",
#    "7" : "]BOT3[Ardh-",
#    "8" : "BOT3[Ardh-]",
#    "9" : "OT3[Ardh-]B",
#    "10" : "T3[Ardh-]BO",
#    "11" : "3[Ardh-]BOT"
#}
#bot4_name = {
#    "1" : "[Ardh-]BOT4",
#    "2" : "Ardh-]BOT4[",
#    "3" : "rdh-]BOT4[A",
#    "4" : "dh-]BOT4[Ar",
#    "5" : "h-]BOT4[Ard",
#    "6" : "-]BOT4[Ardh",
#    "7" : "]BOT4[Ardh-",
#    "8" : "BOT4[Ardh-]",
#    "9" : "OT4[Ardh-]B",
#    "10" : "T4[Ardh-]BO",
#    "11" : "4[Ardh-]BOT"
#}
#bot5_name = {
#    "1" : "[Ardh-]BOT5",
#    "2" : "Ardh-]BOT5[",
#    "3" : "rdh-]BOT5[A",
#    "4" : "dh-]BOT5[Ar",
#    "5" : "h-]BOT5[Ard",
#    "6" : "-]BOT5[Ardh",
#    "7" : "]BOT5[Ardh-",
#    "8" : "BOT5[Ardh-]",
#    "9" : "OT5[Ardh-]B",
#    "10" : "T5[Ardh-]BO",
#    "11" : "5[Ardh-]BOT"
#}

setTime = {}
setTime = wait2['setTime']

#def upload_tempimage(client):
#    '''
#        Upload a picture of a kitten. We don't ship one, so get creative!
#    '''

    # Here's the metadata for the upload. All of these are optional, including
    # this config dict itself.
#    config = {
#        'album': album,
#        'name':  'bot auto upload',
#        'title': 'bot auto upload',
#        'description': 'bot auto upload'
#    }

#    print("Uploading image... ")
#    image = client.upload_from_path(image_path, config=config, anon=False)
#    print("Done")
#    print()

#    return image


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if cancelinvite["autoCancelUrl"] == True:
                if cl.getGroup(op.param1).preventJoinByTicket == False:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in admin:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        cl.reissueGroupTicket(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        print "Url Opened, Autokick on"
                else:
                    print "random group update"
            else:
                pass

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    print "BOT 1 Joined"
                else:
                    print "autoJoin is Off"

            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    kk.acceptGroupInvitation(op.param1)
                    print "BOT 2 Joined"
                else:
                    print "autoJoin is Off"

            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    ki.acceptGroupInvitation(op.param1)
                    print "BOT 3 Joined"
                else:
                    print "autoJoin is Off"

            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    kc.acceptGroupInvitation(op.param1)
                    print "BOT 4 Joined"
                else:
                    print "autoJoin is Off"
            else:
                if cancelinvite["autoCancel"] == True:
                    try:
                        X = cl.getGroup(op.param1)
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(op.param1, gInviMids)
                        print gInviMids + "invite canceled"
                    except:
                        try:
                            print "Retry canceling invitation"
                            X = random.choice(KAC).getGroup(op.param1)
                            gInviMids = [contact.mid for contact in X.invitee]
                            random.choice(KAC).cancelGroupInvitation(op.param1, gInviMids)
                            print gInviMids + "invite canceled"
                        except:
                            print "Bot can't cancel the invitation"
                            pass

        if op.type == 15:
            random.choice(KAC).sendText(op.param1, "Good Bye :)")
            print op.param3 + "has left the group"

        if op.type == 17:
            if op.param3 in wait["blacklist"]:
                try:
                    cl.kickoutFromGroup(op.param1, op.param3)
                except:
                    random.choice(KAC).kickoutFromGroup(op.param1, op.param3)

        if op.type == 19:
            print "someone was kicked"
            if op.param3 in admin:
                print "Admin has been kicked"
                if op.param2 in Bots:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        cl.inviteIntoGroup(op.param1,op.param3)
                        adm.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        adm.acceptGroupInvitation(op.param1)
                print "Admin Joined"      

            if mid in op.param3:
                print "BOT1 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        kk.inviteIntoGroup(op.param1,op.param3)
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        cl.acceptGroupInvitation(op.param1)
                    print "BOT1 Joined"

            if Amid in op.param3:
                print "BOT2 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        ki.inviteIntoGroup(op.param1,op.param3)
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        kk.acceptGroupInvitation(op.param1)
                    print "BOT2 Joined"

            if Bmid in op.param3:
                print "BOT3 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        kc.inviteIntoGroup(op.param1,op.param3)
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        ki.acceptGroupInvitation(op.param1)
                    print "BOT3 Joined"

            if Cmid in op.param3:
                print "BOT4 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        kg.inviteIntoGroup(op.param1,op.param3)
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        kc.acceptGroupInvitation(op.param1)
                    print "BOT4 Joined"

            else:
                cl.kickoutFromGroup(op.param1,[op.param2])
                kk.kickoutFromGroup(op.param1,[op.param2])
                ki.kickoutFromGroup(op.param1,[op.param2])
                kc.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True
                print "autokick executed"

        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                print "BOT(s) Leaving chat Room"
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                print "BOT(s) Leaving chat Room"

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Already in the Blacklist")
                        wait["wblacklist"] = False
                        print "MID Already in the Blacklist"
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Added to the Blacklist")
                        print [msg.contentMetadata["mid"]] + " Added to the Blacklist"

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Deleted from the Blacklist")
                        wait["dblacklist"] = False
                        print [msg.contentMetadata["mid"]] + " Removed from the Blacklist"

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Contact not in Blacklist")
                        print "MID not in blacklist"
               elif wait["contact"] == True:
                    if msg.from_ in admin:
                        msg.contentType = 0
                        if 'displayName' in msg.contentMetadata:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = cl.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            cl.sendText(msg.to,"[Display Name]:\n" + msg.contentMetadata["displayName"] + "\n\n[MID]:\n" + msg.contentMetadata["mid"] + "\n\n[Status Message]:\n" + contact.statusMessage + "\n\n[Profile Picture]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n[Cover Picture]:\n" + str(cu))
                            print "Contact sent"
                        else:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = cl.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n\n[MID]:\n" + msg.contentMetadata["mid"] + "\n\n[Status Message]:\n" + contact.statusMessage + "\n\n[Profile Picture]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n[Cover Picture]:\n" + str(cu))
                            print "Contact sent"
#-----------------------[Help Section]------------------------                
            elif msg.text in ["/help","/Help"]:
                if wait["lang"] == "JP":
                    random.choice(KAC).sendText(msg.to,helpMessage)
                    print "[Command]/help executed"
                else:
                    cl.sendText(msg.to,helpt)
#-----------------------[Group Name Section]------------------------
            elif "Gh gn " in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gh Gn ","")
                        random.choice(KAC).updateGroup(X)
                        print "[Command]Gn executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
                    print "Gn executed outside group chat"
            elif "Gh gn " in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gh gn ","")
                        random.choice(KAC).updateGroup(X)
                        print "[Command]Gn executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
                    print "Gn executed outside group chat"
#-----------------------[Kick Section]------------------------
            elif "Gh kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Gh kick ","")
                    cl.sendText(msg.to,"Good bye.")
                    random.choice(KAC).kickoutFromGroup(msg.to,[midd])
                    print "[Command]Kick executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Bot Kill Ban","Bot kill ban"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        if matched_list != []:
                            cl.sendText(msg.to,"Blacklisted contact noticed...")
                            cl.sendText(msg.to,"Begin Kicking contact")
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendText(msg.to,"It looks empty here.")
                            return
                        for jj in matched_list:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        print "[Command]Kill ban executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
#-----------------------[Send Profile Section]------------------------                    
            elif msg.text in ["Show bot all","Show bot all"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Amid}
                kk.sendMessage(msg)
                msg.contentMetadata = {'mid': Bmid}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                print "[Command]Bot all executed"

            elif msg.text in ["Bot 1","bot 1"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                print "[Command]Bot 1 executed"

            elif msg.text in ["Bot 2","bot 2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                kk.sendMessage(msg)
                print "[Command]Bot 2 executed"

            elif msg.text in ["Bot 3","bot 3"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                ki.sendMessage(msg)
                print "[Command]Bot 3 executed"

            elif msg.text in ["Bot 4","bot 4"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                print "[Command]Bot 4 executed"

#-----------------------[Cancel invitation Section]------------------------
            elif msg.text in ["cancel inv","Cancel Inv","Cancel inv"]:
                if msg.toType == 2:                    
                    X = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"Canceling all pending(s) invitation")
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        print "[Command]Cancel executed"
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"This group doesn't have any pending invitation")
                            print "[Command]Group don't have pending invitation"
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "Cancel executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[Group link Section]------------------------                        
            elif msg.text in ["Glink off","Link off","glink off","link off","Link Off"]:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation link turned off")
                            print "[Command]Glink off executed"
                        else:
                            cl.sendText(msg.to,"Already turned off")
                            print "[Command]Glink off executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"

                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "[Command]Glink off executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Glink on","Link on","glink on","link on","Link On"]:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation link turned on")
                            print "[Command]Glink on executed"
                        else:
                            cl.sendText(msg.to,"Already turned on")
                            print "[Command]Glink on executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "[Command]Glink on executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[Group info Section]------------------------
            elif msg.text in ["Show Ginfo","Show ginfo"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                        print "[Command]Ginfo executed"
                    else:
                        random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                        print "[Command]Ginfo executed"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "[Command]Ginfo executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[Bot/User/Group ID Section]------------------------
            elif msg.text in ["Show Gid","Show gid"]:
                cl.sendText(msg.to,msg.to)
                print "[Command]Gid executed"
            elif msg.text in ["Show Mid All","Show mid all"]:
                cl.sendText(msg.to,"[Ardh-]Bot(s) ID\n[Ardh-]BOT1\n" + mid + "\n\n[Ardh-]BOT2\n" + Amid + "\n\n[Ardh-]BOT3\n" + Bmid + "\n\n[Ardh-]BOT4\n" + Cmid + "\n\n[Ardh-]BOT5\n" + Dmid)
                print "[Command]Mid executed"
            elif msg.text in ["Bot Mid 1","Bot mid 1"]:
                cl.sendText(msg.to,mid)
                print "[Command]Mid 1 executed"
            elif msg.text in ["Bot Mid 2","Bot mid 2"]:
                kk.sendText(msg.to,Amid)
                print "[Command]Mid 2 executed"
            elif msg.text in ["Bot Mid 3","Bot mid 3"]:
                ki.sendText(msg.to,Bmid)
                print "[Command]Mid 3 executed"
            elif msg.text in ["Bot Mid 4","Bot mid 4"]:
                kc.sendText(msg.to,Cmid)
                print "[Command]Mid 4 executed"
            elif msg.text in ["Bot id","bot id"]:
                cl.sendText(msg.to,msg.from_)
                print "[Command]Yid executed"
#-----------------------[Send Contact Section]------------------------
            elif "Gh Contact" in msg.text:
                mmid = msg.text.replace("Gh Contact ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":AdminMID}
                cl.sendMessage(msg)
                print "[Command]Contact executed"
            elif "Gh contact" in msg.text:
                mmid = msg.text.replace("Gh contact ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":AdminMID}
                cl.sendMessage(msg)
                print "[Command]Contact executed"
#-----------------------[Auto Join Section]------------------------
            elif msg.text in ["Gh Join On","Gh join on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already on")
                        print "[Command]Join on executed"
                    else:
                        cl.sendText(msg.to,"Auto join already on")
                        print "[Command]Join on executed"
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join turned on")
                        print "[Command]Join on executed"
                    else:
                        cl.sendText(msg.to,"Auto join turned on")
                        print "Join on executed"
            elif msg.text in ["Gh Join Off","Gh join off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already off")
                        print "[Command]Join off executed"
                    else:
                        cl.sendText(msg.to,"Auto join already off")
                        print "[Command]Join off executed"
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join turned off")
                        print "[Command]Join off executed"
                    else:
                        cl.sendText(msg.to,"Auto join turned off")
                        print "[Command]Join off executed"
#-----------------------[Group Url Section]------------------------
            elif msg.text in ["Gh Gurl","Gh gurl"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        x = cl.getGroup(msg.to)
                        if x.preventJoinByTicket == True:
                            x.preventJoinByTicket = False
                            cl.updateGroup(x)
                        gurl = cl.reissueGroupTicket(msg.to)
                        cl.sendText(msg.to,"line://ti/g/" + gurl)
                        print "[Command]Gurl executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                        print "[Command]Gurl executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[All bots join group Section]------------------------
            elif msg.text in ["Bot Join","Bot join"]:
                if msg.from_ in admin:
                    try:
                        ginfo = cl.getGroup(msg.to)
                        ginfo.preventJoinByTicket = False
                        cl.updateGroup(ginfo)

                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ginfo = random.choice(KAC).getGroup(msg.to)
                        ginfo.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(ginfo)
                    except:
                        print "Somethings wrong with the url"
                    print "[Command]Join all executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
#-----------------------[Bot(s) Leave Section]------------------------
            elif msg.text in ["@Bye all","@bye all"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            cl.leaveGroup(msg.to)
                            kk.leaveGroup(msg.to)
                            ki.leaveGroup(msg.to)
                            kc.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye all executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["@Bye bot 1","@bye bot 1"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            cl.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 1 executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["@Bye bot 2","@bye bot 2"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = kk.getGroup(msg.to)
                        try:
                            kk.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 2 executed"
                    else:
                        kk.sendText(msg.to,"Command denied.")
                        kk.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["@Bye bot 3","@bye bot 3"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = ki.getGroup(msg.to)
                        try:
                            ki.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 3 executed"
                    else:
                        ki.sendText(msg.to,"Command denied.")
                        ki.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["@Bye bot 4","@bye bot 4"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = kc.getGroup(msg.to)
                        try:
                            kc.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 4 executed"
                    else:
                        kc.sendText(msg.to,"Command denied.")
                        kc.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
#-----------------------[Cleanse Section (USE AT YOUR OWN RISK!)]------------------------
            elif msg.text in ["Clear Group","Clear group"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Cleanse executing"
                        _name = msg.text.replace("Cleanse","")
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        kk.sendText(msg.to,"Group cleansing begin")
                        kc.sendText(msg.to,"Goodbye :)")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        # --------------[Bot and Admin MID]----------------
                        targets.remove(adminMID)
                        targets.remove(mid)
                        targets.remove(Amid)
                        targets.remove(Bmid)
                        targets.remove(Cmid)
                        # --------------[Bot and Admin MID]----------------
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                                try:
                                    klist=[ki,kk,kc,cl]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Group cleansed")
                        print "[Command]Cleanse executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
#-----------------------[Ban/Unban Section]------------------------
            elif "Ban @" in msg.text:
                    if msg.toType == 2:
                        if msg.from_ in admin:
                            print "[Command]Ban executed"
                            _name = msg.text.replace("Gh Ban @","")
                            _nametarget = _name.rstrip('  ')
                            gs = ki.getGroup(msg.to)
                            gs = kk.getGroup(msg.to)
                            gs = kc.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                ki.sendText(msg.to,"Contact not found")
                            else:
                                for target in targets:
                                    try:
                                        wait["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        cl.sendText(msg.to,"Added to Blacklist")
                                    except:
                                        ki.sendText(msg.to,"Error")
                        else:
                            cl.sendText(msg.to,"Command denied.")
                            cl.sendText(msg.to,"Admin permission required.")
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Unban executed"
                        _name = msg.text.replace("Gh Unban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Added to Whitelist")
                                except:
                                    ki.sendText(msg.to,"Added to Whitelist")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Ban","ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"Send Contact to Ban")
                    print "[Command]Ban executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Unban","unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"Send Contact to Unban")
                    print "[Command]Unban executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Banlist","banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"No user is Blacklisted")
                else:
                    cl.sendText(msg.to,"Blacklisted user(s)")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Banlist executed"
#-----------------------[Bot Speak Section]------------------------
            elif "Bc " in msg.text:
                if msg.from_ in staff:
                    bctxt = msg.text.replace("Bc ","")
                    random.choice(KAC).sendText(msg.to,(bctxt))
                    print "[Command]Bc executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
            elif "bc " in msg.text:
                if msg.from_ in staff:
                    bctxt = msg.text.replace("bc ","")
                    cl.sendText(msg.to,(bctxt))
                    print "[Command]Bc executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
#-----------------------[Check Sider]------------------------
            elif msg.text == "$set":
                    cl.sendText(msg.to, "Check sider")
                    ki.sendText(msg.to, "Check sider")
                    kk.sendText(msg.to, "Check sider")
                    kc.sendText(msg.to, "Check sider")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "$read":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-----------------------[Bot speed test Section]------------------------
            elif msg.text in ["Speed","speed"]:
                if msg.from_ in staff:
                    start = time.time()
                    cl.sendText(msg.to, "Bot 1 Processing Request")                    
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))

                    start2 = time.time()                   
                    elapsed_time2 = time.time() - start2
                    kk.sendText(msg.to, "%sseconds" % (elapsed_time2))
                    
                    start3 = time.time()                    
                    elapsed_time3 = time.time() - start3
                    ki.sendText(msg.to, "%sseconds" % (elapsed_time3))
                    
                    start4 = time.time()                   
                    elapsed_time4 = time.time() - start4
                    kc.sendText(msg.to, "%sseconds" % (elapsed_time4))
                    print "[Command]Speed all executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
#-----------------------[Add Staff Section]------------------------
            elif "Add staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Add Staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add Staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Remove Staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove Staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Remove staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#-----------------------[Auto cancel Section]------------------------
            elif msg.text in ["Auto Cancel Off","Auto cancel off"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancel"] == True:
                        cancelinvite["autoCancel"] = False
                        cl.sendText(msg.to, "Auto Cancel turned off")
                        print "[Command]Cancel off executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned off")
                        print "[Command]Cancel off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Auto Cancel On","Auto cancel on"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancel"] == False:
                        cancelinvite["autoCancel"] = True
                        cl.sendText(msg.to, "Auto Cancel turned on")
                        print "[Command]Cancel on executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned on")
                        print "[Command]Cancel on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Auto Url Off","Auto url off"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancelUrl"] == True:
                        cancelinvite["autoCancelUrl"] = False
                        cl.sendText(msg.to, "Auto Cancel Url turned off")
                        print "[Command]Url off executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned off")
                        print "[Command]Url off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Auto Url On","Auto url on"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancelUrl"] == False:
                        cancelinvite["autoCancelUrl"] = True
                        cl.sendText(msg.to, "Auto Cancel Url turned on")
                        print "[Command]Url on executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned on")
                        print "[Command]Url on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
#-----------------------[Misc Section]-------------------------------------------
            elif "Gh random:" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        strnum = msg.text.replace("Ar random:","")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                        try:
                            num = int(strnum)
                            group = cl.getGroup(msg.to)
                            for var in range(0,num):
                                name = "".join([random.choice(source_str) for x in xrange(10)])
                                time.sleep(0.05)
                                group.name = name
                                random.choice(KAC).updateGroup(group)
                        except:
                            cl.sendText(msg.to,"Error")
                        print "[Command]Random executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"

            elif "Gh Random:" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        strnum = msg.text.replace("Ar Random:","")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                        try:
                            num = int(strnum)
                            group = cl.getGroup(msg.to)
                            for var in range(0,num):
                                name = "".join([random.choice(source_str) for x in xrange(10)])
                                time.sleep(0.01)
                                group.name = name
                                cl.updateGroup(group)
                        except:
                            cl.sendText(msg.to,"Error")
                        print "[Command]Random executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Bot Absen","Bot absen"]:
                if msg.from_ in staff:
                    cl.sendText(msg.to, "Hadir")
                    kk.sendText(msg.to, "Hadir")
                    ki.sendText(msg.to, "Hadir")
                    kc.sendText(msg.to, "Hadir")
                    print "[Command]Absen executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Gh Kernel","Gh kernel"]:
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel)
                    print "[Command]Kernel executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"

            # elif "Ar Stalk " in msg.text:
            #     print "[Command]Stalk executing"
            #     stalkID = msg.text.replace("Ar Stalk ","")
            #     subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])   
            #     files = glob.glob("tmp/*.jpg")
            #     for file in files:
            #         os.rename(file,"tmp/tmp.jpg")
            #     fileTmp = glob.glob("tmp/tmp.jpg")
            #     if not fileTmp:
            #         cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
            #         print "[Command]Stalk executed - no image found"
            #     else:
            #         image = upload_tempimage(client)
            #         cl.sendText(msg.to, format(image['link']))
            #         print "[Command]Stalk executed - success"

            # elif "Ar stalk " in msg.text:
            #     print "[Command]Stalk executing"
            #     stalkID = msg.text.replace("Ar stalk ","")
            #     subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])   
            #     files = glob.glob("tmp/*.jpg")
            #     for file in files:
            #         os.rename(file,"tmp/tmp.jpg")
            #     fileTmp = glob.glob("tmp/tmp.jpg")
            #     if not fileTmp:
            #         cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
            #         print "[Command]Stalk executed - no image found"
            #     else:
            #         image = upload_tempimage(client)
            #         cl.sendText(msg.to, format(image['link']))
            #         subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
            #         print "[Command]Stalk executed - success"

            elif "Bot Add @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Add executing"
                        _name = msg.text.replace("Bot Add @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    cl.findAndAddContactsByMid(target)
                                except:
                                    ki.sendText(msg.to,"Error")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")

            elif "Bot add @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Add executed"
                        _name = msg.text.replace("Bot Add @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                cl.findAndAddContactsByMid(target)
                                ki.findAndAddContactsByMid(target)
                                kk.findAndAddContactsByMid(target)
                                kc.findAndAddContactsByMid(target)
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        
            elif msg.text in ["Bot Like", "Bot like"]:
                if msg.from_ in staff:
                    print "[Command]Like executed"
                    cl.sendText(msg.to,"Trying to Like post(s) from staff")
                    try:
                        likePost()
                    except:
                        pass


            elif msg.text in ["Bot Tag All", "Bot tag All"]:
                group = cl.getGroup(msg.to)
                msg_appended = ""
                mem = [contact.mid for contact in group.members]                
                for mm in mem:
                    xname = cl.getContact(mm).displayName
                    xlen = str(len(xname)+1)
                    msg.contentType = 0
                    msg.text = "@"+xname+" "
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mm)+'}]}','EMTVER':'4'}
                    # msg_appended += "->" +msg+ "\n"
                    try:
                        cl.sendMessage(msg)
                    except Exception as error:
                        print error        

            else:
                if cl.getGroup(msg.to).preventJoinByTicket == False:
                    cl.reissueGroupTicket(msg.to)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                else:
                    if msg.from_ in Bots:
                        pass
                    else:
                        print "No Action"
        if op.type == 59:
            print op


    except Exception as error:
        print error

# def nameUpdate_Bot1():
#     while True:
#         try:
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["1"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["2"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["3"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["4"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["5"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["6"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["7"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["8"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["9"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["10"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["11"]
#             cl.updateProfile(profile)
#             time.sleep(0.5)
#         except:
#             pass

# def nameUpdate_Bot2():
#     while True:
#         try:
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["1"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["2"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["3"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["4"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["5"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["6"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["7"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["8"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["9"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["10"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kk.getProfile()
#             profile.displayName = bot2_name["11"]
#             kk.updateProfile(profile)
#             time.sleep(0.5)
#         except:
#             pass

# def nameUpdate_Bot3():
#     while True:
#         try:
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["1"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["2"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["3"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["4"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["5"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["6"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["7"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["8"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["9"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["10"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["11"]
#             ki.updateProfile(profile)
#             time.sleep(0.5)
#         except:
#             pass

# def nameUpdate_Bot4():
#     while True:
#         try:
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["1"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["2"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["3"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["4"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["5"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["6"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["7"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["8"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["9"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["10"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["11"]
#             kc.updateProfile(profile)
#             time.sleep(0.5)
#         except:
#             pass

# def nameUpdate_Bot5():
#     while True:
#         try:
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["1"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["2"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["3"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["4"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["5"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["6"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["7"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["8"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["9"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["10"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["11"]
#             kg.updateProfile(profile)
#             time.sleep(0.5)
#         except:
#             pass

# def nameUpdate():
#     while True:
#         try:
#         #while a2():
#             #pass
#             if wait["clock"] == True:
#                 now2 = datetime.now()
#                 nowT = datetime.strftime(now2,"(%H:%M)")
#                 profile = cl.getProfile()
#                 profile.displayName = wait["cName"]
#                 cl.updateProfile(profile)

#                 profile2 = kk.getProfile()
#                 profile2.displayName = wait["cName2"]
#                 kk.updateProfile(profile2)

#                 profile3 = ki.getProfile()
#                 profile3.displayName = wait["cName3"]
#                 ki.updateProfile(profile3)

#                 profile4 = kc.getProfile()
#                 profile4.displayName = wait["cName4"]
#                 kc.updateProfile(profile4)

#                 profile5 = kg.getProfile()
#                 profile5.displayName = wait["cName5"]
#                 kg.updateProfile(profile5)
#             time.sleep(600)
#         except:
#             pass
# thread2 = threading.Thread(target=nameUpdate)
# thread2.daemon = True
# thread2.start()

def likePost():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in staff:
                try:    
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by ig @muhammadalviann")
                    print "Like"
                except:
                    pass
            else:
                print "Not Admin or staff"

# Auto Changing name
# thread1 = threading.Thread(target=nameUpdate_Bot1)
# thread1.daemon = True
# thread1.start()
# thread2 = threading.Thread(target=nameUpdate_Bot2)
# thread2.daemon = True
# thread2.start()
# thread3 = threading.Thread(target=nameUpdate_Bot3)
# thread3.daemon = True
# thread3.start()
# thread4 = threading.Thread(target=nameUpdate_Bot4)
# thread4.daemon = True
# thread4.start()
# thread5 = threading.Thread(target=nameUpdate_Bot5)
# thread5.daemon = True
# thread5.start()
# END


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
