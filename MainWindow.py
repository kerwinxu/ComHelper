# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,
    QMetaObject, QRect,
    QSize)
# from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#     QFont, QFontDatabase, QGradient, QIcon,
#     QImage, QKeySequence, QLinearGradient, QPainter,
#     QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import ( QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit,  QMenuBar, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(813, 602)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.label)

        self.combo_name = QComboBox(self.frame)
        self.combo_name.setObjectName(u"combo_name")

        self.horizontalLayout_3.addWidget(self.combo_name)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.combo_baudrate = QComboBox(self.frame)
        self.combo_baudrate.setObjectName(u"combo_baudrate")

        self.horizontalLayout_3.addWidget(self.combo_baudrate)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.combo_bytesize = QComboBox(self.frame)
        self.combo_bytesize.setObjectName(u"combo_bytesize")

        self.horizontalLayout_3.addWidget(self.combo_bytesize)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.combo_parity = QComboBox(self.frame)
        self.combo_parity.setObjectName(u"combo_parity")

        self.horizontalLayout_3.addWidget(self.combo_parity)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.combo_stopsize = QComboBox(self.frame)
        self.combo_stopsize.setObjectName(u"combo_stopsize")

        self.horizontalLayout_3.addWidget(self.combo_stopsize)

        self.btn_open = QPushButton(self.frame)
        self.btn_open.setObjectName(u"btn_open")

        self.horizontalLayout_3.addWidget(self.btn_open)

        self.btn_close = QPushButton(self.frame)
        self.btn_close.setObjectName(u"btn_close")

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.frame)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy3)
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 793, 325))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txt_send = QPlainTextEdit(self.groupBox_2)
        self.txt_send.setObjectName(u"txt_send")

        self.verticalLayout_2.addWidget(self.txt_send)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.frame_2 = QFrame(self.groupBox_2)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setMinimumSize(QSize(0, 75))
        self.frame_2.setMaximumSize(QSize(16777215, 150))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setMinimumSize(QSize(100, 0))
        self.frame_4.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.radio_send_text_mode = QRadioButton(self.frame_4)
        self.radio_send_text_mode.setObjectName(u"radio_send_text_mode")

        self.verticalLayout_7.addWidget(self.radio_send_text_mode)

        self.radio_send_hex_mode = QRadioButton(self.frame_4)
        self.radio_send_hex_mode.setObjectName(u"radio_send_hex_mode")

        self.verticalLayout_7.addWidget(self.radio_send_hex_mode)

        self.radio_send_doublebyte = QRadioButton(self.frame_4)
        self.radio_send_doublebyte.setObjectName(u"radio_send_doublebyte")

        self.verticalLayout_7.addWidget(self.radio_send_doublebyte)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.horizontalLayout_6.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.btn_send_data = QPushButton(self.frame_3)
        self.btn_send_data.setObjectName(u"btn_send_data")

        self.gridLayout.addWidget(self.btn_send_data, 1, 1, 1, 1)

        self.btn_send_clear = QPushButton(self.frame_3)
        self.btn_send_clear.setObjectName(u"btn_send_clear")

        self.gridLayout.addWidget(self.btn_send_clear, 0, 0, 1, 1)

        self.btn_send_file = QPushButton(self.frame_3)
        self.btn_send_file.setObjectName(u"btn_send_file")

        self.gridLayout.addWidget(self.btn_send_file, 1, 0, 1, 1)

        self.btn_send_save = QPushButton(self.frame_3)
        self.btn_send_save.setObjectName(u"btn_send_save")

        self.gridLayout.addWidget(self.btn_send_save, 0, 1, 1, 1)

        self.chk_autosend = QCheckBox(self.frame_3)
        self.chk_autosend.setObjectName(u"chk_autosend")

        self.gridLayout.addWidget(self.chk_autosend, 2, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.txt_send_period = QLineEdit(self.frame_3)
        self.txt_send_period.setObjectName(u"txt_send_period")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.txt_send_period.sizePolicy().hasHeightForWidth())
        self.txt_send_period.setSizePolicy(sizePolicy5)
        self.txt_send_period.setMinimumSize(QSize(50, 0))
        self.txt_send_period.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_10.addWidget(self.txt_send_period)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)


        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.frame_3)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.txt_recv = QPlainTextEdit(self.groupBox)
        self.txt_recv.setObjectName(u"txt_recv")

        self.verticalLayout_4.addWidget(self.txt_recv)

        self.frame_5 = QFrame(self.groupBox)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy4.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy4)
        self.frame_5.setMinimumSize(QSize(0, 75))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy2.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy2)
        self.frame_6.setMinimumSize(QSize(100, 0))
        self.frame_6.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.frame_6.setFrameShape(QFrame.Box)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.radio_recv_text_mode = QRadioButton(self.frame_6)
        self.radio_recv_text_mode.setObjectName(u"radio_recv_text_mode")

        self.verticalLayout_10.addWidget(self.radio_recv_text_mode)

        self.radio_recv_hex_mode = QRadioButton(self.frame_6)
        self.radio_recv_hex_mode.setObjectName(u"radio_recv_hex_mode")

        self.verticalLayout_10.addWidget(self.radio_recv_hex_mode)

        self.radio_recv_doublebyte = QRadioButton(self.frame_6)
        self.radio_recv_doublebyte.setObjectName(u"radio_recv_doublebyte")

        self.verticalLayout_10.addWidget(self.radio_recv_doublebyte)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)


        self.horizontalLayout_8.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Box)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.btn_recv_clear = QPushButton(self.frame_7)
        self.btn_recv_clear.setObjectName(u"btn_recv_clear")

        self.gridLayout_3.addWidget(self.btn_recv_clear, 0, 0, 1, 1)

        self.btn_recv_save = QPushButton(self.frame_7)
        self.btn_recv_save.setObjectName(u"btn_recv_save")

        self.gridLayout_3.addWidget(self.btn_recv_save, 1, 0, 1, 1)

        self.btn_recv_copy = QPushButton(self.frame_7)
        self.btn_recv_copy.setObjectName(u"btn_recv_copy")

        self.gridLayout_3.addWidget(self.btn_recv_copy, 2, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.frame_7)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)


        self.verticalLayout_4.addWidget(self.frame_5)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayoutWidget = QWidget(self.tab_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 781, 395))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.groupBox_5 = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.label_8)

        self.txt_modbus_read_address = QLineEdit(self.groupBox_5)
        self.txt_modbus_read_address.setObjectName(u"txt_modbus_read_address")
        sizePolicy5.setHeightForWidth(self.txt_modbus_read_address.sizePolicy().hasHeightForWidth())
        self.txt_modbus_read_address.setSizePolicy(sizePolicy5)
        self.txt_modbus_read_address.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_11.addWidget(self.txt_modbus_read_address)

        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.label_9)

        self.combo_modbus_read_data_style = QComboBox(self.groupBox_5)
        self.combo_modbus_read_data_style.setObjectName(u"combo_modbus_read_data_style")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.combo_modbus_read_data_style.sizePolicy().hasHeightForWidth())
        self.combo_modbus_read_data_style.setSizePolicy(sizePolicy6)

        self.horizontalLayout_11.addWidget(self.combo_modbus_read_data_style)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.txt_modbus_read_data_count = QLineEdit(self.groupBox_5)
        self.txt_modbus_read_data_count.setObjectName(u"txt_modbus_read_data_count")
        sizePolicy5.setHeightForWidth(self.txt_modbus_read_data_count.sizePolicy().hasHeightForWidth())
        self.txt_modbus_read_data_count.setSizePolicy(sizePolicy5)
        self.txt_modbus_read_data_count.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_12.addWidget(self.txt_modbus_read_data_count)

        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.label_11)

        self.combo_modbus_read_byte_sort = QComboBox(self.groupBox_5)
        self.combo_modbus_read_byte_sort.setObjectName(u"combo_modbus_read_byte_sort")
        sizePolicy6.setHeightForWidth(self.combo_modbus_read_byte_sort.sizePolicy().hasHeightForWidth())
        self.combo_modbus_read_byte_sort.setSizePolicy(sizePolicy6)

        self.horizontalLayout_12.addWidget(self.combo_modbus_read_byte_sort)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.btn_modbus_read = QPushButton(self.groupBox_5)
        self.btn_modbus_read.setObjectName(u"btn_modbus_read")

        self.horizontalLayout_13.addWidget(self.btn_modbus_read)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)

        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)

        self.horizontalLayout_14.addWidget(self.label_12)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.txt_modbus_read_send = QLineEdit(self.groupBox_5)
        self.txt_modbus_read_send.setObjectName(u"txt_modbus_read_send")

        self.verticalLayout_6.addWidget(self.txt_modbus_read_send)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)

        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.label_13)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)

        self.txt_modbus_read_receive = QTextEdit(self.groupBox_5)
        self.txt_modbus_read_receive.setObjectName(u"txt_modbus_read_receive")

        self.verticalLayout_6.addWidget(self.txt_modbus_read_receive)


        self.horizontalLayout_5.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_14 = QLabel(self.groupBox_6)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)

        self.horizontalLayout_17.addWidget(self.label_14)

        self.txt_modbus_write_address = QLineEdit(self.groupBox_6)
        self.txt_modbus_write_address.setObjectName(u"txt_modbus_write_address")
        sizePolicy5.setHeightForWidth(self.txt_modbus_write_address.sizePolicy().hasHeightForWidth())
        self.txt_modbus_write_address.setSizePolicy(sizePolicy5)
        self.txt_modbus_write_address.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_17.addWidget(self.txt_modbus_write_address)

        self.label_15 = QLabel(self.groupBox_6)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)

        self.horizontalLayout_17.addWidget(self.label_15)

        self.combo_modbus_write_data_style = QComboBox(self.groupBox_6)
        self.combo_modbus_write_data_style.setObjectName(u"combo_modbus_write_data_style")
        sizePolicy6.setHeightForWidth(self.combo_modbus_write_data_style.sizePolicy().hasHeightForWidth())
        self.combo_modbus_write_data_style.setSizePolicy(sizePolicy6)

        self.horizontalLayout_17.addWidget(self.combo_modbus_write_data_style)


        self.verticalLayout_12.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_16 = QLabel(self.groupBox_6)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_18.addWidget(self.label_16)

        self.txt_modbus_write_data_count = QLineEdit(self.groupBox_6)
        self.txt_modbus_write_data_count.setObjectName(u"txt_modbus_write_data_count")
        sizePolicy5.setHeightForWidth(self.txt_modbus_write_data_count.sizePolicy().hasHeightForWidth())
        self.txt_modbus_write_data_count.setSizePolicy(sizePolicy5)
        self.txt_modbus_write_data_count.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_18.addWidget(self.txt_modbus_write_data_count)

        self.label_17 = QLabel(self.groupBox_6)
        self.label_17.setObjectName(u"label_17")
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)

        self.horizontalLayout_18.addWidget(self.label_17)

        self.combo_modbus_write_byte_sort = QComboBox(self.groupBox_6)
        self.combo_modbus_write_byte_sort.setObjectName(u"combo_modbus_write_byte_sort")
        sizePolicy6.setHeightForWidth(self.combo_modbus_write_byte_sort.sizePolicy().hasHeightForWidth())
        self.combo_modbus_write_byte_sort.setSizePolicy(sizePolicy6)

        self.horizontalLayout_18.addWidget(self.combo_modbus_write_byte_sort)


        self.verticalLayout_12.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_10)

        self.btn_modbus_write = QPushButton(self.groupBox_6)
        self.btn_modbus_write.setObjectName(u"btn_modbus_write")

        self.horizontalLayout_19.addWidget(self.btn_modbus_write)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_11)


        self.verticalLayout_12.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_12)

        self.label_18 = QLabel(self.groupBox_6)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)

        self.horizontalLayout_20.addWidget(self.label_18)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_13)


        self.verticalLayout_12.addLayout(self.horizontalLayout_20)

        self.txt_modbus_write_return = QLineEdit(self.groupBox_6)
        self.txt_modbus_write_return.setObjectName(u"txt_modbus_write_return")

        self.verticalLayout_12.addWidget(self.txt_modbus_write_return)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_14)

        self.label_19 = QLabel(self.groupBox_6)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)

        self.horizontalLayout_21.addWidget(self.label_19)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_15)


        self.verticalLayout_12.addLayout(self.horizontalLayout_21)

        self.txt_modubs_write_send = QTextEdit(self.groupBox_6)
        self.txt_modubs_write_send.setObjectName(u"txt_modubs_write_send")

        self.verticalLayout_12.addWidget(self.txt_modubs_write_send)


        self.horizontalLayout_5.addWidget(self.groupBox_6)

        self.groupBox_3 = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.txt_crc_input = QLineEdit(self.groupBox_3)
        self.txt_crc_input.setObjectName(u"txt_crc_input")
        self.txt_crc_input.setGeometry(QRect(10, 22, 231, 20))
        self.widget = QWidget(self.groupBox_3)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_16 = QHBoxLayout(self.widget)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(13, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)

        self.btn_calu_crc = QPushButton(self.widget)
        self.btn_calu_crc.setObjectName(u"btn_calu_crc")

        self.horizontalLayout_16.addWidget(self.btn_calu_crc)

        self.horizontalSpacer_8 = QSpacerItem(13, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_8)

        self.txt_crc_result = QLineEdit(self.widget)
        self.txt_crc_result.setObjectName(u"txt_crc_result")
        sizePolicy5.setHeightForWidth(self.txt_crc_result.sizePolicy().hasHeightForWidth())
        self.txt_crc_result.setSizePolicy(sizePolicy5)
        self.txt_crc_result.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_16.addWidget(self.txt_crc_result)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_9)

        self.widget1 = QWidget(self.groupBox_3)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 80, 239, 25))
        self.horizontalLayout_22 = QHBoxLayout(self.widget1)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.combo_toolbox_data_style = QComboBox(self.widget1)
        self.combo_toolbox_data_style.setObjectName(u"combo_toolbox_data_style")

        self.horizontalLayout_22.addWidget(self.combo_toolbox_data_style)

        self.horizontalSpacer_16 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_16)

        self.combo_toolbox_data_sort = QComboBox(self.widget1)
        self.combo_toolbox_data_sort.setObjectName(u"combo_toolbox_data_sort")

        self.horizontalLayout_22.addWidget(self.combo_toolbox_data_sort)

        self.horizontalSpacer_17 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_17)

        self.btn_toolbox_convert_data = QPushButton(self.widget1)
        self.btn_toolbox_convert_data.setObjectName(u"btn_toolbox_convert_data")

        self.horizontalLayout_22.addWidget(self.btn_toolbox_convert_data)


        self.horizontalLayout_5.addWidget(self.groupBox_3)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.lbl_state = QLabel(self.centralwidget)
        self.lbl_state.setObjectName(u"lbl_state")

        self.verticalLayout.addWidget(self.lbl_state)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 813, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ComHelper", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u540d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u8282\u4f4d", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6821\u9a8c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u4f4d", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.radio_send_text_mode.setText(QCoreApplication.translate("MainWindow", u"\u6587\u672c\u6a21\u5f0f", None))
        self.radio_send_hex_mode.setText(QCoreApplication.translate("MainWindow", u"\u5341\u516d\u8fdb\u5236\u6a21\u5f0f", None))
#if QT_CONFIG(tooltip)
        self.radio_send_doublebyte.setToolTip(QCoreApplication.translate("MainWindow", u"\u6bd4\u5982\u53d1\u9001\u5355\u5b57\u7b26'A'\uff0c\u5b9e\u9645\u53d1\u9001\u7684\u662f\u53cc\u5b57\u7b26'41'\uff0c'A'=0x41", None))
#endif // QT_CONFIG(tooltip)
        self.radio_send_doublebyte.setText(QCoreApplication.translate("MainWindow", u"\u53cc\u5b57\u8282", None))
        self.btn_send_data.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6570\u636e", None))
        self.btn_send_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u53d1\u9001\u6570\u636e", None))
        self.btn_send_file.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6587\u4ef6", None))
        self.btn_send_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u53d1\u9001\u6570\u636e", None))
        self.chk_autosend.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u53d1\u9001", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5468\u671f", None))
        self.txt_send_period.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u63a5\u6536", None))
        self.radio_recv_text_mode.setText(QCoreApplication.translate("MainWindow", u"\u6587\u672c\u6a21\u5f0f", None))
        self.radio_recv_hex_mode.setText(QCoreApplication.translate("MainWindow", u"\u5341\u516d\u8fdb\u5236\u6a21\u5f0f", None))
#if QT_CONFIG(tooltip)
        self.radio_recv_doublebyte.setToolTip(QCoreApplication.translate("MainWindow", u"\u6bd4\u5982\u63a5\u6536\u7684\u662f\u53cc\u5b57\u7b26'41'\uff0c\u8f6c\u6362\u6210\u5355\u5b57\u7b26'A', 'A'=0x41", None))
#endif // QT_CONFIG(tooltip)
        self.radio_recv_doublebyte.setText(QCoreApplication.translate("MainWindow", u"\u53cc\u5b57\u8282", None))
        self.btn_recv_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u63a5\u6536\u533a", None))
        self.btn_recv_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u63a5\u6536\u6570\u636e", None))
        self.btn_recv_copy.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u63a5\u6536\u6570\u636e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u666e\u901a\u4e32\u53e3", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5730\u5740:0x", None))
        self.txt_modbus_read_address.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u7c7b\u578b:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4e2a\u6570:", None))
        self.txt_modbus_read_data_count.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u8282\u6392\u5e8f:", None))
        self.btn_modbus_read.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u6570\u636e:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536\u5230:", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u5199\u5165", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u5730\u5740:0x", None))
        self.txt_modbus_write_address.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u7c7b\u578b:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4e2a\u6570:", None))
        self.txt_modbus_write_data_count.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u8282\u6392\u5e8f:", None))
        self.btn_modbus_write.setText(QCoreApplication.translate("MainWindow", u"\u5199\u5165", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u72b6\u6001", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u8981\u5199\u5165\u7684\u6570\u636e\uff0c\u884c\u533a\u5206:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5c0f\u5de5\u5177", None))
        self.btn_calu_crc.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97CRC", None))
        self.btn_toolbox_convert_data.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"modbus", None))
        self.lbl_state.setText("")
    # retranslateUi

