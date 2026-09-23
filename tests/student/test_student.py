import unittest
from src.student.student import Student

class TestStudent(unittest.TestCase):

    def test_student_introduction(self):
        student = Student("Winifred")
        self.assertEqual(student.name, "winifred")
        self.assertEqual(student.grade, 1)

    def test_student_promotion(self):
        student = Student("Winifred")
        student.promote()
        self.assertEqual(student.grade, 2)


    def test_if_student_passed(self):
        student = Student("Winifred")
        self.assertEqual(student.has_passed(80), "Pass")


    def test_if_student_failed(self):
        student = Student("Winifred")
        self.assertEqual(student.has_passed(30), "Fail")

    def test_if_student_score_is_invalid(self):
        student = Student("Winifred")
        self.assertEqual(student.has_passed(-20), "Invalid score")


    def test_again_if_student_score_is_invalid(self):
        student = Student("Winifred")
        self.assertEqual(student.has_passed(120), "Invalid score")


    def test_student_name_update(self):
        student = Student("Winifred")
        student.update_name("Cara")
        self.assertEqual(student.name, "Cara")


    def test_student_introduction(self):
        student = Student("Winifred")
        for count in range(11):
            student.promote()

        self.assertEqual(student.is_graduating(), "Graduating: Final Grade Level")
