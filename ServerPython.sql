

-- Creating Python apps using Microsoft SQL Server 2002 
-- DEVELOPER EDITION on Windows

CREATE DATABASE SamplePython;
USE SamplePython;

DROP TABLE Employees;

CREATE TABLE Employees
(
  Id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  Name NVARCHAR(50),
  Location NVARCHAR(50)
);

-- query to insert values to table Employees
INSERT INTO Employees
  (Name, Location)
VALUES
  (N'Uchefuna', N'Southend'),
  (N'Dragos', N'London'),
  (N'Grace', N'Leigh'),
  (N'Franc', N'Basildon'),
  (N'Joe', N'Stratford'),
  (N'Malik', N'Luton'),
  (N'Peter', N'Tilbury'),
  (N'Neil', N'Southend'),
  (N'Liz', N'Stratford'),
  (N'Sam', N'Grays');

SELECT *
FROM Employees;