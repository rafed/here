import json
from datetime import datetime

# with open('dtf2.txt') as f:
#     data = json.load(f)

# for RWS in data['RWS']:
#     for RW in RWS['RW']:
#         for FIS in RW['FIS']:
#             for FI in FIS['FI']:
#                 print FI['CF']

try:
    a = 2/0
except Exception as e:
    s = "%s %s" % (datetime.now(), e)
    print s
