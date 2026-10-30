students = [
    ["Deekshitha", 90, 75, 85, 50000],
    ["honey", 85, 70, 90, 40000],
    ["Sweety", 95, 80, 95, 30000]
]

eligible = []

for s in students:
    name, marks, subject, attendance, income = s

    if marks >= 80 and subject >= 60 and attendance >= 75 and income <= 100000:
        eligible.append(s)

# Rank based on aggregate marks
eligible.sort(key=lambda x: x[1], reverse=True)

print("Scholarship Ranking:")

for rank, s in enumerate(eligible, 1):
    print(rank, s[0], "Marks:", s[1])
