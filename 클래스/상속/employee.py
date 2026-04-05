''' **상속(Inheritance)**은 객체 지향 프로그래밍(OOP)의 핵심 개념 중 하나로, 
한 클래스의 속성과 메서드를 다른 클래스가 그대로 물려받는 것'''

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"안녕하세요, 저는 {self.name}입니다."
    
# Person을 상속받은 Employee 클래스
class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name) #부모의 속성
        self.employee_id = employee_id #사번(사원의 고유 속성)

    # 소개 메서드 재정의(오버라이딩)
    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro} 제 사번은 {self.employee_id}입니다."
    
person1 = Person("김부장")
print(person1.introduce())

emp1 = Employee("이대리", "e1001")
print(emp1.introduce())