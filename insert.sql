SELECT E.*, D.DepartmentName
FROM Employees E
INNER JOIN Departments D
ON E.Department = D.DepartmentID;
