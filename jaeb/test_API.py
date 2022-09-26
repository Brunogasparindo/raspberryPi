import json
from urllib.request import urlopen

url = "http://192.168.137.64:5000/items"

response = urlopen(url)

data_json = json.loads(response.read())
#print(data_json)
for item in data_json:
    print(item[0], item[1], item[2])

# DB-QUERY
# def lightQuery():
#     connection = sqlite3.connect('jaeb/db/light.db')
#     cursor = connection.cursor()
#     cursor.execute(f'SELECT * FROM light;')
#     values = cursor.fetchall()

#     connection.commit()
#     cursor.close()

#     return values

# prepare data for the GUI
# def fillTableIn(table):
#     values = lightQuery()
#     counter = 0
#     for value in values:
#         table.insert(parent='', index='end', iid=counter, values=(value[1], value[2]))
#         counter += 1


# def fillArray(isBrightness):
#     values = lightQuery()
#     returnArray = []
#     counter = 0
#     for value in values:
#         if isBrightness:
#             returnArray.append(value[1])
#         else:
#             returnArray.append(value[2])
#         counter += 1
    
#     return returnArray