WITH 
    date_range AS (
        SELECT 
            toStartOfDay(timestamp) AS day
        FROM 
            default.churn_submits
        GROUP BY 
            day
    ),
    active_users AS (
        SELECT 
            day,
            COUNT(DISTINCT user_id) AS wau
        FROM 
            default.churn_submits
        WHERE 
            timestamp >= day - INTERVAL 6 DAY AND timestamp <= day
        GROUP BY 
            day
    )
SELECT 
    day,
    wau
FROM 
    date_range
LEFT JOIN 
    active_users ON date_range.day = active_users.day
ORDER BY 
    day ASC;