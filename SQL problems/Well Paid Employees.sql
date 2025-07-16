-- link to problem: https://datalemur.com/questions/sql-well-paid-employees

SELECT emp.employee_id, emp.name AS employee_name FROM employee mgr 
INNER JOIN employee emp
  ON mgr.employee_id = emp.manager_id
WHERE emp.salary > mgr.salary
