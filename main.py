from MainWindow import Ui_MainWindow
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide6.QtCore import QTimer
import sys
from PySide6.QtUiTools import QUiLoader
import serial
import serial.tools.list_ports
import pyperclip
import os
import datetime
import time
from modbus_crc import modbus_crc

import logging
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(handler)
logger.addHandler(console)

# 波特率纯数字
lst_baudrate = [str(i) for i in [600, 1200, 2400, 4800, 9600, 19200, 38400, 56000, 57600, 115200]] # 常用的波特率
# 数据位，一个字典
dict_bytesize = {
    '5':serial.FIVEBITS, 
    '6':serial.SIXBITS, 
    '7':serial.SEVENBITS, 
    '8':serial.EIGHTBITS
    }
# 校验，也是一个字典。
dict_parity = {
    '无校验':serial.PARITY_NONE, 
    '奇校验':serial.PARITY_ODD, 
    '偶校验':serial.PARITY_EVEN,
    'PARITY_MARK':serial.PARITY_MARK, 
    'PARITY_SPACE':serial.PARITY_SPACE
}
# 停止位，也是一个字典。
dict_stopbits = {
    '1':serial.STOPBITS_ONE,
    '1.5':serial.STOPBITS_ONE_POINT_FIVE,
    '2':serial.STOPBITS_TWO
}

# modbus的数据类型
modbus_data_style = {
    ''

}


key_serial_name = "串口名"
key_baudrate = "波特率"
key_bytesize = "数据位"
key_parity = "校验"
key_stopbits = "停止位"

# 接收的定时器的计时器。
receive_timer_interval = 100

class MainWindow(QMainWindow):
    '''这个是主窗口'''
    def __init__(self) -> None:
        super().__init__()
        # 这里调用的是窗口的ui界面
        # self.ui = QUiLoader().load('MainWindow.ui') # 用这个好像不能自动补全。
        # 我用一个脚本来将ui文件转成py文件，然后用如下的方式来初始化。
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupUi()

    def getSerialParameter(self)->dict:
        # 这个是取得串口的参数信息
        result = {}
        if len(self.ui.combo_name.currentText()) != 0:
            # 先是串口名称
            result[key_serial_name] = self.ui.combo_name.currentText()
            # 然后是波特率
            result[key_baudrate] = int(self.ui.combo_baudrate.currentText())
            # 数据位
            result[key_bytesize] = dict_bytesize[self.ui.combo_bytesize.currentText()]
            # 校验
            result[key_parity] = dict_parity[self.ui.combo_parity.currentText()]
            # 结束位
            result[key_stopbits] = dict_stopbits[self.ui.combo_stopsize.currentText()]

        return result
    
    def show_state(self, msg):
        # 显示当前的状态
        self.ui.lbl_state.setText(
            "串口状态：{} , {}".format(
            "打开" if self.serial is not None and self.serial.isOpen() else "关闭",
            msg)
        )

    # 如下的几个函数是对log日志的包装，同时也发到界面上。
    def log_error(self, msg):
        logger.error(msg)
        self.show_state(msg)
    
    def log_info(self, msg):
        logger.info(msg)
        self.show_state(msg)

    def log_debug(self, msg):
        logger.debug(msg)
        self.show_state(msg)
    
    def setupUi(self):
        # 设置界面的
        lst_names = [i.name for i in list(serial.tools.list_ports.comports())]
        self.ui.combo_name.addItems(lst_names) # 串口名，
        self.ui.combo_baudrate.addItems(lst_baudrate)
        self.ui.combo_parity.addItems(list(dict_parity.keys()))
        self.ui.combo_bytesize.addItems(list(dict_bytesize.keys()))
        self.ui.combo_stopsize.addItems(list(dict_stopbits.keys()))

        # 设置默认的选项
        self.ui.combo_baudrate.setCurrentIndex(lst_baudrate.index('9600'))
        self.ui.combo_bytesize.setCurrentText('8')
        self.ui.combo_parity.setCurrentText('无校验')
        self.ui.combo_stopsize.setCurrentText('1')

        # 设置默认选中,我这里默认是16进制。其他的默认都是没有选中的。
        self.ui.radio_recv_hex_mode.setChecked(True)
        self.ui.radio_send_hex_mode.setChecked(True)

        #
        self.serial = None
        self.thread_serial_recv = None
        self.serial_recv_state = False # 线程的状态

        # 如下是一堆的事件处理
        self.serial_state = False # 串口的连接状态
        self.ui.btn_open.clicked.connect(self.open_serial)
        self.ui.btn_close.clicked.connect(self.close_serial)
        self.ui.btn_recv_clear.clicked.connect(self.clear_recv_text)
        self.ui.btn_recv_copy.clicked.connect(self.copy_recv_text)
        self.ui.btn_recv_save.clicked.connect(self.save_recv_text)
        self.ui.btn_send_clear.clicked.connect(self.clear_send_text)
        self.ui.btn_send_file.clicked.connect(self.send_file)
        self.ui.btn_send_data.clicked.connect(self.send_data)
        self.ui.chk_autosend.stateChanged.connect(self.auto_send_changed)
        #modbus
        self.ui.btn_calu_crc.clicked.connect(self.calu_crc)
        

        # 默认关闭按钮是灰色的。
        self.ui.btn_close.setEnabled(False)

        # 定时器
        # 接收的定时器
        self.recv_buf = bytearray() 
        self.recv_timer = QTimer(self)
        self.recv_timer.timeout.connect(self.serial_recv)
        self.recv_timer.start(receive_timer_interval) # 直接启动。
        # 自动发送的定时器
        self.auto_send_timer = QTimer(self)
        self.auto_send_timer.timeout.connect(self.send_data) # 事件是发送吧。 
        self.last_recv_time = None     

        self.show_state('程序启动完毕')
    
    def calu_crc(self):
        # 这里首先取得输入的值
        _input = self.ui.txt_crc_input.text()
        _data = bytearray.fromhex(_input)
        _crc = modbus_crc(_data)
        self.ui.txt_crc_result.setText(hex(_crc))

    def auto_send_changed(self):
        if self.ui.chk_autosend.isChecked():
            self.auto_send_timer.start(int(self.ui.txt_send_period.text()))
        else:
            self.auto_send_timer.stop()
        pass

    def close_serial(self):
        # 关闭串口
        if self.serial is not None:
            self.serial.close()
        self.serial_state = False
        self.serial = None
        self.log_info("关闭串口")
        self.ui.btn_open.setEnabled(True)
        self.ui.btn_close.setEnabled(False)


    def open_serial(self):
        # 首先获得参数
        parm = self.getSerialParameter()
        if parm != {}:
            try:
                self.serial = serial.Serial(
                    port=parm[key_serial_name],
                    baudrate=parm[key_baudrate],
                    bytesize=parm[key_bytesize],
                    parity=parm[key_parity],
                    stopbits=parm[key_stopbits],
                    timeout=0 # 读取超时。
                )
                if self.serial.isOpen():
                    self.log_info('成功打开串口')
                    self.ui.btn_open.setEnabled(False)
                    self.ui.btn_close.setEnabled(True)

                else:
                    self.log_error("串口打开失败")
            except Exception as err:
                self.log_error("错误：{}".format(err))
        else:
            self.log_error("参数失败")
    
    def serial_recv(self):
        # 线程接收，用定时器启动的。
        try:
            if self.serial is not None and  self.serial.in_waiting:
                newline = False # 默认不换行
                append_time = False # 默认不需要添加时间。
                if self.last_recv_time is not None:
                    # 如果存在最后接收的时间，就判断是否超过了阈值
                    newline = (datetime.datetime.now() - self.last_recv_time).microseconds > 2 * receive_timer_interval
                    append_time = newline
                else:
                    # 换行得看是否有数据，有可能是发送的数据。
                    newline=len(self.ui.txt_recv.toPlainText()) > 0
                    # 需要添加时间。
                    append_time = True
                self.last_recv_time = datetime.datetime.now()
                tmp_buf = bytearray() # 接收的临时的缓冲区。
                tmp_buf.extend(self.serial.read_all()) # 接收信息。
                self.recv_buf.extend(tmp_buf)          # 保存到上边的缓冲区。
                # todo 这里可以保存到modbus的缓冲区。
                # 这里要判断一下怎么显示了。
                if self.ui.radio_recv_hex_mode.isChecked():
                    # 这里表示是十六进制显示
                    self.appendPlainText(self.recv_buf.hex(' ') + ' ', newline=newline, append_time=append_time)
                    self.recv_buf.clear()
                elif self.ui.radio_recv_text_mode.isChecked():
                    # 这里表示是文本显示
                    # 默认是 utf-8编码
                    self.appendPlainText(self.recv_buf.decode('utf-8'), newline=newline, append_time=append_time)
                    self.recv_buf.clear()
                else:
                    # 这里表示是双字节。这里暂时
                    _count  = len(self.recv_buf)
                    _count_2 = _count // 4 # 每4个
                    buf2 = self.recv_buf[0:_count_2*4] # 截取
                    _s_tmp = buf2.decode('ascii') # 这里先按照ascii，其基本都是数字啊，这个是16进制的字符串。
                    buf3 = bytearray.fromhex(_s_tmp) # 这个转成了byte
                    self.appendPlainText(buf3.decode('utf-8'), newline=newline, append_time=append_time)
                    self.recv_buf = self.recv_buf[_count_2*4:]
        except Exception as err:
            self.log_error('线程接收错误：{}'.format(err))

    # 如下接收部分的按钮事件处理
    def clear_recv_text(self):
        self.ui.txt_recv.clear()
    def save_recv_text(self):
        # 保存读取的文件
        file_path,_ = QFileDialog(self).getSaveFileName(self, '选择文件')
        with open(file_path, 'w') as f:
            f.write(self.ui.txt_recv.toPlainText())

    def copy_recv_text(self):
        pyperclip.copy(self.ui.txt_recv.toPlainText())
        pass

    # 如下是发送的按钮事件处理
    def clear_send_text(self):
        self.ui.txt_send.clear()

    def save_send_text(self):
        # 保存发送的信息。
        file_path,_ = QFileDialog(self).getSaveFileName(self, '选择文件')
        with open(file_path, 'w') as f:
            f.write(self.ui.txt_send.toPlainText())

    def send_file(self):
        # 这里是发送一个文件，
        try:
            file_path, _ = QFileDialog(self).getOpenFileName(self, '选择文件')
            if os.path.exists(file_path):
                if self.serial is not None and  self.serial.isOpen():
                    # 这里表示实际发送的
                    with open(file_paht, 'rb') as f:
                        # 二进制读取
                        self.serial.write(f.read())
                    self.log_info("发送文件成功")
                else:
                    self.log_error("串口没有打开")
            else:
                self.log_error("文件：'{}' 不存在".format(file_apth))
        except Exception as err:
            self.log_error("错误：{}".format(err))

    def send_data(self):
        # 发送数据
        # 首先判断串口是否打开
        try:
            if self.serial is not None and self.serial.isOpen():
                # 这里先判断是否是16进制
                if self.ui.radio_send_hex_mode.isChecked():
                    # 十六进制
                    self.serial.write(bytearray.fromhex(self.ui.txt_send.toPlainText()))
                elif self.ui.radio_send_text_mode.isChecked():
                    # 文本，默认是utf-8编码。
                    self.serial.write(bytearray(self.ui.txt_send.toPlainText(), 'utf-8'))
                else:
                    # 这里表示是双字节
                    # 这里首先要将文本转成
                    self.serial.write(
                        bytearray(self.ui.txt_send.toPlainText(), 'utf-8').hex() # 这样子就转成双字节了
                    )
                # 这里直接显示发送的信息
                self.appendPlainText(self.ui.txt_send.toPlainText(), newline=True, append_time=True, is_receive=False)
            else:
                self.log_error("串口没有打开，发送失败.")
        except Exception as err:
            self.log_error("发送错误:{}".format(err))

    def appendPlainText(self, text, newline=False, append_time = False, is_receive=True):
        # 因为默认的清空下，这个会添加回车，这个解决一下
        self.ui.txt_recv.moveCursor(QTextCursor.End) # 移动到最后
        precursor =self.ui.txt_recv.textCursor() # 
        pos = precursor.position() # 这个位置
        prefix  = "" # 前缀
        if newline and len(self.ui.txt_recv.toPlainText()) > 0:
            # 如果不是空白的，就需要添加一个回车
            prefix += '\n'
        if append_time:
            # 如果需要添加时间
            # 然后添加日期
            prefix += time.strftime("%H:%M:%S ") # 添加日期
            # 然后添加是发送还是接收。
            if is_receive:
                prefix += '收<- :'
            else:
                prefix += '发-> :'
        self.ui.txt_recv.appendPlainText(prefix + text) # 追加文本
        if pos == 0:
            # 如果是第一行，不需要删除回车
            return
        # 定位到前面的回车，并且删除这个回车。
        precursor.setPosition(pos)
        self.ui.txt_recv.setTextCursor(precursor)
        self.ui.txt_recv.textCursor().deleteChar()
    

if __name__  == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    # mainWindow.ui.show()
    mainWindow.show()
    app.exec()
 
