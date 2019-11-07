import json
import pymongo
from search_state import SearchAdvisor

city, state = SearchAdvisor().city_name()
specialist = SearchAdvisor().specialization()
income = SearchAdvisor().cus_income()
age = SearchAdvisor().cus_age()
ex = SearchAdvisor().experience()


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb['Advisor_data']
advisor=mycol.find_one({},{'_id':0})

#advisor = json.loads(open('/home/am/python/output.json').read())
output_data = {}
output_data['advisors'] = []
id=1
for i in range(len(advisor['item']["advisors"])):
    for j in advisor['item']["advisors"][i]:
        if int(advisor['item']["advisors"][i]['Experience']) in ex:
            data = {}
            data['id']=id
            data['Name'] = advisor['item']["advisors"][i]['Name']
            data['Gender'] = advisor['item']["advisors"][i]['Gender']
            data['Experience'] = advisor['item']["advisors"][i]['Experience']
            data['State'] = advisor['item']["advisors"][i]['state']
            data['city'] = advisor['item']["advisors"][i]['city']
            output_data['advisors'].append(data)
            id+=1
            break
print(output_data)


#print(output_data)
