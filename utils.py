import re
import random
import string


def generate_random_string(length=6):
    # 生成数字和字母混合的字符集
    characters = string.ascii_letters + string.digits
    
    # 使用随机抽样生成指定长度的字符串
    random_string = ''.join(random.choices(characters, k=length))
    
    return random_string

def is_valid_email(email):
    # 定义邮箱格式的正则表达式模式
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True
    else:
        return False
    
def is_valid_team_id(s):
    # 定义正则表达式模式，表示字符串必须是长度为 6，且只包含大小写字母和数字
    pattern = r'^[a-zA-Z0-9]{6}$'
    
    # 使用 re.match() 方法检查字符串是否符合模式
    if re.match(pattern, s):
        return True
    else:
        return False