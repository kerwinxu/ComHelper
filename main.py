from numpy import byte
from MainWindow import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication
import sys
from PySide2.QtUiTools import QUiLoader
import serial
import serial.tools.list_ports
from threading import Thread

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


key_serial_name = "串口名"
key_baudrate = "波特率"
key_bytesize = "数据位"
key_parity = "校验"
key_stopbits = "停止位"



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
        lst_names = list(serial.tools.list_ports.comports())
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



        self.show_state('程序启动完毕')

    def close_serial(self):
        # 关闭串口
        if self.serial is not None:
            self.serial.close()
        self.serial_state = False
        self.serial_recv_state = False
        self.log_info("关闭串口")

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
                    stopbits=parm[key_stopbits]
                )
                if self.serial.isOpen():
                    # 这里打开线程
                    if self.serial_recv_state:
                        # 如果原先有线程，就关闭。
                        self.serial_recv_state = False
                        self.thread_serial_recv.join() # 等待线程结束
                    self.serial_recv_state = True
                    self.thread_serial_recv = Thread(target=self.serial_recv)
                    self.thread_serial_recv.start() # 启动线程
                    self.serial_state = True
                    self.log_info('成功打开串口')
                else:
                    self.log_error("串口打开失败")
            except Exception as err:
                self.log_error("错误：{}".format(err))
        else:
            self.log_error("参数失败")
    
    def serial_recv(self):
        # 线程接收类
        buf = bytearray() # 一个接收的缓冲区
        try:
            while self.serial_recv_state:
                if self.serial.in_waiting:
                    buf.extend(self.serial.read_all())
                    # 这里要判断一下怎么显示了。
                    if self.ui.radio_recv_hex_mode.isChecked():
                        # 这里表示是十六进制显示
                        self.ui.txt_recv.append(buf.hex() + ' ')
                        buf.clear()
                    elif self.ui.radio_recv_text_mode.isChecked():
                        # 这里表示是文本显示
                        # 默认是 utf-8编码
                        self.ui.txt_recv.append(buf.decode('utf-8'))
                        buf.clear()
                    else:
                        # 这里表示是双字节。这里暂时
                        _count  = len(buf)
                        _count_2 = _count // 4 # 每4个
                        buf2 = buf[0:_count_2*4] # 截取
                        _s_tmp = buf2.decode('ascii') # 这里先按照ascii，其基本都是数字啊，这个是16进制的字符串。
                        buf3 = bytearray.fromhex(_s_tmp) # 这个转成了byte
                        self.ui.txt_recv.append(buf3.decode('utf-8'))
                        buf = buf[_count_2*4:]
        except Exception as err:
            self.log_error('线程接收错误：{}'.format(err))
        # 最后要设置这个为None
        self.thread_serial_recv = None

    # 如下接收部分的按钮事件处理
    def clear_recv_text(self):
        self.ui.txt_recv.clear()
    def save_recv_text(self):
        pass
    def copy_recv_text(self):
        pass

    # 如下是发送的按钮事件处理
    def clear_send_text(self):
        self.ui.txt_send.clear()
    def save_send_text(self):
        pass
    def send_file(self):
        pass
    def send_data(self):
        # 发送数据
        # 首先判断串口是否打开
        if self.serial is not None and self.serial.isOpen():
            # 这里先判断是否是16进制
            if self.ui.radio_send_hex_mode.isChecked():
                # 十六进制
                self.serial.write(bytearray.fromhex(self.ui.txt_send.currentText()))
            elif self.ui.radio_send_text_mode.isChecked():
                # 文本，默认是utf-8编码。
                self.serial.write(bytearray(self.ui.txt_send.currentText(), 'utf-8'))
            else:
                # 这里表示是双字节
                
                pass
        else:
            self.log_error("串口没有打开，发送失败.")
        pass



if __name__  == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    # mainWindow.ui.show()
    mainWindow.show()
    app.exec_()