import random

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}

end = "Exit"
state, capital = random.choice(list(capitals_dict.items()))
while True:
    user_input = input(f"What is the capital of {state}?").lower().lstrip()
    if user_input == end.lower():
        print(f"The capital of {state} is {capital}!")
        print("Goodbye!")
        break
    elif user_input == capital.lower():
        print("Correct answer!")
        break


