import datetime


def get_current_unix_time():
    return int(datetime.datetime.now().timestamp())


def convert_unix_time(date):
    datetime_obj = datetime.datetime.combine(date, datetime.datetime.min.time())
    return int(datetime_obj.timestamp())


def convert_datetime(unix_time):
    return datetime.datetime.fromtimestamp(unix_time).strftime("%d-%m-%Y")
