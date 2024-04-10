import csv

class Budget:
  department: str
  actual: int

  def __init__(self, department, actual):
    self.department = department
    self.actual = actual

with open("expenditures.csv") as file:
  reader = csv.reader(file, delimiter = ",")
  info_list = []
  row_number = 1

  for list in reader:
    if row_number != 1:
      dept_and_cost = Budget(list[0], list[3])
      info_list.append(dept_and_cost)
      row_number += 1
    else:
      row_number+=1

budget_dict = {}

for item in info_list:
  if item.actual == '':
    continue

  temp_amt = int(item.actual)
  if item.department not in budget_dict:
    budget_dict[item.department] = [temp_amt]

  else:
    costs = budget_dict[item.department]
    costs.append(temp_amt)
   

for department in budget_dict:
  total = sum(budget_dict[department])
  print(f"\nDepartment: {department} \nTotal Spent: ${total}")