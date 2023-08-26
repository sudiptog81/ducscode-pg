-- database definition

DROP DATABASE IF EXISTS university;

CREATE DATABASE university;
USE university;

DROP TABLE IF EXISTS department, course, section, student, instructor, takes, teaches;

CREATE TABLE department
(
    dept_name VARCHAR(255),
    building  VARCHAR(255),
    budget    NUMERIC(10, 2),
    PRIMARY KEY (dept_name)
);

CREATE TABLE student
(
    ID         INTEGER,
    name       VARCHAR(255),
    dept_name  VARCHAR(255),
    total_cred NUMERIC(3, 0) DEFAULT 0,
    PRIMARY KEY (ID),
    CHECK (total_cred >= 0),
    FOREIGN KEY (dept_name) REFERENCES department
);

CREATE TABLE instructor
(
    ID        INTEGER,
    name      VARCHAR(255),
    dept_name VARCHAR(255),
    salary    NUMERIC(8, 2),
    PRIMARY KEY (ID),
    FOREIGN KEY (dept_name) REFERENCES department
);

CREATE TABLE course
(
    course_id VARCHAR(255),
    title     VARCHAR(255),
    dept_name VARCHAR(255),
    credits   NUMERIC(3, 0),
    PRIMARY KEY (course_id),
    FOREIGN KEY (dept_name) REFERENCES department
);

CREATE TABLE section
(
    sec_id       VARCHAR(20),
    semester     VARCHAR(255),
    YEAR         INTEGER,
    course_id    VARCHAR(255),
    building     VARCHAR(255),
    room_number  VARCHAR(255),
    time_slot_id VARCHAR(255),
    PRIMARY KEY (course_id, sec_id, semester, YEAR)
);

CREATE TABLE takes
(
    ID        INTEGER,
    course_id VARCHAR(255),
    sec_id    VARCHAR(20),
    semester  VARCHAR(255),
    YEAR      INTEGER,
    grade     NUMERIC(3, 2),
    PRIMARY KEY (ID, course_id, sec_id, semester, YEAR),
    CHECK (grade >= 0 AND grade <= 10),
    FOREIGN KEY (ID) REFERENCES student,
    FOREIGN KEY (course_id, sec_id, semester, year) REFERENCES section
);

CREATE TABLE teaches
(
    ID        INTEGER,
    course_id VARCHAR(255),
    sec_id    VARCHAR(20),
    semester  VARCHAR(255),
    YEAR      INTEGER,
    PRIMARY KEY (ID, course_id, sec_id, semester, YEAR),
    FOREIGN KEY (ID) REFERENCES instructor,
    FOREIGN KEY (course_id, sec_id, semester, YEAR) REFERENCES section
);


CREATE TABLE advisor
(
    s_id INTEGER,
    i_id INTEGER,
    PRIMARY KEY (s_id, i_id),
    FOREIGN KEY (s_id) REFERENCES student (ID),
    FOREIGN KEY (i_id) REFERENCES instructor (ID)
);

-- trigger for insert
#
# DELIMITER //
# DROP TRIGGER IF EXISTS insert_grades;
# CREATE TRIGGER insert_grades
#     AFTER INSERT
#     ON takes
#     FOR EACH ROW
# BEGIN
#     DECLARE new_credits INTEGER UNSIGNED DEFAULT 0;
#     SELECT credits
#     INTO new_credits
#     FROM course
#     WHERE course.course_id = NEW.course_id;
#     CASE
#         WHEN NEW.grade IS NOT NULL THEN BEGIN
#             UPDATE student
#             SET total_cred = total_cred
#                 + ROUND(new_credits * (grade / 10))
#             WHERE ID = NEW.ID;
#         END;
#         ELSE BEGIN
#         END;
#         END CASE;
# END //
# DELIMITER ;
#
# -- trigger for update
#
# DELIMITER //
# DROP TRIGGER IF EXISTS update_grades;
# CREATE TRIGGER update_grades
#     BEFORE UPDATE
#     ON takes
#     FOR EACH ROW
# BEGIN
#     DECLARE old_credits INTEGER UNSIGNED DEFAULT 0;
#     DECLARE new_credits INTEGER UNSIGNED DEFAULT 0;
#
#     CASE
#         WHEN NEW.course_id <> OLD.course_id THEN BEGIN
#             SELECT credits
#             INTO old_credits
#             FROM course
#             WHERE course.course_id = OLD.course_id;
#
#             SELECT credits
#             INTO new_credits
#             FROM course
#             WHERE course.course_id = NEW.course_id;
#         END;
#         ELSE SELECT credits, credits
#              INTO new_credits, old_credits
#              FROM course
#              WHERE course.course_id = NEW.course_id;
#         END CASE;
#
#     CASE
#         WHEN OLD.grade IS NOT NULL AND NEW.grade IS NULL
#             THEN UPDATE student
#                  SET total_cred = total_cred
#                      - ROUND(old_credits * (OLD.grade / 10))
#                  WHERE ID = NEW.ID;
#         WHEN OLD.grade IS NOT NULL AND NEW.grade IS NOT NULL
#             THEN UPDATE student
#                  SET total_cred = total_cred
#                                       - ROUND(old_credits * (OLD.grade / 10))
#                      + ROUND(new_credits * (NEW.grade / 10))
#                  WHERE ID = NEW.ID;
#         WHEN OLD.grade IS NULL AND NEW.grade IS NOT NULL
#             THEN UPDATE student
#                  SET total_cred = total_cred
#                      + ROUND(new_credits * (NEW.grade / 10))
#                  WHERE ID = NEW.ID;
#         ELSE BEGIN
#         END;
#         END CASE;
# END //
# DELIMITER ;

DELIMITER //
DROP TRIGGER IF EXISTS update_grades;
CREATE TRIGGER update_grades
    AFTER UPDATE
    ON student
    FOR EACH ROW
BEGIN
    DECLARE course_credits INTEGER DEFAULT 0;
    DECLARE grade_numeric NUMERIC(3, 2) DEFAULT 0;

    SELECT credits
    INTO course_credits
    FROM student
             NATURAL JOIN takes
             NATURAL JOIN course
    WHERE ID = NEW.ID;

    SET grade_numeric = (NEW.total_cred / course_credits) * 10;

    UPDATE takes
    SET grade = grade_numeric
    WHERE takes.ID = NEW.ID;
END //
DELIMITER ;


-- database population

USE university;

INSERT INTO department
VALUES ("Computer Science", "LT-1", 10000000),
       ("Mathematics", "LT-2", 40000000),
       ("Statistics", "LT-1", 9000000),
       ("Literature", "LT-3", 50000000),
       ("Botany", "LT-4", 20000000);

INSERT INTO student(ID, name, dept_name)
VALUES (1, "Aditya", "Computer Science"),
       (2, "Akanksha", "Mathematics"),
       (3, "Akshita", "Computer Science"),
       (4, "anjali", "Statistics"),
       (5, "Devanshu", "Mathematics"),
       (6, "Divyanshu", "Literature"),
       (7, "Harshit", "Botany"),
       (8, "Jagriti", "Computer Science"),
       (9, "Tanuja", "Mathematics"),
       (10, "Stuti", "Statistics"),
       (11, "Ashish", "Literature"),
       (12, "Akash", "Computer Science"),
       (13, "Abhinav", "Computer Science"),
       (14, "Sudeepto", "Computer Science"),
       (15, "Kinshuk", "Computer Science"),
       (16, "Aviral", "Literature"),
       (17, "Apurva", "Botany"),
       (18, "Sunil", "Statistics"),
       (19, "Shubham", "Botany"),
       (20, "Vallabh", "Mathematics"),
       (21, "Gagan", "Computer Science"),
       (22, "Adarsh", "Statistics"),
       (23, "Neha", "Statistics"),
       (24, "Stuti", "Computer Science"),
       (25, "Adamya", "Computer Science"),
       (26, "Abhishek", "Literature"),
       (27, "Divya", "Literature"),
       (28, "Rohan", "Botany"),
       (29, "Rahul", "Botany"),
       (30, "Rishabh", "Mathematics");


INSERT INTO course
VALUES ("BSB", "BS Botany", "Botany", 300),
       ("MS", "MSc Computer Science", "Computer Science", 140),
       ("MTech", "MTech CS", "Computer Science", 150),
       ("MA", "MA English", "Literature", 120),
       ("BSc", "BSc Mathematics", "Mathematics", 260),
       ("BS", "BS Statistics", "Statistics", 300);


INSERT INTO instructor
VALUES (1, "Vikas", "Computer Science", 100000),
       (2, "Bharti", "Computer Science", 100000),
       (3, "Vasudha", "Computer Science", 200000),
       (4, "Mukesh", "Mathematics", 100000),
       (5, "Awadesh", "Mathematics", 200000),
       (6, "Naveen", "Mathematics", 200000),
       (7, "Akhilesh", "Statistics", 80000),
       (8, "Poonam", "Statistics", 80000),
       (9, "Manisha", "Literature", 100000),
       (10, "Geeta", "Literature", 200000),
       (11, "Jitendra", "Literature", 100000),
       (12, "Madhoolika", "Botany", 200000),
       (13, "Kuldeep", "Botany", 100000);

INSERT INTO section(course_id, sec_id, semester, YEAR, building, room_number, time_slot_id)
VALUES ("BS", "A", 1, 1, "LT-1", "LT-1A", "09 AM-11 AM"),
       ("BS", "A", 2, 1, "LT-1", "LT-1A", "11 AM-01 PM"),
       ("BS", "B", 3, 2, "LT-1", "LT-1A", "01 PM-03 PM"),
       ("BS", "B", 4, 2, "LT-1", "LT-1A", "03 PM-05 PM"),
       ("BS", "C", 5, 3, "LT-1", "LT-1B", "09 AM-01 PM"),
       ("BS", "C", 6, 3, "LT-1", "LT-1B", "01 PM-05 PM"),
       ("BSB", "A", 1, 1, "LT-4", "LT-4A", "09 AM-11 AM"),
       ("BSB", "A", 2, 1, "LT-4", "LT-4A", "11 AM-01 PM"),
       ("BSB", "B", 3, 2, "LT-4", "LT-4A", "01 PM-03 PM"),
       ("BSB", "B", 4, 2, "LT-4", "LT-4A", "03 PM-05 PM"),
       ("BSB", "C", 5, 3, "LT-4", "LT-4B", "09 AM-01 PM"),
       ("BSB", "C", 6, 3, "LT-4", "LT-4B", "01 PM-05 PM"),
       ("BSc", "A", 1, 1, "LT-2", "LT-2A", "09 AM-11 AM"),
       ("BSc", "A", 2, 1, "LT-2", "LT-2A", "11 AM-01 PM"),
       ("BSc", "B", 3, 2, "LT-2", "LT-2A", "01 PM-03 PM"),
       ("BSc", "B", 4, 2, "LT-2", "LT-2A", "03 PM-05 PM"),
       ("BSc", "C", 5, 3, "LT-2", "LT-2B", "09 AM-01 PM"),
       ("BSc", "C", 6, 3, "LT-2", "LT-2B", "01 PM-05 PM"),
       ("MA", "A", 1, 1, "LT-3", "LT-3A", "09 AM-01 PM"),
       ("MA", "A", 2, 1, "LT-3", "LT-3A", "01 PM-05 PM"),
       ("MA", "B", 3, 2, "LT-3", "LT-3B", "09 AM-01 PM"),
       ("MA", "B", 4, 2, "LT-3", "LT-3B", "01 PM-05 PM"),
       ("MS", "A", 1, 1, "LT-1", "LT-1C", "09 AM-01 PM"),
       ("MS", "A", 2, 1, "LT-1", "LT-1C", "01 PM-05 PM"),
       ("MS", "B", 3, 2, "LT-1", "LT-1D", "09 AM-01 PM"),
       ("MS", "B", 4, 2, "LT-1", "LT-1D", "01 PM-05 PM"),
       ("MTech", "A", 1, 1, "LT-1", "LT-1E", "09 AM-01 PM"),
       ("MTech", "A", 2, 1, "LT-1", "LT-1E", "01 PM-05 PM"),
       ("MTech", "B", 3, 2, "LT-1", "LT-1F", "09 AM-01 PM"),
       ("MTech", "B", 4, 2, "LT-1", "LT-1F", "01 PM-05 PM");


INSERT INTO takes(ID, course_ID, sec_ID, semester, YEAR)
VALUES (1, "MS", "A", 1, 1),
       (2, "BSc", "A", 1, 1),
       (3, "MS", "B", 3, 2),
       (4, "BS", "A", 2, 1),
       (5, "BSc", "B", 3, 2),
       (6, "MA", "A", 1, 1),
       (7, "BSB", "A", 2, 1),
       (8, "MTech", "A", 1, 1),
       (9, "BSc", "A", 2, 1),
       (10, "BS", "B", 4, 2),
       (11, "MA", "A", 1, 1),
       (12, "MS", "B", 3, 2),
       (13, "MS", "A", 1, 1),
       (14, "MTEch", "B", 4, 2),
       (15, "MTech", "B", 4, 2),
       (16, "MA", "A", 2, 1),
       (17, "BSB", "A", 2, 1),
       (18, "BS", "C", 6, 3),
       (19, "BSB", "B", 4, 2),
       (20, "BSc", "C", 5, 3),
       (21, "MS", "B", 4, 2),
       (22, "BS", "C", 5, 3),
       (23, "BS", "C", 6, 3),
       (24, "MS", "B", 4, 2),
       (25, "MTech", "A", 2, 1),
       (26, "MA", "B", 3, 2),
       (27, "MA", "A", 1, 1),
       (28, "BSB", "C", 5, 3),
       (29, "BSB", "B", 3, 2),
       (30, "BSc", "C", 5, 3);

INSERT INTO teaches
VALUES (1, "MS", "A", 1, 1),
       (1, "MTech", "B", 3, 2),
       (1, "MTech", "B", 4, 2),
       (2, "MS", "B", 3, 2),
       (2, "MS", "A", 2, 1),
       (2, "MS", "B", 4, 2),
       (3, "MTech", "A", 2, 1),
       (3, "MS", "A", 2, 1),
       (3, "MS", "B", 3, 2),
       (3, "MTech", "A", 1, 1),
       (4, "BSc", "A", 1, 1),
       (5, "BSc", "A", 2, 1),
       (6, "BSc", "A", 1, 1),
       (4, "BSc", "B", 3, 2),
       (5, "BSc", "B", 3, 2),
       (6, "BSc", "B", 4, 2),
       (4, "BSc", "C", 5, 3),
       (5, "BSc", "C", 5, 3),
       (6, "BSc", "C", 6, 3),
       (6, "BSc", "C", 5, 3),
       (7, "BS", "A", 1, 1),
       (8, "BS", "A", 2, 1),
       (7, "BS", "B", 3, 2),
       (8, "BS", "B", 4, 2),
       (7, "BS", "C", 5, 3),
       (8, "BS", "C", 6, 3),
       (9, "MA", "A", 1, 1),
       (9, "MA", "B", 3, 2),
       (9, "MA", "A", 2, 1),
       (10, "MA", "B", 3, 2),
       (11, "MA", "B", 4, 2),
       (12, "BSB", "A", 1, 1),
       (12, "BSB", "C", 5, 3),
       (12, "BSB", "B", 3, 2),
       (12, "BSB", "A", 2, 1),
       (13, "BSB", "B", 4, 2),
       (13, "BSB", "A", 2, 1),
       (13, "BSB", "C", 5, 3),
       (13, "BSB", "C", 6, 3);


INSERT INTO advisor
VALUES (1, 1),
       (2, 4),
       (3, 2),
       (4, 7),
       (5, 6),
       (6, 11),
       (7, 12),
       (8, 2),
       (9, 4),
       (10, 7),
       (11, 11),
       (12, 3),
       (13, 3),
       (14, 2),
       (15, 1),
       (16, 9),
       (17, 13),
       (18, 8),
       (19, 13),
       (20, 6),
       (21, 1),
       (22, 7),
       (23, 7),
       (24, 2),
       (25, 2),
       (26, 10),
       (27, 9),
       (28, 13),
       (29, 12),
       (30, 5);

