import keen
import pandas as pd
import json

keen.project_id = "[xxxxx]"
keen.write_key = "[xxxxx]"
keen.read_key = "[xxxxx]"

df = pd.read_csv('filename.csv', low_memory=False)
collname = 'filename'
recs = len(df)
cols = df.columns
i = 0
recs = len(df)
while i < recs:
    y = {}
    j = 0
    while j < len(cols):
    # need to put stuff in the appropriate double quotes where required....
        y[cols[j]] = df[cols[j]][i]
        j += 1
    # yz = json.dumps(y)
    keen.add_event(collname, y)
    i += 1

x = keen.count(collname)
print x
