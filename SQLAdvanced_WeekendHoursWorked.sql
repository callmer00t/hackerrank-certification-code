# MySQL
WITH employee_times AS (
    SELECT 
        emp_id,
        DATE(timestamp) as work_date,
        MIN(timestamp) as login_time,
        MAX(timestamp) as logout_time
    FROM attendance
    GROUP BY emp_id, DATE(timestamp)
)
SELECT 
    emp_id,
    SUM(
        CASE 
            WHEN DAYOFWEEK(work_date) IN (1,7) 
            THEN FLOOR(TIMESTAMPDIFF(HOUR, login_time, logout_time))
            ELSE 0 
        END
    ) as weekend_hours
FROM employee_times
GROUP BY emp_id
ORDER BY weekend_hours DESC;
