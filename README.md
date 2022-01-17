# NekoBirthday

由于谷歌日历不支持生成联系人农历生日，本项目利用 borax 模块计算出农历生日并生成 csv 文件，生成完成后可直接导入日历。

## 环境配置

1. 安装 Python 3.6+

2. 安装相关依赖

    克隆项目到本地，进入项目文件夹执行 `pip install -r requirements.txt`。


## 修改配置

修改 `lunar_calendar_csv.py` 中的部分参数：

```
# 设置姓名和对应的阳历生日，如 Nekoha 阳历生日为 2016/6/24，设置如下
person = 'Nekoha'
lst_lunardate = get_lunardate(2016, 6, 24)
```

## 运行脚本

上述步骤完成后启动脚本：

```
python3 lunar_calendar_csv.py
```

## 导入数据

脚本运行完成后会生成 [lunar_birthday.csv](./lunar_birthday.csv) 文件，将文件导入到谷歌日历即可。导入方法参照：[将活动导入到 Google 日历](https://support.google.com/a/users/answer/37118) 。

注意导入的数据无法批量删除，建议新建一个日历专门存放农历生日数据。