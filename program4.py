class employ:
    employee="lte tester"

    def __init__(self,name,employid):
         self.name=name
         self.employid=employid

    def setname(self,name):
        self.name=name

    def getname(self):
        return self.name
thunder=employ ("Amit","suman")
id=employ("442","443")

print("company employes")
print("company project :",thunder.employee)
print("employ name :",thunder.name )
print("employ id no :",id.employid)

thunder.setname("Amarjeet")
print(thunder.getname())
