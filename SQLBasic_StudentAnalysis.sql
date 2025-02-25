# MySQL
SELECT s.roll_number, s.name
FROM student_information s
JOIN examination_marks e ON s.roll_number = e.roll_number
WHERE (e.subject_one + e.subject_two + e.subject_three) < 100;
