from datetime import timedelta
from borax.calendars import LunarDate
import pandas as pd


def get_lunardate(y, m, d):
    # 输入公立日期，返回农历日期列表
    ld = LunarDate.from_solar_date(y, m, d)
    lst_ymd = ld.strftime('%y, %m, %d').split(', ')
    return lst_ymd


def get_solar_cal(y, m, d):
    # 输入农历日期，返回公立日期
    lu = LunarDate(y, m, d).to_solar_date()
    return lu.strftime('%Y/%m/%d')


def save_csv():
    # 将得到的日期列表转换为 csv 文件保存
    dataframe = pd.DataFrame({
        'Subject': person + '的农历生日', 'Start Date': lst_solar_cal, 'Start Time': '',
        'End Date': lst_solar_cal, 'End Time': '', 'All Day Event': '',
        'Description': '', 'Location': '', 'Private': ''
    })
    # 将 DataFrame 存储为 csv, index 表示是否显示行名，default=True
    dataframe.to_csv("lunar_birthday.csv", index=False, sep=',', encoding='gbk')
    return "保存成功"


# 设置姓名和对应的阳历生日，如 Nekoha 阳历生日为 2016/6/24，设置如下
person = 'Nekoha'
lst_lunardate = get_lunardate(2016, 6, 24)
lst_solar_cal = []

# 输出到 2100 年所有农历日期
for i in range(int(lst_lunardate[0]), 2101):
    lst_solar_cal.append(get_solar_cal(i, int(lst_lunardate[1]), int(lst_lunardate[2])))
print(save_csv())