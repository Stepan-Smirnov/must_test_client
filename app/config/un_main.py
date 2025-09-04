# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'must_client.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListView, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QWidget)
import app.config.res_rс

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, \n"
"    stop:0 rgba(140, 140, 140, 255), \n"
"    stop:0.42 rgba(80, 0, 130, 235), \n"
"    stop:1 rgba(180, 120, 180, 255));\n"
"\n"
"font-family: Rubik;")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(30, 15, 30, 15)
        self.list_data = QListView(self.centralwidget)
        self.list_data.setObjectName(u"list_data")
        self.list_data.setStyleSheet(u"background: rgba(255, 255, 255, 50);\n"
"border-radius: 20px;\n"
"padding: 20px;\n"
"color: white;\n"
"font-size: 20px")

        self.gridLayout.addWidget(self.list_data, 2, 0, 1, 1)

        self.add_data_frame = QWidget(self.centralwidget)
        self.add_data_frame.setObjectName(u"add_data_frame")
        self.add_data_frame.setEnabled(True)
        self.add_data_frame.setMinimumSize(QSize(0, 0))
        self.add_data_frame.setBaseSize(QSize(0, 0))
        self.add_data_frame.setStyleSheet(u"background: transparent;")
        self.horizontalLayout = QHBoxLayout(self.add_data_frame)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_data_text = QLineEdit(self.add_data_frame)
        self.add_data_text.setObjectName(u"add_data_text")
        self.add_data_text.setStyleSheet(u"QLineEdit {\n"
"background: rgba(255, 255, 255, 50);\n"
"border-radius: 20px;\n"
"padding: 0 10px;\n"
"height: 50px;\n"
"font-size:28px;\n"
"color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgba(78,87,84, 200)\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 2px solid rgba(78,87,84, 200)\n"
"}\n"
"")
        self.add_data_text.setMaxLength(32)
        self.add_data_text.setCursorPosition(0)
        self.add_data_text.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.add_data_text)

        self.add_data_btn = QPushButton(self.add_data_frame)
        self.add_data_btn.setObjectName(u"add_data_btn")
        self.add_data_btn.setEnabled(True)
        self.add_data_btn.setStyleSheet(u"QPushButton{\n"
"background: rgba(255, 255, 255, 50);\n"
"border-radius: 20px;\n"
"height: 50px;\n"
"padding: 0 10px;\n"
"font-size:30px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid rgba(78,87,84, 200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(78,87,84, 200)\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_data_btn.setIcon(icon)
        self.add_data_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.add_data_btn)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.gridLayout.addWidget(self.add_data_frame, 0, 0, 1, 1)

        self.pagination_frame = QFrame(self.centralwidget)
        self.pagination_frame.setObjectName(u"pagination_frame")
        self.pagination_frame.setMinimumSize(QSize(700, 0))
        self.pagination_frame.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_5 = QHBoxLayout(self.pagination_frame)
        self.horizontalLayout_5.setSpacing(50)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.paginate_btn = QFrame(self.pagination_frame)
        self.paginate_btn.setObjectName(u"paginate_btn")
        self.paginate_btn.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_4 = QHBoxLayout(self.paginate_btn)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.prev_page_btn = QPushButton(self.paginate_btn)
        self.prev_page_btn.setObjectName(u"prev_page_btn")
        self.prev_page_btn.setStyleSheet(u"QPushButton{\n"
"background: rgba(255, 255, 255, 50);\n"
"border-radius: 20px;\n"
"height: 50px;\n"
"padding: 0 10px;\n"
"font-size:20px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid rgba(78,87,84, 200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(78,87,84, 200)\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/prev.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prev_page_btn.setIcon(icon1)
        self.prev_page_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.prev_page_btn)

        self.next_page_btn = QPushButton(self.paginate_btn)
        self.next_page_btn.setObjectName(u"next_page_btn")
        self.next_page_btn.setStyleSheet(u"QPushButton{\n"
"background: rgba(255, 255, 255, 50);\n"
"border-radius: 20px;\n"
"height: 50px;\n"
"padding: 0 10px;\n"
"font-size:20px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid rgba(78,87,84, 200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(78,87,84, 200)\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/next.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.next_page_btn.setIcon(icon2)
        self.next_page_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.next_page_btn)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

        self.horizontalLayout_5.addWidget(self.paginate_btn)

        self.paginate_page = QFrame(self.pagination_frame)
        self.paginate_page.setObjectName(u"paginate_page")
        self.paginate_page.setMaximumSize(QSize(16777215, 50))
        self.paginate_page.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_3 = QHBoxLayout(self.paginate_page)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.curent_page = QLabel(self.paginate_page)
        self.curent_page.setObjectName(u"curent_page")
        self.curent_page.setMinimumSize(QSize(0, 0))
        self.curent_page.setBaseSize(QSize(0, 50))
        self.curent_page.setStyleSheet(u"background: rgba(255, 255, 255, 50);\n"
"border-radius: 20px;\n"
"height: 50px;\n"
"padding: 0 10px;\n"
"font-size:20px;\n"
"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout_3.addWidget(self.curent_page)

        self.total_pages = QLabel(self.paginate_page)
        self.total_pages.setObjectName(u"total_pages")
        self.total_pages.setStyleSheet(u"background: rgba(255, 255, 255, 50);\n"
"border-radius: 20px;\n"
"height: 50px;\n"
"padding: 0 10px;\n"
"font-size:20px;\n"
"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout_3.addWidget(self.total_pages)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)

        self.horizontalLayout_5.addWidget(self.paginate_page)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 4)

        self.gridLayout.addWidget(self.pagination_frame, 3, 0, 1, 1)

        self.get_data_frame = QWidget(self.centralwidget)
        self.get_data_frame.setObjectName(u"get_data_frame")
        self.get_data_frame.setStyleSheet(u"background: rgba(255, 255, 255, 50);\n"
"border-radius: 20px;")
        self.horizontalLayout_2 = QHBoxLayout(self.get_data_frame)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.get_data_btn = QPushButton(self.get_data_frame)
        self.get_data_btn.setObjectName(u"get_data_btn")
        self.get_data_btn.setStyleSheet(u"QPushButton{\n"
"background: rgba(255, 255, 255, 50);\n"
"border-radius: 20px;\n"
"height: 50px;\n"
"padding: 0 10px;\n"
"font-size:30px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid rgba(78,87,84, 200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(78,87,84, 200)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/data.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.get_data_btn.setIcon(icon3)
        self.get_data_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.get_data_btn)

        self.page_count = QSpinBox(self.get_data_frame)
        self.page_count.setObjectName(u"page_count")
        self.page_count.setStyleSheet(u"QSpinBox {\n"
"padding: 0 10px;\n"
"border-radius: 7px;\n"
"height: 50px;\n"
"font-size:20px;\n"
"color: white;\n"
"}\n"
"\n"
"QSpinBox:hover{\n"
"border: 2px solid rgba(78,87,84, 200)\n"
"}")
        self.page_count.setMinimum(1)
        self.page_count.setMaximum(10)
        self.page_count.setValue(10)

        self.horizontalLayout_2.addWidget(self.page_count)

        self.total_data = QLabel(self.get_data_frame)
        self.total_data.setObjectName(u"total_data")
        self.total_data.setStyleSheet(u"\n"
"background: rgba(255, 255, 255, 50);\n"
"border-radius: 20px;\n"
"height: 50px;\n"
"padding: 0 10px;\n"
"font-size:30px;\n"
"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout_2.addWidget(self.total_data)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(2, 4)

        self.gridLayout.addWidget(self.get_data_frame, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_data_text.setText("")
        self.add_data_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"add your data", None))
#if QT_CONFIG(whatsthis)
        self.add_data_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041a\u043d\u043e\u043f\u043a\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0434\u0430\u0442\u044b</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.add_data_btn.setText(QCoreApplication.translate("MainWindow", u"Add Data", None))
        self.prev_page_btn.setText("")
        self.next_page_btn.setText("")
        self.curent_page.setText(QCoreApplication.translate("MainWindow", u"Current Page: 1", None))
        self.total_pages.setText(QCoreApplication.translate("MainWindow", u"Total Pages: 10", None))
        self.get_data_btn.setText(QCoreApplication.translate("MainWindow", u"Get Data", None))
        self.page_count.setSuffix("")
        self.page_count.setPrefix(QCoreApplication.translate("MainWindow", u"on page: ", None))
        self.total_data.setText(QCoreApplication.translate("MainWindow", u"Total Data: 255", None))
    # retranslateUi

