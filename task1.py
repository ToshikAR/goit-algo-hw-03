# task1
# розрахує кількість днів між заданою датою і поточною датою 

from datetime import datetime


def get_days_from_today(date):
    try:
        obj_date = datetime.strptime(date, "%Y-%m-%d")
        obj_date_now = datetime.today()
        obj_date_diff = obj_date_now - obj_date
        return obj_date_diff.days
    except ValueError:
        return "Enter date in 'YYYY-MM-DD' format."

print(get_days_from_today("2020-10-09"))