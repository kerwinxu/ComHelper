# ComHelper
串口助手

# 目标
做一个串口助手

# 参数
   - 串口名称
   - 波特率
   - 字节位
   - 校验位
   - 结束位

# 发送接收
   - 发送
     - 发送框
     - 是否十六进制
     - 清空接收区
     - 保存接收内容
   - 接收
     - 接收框
     - 是否十六进制
     - 发送文件
     - 发送数据
     - 自动发送
       - 发送间隔 ms

# 编译成exe文件

pyinstaller -F -w main.py --hidden-import PySide2.QtXml
