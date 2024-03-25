if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # Calculate the sum of the marks for the student with query_name
    sum_marks = sum(student_marks[query_name])

    # Calculate the average and print it with 2 decimal places
    avg_marks = sum_marks / len(student_marks[query_name])
    print("{:.2f}".format(avg_marks))
