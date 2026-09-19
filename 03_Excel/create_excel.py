from pathlib import Path
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'02_Data/processed/customer_360.csv')
out=ROOT/'03_Excel/EdTech_Customer_Churn_Analysis.xlsx'
wb=Workbook()
ws=wb.active; ws.title='KPI Dashboard'
kpis=[
('Total Customers','=COUNTA(\'Customer 360\'!A2:A25001)'),
('Churn Rate','=AVERAGE(\'Customer 360\'!M2:M25001)'),
('Retention Rate','=1-B3'),
('Completion Rate','=AVERAGE(\'Customer 360\'!I2:I25001)'),
('Avg Session Minutes','=AVERAGE(\'Customer 360\'!J2:J25001)'),
('ARPU','=AVERAGE(\'Customer 360\'!Z2:Z25001)'),
('Estimated LTV','=AVERAGE(\'Customer 360\'!AA2:AA25001)')]
for r,(k,v) in enumerate(kpis,1): ws.cell(r,1,k); ws.cell(r,2,v)
ws['A1'].font=Font(bold=True)
seg=wb.create_sheet('Segment Analysis')
seg.append(['Customer Segment','Customers','Churn Rate','Avg Engagement','Completion Rate','Avg Revenue'])
for name,g in df.groupby('customer_segment'):
    seg.append([name,len(g),float(g.churn_flag.mean()),float(g.engagement_score.mean()),float(g.course_completion_rate.mean()),float(g.total_revenue.mean())])
raw=wb.create_sheet('Customer 360')
for c,h in enumerate(df.columns,1): raw.cell(1,c,h)
for row in df.itertuples(index=False):
    raw.append(list(row))
for sheet in wb.worksheets:
    sheet.freeze_panes='A2'
    for cell in sheet[1]: cell.font=Font(bold=True)
wb.save(out)
print(out)
