import json


class SearchAdvisor:
    def __init__(self, ste='', cty=''):
        input_data = json.loads(open('data1.json').read())
        data = json.loads(open('/home/am/python/Indian-States-And-Districts/states-and-districts.json').read())
        state = input_data['State']
        output_states = [data['states'][i]['state'] for i in range(len(data['states']))]
        self.input_data = input_data

    def customer_details(self):
        anual_income = self.input_data['anual_income']
        total_saving = self.input_data['total_saving']
        own_b = self.input_data['own_b']
        wwfa = self.input_data['wwfa']
        looking_for = self.input_data['looking_for']
        tlooking_for = self.input_data['tlooking_for']
        goals = self.input_data['goals']
        pin = self.input_data['pin']
        Marital_status = self.input_data['Marital_status']
        age = self.input_data['age']
        state = self.input_data['State']
        city = self.input_data['City']
        pin = self.input_data['pin']
        age = self.input_data['age']
        specialization = self.input_data['specialization']
        ex_range = []
        ex = self.input_data['experience']
        for i in range(self.input_data['experience'] - 5, self.input_data['experience'] + 1):
            if i == 0:
                continue
            ex_range.append(i)
        return (anual_income, total_saving, own_b, wwfa, looking_for, tlooking_for, goals,
                pin, Marital_status, age, state, city, age, ex_range,specialization,pin)

    def details_finder(self):
        anual_income, total_saving, own_b, wwfa, \
        looking_for, tlooking_for, goals, \
        pin, Marital_status, age, state, city, age, \
        experience, specialization, pin = SearchAdvisor.customer_details(self)
        advisor = json.loads(open('output.json').read())
        advisor_return = {'advisor': []}
        i = 0
        for j in advisor['item']["advisors"]:
            detail = advisor['item']["advisors"][i]
            user = {}
            if detail['state'] == state and detail['city'] == city \
                    and int(detail['Experience']) in experience and specialization[0] in detail['specialization']\
                    and detail['pin'] == pin:
                user['id'] = advisor['item']["advisors"][i]['id']
                user['Name'] = advisor['item']["advisors"][i]['Name']
                user["Gender"] = advisor['item']["advisors"][i]['Gender']
                user["Experiience"] = advisor['item']["advisors"][i]['Experience']
                user["specialization"] = advisor['item']["advisors"][i]['specialization']
                user["pin"] = advisor['item']["advisors"][i]['pin']
                advisor_return['advisor'].append(user)
            i += 1
        if len(advisor_return['advisor']) >= 1:
            return advisor_return
        else:
            return 'No Data Found'


OutputJsonData = SearchAdvisor().details_finder()
print(OutputJsonData)
