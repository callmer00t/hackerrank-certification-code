# MySQL
SELECT ua.id AS user_id, ua.first_name, ua.last_name, 
       c.id AS customer_id, c.customer_name, COUNT(ct.id) AS contact_count
FROM contact ct
JOIN user_account ua ON ct.user_account_id = ua.id
JOIN customer c ON ct.customer_id = c.id
GROUP BY ua.id, ua.first_name, ua.last_name, c.id, c.customer_name
HAVING COUNT(ct.id) > 1
ORDER BY ua.id ASC;
