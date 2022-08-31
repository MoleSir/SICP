create table parents as
    select "delano" as parent, "herber" as child union
    select "abraham"         , "barack"          union
    select "abraham"         , "clintion"        union
    select "fillmore"        , "abraham"         union
    select "fillmore"        , "delano"          union
    select "fillmore"        , "grover"          union
    select "eisenhower"      , "fillmore";

CREATE TABLE dogs AS
    SELECT "abraham" AS name, "long" AS fur UNION
    SELECT "barack"         , "short"       UNION
    SELECT "clintion"       , "long"        UNION
    SELECT "delano"         , "long"        UNION
    SELECT "eisenhower"     , "short"       UNION
    SELECT "fillmore"       , "curly"       UNION
    SELECT "grover"         , "short"       UNION
    SELECT "herber"         , "curly";

-- Grand
CREATE TABLE grandparents AS
    SELECT  
        p.parent AS grandog,
        s.child AS granpup
    FROM parents as s
    JOIN parents as p
        ON s.parent = p.child;

-- string expressions
