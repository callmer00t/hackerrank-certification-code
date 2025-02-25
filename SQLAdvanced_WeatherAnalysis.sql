# MySQL
SELECT 
    MONTH(STR_TO_DATE(record_date, '%Y-%m-%d')) as month,
    MAX(CASE WHEN data_type = 'max' THEN data_value END) as monthly_max,
    MIN(CASE WHEN data_type = 'min' THEN data_value END) as monthly_min,
    ROUND(AVG(CASE WHEN data_type = 'avg' THEN data_value END)) as monthly_avg
FROM temperature_records 
WHERE record_date >= '2020-07-01' 
AND record_date <= '2020-12-31'
GROUP BY MONTH(STR_TO_DATE(record_date, '%Y-%m-%d'))
ORDER BY month;
