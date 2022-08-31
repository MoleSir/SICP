create table parents as
    select "delano" as parent, "herber" as child union
    select "abraham"         , "barack"          union
    select "abraham"         , "clintion"        union
    select "fillmore"        , "abraham"         union
    select "fillmore"        , "delano"          union
    select "fillmore"        , "grover"          union
    select "eisenhower"      , "fillmore";

create table lift as 
    select 101 as chair, 2 as single, 2 as couple union
    select 102         , 0          , 3           union
    select 103         , 4          , 1;

create table ints as
    select 'zero' as word, 0 as one, 0 as two, 0 as four, 0 as eight union
    select 'one'         , 1       , 0       , 0        , 0          union
    select 'two'         , 0       , 1       , 0        , 0          union
    select 'three'       , 1       , 1       , 0        , 0          union
    select 'four'        , 0       , 0       , 1        , 0          union
    select 'five'        , 1       , 0       , 1        , 0          union
    select 'siz'         , 0       , 1       , 1        , 0          union
    select 'seven'       , 1       , 1       , 1        , 0          union
    select 'eight'       , 0       , 0       , 0        , 1          union
    select 'nine'        , 1       , 0       , 0        , 1;