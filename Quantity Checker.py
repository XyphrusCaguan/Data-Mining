import pandas as pd
df = pd.read_csv("Carbonilla_Caguan_csv dataset.csv")


female_students = len(df[df['sex'] == 'F'])
male_students = len(df[df['sex'] == 'M'])

print("M :", male_students)
print("F :", female_students)
""""
if female_students > male_students:
    print("There are more females than males")
else:
    print("There are more males than females")
"""
print("\n")
age16_students = len(df[df['age'] == 16])
lessage_students = len(df[df['age'] < 16])
moreage_students = len(df[df['age'] > 16])

print("Less than 16 :", lessage_students)
print("Equal to 16 :", age16_students)
print("Greater than 16 :", moreage_students)
print("\n")
urban_students = len(df[df['address'] == 'U'])
rural_students = len(df[df['address'] == 'R'])

print("Urban Address: ", urban_students)
print("Rural Address: ", rural_students)