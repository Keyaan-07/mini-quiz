import random

questions = [
    {'question': 'What is 5*6-3?', "options":['1. 15', '2. 27', '3. 30', '4. 33'], 'answer':2},
    {'question': 'What is the capital of France?', "options":['1. Paris', '2. London', '3. Washington', '4. Mumbai'], 'answer':1},
    {'question': 'What is the largest Planet in our Solar System?', "options":['1. Earth', '2. Mars', '3. jupiter', '4. Uranus'], 'answer':3},
    {'question': 'What is the chemical Symbol for Tungsten?', "options":['1. Au', '2. T', '3. Tg', '4. W'], 'answer':4},
    {'question': 'Who is known as the father of Computers?', "options":['1. Alan Turing', '2. Charles Babbage', '3. Blaise Pascal', '4. Robert Oppenheimer'], 'answer':2},
    {'question': 'What was the first programming languae?', "options":['1. C', '2. Python', '3. BASIC', '4. FORTRAN'], 'answer':4},
    {'question': 'In which year did India gain independence?', "options":['1. 1955', '2. 1927', '3. 1947', '4. 1949'], 'answer':3},
    {'question': 'What is the hardest natural substance on Earth?', "options":['1. Diamond', '2. Graphite', '3. Steel', '4. Quartz'], 'answer':1},
    {'question': 'Which country has the largest population in the world?', "options": ['1. India', '2. China', '3. United States', '4. Indonesia'], 'answer': 2},
    {'question': 'Who wrote the famous play "Romeo and Juliet"?', "options": ['1. William Shakespeare', '2. Charles Dickens', '3. J.K. Rowling', '4. George Orwell'], 'answer': 1},
    {'question': 'What is the main ingredient in guacamole?', "options": ['1. Tomato', '2. Avocado', '3. Onion', '4. Cucumber'], 'answer': 2},
    {'question': 'What is the capital city of Australia?', "options": ['1. Sydney', '2. Canberra', '3. Melbourne', '4. Brisbane'], 'answer': 2},
    {'question': 'What is the hardest natural substance on Earth?', "options": ['1. Graphite', '2. Quartz', '3. Diamond', '4. Steel'], 'answer': 3},
    {'question': 'Which planet is closest to the sun?', "options": ['1. Mercury', '2. Venus', '3. Earth', '4. Mars'], 'answer': 1},
    {'question': 'What is the square root of 144?', "options": ['1. 11', '2. 12', '3. 13', '4. 14'], 'answer': 2},
    {'question': 'Which chemical element has the symbol "O"?', "options": ['1. Osmium', '2. Oxygen', '3. Oganesson', '4. Oxide'], 'answer': 2},
    {'question': 'In which year did World War II end?', "options": ['1. 1944', '2. 1945', '3. 1946', '4. 1947'], 'answer': 2},
    {'question': 'Which is the largest ocean in the world?', "options": ['1. Atlantic Ocean', '2. Pacific Ocean', '3. Indian Ocean', '4. Arctic Ocean'], 'answer': 2},
    {'question': 'Which programming language is known as the “mother of all languages”?', "options": ['1. Assembly', '2. FORTRAN', '3. C', '4. Python'], 'answer': 3},
    {'question': 'What is the national animal of India?', "options": ['1. Elephant', '2. Bengal Tiger', '3. Peacock', '4. Lion'], 'answer': 2},
    {'question': 'Which sport is known as the “king of sports”?', "options": ['1. Cricket', '2. Basketball', '3. Football (Soccer)', '4. Tennis'], 'answer': 3},
    {'question': 'What is the tallest mountain in the world?', "options": ['1. Mount Everest', '2. K2', '3. Kangchenjunga', '4. Lhotse'], 'answer': 1},
    {'question': 'Which country invented pizza?', "options": ['1. France', '2. Italy', '3. United States', '4. Greece'], 'answer': 2},
    {'question': 'What is the name of the ship that sank in 1912, known as a major disaster?', "options": ['1. Britannic', '2. Titanic', '3. Lusitania', '4. Endeavour'], 'answer': 2},
    {'question': 'Which famous scientist developed the theory of relativity?', "options": ['1. Isaac Newton', '2. Galileo Galilei', '3. Albert Einstein', '4. Nikola Tesla'], 'answer': 3},
    {'question': 'Which desert is the largest in the world?', "options": ['1. Gobi', '2. Sahara', '3. Kalahari', '4. Antarctic Desert'], 'answer': 4},
    {'question': 'What is the chemical formula for water?', "options": ['1. H2O', '2. CO2', '3. O2', '4. CH4'], 'answer': 1},
    {'question': 'What is the fastest land animal?', "options": ['1. Lion', '2. Cheetah', '3. Gazelle', '4. Leopard'], 'answer': 2},
    {'question':'What part of the human body produces insulin?', "options":['1. Heart', '2. Pancreas', '3. Adrenal Glands', '4. Kidneys'], 'answer':2}
]

questions = random.sample(questions, 5)

score = 0

for i,q in enumerate(questions):
    print(f"Question Number {i+1}: {q['question']}")
    for option in q['options']:
        print(option)
    answer = int(input("Enter your answer's number:"))
    if answer == q['answer']:
        print('Correct Answer!\n')
        score += 1
    else:
        print(f"Wrong! The correct Answer is {q['answer']}\n")

print(f"Your Final Score is: {score}/5")
print("Goodbye!")
