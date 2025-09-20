print("Program starting.")
print("Estimate how many minutes you spent on programming...", end="\n\n")
t1 = int(input("A1_T1: "))
t2 = int(input("A1_T2: "))
t3 = int(input("A1_T3: "))
t4 = int(input("A1_T4: "))
t5 = int(input("A1_T5: "))
t6 = int(input("A1_T6: "))
t7 = int(input("A1_T7: "))
sum = t1+t2+t3+t4+t5+t6+t7
avarage = sum/7
print(f"\nIn total you spent {sum} minutes on programming.")
print(f"Avarage per task was {round(avarage, 2)} min and same rounded to nearest integer {round(avarage)} min.", end="\n\n")
print("Program ending.")
