students = [
    ("Arjun", 85),
    ("Priya", 92),
    ("Rahul", 58),
    ("Sneha", 76),
    ("Dev", 45)
]

print("📊 Student Grade Report")
print("-" * 30)

for i, (name, score) in enumerate(students, 1):
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"
    
    status = "Pass" if score >= 60 else "Fail"
    print(f"{i}. {name:<10} Score: {score}  Grade: {grade}  Status: {status}")

scores = [s for _, s in students]
print("-" * 30)
print(f"Class Average : {sum(scores) / len(scores):.1f}")
print(f"Highest Score : {max(scores)}")
print(f"Lowest Score  : {min(scores)}")
