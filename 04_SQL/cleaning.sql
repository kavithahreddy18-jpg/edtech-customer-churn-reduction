-- Standardize source fields before analysis
WITH cleaned_customers AS (
    SELECT
        TRIM(customer_id) AS customer_id,
        CAST(signup_date AS DATE) AS signup_date,
        age,
        UPPER(TRIM(gender)) AS gender,
        UPPER(TRIM(country)) AS country,
        UPPER(TRIM(acquisition_channel)) AS acquisition_channel,
        UPPER(TRIM(subscription_plan)) AS subscription_plan,
        engagement_score,
        course_completion_rate,
        avg_session_duration_minutes,
        support_ticket_count,
        nps_score,
        churn_flag
    FROM customers
)
SELECT * FROM cleaned_customers;
