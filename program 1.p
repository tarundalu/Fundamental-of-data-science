import numpy as np
student_scores = np.array([
    [85, 90, 78, 88],
    [92, 88, 79, 76],
    [78, 85, 88, 90],
    [85, 80, 92, 87]
])
average_scores = np.mean(student_scores, axis=0)
highest_avg_score_subject = np.argmax(average_scores)
subject_names = ["Math", "Science", "English", "History"]
for i, subject in enumerate(subject_names):
    print(f"Average score in {subject}: {average_scores[i]}")
print(f"The subject with the highest average score is {subject_names[highest_avg_score_subject]} with an average score of {average_scores[highest_avg_score_subject]}")

