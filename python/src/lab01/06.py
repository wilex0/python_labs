class Participant:
    def __init__(self, surname, name, age, form):
        self.name = name
        self.surname = surname
        self.age = int(age)
        self.form = form == "True"


n = int(input("Number of lines: "))
list = []
for i in range(0, n):
    el = input(f"in_{i+1}: ").split()
    assert len(el) == 4
    list.append(Participant(*el))
fullTime = sum(map(lambda x: x.form, list))
selfTime = n - fullTime
print(f"out {fullTime} {selfTime}")
