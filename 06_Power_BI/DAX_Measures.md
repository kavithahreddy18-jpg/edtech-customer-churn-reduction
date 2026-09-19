# Power BI DAX Measures

```DAX
Total Customers = DISTINCTCOUNT(Customer360[customer_id])
Churn Rate = DIVIDE(SUM(Customer360[churn_flag]), DISTINCTCOUNT(Customer360[customer_id]))
Retention Rate = 1 - [Churn Rate]
Completion Rate = AVERAGE(Customer360[course_completion_rate])
Average Session Minutes = AVERAGE(Customer360[avg_session_duration_minutes])
ARPU = AVERAGE(Customer360[arpu])
Estimated LTV = AVERAGE(Customer360[estimated_ltv])
At Risk Customers = CALCULATE([Total Customers], Customer360[customer_segment] = "At-Risk")
```
