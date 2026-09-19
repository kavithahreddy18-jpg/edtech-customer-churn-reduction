# EdTech Churn Synthetic Data Generator — portfolio source pipeline
# NOTE: the repository also contains a processed customer_360 table and analytical artifacts.
# Generates the relational source data used by the portfolio.
# Run: python generate_data.py
#
# The data is synthetic and intentionally documented as such.

import os
import numpy as np
import pandas as pd

SEED = 42
rng = np.random.default_rng(SEED)
OUT = os.path.join(os.path.dirname(__file__), "..", "02_Data", "raw")
os.makedirs(OUT, exist_ok=True)

N_CUSTOMERS = 25000
N_COURSES = 120
START = pd.Timestamp("2024-01-01")
END = pd.Timestamp("2025-12-31")

def dates(n):
    days = (END - START).days
    return START + pd.to_timedelta(rng.integers(0, days + 1, n), unit="D")

# Courses
course_levels = ["Beginner", "Intermediate", "Advanced"]
course_categories = ["Data Analytics", "Programming", "Cloud", "Business", "AI/ML", "Test Prep", "K-12"]
courses = pd.DataFrame({
    "course_id": [f"C{i:04d}" for i in range(1, N_COURSES + 1)],
    "course_name": [f"{c} Course {i:03d}" for i, c in enumerate(rng.choice(course_categories, N_COURSES), 1)],
    "category": rng.choice(course_categories, N_COURSES),
    "difficulty": rng.choice(course_levels, N_COURSES, p=[.4,.4,.2]),
    "price": rng.choice([49,79,99,129,159,199,249], N_COURSES)
})
courses.to_csv(os.path.join(OUT, "courses.csv"), index=False)

# Customers
signup = dates(N_CUSTOMERS)
customers = pd.DataFrame({
    "customer_id": [f"CU{i:06d}" for i in range(1, N_CUSTOMERS + 1)],
    "signup_date": signup,
    "age": rng.integers(16, 61, N_CUSTOMERS),
    "gender": rng.choice(["Female","Male","Non-binary","Prefer not to say"], N_CUSTOMERS, p=[.45,.45,.03,.07]),
    "country": rng.choice(["India","United States","United Kingdom","Canada","Australia","Singapore"], N_CUSTOMERS, p=[.45,.22,.12,.08,.08,.05]),
    "acquisition_channel": rng.choice(["Organic Search","Paid Search","Social","Referral","Email","Partner"], N_CUSTOMERS),
    "device_type": rng.choice(["Mobile","Desktop","Tablet"], N_CUSTOMERS, p=[.55,.35,.10])
})
customers.to_csv(os.path.join(OUT, "customers.csv"), index=False)

# Enrollments: 1-4 per customer
counts = rng.choice([1,2,3,4], N_CUSTOMERS, p=[.42,.32,.18,.08])
customer_ids = np.repeat(customers.customer_id.values, counts)
enroll = pd.DataFrame({
    "enrollment_id": [f"EN{i:07d}" for i in range(1, len(customer_ids)+1)],
    "customer_id": customer_ids,
    "course_id": rng.choice(courses.course_id.values, len(customer_ids)),
    "enrollment_date": dates(len(customer_ids)),
})
# Make completion related to engagement propensity
completion = np.clip(rng.normal(58, 27, len(enroll)), 0, 100)
enroll["completion_rate_pct"] = np.round(completion, 1)
enroll["completed_flag"] = (enroll.completion_rate_pct >= 85).astype(int)
enroll.to_csv(os.path.join(OUT, "enrollments.csv"), index=False)

# Activity: 8-20 events per customer on average, with engagement heterogeneity
events_per = rng.poisson(10, N_CUSTOMERS) + 1
activity_customer = np.repeat(customers.customer_id.values, events_per)
activity = pd.DataFrame({
    "activity_id": [f"AC{i:08d}" for i in range(1, len(activity_customer)+1)],
    "customer_id": activity_customer,
    "activity_date": dates(len(activity_customer)),
    "session_duration_minutes": np.round(np.clip(rng.gamma(2.2, 22, len(activity_customer)), 2, 240), 1),
    "pages_viewed": rng.integers(1, 30, len(activity_customer)),
    "content_interactions": rng.integers(0, 15, len(activity_customer))
})
activity.to_csv(os.path.join(OUT, "user_activity.csv"), index=False)

# Subscriptions and payments
plan = rng.choice(["Free","Basic","Standard","Premium"], N_CUSTOMERS, p=[.20,.28,.34,.18])
monthly_price = pd.Series(plan).map({"Free":0,"Basic":49,"Standard":89,"Premium":149}).values
sub_start = customers.signup_date.values
renewal = rng.random(N_CUSTOMERS) < np.clip(.35 + (monthly_price/300), .25, .88)
cancelled = ~renewal
subscriptions = pd.DataFrame({
    "subscription_id": [f"SUB{i:07d}" for i in range(1,N_CUSTOMERS+1)],
    "customer_id": customers.customer_id,
    "subscription_plan": plan,
    "monthly_price": monthly_price,
    "subscription_start": sub_start,
    "renewal_flag": renewal.astype(int),
    "cancelled_flag": cancelled.astype(int)
})
subscriptions.to_csv(os.path.join(OUT, "subscriptions.csv"), index=False)

payments = subscriptions.loc[subscriptions.monthly_price > 0, ["subscription_id","customer_id"]].copy()
payments["payment_id"] = [f"PAY{i:08d}" for i in range(1,len(payments)+1)]
payments["payment_date"] = dates(len(payments))
payments["amount"] = payments.subscription_id.map(subscriptions.set_index("subscription_id").monthly_price)
payments["refund_flag"] = (rng.random(len(payments)) < .035).astype(int)
payments.to_csv(os.path.join(OUT, "payments.csv"), index=False)

# Feedback and support
feedback_n = int(N_CUSTOMERS * .62)
fb_ids = rng.choice(customers.customer_id.values, feedback_n, replace=False)
feedback = pd.DataFrame({
    "feedback_id": [f"FB{i:07d}" for i in range(1,feedback_n+1)],
    "customer_id": fb_ids,
    "feedback_date": dates(feedback_n),
    "nps_score": rng.integers(0,11,feedback_n),
    "rating": rng.integers(1,6,feedback_n),
    "feedback_channel": rng.choice(["In-app","Email","Survey","Review"], feedback_n)
})
feedback.to_csv(os.path.join(OUT, "feedback.csv"), index=False)

ticket_n = int(N_CUSTOMERS * .8)
tk_ids = rng.choice(customers.customer_id.values, ticket_n, replace=True)
tickets = pd.DataFrame({
    "ticket_id": [f"TK{i:07d}" for i in range(1,ticket_n+1)],
    "customer_id": tk_ids,
    "ticket_date": dates(ticket_n),
    "issue_type": rng.choice(["Content","Billing","Technical","Access","Course Difficulty","Other"], ticket_n),
    "resolution_hours": np.round(np.clip(rng.gamma(2.0, 10, ticket_n), .5, 240), 1),
    "resolved_flag": (rng.random(ticket_n) < .94).astype(int)
})
tickets.to_csv(os.path.join(OUT, "support_tickets.csv"), index=False)

print("Synthetic relational EdTech dataset generated in 02_Data/raw")
