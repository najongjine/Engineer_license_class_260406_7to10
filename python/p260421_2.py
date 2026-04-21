#########클래스############
class Person:
    c="클래스 변수"
    def __init__(self,a,b):
        self.a=a
        self.name=b
        pass

# 객체 생성
p1 = Person(0,"모모")
p2=Person(1,"페페")
#print(f"p1" ,p1.c)
#print(f"p2" ,p2.c)
p1.c="클래스 변수2"
#print(f"p1" ,p1.c)
#print(f"p2" ,p2.c)

Person.c="클래스 변수3"
#print(f"Person.c=클래스 변수3" )
#print(f"p1" ,p1.c)
#print(f"p2" ,p2.c)

"""
파이썬의 클래스 변수는 자바의 static 속성과 많이 틀려요.
인스턴스가 생성됬을땐 class 의 클래스변수와 연결이 되있습니다.
하지만 인스턴스.클래스변수 = "값바꿈" 이렇게 하면 
인스턴스에 새로운 클래스 변수가 생성되서 class.클래스 변수와의 연결이 끊어져요.
만약 인스턴스의 클래스변수 값을 바꾸지 않았다면, class.클래스변수와 연결이 되있습니다.
클래스이름.클래스변수="값바꿈" 하면 연결되 있는 인스턴스들의 클래스변수는 값이 바뀌어요.
"""

class Parent:
    c="부모 클래스 변수"
    def __init__(self):
        self.value="부모"
        pass
    def show(self):
        print(f"난 부모show",self.value)

class Child(Parent):
    def __init__(self):
        super().__init__()
        pass
    def show(self):
        print(f"난 자식show",self.value)

child=Child()
child.value="자식"
#print(child.value)
#print(child.c)
#child.show()

p=Parent()
p.value="부모2"
#print(p.value)
#print(p.c)
#p.show()

#######class 를 list comprehension으로 생성하기#######
class Person:
    def __init__(self,a,b):
        self.a=a
        self.name=b
        pass
    def change(self,_p):
        p.a+=10
        pass

p=[Person(i,"hi"+str(i)) for i in range(3)]
#p=[Person(0,"hi1"),Person(1,"hi2"),Person(2,"hi3")]
p[0].change(p[1])
print(p[1].a)