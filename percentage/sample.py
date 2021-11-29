Dict1 = {'Name': 'Beta', 'Grades': [1, 2, 3, 4, 5]}
Dict2 = {'Name': 'Alpha', 'Grades': [6, 7, 8, 9, 10]}

query_name = input()


def query():
    if query_name == (Dict1['Name']):
        print("yes")
        values = Dict1['Grades']
        average = sum(values)/5
        print(average)
    elif query_name == (Dict2['Name']):
        values = Dict2['Grades']
        average = sum(values)/5
        print(average)

query()