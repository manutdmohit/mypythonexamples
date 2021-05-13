import csv
with open('emp.csv','w',newline='') as f:
    w=csv.writer(f) #returns writer object to write data
    w.writerow(['ENO','ENAME','ESAL','EADDR'])
    while True:
        eno=int(input('Enter Employee Number:'))
        ename=input('Enter Employee Name:')
        esal=float(input('Enter Employee Salary:'))
        eaddr=input('Enter Employee Address:')
        w.writerow([eno,ename,esal,eaddr])
        option=input('Do you want to insert one more record[Yes/No]:')
        if option.lower()=='no':
            break

print('writing data to the file completed successfully')


