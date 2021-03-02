import psycopg2
import datapane as dp
import altair as alt
import pandas as pd

conn = psycopg2.connect(database="database_name", user = "user_name", password = "password", host = "ip_address", port = "5432")
sql_str = '''select "RACE", "TRANSFUSION_INSTANCE" FROM public."platelet_UC" limit 200'''

dat = pd.read_sql_query(sql_str, conn)
conn = None

print ("Opened database successfully")




print (dat)

chart = alt.Chart(dat).mark_point().encode(
  x='RACE',
  y='TRANSFUSION_INSTANCE'
).interactive()

r = dp.Report(dp.DataTable(dat), dp.Plot(chart))
r.save(path='report_2.html', open=True)
