import json
from difflib import get_close_matches


class SearchAdvisor:
    def __init__(self, ste='', cty=''):
        recieve_data = json.loads(open('data.json').read())
        data = json.loads(open('/home/am/python/Indian-States-And-Districts/states-and-districts.json').read())
        state = recieve_data['state']
        f = [data['states'][i]['state'] for i in range(len(data['states']))]
        self.state = state
        self.data = data
        self.f = f
        self.ste = ste
        self.cty = cty
        self.recieve_data = recieve_data

    def state_one(self):
        if self.state in self.f:
            st = self.state
            # print(f'Selected State {st}')
            self.ste = st + self.ste
            return self.ste, self.data, self.f
        find_state = [i for i in get_close_matches(self.state, self.f)]
        if len(find_state) == 1:
            for i in find_state:
                st = i
                # print(f'Selected State {st}')
                self.ste = st + self.ste
                return self.ste, self.data, self.f
        elif len(find_state) >= 2:
            j = 1
            state_more = []
            for i in find_state:
                print(f'{j}.{i}')
                state_more.append(i)
                j += 1
            in_again = int(input('Choose any one: '))
            if state_more[in_again - 1] in state_more:
                st = state_more[in_again - 1]
                # print(f'Selected State {st}')
                self.ste = st + self.ste
                return self.ste, self.data, self.f
            else:
                print('enter correct')
        else:
            print('State not found!')
        print(self.ste)
        raise SystemExit()

    def city_name(self):
        SearchAdvisor.state_one(self)
        city = self.recieve_data['City']
        # for s in range(len(data['states'])):
        find_city = [i for i in get_close_matches(city, self.data['states'][self.f.index(self.ste)]['districts'])]
        if city in self.data['states'][self.f.index(self.ste)]['districts']:
            ct = city
            # print(f'Selected City {ct}')
            self.cty = ct + self.cty
            return self.cty, self.ste
        elif len(find_city) == 1:
            for i in find_city:
                ct = i
                # print(f'Selected City {ct}')
                self.cty = ct + self.cty
                return self.cty, self.ste
        elif len(find_city) >= 2:

            for i in find_city:
                j = 1
            city_more = []
            for i in find_city:
                print(f'{j}.{i}')
                city_more.append(i)
                j += 1
            in_again = int(input('Choose any one: '))
            if city_more[in_again - 1] in city_more:
                ct = city_more[in_again - 1]
                # print(f'Selected City {ct}')
                self.cty = ct + self.cty
                return self.cty, self.ste
            else:
                print('enter correct')
            # return st
        else:
            print('State not found!')
            raise SystemExit()

    def specialization(self):
        specialist = self.recieve_data['specialization']
        # print(specialist)
        return specialist

    def cus_income(self):
        income = self.recieve_data['AUN']
        return income

    def cus_age(self):
        age=self.recieve_data['age']
        return age

    def experience(self):
        ex_range=[]
        ex = self.recieve_data['experience']
        for i in range(self.recieve_data['experience'] - 5, self.recieve_data['experience'] + 1):
            if i == 0:
                continue

            ex_range.append(i)
        return ex_range

