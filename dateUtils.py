from datetime import datetime, timedelta

def date_to_str(date):
    return '{:%Y-%m-%d %H:%M}'.format(date)

def str_to_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M')

def add_hour_to_date(date, h):
    return date + timedelta(hours=h)