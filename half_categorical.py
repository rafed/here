#!usr/bin/python

# pip3 install mysql-connector

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rafedmou",
  database="process"
)

mycursor = mydb.cursor()

roads = set()

sql = "SELECT DISTINCT src FROM data;"
mycursor.execute(sql)
result = mycursor.fetchall()

for r in result:
    roads.add(r[0])

sql = "SELECT DISTINCT dst FROM data;"
mycursor.execute(sql)
result = mycursor.fetchall()

for r in result:
    roads.add(r[0])

roads = list(roads)
roads.sort()
roads = dict(enumerate(roads))

#for r in roads: 
#    print(r, roads[r])

index = 0
for i in roads: 
	print(roads[i])
	if(roads[i].startswith("P")):
		index = i
		break

# with open("roads.txt", "w") as f:
#     for i in roads: 
#         s = ("%d %s\n") % (i, roads[i])
#         f.write(s)

for i in range(index, len(roads)):
    rd = roads[i]
    
    # sql = '''UPDATE data SET
    #             src=CASE
    #                 WHEN src='{0}' THEN '{1}'
    #             END,
    #             dst=CASE
    #                 WHEN dst='{0}' THEN '{1}'
    #             END
    #             WHERE src='{0}' or dst='{0}' '''.format(rd, i)
    
    print("Running query {} for src for {}".format(i, rd))
    sql = "UPDATE data SET src=\"{}\" WHERE src=\"{}\"".format(i, rd)
    mycursor.execute(sql)
    mydb.commit()

    print("Running query {} for dst for {}".format(i, rd))
    sql = "UPDATE data SET dst=\"{}\" WHERE dst=\"{}\"".format(i, rd)
    mycursor.execute(sql)
    mydb.commit()