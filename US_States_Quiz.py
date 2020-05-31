# Digant Kumar

import random # For shuffling the questions

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

keys = list(capitals.keys())    # Since dictionaries cannot be shuffled, we create lists of their keys and values and them shuffle them
values = list(capitals.values())
answer_list = []
right_ans, wrong_ans = 0,0       # For keeping track of total right and wrong answers
for quizNum in range(25):
    random.shuffle(keys)
    random.shuffle(values)
    state = ""
    shuffled_state = state.join(random.sample(keys,1))     # Shuffling the keys and taking 1 input at random
    print("What is the capital of %s:" %(shuffled_state))
    for key,value in capitals.items():
        if key == shuffled_state:
            wrong_answers = random.sample(values,3)            # Randomly choosing 3 wrong answers from the values
            correct_answer = value
            while correct_answer in wrong_answers:            # Since we dont want the correct answer to pop up two times in the options
                wrong_answers = random.sample(values,3)
            answer_list = wrong_answers + [correct_answer]
            random.shuffle(answer_list)
            print(answer_list)
            answer = input("Choose anyone from above: ")
            if answer == value:                           # If answer is matched with the value, it prints "Correct answer"
                print("Correct answer")
                right_ans += 1
                print()
            else:
                print("Wrong answer")
                wrong_ans += 1
                print()
print("Total correct answers:", right_ans)
print("Total wrong answers:", wrong_ans)


