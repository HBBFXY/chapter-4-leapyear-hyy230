def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

try:
    year = int(input("请输入年份: "))
    
    if is_leap_year(year):
        print(f"{year}年是闰年")
    else:
        print(f"{year}年不是闰年")
        
except ValueError:
    print("错误：请输入有效的年份数字！")
