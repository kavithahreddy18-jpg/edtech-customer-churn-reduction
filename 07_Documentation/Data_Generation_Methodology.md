# Synthetic Data Generation

This project uses synthetic data because the capstone requirement document does not provide a source dataset.

The generator is designed to create relational EdTech data with shared Customer_ID/Course_ID keys and realistic business relationships. It is the reproducible source for the raw-data layer.

Planned entities:
- customers
- courses
- enrollments
- user_activity
- subscriptions
- payments
- feedback
- support_tickets

The generated data intentionally includes variation and noise rather than deterministic one-to-one rules. Churn-related behaviour is influenced by engagement, completion, support experience, pricing/plan characteristics and customer lifecycle signals.

The repository will document the synthetic nature of the data and will not present it as real company/customer information.
