# e90 -> store name and grade of each student, calculate status, return all
# e91 -> 
from datetime import datetime
from dateutil import relativedelta


bdate = datetime(1990, 4, 1).date()
date2 = datetime(2013, 8, 14).date()
now = datetime.now()

sixty_bday = datetime(bdate.year + 60, bdate.month, bdate.day).date()
remaining = (sixty_bday - date2).days

print(sixty_bday)
print(remaining)