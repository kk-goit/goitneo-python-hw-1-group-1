from collections import defaultdict
from datetime import datetime

def get_birthdays_per_week(users):
    week_birthdays = defaultdict(list)
    week_days_names = ("Monday","Tuesday","Wednesday","Thursday","Friday")
    cur_year = datetime.today().year
    cur_date = datetime.today().date()
    cur_week_day = cur_date.weekday()
    for user in users:
        birthday = user['birthday'].date().replace(year=cur_year)
        if birthday < cur_date:
            birthday = birthday.replace(year=birthday.year+1)
        delta_days = (birthday - cur_date).days
        if delta_days >= 7:
            continue # birthday to far
        week_day = birthday.weekday()
        if week_day > 4:
            if cur_week_day in [0,6]:
                continue # will be congraduate at next week
            week_day = 0
        week_birthdays[week_days_names[week_day]].append(user['name'])

    for day in week_birthdays.keys():
        print("{}: {}".format(day, ", ".join(week_birthdays[day])))

if __name__ == "__main__":
    # test data
    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
        {"name": "Join Dou", "birthday": datetime(1977, 2, 27)},
        {"name": "Mari Stiu", "birthday": datetime(1734, 3, 2)}
        ]
    
    get_birthdays_per_week(users)
