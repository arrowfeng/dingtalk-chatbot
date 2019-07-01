#!/usr/bin/env python3
import subprocess
import os
from dingtalkchatbot.chatbot import DingtalkChatbot

if 'WEBHOOK' not in os.environ:
  raise RuntimeError('No WEBHOOK')

if 'APPNAME' not in os.environ:
  raise RuntimeError('No APPNAME')

if 'COMMAND' not in os.environ:
  raise RuntimeError('No COMMAND')

webhook = os.getenv('WEBHOOK')

appname = os.getenv('APPNAME')

command = os.getenv('COMMAND')

status, content = subprocess.getstatusoutput(COMMAND)

if status != 0:
   raise RuntimeError('Command Error')

xiaoding = DingtalkChatbot(webhook)

at_mobiles=[]

if 'AT' in os.environ:
   at = os.getenv('AT')
   at_mobiles = at.split(',')

xiaoding.send_text(msg=appname + '\n' + content, at_mobiles=at_mobiles)

print('send successfully')
