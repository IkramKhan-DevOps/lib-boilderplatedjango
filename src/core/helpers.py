from datetime import datetime

import pytz


def get_current_datetime():
    return datetime.now(pytz.utc)
