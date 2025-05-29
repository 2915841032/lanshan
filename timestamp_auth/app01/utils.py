import time

# 计算校验位：取时间戳前12位各位数之和的个位数
def calculate_check_bit(timestamp_without_check):
    total = sum(int(digit) for digit in str(timestamp_without_check))
    return total % 10

# 生成带校验位的时间戳
def generate_timestamp_with_check():
    # 获取当前的13位毫秒级时间戳
    timestamp = int(time.time() * 1000)

    # 提取前12位时间戳
    timestamp_without_check = timestamp // 10

    # 计算校验位
    check_bit = calculate_check_bit(timestamp_without_check)

    # 拼接时间戳和校验位
    return timestamp_without_check * 10 + check_bit

# 校验时间戳的有效性
def validate_timestamp(timestamp_with_check):
    # 提取时间戳的前12位和校验位
    timestamp_without_check = timestamp_with_check // 10
    provided_check_bit = timestamp_with_check % 10

    # 计算正确的校验位
    calculated_check_bit = calculate_check_bit(timestamp_without_check)

    # 校验时间戳的校验位是否正确
    return provided_check_bit == calculated_check_bit
