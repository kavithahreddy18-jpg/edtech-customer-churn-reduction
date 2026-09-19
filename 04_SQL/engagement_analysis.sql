SELECT
    CASE
        WHEN engagement_score < 30 THEN 'Low'
        WHEN engagement_score < 60 THEN 'Medium'
        ELSE 'High'
    END AS engagement_band,
    COUNT(*) AS customers,
    AVG(churn_flag) AS churn_rate,
    AVG(course_completion_rate) AS completion_rate,
    AVG(avg_session_duration_minutes) AS avg_session_duration
FROM customer_360
GROUP BY
    CASE
        WHEN engagement_score < 30 THEN 'Low'
        WHEN engagement_score < 60 THEN 'Medium'
        ELSE 'High'
    END
ORDER BY churn_rate DESC;
