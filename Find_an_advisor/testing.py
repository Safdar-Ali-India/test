import json


class SearchAdvisor:
    def __init__(self, ste='', cty=''):
        input_data = json.loads(open('data1.json').read())
        data = json.loads(open('/home/am/python/Indian-States-And-Districts/states-and-districts.json').read())
        state = input_data['State']
        output_states = [data['states'][i]['state'] for i in range(len(data['states']))]
        self.input_data = input_data

    def anual_income(self):
        anual_income = self.input_data['anual_income']
        return anual_income

    def total_saving(self):
        total_saving = self.input_data['total_saving']
        return total_saving

    def own_b(self):
        own_b = self.input_data['own_b']
        return own_b

    def wwfa(self):
        wwfa = self.input_data['wwfa']
        return wwfa

    def looking_for(self):
        looking_for = self.input_data['looking_for']
        return looking_for

    def tlooking_for(self):
        tlooking_for = self.input_data['tlooking_for']
        return tlooking_for

    def goals(self):
        goals = self.input_data['goals']
        return goals

    def pin(self):
        pin = self.input_data['pin']
        return pin

    def marital_status(self):
        Marital_status = self.input_data['Marital_status']
        return Marital_status

    def age(self):
        age = self.input_data['age']
        return age

    def state_find(self):
        state = self.input_data['State']
        return state

    def city_find(self):
        city = self.input_data['City']
        return city

    def specialization(self):
        specialist = self.input_data['specialization']
        # print(specialist)
        return specialist

    def cus_income(self):
        income = self.input_data['AUN']
        return income

    def cus_age(self):
        age = self.input_data['age']
        return age

    def experience(self):
        ex_range = []
        ex = self.input_data['experience']
        for i in range(self.input_data['experience'] - 5, self.input_data['experience'] + 1):
            if i == 0:
                continue
            ex_range.append(i)
        return ex_range
