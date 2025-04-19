# 铁路票务自动化预定

该项目通过使用 Selenium WebDriver 和 Python 自动化实现了12306网站的火车票预定。通过自动化登录、验证码处理、座位选择和支付等步骤，帮助用户高效购买车票。

## 环境要求

运行该项目需要在机器上安装 Python。同时，你还需要安装以下库：

- **Selenium**：用于模拟人的行为，自动化浏览器操作。

### Python版本

- Python 3.8+

## 安装
（只用下载buy.py和account_information.txt并配置环境就可以了，其他可以不用下载）

安装所需的 Python 库：
pip install selenium==4.31.0

克隆该项目或下载文件：
   ```bash
   git clone https://github.com/yourusername/railway-ticket-booking.git
   ```
#### 配置
在运行程序之前，确保在根目录下的 account_information.txt 文件中提供你的账户信息。

文件格式如下：
username=你的用户名
password=你的密码
id=身份证后四位

#### 使用方法
激活虚拟环境（如果有使用虚拟环境）：

source venv/bin/activate   # 对于 Linux/Mac
.\venv\Scripts\activate    # 对于 Windows
运行脚本：

使用以下命令启动程序：

python buy.py
程序会自动打开浏览器窗口并执行以下步骤：

登录到你的 12306 账户。

等待直到设定的预定时间（你可以在脚本中修改这个时间）。

自动选择车次和乘客。

完成购票过程。

自定义脚本
目标时间：你可以在 buy.py 脚本中修改 target_time 来设置预定的开始时间。

target_time = datetime.datetime(2025, 4, 17, 20, 30, 0)  # 修改这行
常见问题
ChromeDriver 版本：确保你的 ChromeDriver 与安装的 Chrome 版本匹配。

验证码处理：脚本包含验证码处理的占位符。如果验证码无法自动处理，脚本会等待你手动输入验证码。

许可证
该项目使用 MIT 许可证 - 详情请参见 LICENSE 文件。







