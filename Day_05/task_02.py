student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]

max_in_total = 0

for max in student_scores:
    if max > max_in_total:
        max_in_total = max

print(max_in_total)