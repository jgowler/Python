import random
from wordlist import common_spanish_words

def quiz_user(common_spanish_words):
    random.shuffle(common_spanish_words)
    score = 0
    count = 0
    
    while count < 15:
        for word in common_spanish_words:
            if count >= 15:
                print(f"The quiz is over. You scored {score} out of {count}.")
                break

            print(f"What is the English translation of the '{word['spanish']}'?")
            user_answer = input("Your answer: ").strip().lower()
            correct_answer = word['english'].lower()

            if user_answer == correct_answer:
                score += 1
                count += 1
                print(f"Correct! {word['english']} is the translation of {word['spanish']}!")
                print(f"Your score so far is {score}.")
                
            else:
                count +=1
                print(f"Incorrect! The english translation of {word['spanish']} is {word['english']}. You have selected {user_answer}")
                print(f"Your score so far is {score}.")
                
    

def language_app():
    print("Language learning quiz\n")
    print("Press Enter to begin...")
    quiz_user(common_spanish_words)

if __name__ == "__main__":
    language_app()