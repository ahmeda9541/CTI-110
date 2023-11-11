# CTI-110
# P4HW1 - Score List
# Your Name
# Date

def get_valid_score(score_number):
    while True:
        user_input = input(f"Enter score # {score_number}:")
        if user_input.isdigit():
            score = float(user_input)
            if 0 <= 100:
                return score
        print("Invalid input. Please enter a valid score.")

def calculate_average_and_grade(scores):
    scores.remove(min(scores))
    average = sum(scores) / len(scores)
    return average, 'A' if average >= 90 else 'B' if average >= 80 else 'C' if average >= 70 else 'D' if average >= 60 else 'F'

def main():
    num_scores = int(input("Enter the number of scores you want to enter: "))
    scores = []

    for i in range(1, num_scores + 1):
        score = get_valid_score(i)
        scores.append(score)

    print("\nResults")
    print(f'Lowest Score Entered: {min(scores)}')
    print(f'Score List after Dropping Lowest Score: {scores}')

    average, letter_grade = calculate_average_and_grade(scores)
    print(f'Average of Scores in Modified List: {average:.2f}')
    print(f'Letter Grade: {letter_grade}')
    print('-----------------------------------------')

main()
