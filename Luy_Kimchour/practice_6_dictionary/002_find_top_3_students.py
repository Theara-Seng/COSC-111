scores = {
    'Alice': 85, 'Bob': 92, 'Charlie': 78,
    'David': 90, 'Eve': 88, 'Frank': 95, 'Grace': 80
}

def find_top_3_student_names(scores):
    if len(scores) > 3:
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for i in range(3):
            name = sorted_scores[i][0]
            score = sorted_scores[i][1]

            print(f"Top {i+1}: {name}, {score}")
    else:
        print("the dictionary of containing students is too small")

if __name__ == '__main__':
    find_top_3_student_names(scores)
