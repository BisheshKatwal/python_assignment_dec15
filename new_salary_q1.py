def cal_new(salary):
    new_salary = []
    for each in salary:
        new_salary.append( each+ each*0.23)
    print(new_salary)


salary=[15000,20000,17000,18900,30000]
cal_new(salary)
