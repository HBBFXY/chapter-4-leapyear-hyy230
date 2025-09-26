try:
    # 获取用户输入并尝试转换为整数（处理空输入、非数字、浮点数）
    year_input = input().strip()
    year = int(year_input)
    
    # 闰年判断逻辑：能被400整除，或能被4整除但不能被100整除
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"{year}年是闰年")
    else:
        print(f"{year}年不是闰年")

# 捕获非整数输入的异常（空输入、字母、浮点数均触发）
except ValueError:
    print("输入错误")
