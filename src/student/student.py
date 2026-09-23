class Student:
    def __init__(self, name)->None:
        self.name = name.lower()
        self.grade = 1

    def introduce(self, name, grade):
        print(f"My name is, {self.name}," )
        print(f"My Grade is, {grade}")


    def promote(self):
        self.grade += 1


    def has_passed(self, score) -> str:
       if score >=0 and score <= 100:
            if score >= 50:
                return "Pass"
            return "Fail"
       return "Invalid score"


    def update_name(self, new_name):
        self.name = new_name


    def is_graduating(self) -> str:
        if 1 <= self.grade <= 12:
            return "Graduating: Final Grade Level"
        return "Not Graduating: Student Not In Final Grade Level"

