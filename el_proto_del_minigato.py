encryption=False
from microbit import*
import radio
if encryption:
 import random
 import aes
seqNum=0
tryTime=100
Timeout=300
ackMsgId=255
radio.config(channel=4,address=50)
radio.on()
if encryption:
 key=bytes([156,110,239,52,206,138,164,35,3,76,3,60,84,199,63,253])
 iv=bytes([0 for _ in range(16)])
 cipher=aes.AES(key)
class Message:
 def __init__(self,dest:int,exped:int,seqNum:int,msgId:int,payload:List[int],crc:int):
  self.exped=exped
  self.dest=dest
  self.seqNum=seqNum
  self.msgId=msgId
  self.payload=payload
  self.crc=crc
 def msgStr(self):
  return str(self.exped)+" -> "+str(self.dest)+"n["+str(self.seqNum)+"] "+" : type "+str(self.msgId)+" : "+str(self.payload)+" (crc="+str(self.crc)+")"
def bytes_to_int(bytesPayload:bytes):
 intPayload=[]
 for i in bytesPayload:
  intPayload.append(ord(bytes([i])))
 return intPayload
def int_to_bytes(intPayload:List[int]):
 return bytes(intPayload)
def msg_to_trame(rawMsg:Message):
 l=[rawMsg.dest,rawMsg.exped,rawMsg.seqNum,rawMsg.msgId]+rawMsg.payload
 rawMsg.crc=sum(l)%256
 trame=l+[rawMsg.crc]
 if encryption:
  trame=cipher.encrypt_cfb(trame,iv)
 return int_to_bytes(trame)
def trame_to_msg(trame:bytes,userId:int):
 trame=bytes_to_int(trame)
 if encryption:
  trame=bytes_to_int(cipher.decrypt_cfb(trame,iv))
 msgObj=Message(trame[0],trame[1],trame[2],trame[3],trame[4:-1],trame[-1])
 if msgObj.crc==sum(trame[:-1])%256:
  if msgObj.dest==userId:
   return msgObj
def ack_msg(msg:Message):
 msgAck=Message(msg.exped,msg.dest,msg.seqNum,ackMsgId,[],0)
 trame=msg_to_trame(msgAck)
 radio.send_bytes(trame)
def receive_ack(msg:Msg):
 new_trame=radio.receive_bytes()
 if new_trame:
  msgRecu=trame_to_msg(new_trame,msg.exped)
  return msgRecu and msgRecu.exped==msg.dest and msgRecu.dest==msg.exped and msgRecu.seqNum==msg.seqNum and msgRecu.msgId==ackMsgId
 else:
  return False
def send_msg(msgId:int,payload:List[int],userId:int,dest:int):
 global seqNum
 msg=Message(dest,userId,seqNum,msgId,payload,0)
 acked=False
 t0=running_time()
 while not acked and running_time()-t0<Timeout:
  trame=msg_to_trame(msg)
  radio.send_bytes(trame)
  sleep(tryTime//2)
  display.clear()
  sleep(tryTime//2)
  acked=receive_ack(msg)
 seqNum=(seqNum+1)%256
 return acked
def receive_msg(userId:int):
 new_trame=radio.receive_bytes()
 if new_trame:
  msgRecu=trame_to_msg(new_trame,userId)
  if msgRecu and msgRecu.msgId!=ackMsgId:
   ack_msg(msgRecu)
   return msgRecu