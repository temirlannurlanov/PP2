class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.


class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)