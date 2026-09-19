SELECT
    subscription_plan,
    COUNT(*) AS customers,
    SUM(total_revenue) AS revenue,
    AVG(arpu) AS arpu,
    AVG(estimated_ltv) AS estimated_ltv,
    AVG(churn_flag) AS churn_rate
FROM customer_360
GROUP BY subscription_plan
ORDER BY revenue DESC;
