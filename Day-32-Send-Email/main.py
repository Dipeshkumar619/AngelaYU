# import smtplib
# myemail="dipeshkumar.gupta@hcl.com"
# with smtplib.SMTP(host="smtp.office365.com") as connection:
#     connection.starttls()
#     connection.login(user=myemail,password="Shambhu@789")
#     connection.sendmail(to_addrs=myemail,from_addr=myemail,msg="Hello Mail via Python")

import datetime as dt
import random

now=dt.datetime.now()
weekday=now.weekday()
if weekday==4:
    with open(file="quote.txt") as file:
        all_quote=file.readlines()
        quote=random.choice(all_quote)
    print(quote)