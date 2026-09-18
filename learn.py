from datetime import date, time, datetime,timedelta,timezone

date(2026,9,18)
time(14,30)
datetime(2026,9,18,14,30)
timedelta(days=3,hours=2)
print(datetime.now(timezone.utc))