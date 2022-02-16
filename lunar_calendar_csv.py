from datetime import timedelta
from borax.calendars import LunarDate
import pandas as pd


def get_lunardate(y, m, d):
    # 输入公立日期，返回农历日期列表
    ld = LunarDate.from_solar_date(int(y), int(m), int(d))
    lst_ymd = ld.strftime('%y, %m, %d').split(', ')
    return lst_ymd


def get_solar_cal(y, m, d):
    # 输入农历日期，返回公立日期
    lu = LunarDate(int(y), int(m), int(d)).to_solar_date()
    return str(lu.strftime('%Y/%m/%d'))


def dict_conv(dict_cal):
    # 将包含阳历日历的字典转换为阴历日历字典
    dict_tmp1 = {}
    for key1 in dict_cal:
        in_ymd1 = dict_cal[key1].split(',')
        tmp_year = ", ".join(get_lunardate(in_ymd1[0], in_ymd1[1], in_ymd1[2]))
        dict_tmp1[key1] = tmp_year
    return dict_tmp1


def save_csv():
    # 将得到的日期列表转换为 csv 文件保存
    dataframe = pd.DataFrame({
        'Subject': lst_person, 'Start Date': lst_date, 'Start Time': '',
        'End Date': lst_date, 'End Time': '', 'All Day Event': '',
        'Description': '', 'Location': '', 'Private': ''
    })
    # 将 DataFrame 存储为 csv, index 表示是否显示行名，default=True
    dataframe.to_csv("lunar_birthday.csv", index=False, sep=',', encoding='gbk')
    print("保存成功")


# 设置日历类型，阳历为 1，阴历为 2
cal_type = 1
# 用字典的形式写入联系人生日，{联系人称呼：生日}
dict_b = {'Nekoha ': '2016, 6, 24', 'Rikka': '2002, 12, 5'}

lst_person = []
lst_date = []


if cal_type == 1:
    # 阳历字典先转换为阴历
    dict_a = dict_conv(dict_b)
elif cal_type == 2:
    dict_a = dict_b
else:
    print("错误参数，请将 cal_type 设置为 1 或 2")

for key in dict_a:
    in_ymd = dict_a[key].split(',')
    year = int(in_ymd[0])
    for i in range(year, 2101):
        lst_person.append(key + "的农历生日")
        lst_date.append(get_solar_cal(year, in_ymd[1], in_ymd[2]))
        year += 1
save_csv()

