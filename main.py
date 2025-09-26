def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    print("=== 闰年判断程序 ===")
    
    while True:
        try:
            year_input = input("请输入年份（输入'quit'退出程序）: ")
            
            if year_input.lower() == 'quit':
                print("程序已退出，再见！")
                break
            
            year = int(year_input)
            
            if is_leap_year(year):
                print(f"{year}年是闰年 ✓")
            else:
                print(f"{year}年不是闰年 ✗")
                
            print("-" * 30)
            
        except ValueError:
            print(f"错误：'{year_input}' 不是有效的年份数字！")
            print("请重新输入有效的年份数字。")
            print("-" * 30)
        
        except Exception as e:
            print(f"发生未知错误：{e}")
            print("-" * 30)

if __name__ == "__main__":
    main()
