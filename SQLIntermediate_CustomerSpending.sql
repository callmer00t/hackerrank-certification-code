# MySQL
WITH avg_spending AS (
    SELECT AVG(total_price) as avg_amount
    FROM invoice
)
SELECT 
    c.customer_name,
    FORMAT(SUM(i.total_price), 6) as amount_spent
FROM customer c
JOIN invoice i ON c.id = i.customer_id
GROUP BY c.id, c.customer_name
HAVING SUM(i.total_price) <= (SELECT avg_amount * 0.25 FROM avg_spending)
ORDER BY SUM(i.total_price) DESC;
