import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


student_data = pd.read_csv('student_data.csv')


correlation = student_data['study_time'].corr(student_data['exam_score'])
print(f"The correlation between study time and exam scores is: {correlation}")


plt.scatter(student_data['study_time'], student_data['exam_score'])
plt.xlabel("Study Time (hours)")
plt.ylabel("Exam Score")
plt.title("Study Time vs Exam Score")
plt.show()


plt.xlabel("Study Time (hours)")
plt.ylabel("Exam Score")
plt.title("Study Time vs Exam Score")
plt.show()


sns.boxplot(x=student_data['study_time'], y=student_data['exam_score'])
plt.xlabel("Study Time (hours)")
plt.ylabel("Exam Score")
plt.title("Study Time vs Exam Score")
plt.show()
