SELECT e.*, d.name AS department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;