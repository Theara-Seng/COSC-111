scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 79,
    "David":90,
    "Eve":88
}

# find the names of the names of the student with the highest score

# find the student with the max score
def find_and_print_top_student(scores):
    max_student_score = max(scores.items(), key = lambda x: x[1])
    print(f"Top student: {max_student_score[0]}, Score: {max_student_score[1]}")
    
    return max_student_score[0]

def calculate_and_print_avg_score(scores):
    sum_of_scores = 0
    # calculate average score
    for score in scores.values():
        sum_of_scores += score
    avg_score = sum_of_scores/len(scores)
    print(f"Class's average score {avg_score}")
    return avg_score

def grade_B_or_above(scores):
    return {k:v for k, v in scores.items() if v >= 80}.copy()

if __name__ == "__main__":
    find_and_print_top_student(scores)
    calculate_and_print_avg_score(scores)
    print(grade_B_or_above(scores))
