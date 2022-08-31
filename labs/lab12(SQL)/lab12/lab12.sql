.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet
  FROM students
  WHERE color = 'blue' AND pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song
  FROM students
  WHERE color = 'blue' AND pet = 'dog';


CREATE TABLE smallest_int AS
  SELECT time, smallest
  FROM students
  WHERE smallest > 2
  ORDER BY smallest
  LIMIT 20;


CREATE TABLE matchmaker AS
  SELECT m.pet, m.song, m.color, w.color
  FROM students as m, students as w
  WHERE m.pet = w.pet AND m.song = w.song AND m.time <> w.time;


CREATE TABLE sevens AS
  SELECT s.seven
  FROM students as s, numbers as n
  WHERE s.time == n.time AND s.number = 7 AND n.'7' = "True";

