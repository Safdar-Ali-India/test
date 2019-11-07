from search_state import SearchAdvisor
import json
# from specialization import special
city, state = SearchAdvisor().city_name()
specialist = SearchAdvisor().specialization()
income = SearchAdvisor().cus_income()
age = SearchAdvisor().cus_age()
ex = SearchAdvisor().experience()

advisor = json.loads(open('output.json').read())

# for i in range(len(advisor['item']["advisors"])):
i = 0
for j in advisor['item']["advisors"]:
    detail = advisor['item']["advisors"][i]
    if detail['state'] == state and detail['city'] == city and int(detail['Experience']) in ex:
        print("Name :", advisor['item']["advisors"][i]['Name'])
        print("Gender :", advisor['item']["advisors"][i]['Gender'])
        print("Experiience :", advisor['item']["advisors"][i]['Experience'])
    i += 1

