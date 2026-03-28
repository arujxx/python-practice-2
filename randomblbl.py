sn=input("Enter student name:")
mg=float(input("Enter Math grade:"))
phg=float(input("Enter Physics grade:"))
pyg=float(input("Enter Python grade:"))


avg=(mg+phg+pyg)/3


grades = [mg, phg, pyg]
subjects = ['Math', 'Physics', 'Python']

print("=" * 30)
print("Student:", sn.upper())
print("Math:", mg)
print("Physics:", phg)
print("Python:", pyg)
print("-" * 30)
print("Average:", round(avg, 1))

if avg>=90:
   print("Letter grade:A")
elif avg>=75:
    print("Letter grade:B")
elif avg >=60:
    print("Letter grade:C")
elif avg>=50:
    print("Letter grade:D")
else:
    print("Letter grade:F")
print("Scholarship:", avg>=90 and mg>=70 and phg>=70 and pyg>=70)
print("=" * 30)

for i in range(len(grades)):
    if grades[i]>=90:
        print(subjects[i],':',grades[i], '->Excellent')
    elif grades[i]>=75:
        print(subjects[i],':', grades[i], '->Good')
    elif grades[i]>=60:
        print(subjects[i],':', grades[i], '->Satisfactory')
    else:
        print(subjects[i],':', grades[i], '->Fail')


print('Name uppercase:', sn.upper())
print('Name lowercase:', sn.lower())
print('Name length:', len(sn))
print('Masked name:', sn.replace(sn[0],'*', 1))

