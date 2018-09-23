import json
from pprint import pprint

FILENAME_IN = "messageLen.json"
FILENAME_OUT = "messagesLen.txt"
with open(FILENAME_IN) as f:
    data = json.load(f)

msgs = data["messages"]
txt = open(FILENAME_OUT,"w+")
for entry in msgs:
    for node in entry:
        if node == "content":
            txt.write(entry[node] + " ")
            

txt.close()
