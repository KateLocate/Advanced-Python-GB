from datetime import datetime


def get_upper_text(data):
    return data.upper()


def get_lower_text(data):
    return data.lower()


def get_time(data):
    date = datetime.now()
    return date.strftime('%d-%m-%yT%H:%M:%S')
