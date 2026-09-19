SELECT
    customer_segment,
    COUNT(*) AS customers,
    AVG(churn_flag) AS churn_rate,
    AVG(engagement_score) AS engagement,
    AVG(course_completion_rate) AS completion_rate,
    AVG(total_revenue) AS avg_revenue,
    AVG(support_tickets) AS avg_support_tickets
FROM customer_360
GROUP BY customer_segment
ORDER BY customers DESC;
