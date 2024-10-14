class Employee:
    def __init__(self):
        print('Employee created')
    def __del__(self):
        print('Employee destroyed')
    def show(self):
        print('hi i am bob i am inside show function')


c1=Employee()
c1.show()