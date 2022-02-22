# * ******************************************************************************
# * Author: xborner
# * Email: xbornerw@gmail.com
# * Last modified: 2022-02-19 14:15
# * Filename: bulk_del_cal_events.py
# * Version: 1.0.4
# * Description: 批量删除谷歌日历活动
# * *****************************************************************************
import re
import datetime


def get_ics_file(file_name):
    # 将导出的 ics 文件内容赋值给变量
    # 输入文本名称，返回文本内容
    with open(file_name, 'rt', encoding='utf-8') as f:
        s1 = f.read()
        return s1


def deal_with_var(date, str1):
    # 处理文本，输入日期删除对应的日历活动
    # 输入日期、包含日历活动的变量，返回删除对应活动后新的字符串
    end_vevent = '\n(.*\n)+?END:VEVENT'
    re1 = 'BEGIN:.*\nDTSTART.*?' + date + end_vevent
    str2 = re.sub(re1, '', str1)
    return str2


def save_file(str1, file_name):
    # 将变量内容重新保存到文本中
    # 输入变量、新的文本名称，无返回值
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(str1)
    print("新的 ics 文件保存成功")


def get_dates(start_date, end_date):
    # 返回时间段内的所有日期
    # 输入开始日期、结束日期（例：'20220126', '20220325'），返回时间列表（例：['20220126', '20220127'...]）
    list = []
    datestart = datetime.datetime.strptime(start_date, '%Y%m%d')
    dateend = datetime.datetime.strptime(end_date, '%Y%m%d')
    list.append(datestart.strftime('%Y%m%d'))
    while datestart < dateend:
        datestart += datetime.timedelta(days=1)
        list.append(datestart.strftime('%Y%m%d'))
    return list


# 设置 ics 文件名称
ics_file_name = '123.ics'
# 指定需要删除日历活动对应的日期
del_date = ('20220220', '20220221', '20220222', '20220223', '20220224', '20220225', '20220226')
# 像上面这种连续的时间可以简写成下面这种形式
# del_date = get_dates('20220220', '20220226')

ics_var = get_ics_file(ics_file_name)
for i in del_date:
    new_ics = deal_with_var(i, ics_var)
    ics_var = new_ics
save_file(new_ics, 'new' + ics_file_name)
