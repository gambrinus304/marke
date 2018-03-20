friends = [
    {'name': 'Nick', 'city': 'Milan', 'age': 23},
    {'name': 'Kate', 'city': 'Paris', 'age': 19},
    {'name': 'Sam', 'city': 'NewYork', 'age': 32}]


def print_age(age):
    print(str(friends[0]['name']) + " age is " + str(friends[0]['age']))
    print(str(friends[1]['name']) + " age is " + str(friends[1]['age']))
    print(str(friends[2]['name']) + " age is " + str(friends[2]['age']))


print_age("age")
print("Friends list:")

a = 10
while a <= 40:
    if a == 23:
        print("It's " + str(friends[0]['name']) + " :)")
    elif a == 19:
        print("It's " + str(friends[1]['name']) + " :)")
    elif a == 32:
        print("It's " + str(friends[2]['name']) + " :)")
    else:
        print("A " + str(a) + " year old friend not found :(")

    a = a + 1
