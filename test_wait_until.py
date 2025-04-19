import datetime
import time

# 获取当前时间（使用本地时间）
def get_current_time():
    return datetime.datetime.now()

# 等待到指定时间
def wait_until(target_time):
    print(f"当前等待到指定时间: {target_time.strftime('%Y-%m-%d %H:%M:%S')}")
    while True:
        now = get_current_time()
        print(f"当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}", end='\r')
        if now >= target_time:
            print(f"\n已到达指定时间，继续执行程序...")
            break
        time.sleep(0.2)  # 每0.2秒检查一次

# 测试代码
if __name__ == "__main__":
    print("开始测试wait_until函数")
    
    # 获取当前时间
    current_time = get_current_time()
    print(f"当前时间: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 设置目标时间为当前时间后5秒
    target_time = current_time + datetime.timedelta(seconds=5)
    print(f"设置目标时间为: {target_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 调用wait_until函数
    wait_until(target_time)
    
    # 验证函数执行完毕后的时间
    after_time = get_current_time()
    print(f"函数执行完毕时间: {after_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 计算实际等待时间
    wait_duration = (after_time - current_time).total_seconds()
    print(f"实际等待时间: {wait_duration:.2f}秒")
    
    print("测试完成")