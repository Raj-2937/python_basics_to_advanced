# # Create a program capable of displaying questions to the user like KBC.
# # Use List data type to store the questions and their correct answers.
# # Display the final amount the person is taking home after playing the game.
   
questions = [
    "What is the capital of India?",
    "Which planet is known as the Red Planet?",
    "Who wrote the national anthem of India?"
]

answers = [
    "Delhi","new delhi","delhi",
    "mars" ,
    "Rabindranath Tagore","rabindranath tagore"
]

prize = [1000, 2000, 5000]

amount = 0

for i in range(len(questions)):
    print("\nQuestion", i + 1)
    print(questions[i])

    answer = input("Your answer: ")

    if answer.lower() == answers[i].lower():
        print("Correct!")
        amount = prize[i]
    else:
        print("Wrong answer!")
        break

print("\nYou are taking home ₹", amount)