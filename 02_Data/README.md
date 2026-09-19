# Dataset

The repository contains the **actual synthetic dataset tables**, stored as compressed CSV files (`.csv.gz`) so the full 25,000-customer dataset can be versioned in GitHub.

## Raw tables

- `customers.csv.gz` — 25,000 customers
- `courses.csv.gz` — 120 courses
- `enrollments.csv.gz` — 47,850 enrollments
- `user_activity.csv.gz` — 299,374 activity records
- `subscriptions.csv.gz` — 25,000 subscriptions
- `payments.csv.gz` — 99,596 payments
- `feedback.csv.gz` — 15,500 feedback records
- `support_tickets.csv.gz` — 20,000 support tickets

Processed:

- `customer_360.csv.gz`

## How to use

1. Open `02_Data/raw` on GitHub.
2. Download the required `.csv.gz` file.
3. Extract it with 7-Zip/WinRAR, or run:

```bash
python 02_Data/extract_dataset.py
```

The extracted files are normal CSV files and can be loaded into Excel, SQL, Python or Power BI.

## Data note

All data is **synthetic** and was generated specifically for this portfolio project. It is not real customer/company data.
