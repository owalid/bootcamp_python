t = (3,30,2019,9,25)

year = t[2]
month_day = (t[3:])[::-1]
time = t[:2]
print(str(year) + "/" + "/".join((map(str, month_day))) + " " + ":".join((map(str, time))))
