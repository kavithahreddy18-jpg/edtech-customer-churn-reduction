SELECT
    customer_segment,
    COUNT(*) AS customers,
    AVG(engagement_score) AS avg_engagement,
    AVG(course_completion_rate) AS avg_completion_rate,
    AVG(avg_session_duration_minutes) AS avg_session_minutes,
    AVG(nps_score) AS avg_nps,
    AVG(churn_flag) AS churn_rate
FROM customer_360
GROUP BY customer_segment
ORDER BY churn_rate DESC;
