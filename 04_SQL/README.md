# SQL Layer

The SQL scripts are intentionally separated by purpose:

- `data_quality.sql` — record counts, duplicates and referential checks.
- `cleaning.sql` — field standardization.
- `customer_analysis.sql` — segment-level churn and engagement.
- `engagement_analysis.sql` — engagement bands versus churn.
- `revenue_analysis.sql` — plan, revenue, ARPU and LTV.
- `segmentation.sql` — decision table for customer segments.

The scripts assume the CSV tables have been imported into a SQL environment with the same table names. They are written as standard SQL and may need small date/type syntax adjustments for a specific engine such as SQL Server, PostgreSQL or MySQL.
