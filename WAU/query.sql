WITH date_range AS (
    SELECT 
        toDate(timestamp) AS day
    FROM 
        default.churn_submits
    GROUP BY 
        day
    ORDER BY 
        day
),

daily_users AS (
    SELECT 
        user_id, 
        arrayJoin(range(7)) AS offset,
        toDate(timestamp) AS activity_day
    FROM 
        default.churn_submits
)

SELECT 
    dr.day,
    COUNT(DISTINCT du.user_id) AS wau
FROM 
    date_range dr
LEFT JOIN 
    daily_users du 
ON 
    dr.day = du.activity_day + INTERVAL du.offset DAY
GROUP BY 
    dr.day
ORDER BY 
    dr.day;
