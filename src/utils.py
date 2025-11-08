import datetime


def convert_unix_time(date):
    datetime_obj = datetime.datetime.combine(date, datetime.datetime.min.time())
    return int(datetime_obj.timestamp())


def convert_datetime(unix_time):
    return datetime.datetime.fromtimestamp(unix_time).strftime("%d-%m-%Y")
