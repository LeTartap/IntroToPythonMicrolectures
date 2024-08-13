# age = 18
# if age >= 18:
#     print("You are eligible to vote.")
#     print("Make sure to register!")
#
#
# age = 16
# if age >= 18:
#     print("You are eligible to vote.")
#     print("Make sure to register!")
# elif age == 17:
#     print("Next year is your time!")
#     print("Check voting requirements in advance.")
# else:
#     print("You are quite young for voting.")
#     print("But it's good to learn about civic duties early on.")
#
#
# age = 20
# has_permission = False
#
# if age >= 18 and has_permission:
#     print("Access granted.")
#     print("Welcome to the system!")
# else:
#     print("Access denied.")
#     print("Either age is too low, or you lack permissions.")


# #evaluatting boolean expressions
#
# is_student = True
# age = 17
#
# # can sign contract?
# print("can sign contract?")
# print(is_student and age >=18)
#
# # brackets!
# has_legal_guardian = True
# print("can sign contract with legal guardian?")
#
# print(is_student and (age >=18 or has_legal_guardian))


score = 82

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is", grade)