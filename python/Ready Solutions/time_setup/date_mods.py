import datetime

a = str(datetime.datetime.today())
r_year = str(a[0]+a[1]+a[2]+a[3])
r_month = str(a[5]+a[6])
r_days = str(a[8]+a[9])
r_hours = str(a[11]+a[12])
r_minutes = str(a[14]+a[15])

r_dat = str(f"{r_year}-{r_month}-{r_days}-{r_hours}-{r_minutes}")
