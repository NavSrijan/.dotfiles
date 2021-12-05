#!/bin/python

import subprocess
import time
import pdb

command = 'heroku logs -n 1500 -a grih-karya | grep -v Restart | grep -v "Na Srijan" | grep sent'

ll = ["Started Grih Karya notifs"]

def extractMsg(output):
    i = output.find("sent")
    output = output.split("\n")
    output = output[-1]
    output = output[i+5:]
    return output

subprocess.run(["notify-send",ll[0]])
while True:
    output = subprocess.getoutput(command)
    msg = extractMsg(output)
    if msg!=ll[-1]:
        subprocess.run(["notify-send", msg])
        ll.append(msg)
    else:
        pass
    time.sleep(120)
