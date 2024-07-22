import re

def is_valid_phone_number(phone_number):
    # 定义中国大陆手机号码的正则表达式
    pattern = r'^1[3-9]\d{9}$'
    # 使用 re.match 检查手机号码是否符合正则表达式
    if re.match(pattern, phone_number):
        return True
    else:
        return False
def main():
    phone_number = input("请输入中国大陆地区手机号码：")
    if is_valid_phone_number(phone_number):
        print("是手机号")
    else:
        print("不是手机号")

if __name__ == "__main__":
    main()