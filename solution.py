def find_hack(arr):
    hacked_names = []
    for record in arr:
        name, total, grades = record
        real_total = sum(30 if grade == "A" else 20 if grade == "B" else 10 if grade == "C" else 5 if grade == "D" else 0 for grade in grades)
        if len(grades) >= 5 and all(grade in ("A", "B") for grade in grades):
            real_total += 20
        real_total = min(real_total, 200)
        if total != real_total:
            hacked_names.append(name)
    return hacked_names
  
  
array = [
    ["name1", 150, ["B", "A", "A", "C", "A", "A"]],
    ["name2", 120, ["B", "A", "A", "A"]],
    ["name3", 160, ["B", "A", "A", "A","A"]],
    ["name4", 140, ["B", "A", "A", "C", "A"]]
]

test.assert_equals(find_hack(array), ["name2", "name4"])
