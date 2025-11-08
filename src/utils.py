import datetime


def convert_unix_time(date):
    datetime_obj = datetime.datetime.combine(date, datetime.datetime.min.time())
    return int(datetime_obj.timestamp())
