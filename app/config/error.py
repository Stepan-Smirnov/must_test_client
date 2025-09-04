# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 500)
        Form.setMinimumSize(QSize(800, 500))
        Form.setMaximumSize(QSize(800, 500))
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, \n"
"    stop:0 rgba(140, 140, 140, 255), \n"
"    stop:0.42 rgba(80, 0, 130, 235), \n"
"    stop:1 rgba(180, 120, 180, 255));\n"
"\n"
"font-family: Rubik;")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.error_layout = QFrame(Form)
        self.error_layout.setObjectName(u"error_layout")
        self.error_layout.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.error_layout)
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 30, 20)
        self.error_text = QLabel(self.error_layout)
        self.error_text.setObjectName(u"error_text")
        self.error_text.setStyleSheet(u"\n"
"background: rgba(255, 255, 255, 50);\n"
"border-radius: 18px;\n"
"height: 50px;\n"
"padding: 0 10px;\n"
"font-size:30px;\n"
"color: red;\n"
"font-weight: bold;")

        self.verticalLayout.addWidget(self.error_text)

        self.error_btn = QPushButton(self.error_layout)
        self.error_btn.setObjectName(u"error_btn")
        self.error_btn.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout.addWidget(self.error_btn)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)

        self.gridLayout.addWidget(self.error_layout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"error message", None))
        self.error_text.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0438\u0437\u043e\u0448\u043b\u0430 \u043e\u0448\u0438\u0431\u043a\u0430, \u0441\u043a\u043e\u0440\u043e \u043c\u044b \u0432\u0441\u0435 \u043f\u043e\u043f\u0440\u0430\u0432\u0438\u043c", None))
        self.error_btn.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

