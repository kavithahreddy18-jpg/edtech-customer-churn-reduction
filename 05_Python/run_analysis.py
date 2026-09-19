from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "02_Data"

customers = pd.read_csv(DATA / "raw/customers.csv")
customer_360 = pd.read_csv(DATA / "processed/customer_360.csv")

print("Customers:", len(customers))
print("Customer 360 rows:", len(customer_360))
print("Churn rate:", customer_360["churn_flag"].mean())

features = ["engagement_score","course_completion_rate","avg_session_duration_minutes","support_ticket_count","nps_score","total_sessions","courses_enrolled","total_revenue"]
X = customer_360[features].fillna(0)
y = customer_360["churn_flag"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=42,stratify=y)
model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
proba=model.predict_proba(X_test)[:,1]
print("ROC-AUC:", roc_auc_score(y_test,proba))
print(classification_report(y_test, model.predict(X_test)))
