import json
import pymongo


def details_finder():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb['output_data']
    input_data = json.loads(open('data1.json').read())
    state = input_data['State']
    city = input_data['City']
    pin = input_data['pin']
    specialization = input_data['specialization']
    experience = []
    ex = input_data['experience']
    for i in range(input_data['experience'] - 5, input_data['experience'] + 1):
        if i == 0:
            continue
        experience.append(i)

    advisor = mycol.find({'state': state, 'city': city, 'pin': str(pin), }, {'_id': 0, 'id':0})
    for detail in advisor:

        if detail['state'] == state and detail['city'] == city \
                and int(detail['Experience']) in experience and specialization[0] in detail['specialization'] \
                and detail['pin'] == str(pin):
            return detail, specialization


print(details_finder())
