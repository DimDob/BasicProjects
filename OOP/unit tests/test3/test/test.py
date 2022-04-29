import sys
import unittest
from project.student_report_card import StudentReportCard


class TestStudentReportCard(unittest.TestCase):
    def setUp(self) -> None:
        self.card = StudentReportCard('Ivan', 5)

    def test_init(self):
        card = StudentReportCard('Ivan', 5)
        self.assertEqual('Ivan', card.student_name)
        self.assertEqual(5,card.school_year)
        self.assertEqual({}, card.grades_by_subject)



    def test_if_name_set_not_properly(self):
        with self.assertRaises(ValueError) as ex:
            self.card.student_name = ''
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))



    def test_if_name_set_prop(self):
        name = 'Ivan'
        self.assertEqual(name, self.card.student_name)



    def test_if_year_is_not_set_prop(self):
        for x in range(13, 100):
            with self.assertRaises(ValueError) as ex:
                self.card.school_year = x
            self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

        for x in range(-100, 0):
            with self.assertRaises(ValueError) as ex:
                self.card.school_year = x
            self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_if_year_is_prop(self):
        year = 5
        self.assertEqual(year, self.card.school_year )

    def test_add_grade(self):
        self.card.grades_by_subject['Arts'] = [3, 5]
        self.assertTrue('Math' not in self.card.grades_by_subject)

        self.card.add_grade('Math', 3)
        self.assertEqual([3], self.card.grades_by_subject['Math'])

        self.card.add_grade('Arts', 6)
        self.assertEqual([3, 5, 6], self.card.grades_by_subject['Arts'])


    def test_average_grade_by_subj(self):
        self.card.grades_by_subject['Arts'] = [3, 5]
        self.card.grades_by_subject['Math'] = [5, 5]

        self.assertTrue(self.card.grades_by_subject['Arts'] == [3,5])
        av_grade = (3+5)/len(self.card.grades_by_subject['Arts'])
        self.assertEqual(4, av_grade)
        av_grade = (5+5)/len(self.card.grades_by_subject['Math'])
        self.assertEqual(av_grade, 5)

        report = self.card.average_grade_by_subject()
        expected = f"Arts: 4.00\nMath: 5.00"
        self.assertEqual(expected, report)


    def test_average_grade_for_all_subjects(self):
        self.card.grades_by_subject['Arts'] = [3, 5]
        self.card.grades_by_subject['Math'] = [5, 5]

        av_grade = (3+5)/len(self.card.grades_by_subject['Arts'])
        av_grade2 = (5+5)/len(self.card.grades_by_subject['Math'])
        final_av_grade = (av_grade2 + av_grade)/len([av_grade, av_grade2])
        result = self.card.average_grade_for_all_subjects()

        self.assertEqual(result, f"Average Grade: {final_av_grade:.2f}")

    def test_repr(self):
        self.card.grades_by_subject['Arts'] = [3, 5]
        self.card.grades_by_subject['Math'] = [5, 5]
        result = repr(self.card)
        expected =f"Name: Ivan\n" \
                 f"Year: 5\n" \
                 f"----------\n" \
                 f"Arts: 4.00\n" \
                  f"Math: 5.00\n" \
                 f"----------\n" \
                 f"Average Grade: 4.50"
        self.assertEqual(result , expected )