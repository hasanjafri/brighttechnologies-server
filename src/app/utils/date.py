import datetime

DEFAULT_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

def format_datetime_object(datetime_object, date_format=DEFAULT_DATE_FORMAT):
    """ Returns the string representation of a datetime object in the format
    specified. Default used if no format specified. """
    
    return datetime_object.strftime(date_format) if datetime_object else ''