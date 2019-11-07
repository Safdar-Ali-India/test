def special_list():
    specialize = ['Equities', 'Bonds', 'Mutual Fund', 'ETFS', 'Future & Options']
    for i in range(len(specialize)):
        print(f'{i + 1}.{specialize[i]}')
    select_specialize = int(input('Choose Specialization by number: '))
    return select_specialize, specialize


def special():
    while True:
        a, specialize = special_list()
        if a <= len(specialize):
            if specialize[a - 1] in specialize:
                specialist = specialize[a - 1]
                return specialist
            break
        else:
            print('Select correctly')

