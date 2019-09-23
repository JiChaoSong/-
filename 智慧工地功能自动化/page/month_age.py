import time
import datetime
import random

def age_month(age):
    """
    月龄换算成时间戳
    :param self:
    :param age: 月龄
    :return: 时间戳
    """
    self_age = age

    day = datetime.timedelta(days=1)

    month = day * 30

    no_1 = datetime.datetime.now()

    no_1 = no_1 - month * self_age

    ans_time = time.mktime(no_1.timetuple())   # 毫秒

    # return ans_time
    dateArray = datetime.datetime.utcfromtimestamp(ans_time)

    otherStyleTime = dateArray.strftime("%Y-%m-%d")

    return otherStyleTime


