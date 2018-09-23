import json
from pprint import pprint

FILENAME_IN = "message.json"
FILENAME_OUT = "messages.txt"
with open(FILENAME_IN) as f:
    data = json.load(f)

msgs = data["messages"]
txt = open(FILENAME_OUT,"w+")
for entry in msgs:
    for node in entry:
        if node == "content":
            txt.write(entry[node] + " ")
            

txt.close()
