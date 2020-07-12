import random



import random

def generate_number(difficulty):
    Secret_number = random.randint(1 , difficulty)
    print(Secret_number)
    return Secret_number

def get_guess_from_user(difficulty):
    Alerted_number = input(f" Print number between 1 to {difficulty}: ")
    return Alerted_number

def compare_results(Secret_number , Alerted_number):
    if(int(Alerted_number) == int(Secret_number)):
        return  True
    else:
        return False

def play( difficulty):
    print("Welcome to the Guess Game ")
    Secret_number = generate_number(difficulty)
    Alerted_number = get_guess_from_user(difficulty)
    Answer = compare_results(Secret_number,Alerted_number)
    return Answer








