# 返回位于和[begin, end]的日期列表
def get_date_list(begin, end):
    date_list = []
    date_str = begin
    date_end = end
    date_list.append(begin)
    while date_str < date_end:
        date_1 = datetime.datetime.strptime(date_str,'%Y-%m-%d').strftime('%Y-%m-%d')
        now = datetime.datetime.strptime(date_str,'%Y-%m-%d')
        aDay = datetime.timedelta(days=1)
        now = now + aDay
        date_str = now.strftime('%Y-%m-%d')
        date_list.append(date_str)
    # print date_list
    return date_list
