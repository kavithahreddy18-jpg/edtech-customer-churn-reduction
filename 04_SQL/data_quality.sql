-- Data quality checks for the EdTech churn project
SELECT COUNT(*) AS customer_count FROM customers;
SELECT COUNT(*) AS enrollment_count FROM enrollments;
SELECT COUNT(*) AS activity_count FROM user_activity;
SELECT COUNT(*) AS payment_count FROM payments;
SELECT COUNT(*) AS feedback_count FROM feedback;
SELECT COUNT(*) AS support_ticket_count FROM support_tickets;

SELECT customer_id, COUNT(*) AS row_count
FROM customers GROUP BY customer_id HAVING COUNT(*) > 1;

SELECT COUNT(*) AS null_customer_ids FROM customers WHERE customer_id IS NULL;
SELECT COUNT(*) AS orphan_enrollments
FROM enrollments e LEFT JOIN customers c ON e.customer_id=c.customer_id
WHERE c.customer_id IS NULL;
