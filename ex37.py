#symbol review:
#1. assert
#here assert ensure that some thing is True.
print("*********************************************assert******************************************************")
def apply_discount(product, discount):
    price = int(product['price'] *(1.0 - discount))
    assert 0 <= price <= product['price']
    return price
shoes = {'name':'fancy Shoe', 'price':14900}
print(apply_discount(shoes, 0.25))

#2. break
#break used to break a loop.
#the below program find the secnod largest number from a list
print("*********************************************Break******************************************************")
def largest(list):
    largest = list[0] 
    for i in range(len(list)):
        if i == (len(list) -1):
            break
        elif largest >= list[i + 1]:
            largest = largest
        else:
            largest = list[i + 1]
    return largest

def second_largest(list):
    lenth = len(list)
    for i in range(2):
        largest1 = largest(list)
        lenth_now = len(list)
        if lenth_now == lenth:
            list.remove(largest1)
        else:
            print(largest1)
second_largest([5, -6, 6, 5])


#3. lambda
#A lambda function can take any number of arguments, but can only have one expression.
#synthax >> lambda arguments : expression
print("***************************************************lambda**********************************************")
x = lambda a: a + 10
print(x(3))

y = lambda a, b : a * b
print(y(10, 3))

#The power of lambda is better shown when you use them as an anonymous function inside another function.

def myfunction(n):
    return lambda a : a * 2
doubler = myfunction(2)
print(doubler(100))

def myfun(n):
    return lambda a: a * n
tripler = myfun(3)
five_times = myfun(5)
print(tripler(10))
print(five_times(10))
print()

#4. class
#Define a class.
print("*********************************************class******************************************************")

class employee:

    rise_amount = 1.04 #class variable
    no_of_employees = 0
    
    def __init__(self, first, last ,pay):
        #instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        employee.no_of_employees += 1

    #in regular method we passing instance (self) as first argument
    def fullname(self): 
        return "{} {}".format(self.last, self.first)

    def incriment(self):
        self.pay = int(self.pay * self.rise_amount)

        
    #in class method we passing cls (class) insted of instance
    @classmethod
    def from_string(cls, string):
        first, last, pay = string.split("-")
        return cls(first, last, int(pay))
    @classmethod
    def set_rise_amount(cls, amount):
        cls.rise_amount = amount

    #in staticmethod no passing instance or cls
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

#inheritance---creating sub-class
class Developer(employee):
    rise_amount = 1.5
    #Adding additionl instance to Developer class other than employee class
    def __init__(self, first, last, pay, prog_lange):
        super().__init__(first, last, pay)
        #employee.__init__(first, last, pay)  we can also call this way
        self.prog_lange = prog_lange

class Manager(employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is  None:
            self.employees = []
        else:
            employees == employees
            self.employees = employees

    def Add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def Remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def Print_emps(self):
        for emp in self.employees:
            print(">>>>", emp.fullname())
            
        


print("no of employees = ", employee.no_of_employees)
empl1 = employee("fairoos", "muhammed" , 90)
empl2 = employee("razi", "muhammed", 90)
print("no of employees = ", employee.no_of_employees)
empl2.rise_amount = 3.13
empl1.incriment()
empl2.incriment()
print(empl2.pay)
print(empl1.pay)
print(employee.fullname(empl1))
print(empl2.fullname())
print(empl1.email)

emp_strintg_1 = "aysha-noora-90"
new_employee = employee.from_string(emp_strintg_1)
print("no of employees = ", employee.no_of_employees)
print(new_employee.pay)
print(new_employee.email)
new_employee.incriment()
print(new_employee.pay)
employee.set_rise_amount(2)
print(new_employee.pay)
new_employee.incriment()
print(new_employee.pay)
print(employee.rise_amount)

import datetime
my_date = datetime.date(2007, 12, 12)
print(employee.is_workday(my_date))

dev1 = Developer("muhammed", "jinan", 90, "python")
print(dev1.email)
print(dev1.prog_lange)
print(dev1.pay)
dev1.incriment()
print(dev1.pay)


mgr1 = Manager("fathima", "sana", 90, [dev1])
print(mgr1.email)
mgr1.Add_employee(empl1)
mgr1.Print_emps()
mgr1.Remove_employee(empl1)
print("After REmove")
mgr1.Print_emps()

#isinstance
print(isinstance(mgr1, Manager))

#issubclass
print(issubclass(Developer, employee))
