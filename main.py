try:
    year = int(input(" ："))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} 是闰年")
    else:
        print(f"{year} 不是闰年")
except ValueError:
    print("输入无效，请输入数字年份")
