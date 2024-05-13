# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainEKfMmA.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)
from . resources import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1309, 740)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.styleSheet.sizePolicy().hasHeightForWidth())
        self.styleSheet.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setSizeConstraint(QLayout.SetMaximumSize)
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        sizePolicy.setHeightForWidth(self.bgApp.sizePolicy().hasHeightForWidth())
        self.bgApp.setSizePolicy(sizePolicy)
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        sizePolicy.setHeightForWidth(self.leftMenuBg.sizePolicy().hasHeightForWidth())
        self.leftMenuBg.setSizePolicy(sizePolicy)
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setWeight(QFont.Normal)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        sizePolicy.setHeightForWidth(self.leftMenuFrame.sizePolicy().hasHeightForWidth())
        self.leftMenuFrame.setSizePolicy(sizePolicy)
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        sizePolicy.setHeightForWidth(self.topMenu.sizePolicy().hasHeightForWidth())
        self.topMenu.setSizePolicy(sizePolicy)
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy1.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy1)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-image1.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy1.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy1)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-settings.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy1.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy1)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-laptop.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy1.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy1)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy1.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy1)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        sizePolicy.setHeightForWidth(self.extraLeftBox.sizePolicy().hasHeightForWidth())
        self.extraLeftBox.setSizePolicy(sizePolicy)
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        sizePolicy.setHeightForWidth(self.extraTopBg.sizePolicy().hasHeightForWidth())
        self.extraTopBg.setSizePolicy(sizePolicy)
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        sizePolicy.setHeightForWidth(self.extraTopMenu.sizePolicy().hasHeightForWidth())
        self.extraTopMenu.setSizePolicy(sizePolicy)
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy1.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy1)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy1.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy1)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy1.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy1)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        sizePolicy.setHeightForWidth(self.extraCenter.sizePolicy().hasHeightForWidth())
        self.extraCenter.setSizePolicy(sizePolicy)
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetNoConstraint)
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        sizePolicy.setHeightForWidth(self.contentBox.sizePolicy().hasHeightForWidth())
        self.contentBox.setSizePolicy(sizePolicy)
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        sizePolicy.setHeightForWidth(self.contentTopBg.sizePolicy().hasHeightForWidth())
        self.contentTopBg.setSizePolicy(sizePolicy)
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(False)
        font3.setItalic(False)
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setStyleSheet(u"font-size: 15px;\n"
"")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        sizePolicy.setHeightForWidth(self.rightButtons.sizePolicy().hasHeightForWidth())
        self.rightButtons.setSizePolicy(sizePolicy)
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        sizePolicy.setHeightForWidth(self.contentBottom.sizePolicy().hasHeightForWidth())
        self.contentBottom.setSizePolicy(sizePolicy)
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        sizePolicy.setHeightForWidth(self.pagesContainer.sizePolicy().hasHeightForWidth())
        self.pagesContainer.setSizePolicy(sizePolicy)
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setLineWidth(-1)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.start_setting = QPushButton(self.home)
        self.start_setting.setObjectName(u"start_setting")
        self.start_setting.setGeometry(QRect(1000, 410, 131, 61))
        self.start_setting.setStyleSheet(u"background: transparent;/* \u8bbe\u7f6e\u6309\u94ae\u7684\u80cc\u666f\u4e3a\u900f\u660e */background-color: rgb(52, 59, 72);color: white; /* \u8bbe\u7f6e\u6587\u672c\u989c\u8272\u4e3a\u767d\u8272 */\n"
"    font-size: 16px; /* \u8bbe\u7f6e\u5b57\u4f53\u5927\u5c0f */\n"
"    font-weight: bold; /* \u8bbe\u7f6e\u5b57\u4f53\u4e3a\u7c97\u4f53 */\n"
"    border: 2px solid #324B58; /* \u8bbe\u7f6e\u8fb9\u6846\u5bbd\u5ea6\u548c\u989c\u8272 */\n"
"    border-radius: 5px; /* \u8bbe\u7f6e\u8fb9\u6846\u7684\u5706\u89d2\u5927\u5c0f */\n"
"    padding: 5px; /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */\n"
"    text-align: center; /* \u8bbe\u7f6e\u6587\u672c\u5c45\u4e2d\u5bf9\u9f50 */")
        self.start_train = QPushButton(self.home)
        self.start_train.setObjectName(u"start_train")
        self.start_train.setGeometry(QRect(1000, 500, 131, 61))
        self.start_train.setStyleSheet(u"background: transparent;/* \u8bbe\u7f6e\u6309\u94ae\u7684\u80cc\u666f\u4e3a\u900f\u660e */background-color: rgb(52, 59, 72);color: white; /* \u8bbe\u7f6e\u6587\u672c\u989c\u8272\u4e3a\u767d\u8272 */\n"
"    font-size: 16px; /* \u8bbe\u7f6e\u5b57\u4f53\u5927\u5c0f */\n"
"    font-weight: bold; /* \u8bbe\u7f6e\u5b57\u4f53\u4e3a\u7c97\u4f53 */\n"
"    border: 2px solid #324B58; /* \u8bbe\u7f6e\u8fb9\u6846\u5bbd\u5ea6\u548c\u989c\u8272 */\n"
"    border-radius: 5px; /* \u8bbe\u7f6e\u8fb9\u6846\u7684\u5706\u89d2\u5927\u5c0f */\n"
"    padding: 5px; /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */\n"
"    text-align: center; /* \u8bbe\u7f6e\u6587\u672c\u5c45\u4e2d\u5bf9\u9f50 */")
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        sizePolicy.setHeightForWidth(self.widgets.sizePolicy().hasHeightForWidth())
        self.widgets.setSizePolicy(sizePolicy)
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.row_1.sizePolicy().hasHeightForWidth())
        self.row_1.setSizePolicy(sizePolicy2)
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        sizePolicy.setHeightForWidth(self.frame_div_content_1.sizePolicy().hasHeightForWidth())
        self.frame_div_content_1.setSizePolicy(sizePolicy)
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        sizePolicy.setHeightForWidth(self.frame_title_wid_1.sizePolicy().hasHeightForWidth())
        self.frame_title_wid_1.setSizePolicy(sizePolicy)
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_title_wid_1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetNoConstraint)
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        sizePolicy.setHeightForWidth(self.labelBoxBlenderInstalation.sizePolicy().hasHeightForWidth())
        self.labelBoxBlenderInstalation.setSizePolicy(sizePolicy)
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        sizePolicy.setHeightForWidth(self.frame_content_wid_1.sizePolicy().hasHeightForWidth())
        self.frame_content_wid_1.setSizePolicy(sizePolicy)
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.select_file = QPushButton(self.frame_content_wid_1)
        self.select_file.setObjectName(u"select_file")
        sizePolicy2.setHeightForWidth(self.select_file.sizePolicy().hasHeightForWidth())
        self.select_file.setSizePolicy(sizePolicy2)
        self.select_file.setMinimumSize(QSize(150, 30))
        self.select_file.setFont(font)
        self.select_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.select_file.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.select_file.setIcon(icon4)
        self.select_file.setAutoExclusive(False)

        self.gridLayout.addWidget(self.select_file, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(5)
        sizePolicy3.setVerticalStretch(2)
        sizePolicy3.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy3)
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        sizePolicy2.setHeightForWidth(self.labelVersion_3.sizePolicy().hasHeightForWidth())
        self.labelVersion_3.setSizePolicy(sizePolicy2)
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(10)
        sizePolicy4.setHeightForWidth(self.row_2.sizePolicy().hasHeightForWidth())
        self.row_2.setSizePolicy(sizePolicy4)
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.cloud_rebuid = QCheckBox(self.row_2)
        self.cloud_rebuid.setObjectName(u"cloud_rebuid")
        sizePolicy2.setHeightForWidth(self.cloud_rebuid.sizePolicy().hasHeightForWidth())
        self.cloud_rebuid.setSizePolicy(sizePolicy2)
        self.cloud_rebuid.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.cloud_rebuid, 0, 1, 1, 1)

        self.model_select_label = QLabel(self.row_2)
        self.model_select_label.setObjectName(u"model_select_label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(2)
        sizePolicy5.setHeightForWidth(self.model_select_label.sizePolicy().hasHeightForWidth())
        self.model_select_label.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.model_select_label, 3, 0, 1, 1)

        self.photo_count_label = QLabel(self.row_2)
        self.photo_count_label.setObjectName(u"photo_count_label")
        sizePolicy5.setHeightForWidth(self.photo_count_label.sizePolicy().hasHeightForWidth())
        self.photo_count_label.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.photo_count_label, 1, 0, 1, 1)

        self.local_rebuid = QCheckBox(self.row_2)
        self.local_rebuid.setObjectName(u"local_rebuid")
        sizePolicy2.setHeightForWidth(self.local_rebuid.sizePolicy().hasHeightForWidth())
        self.local_rebuid.setSizePolicy(sizePolicy2)
        self.local_rebuid.setAutoFillBackground(False)
        self.local_rebuid.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.local_rebuid, 0, 0, 1, 1)

        self.model_select = QComboBox(self.row_2)
        self.model_select.addItem("")
        self.model_select.addItem("")
        self.model_select.addItem("")
        self.model_select.addItem("")
        self.model_select.setObjectName(u"model_select")
        sizePolicy5.setHeightForWidth(self.model_select.sizePolicy().hasHeightForWidth())
        self.model_select.setSizePolicy(sizePolicy5)
        self.model_select.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"color: white; /* \u4fee\u6539\u4e0b\u62c9\u5217\u8868\u9879\u7684\u5b57\u4f53\u989c\u8272\u4e3a\u767d\u8272 */\n"
"")

        self.gridLayout_2.addWidget(self.model_select, 3, 1, 1, 1)

        self.photo_select = QComboBox(self.row_2)
        self.photo_select.addItem("")
        self.photo_select.addItem("")
        self.photo_select.setObjectName(u"photo_select")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(2)
        sizePolicy6.setVerticalStretch(2)
        sizePolicy6.setHeightForWidth(self.photo_select.sizePolicy().hasHeightForWidth())
        self.photo_select.setSizePolicy(sizePolicy6)
        self.photo_select.setFont(font)
        self.photo_select.setAutoFillBackground(False)
        self.photo_select.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"color: white; /* \u4fee\u6539\u4e0b\u62c9\u5217\u8868\u9879\u7684\u5b57\u4f53\u989c\u8272\u4e3a\u767d\u8272 */")
        self.photo_select.setIconSize(QSize(16, 16))
        self.photo_select.setFrame(True)

        self.gridLayout_2.addWidget(self.photo_select, 2, 1, 1, 1)

        self.photo_select_label = QLabel(self.row_2)
        self.photo_select_label.setObjectName(u"photo_select_label")
        sizePolicy5.setHeightForWidth(self.photo_select_label.sizePolicy().hasHeightForWidth())
        self.photo_select_label.setSizePolicy(sizePolicy5)
        self.photo_select_label.setStyleSheet(u"text-align: center; /* \u5c45\u4e2d\u6587\u672c */")

        self.gridLayout_2.addWidget(self.photo_select_label, 2, 0, 1, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(8)
        sizePolicy7.setVerticalStretch(4)
        sizePolicy7.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy7)
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(4)
        sizePolicy8.setVerticalStretch(4)
        sizePolicy8.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy8)
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setSizeConstraint(QLayout.SetNoConstraint)
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy8.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy8)
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 2, 7, 1)

        self.photo_sum = QTextEdit(self.row_2)
        self.photo_sum.setObjectName(u"photo_sum")
        sizePolicy5.setHeightForWidth(self.photo_sum.sizePolicy().hasHeightForWidth())
        self.photo_sum.setSizePolicy(sizePolicy5)
        self.photo_sum.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.photo_sum.setReadOnly(True)
        self.photo_sum.setOverwriteMode(False)

        self.gridLayout_2.addWidget(self.photo_sum, 1, 1, 1, 1)

        self.epoch_select_label = QLabel(self.row_2)
        self.epoch_select_label.setObjectName(u"epoch_select_label")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(2)
        sizePolicy9.setHeightForWidth(self.epoch_select_label.sizePolicy().hasHeightForWidth())
        self.epoch_select_label.setSizePolicy(sizePolicy9)

        self.gridLayout_2.addWidget(self.epoch_select_label, 4, 0, 1, 1)

        self.epoch_select = QComboBox(self.row_2)
        self.epoch_select.addItem("")
        self.epoch_select.addItem("")
        self.epoch_select.addItem("")
        self.epoch_select.setObjectName(u"epoch_select")
        sizePolicy5.setHeightForWidth(self.epoch_select.sizePolicy().hasHeightForWidth())
        self.epoch_select.setSizePolicy(sizePolicy5)
        self.epoch_select.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"color: white; /* \u4fee\u6539\u4e0b\u62c9\u5217\u8868\u9879\u7684\u5b57\u4f53\u989c\u8272\u4e3a\u767d\u8272 */\n"
"")

        self.gridLayout_2.addWidget(self.epoch_select, 4, 1, 1, 1)

        self.start_construction = QPushButton(self.row_2)
        self.start_construction.setObjectName(u"start_construction")
        sizePolicy.setHeightForWidth(self.start_construction.sizePolicy().hasHeightForWidth())
        self.start_construction.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.start_construction, 5, 0, 3, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        sizePolicy2.setHeightForWidth(self.row_3.sizePolicy().hasHeightForWidth())
        self.row_3.setSizePolicy(sizePolicy2)
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.log = QPlainTextEdit(self.row_3)
        self.log.setObjectName(u"log")
        self.log.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.log, 0, 0, 1, 1)


        self.horizontalLayout_12.addLayout(self.gridLayout_3)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setSizeConstraint(QLayout.SetNoConstraint)
        self.row_4 = QFrame(self.new_page)
        self.row_4.setObjectName(u"row_4")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(5)
        sizePolicy10.setHeightForWidth(self.row_4.sizePolicy().hasHeightForWidth())
        self.row_4.setSizePolicy(sizePolicy10)
        self.verticalLayout_18 = QVBoxLayout(self.row_4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_ssh_userpasswd = QLabel(self.row_4)
        self.label_ssh_userpasswd.setObjectName(u"label_ssh_userpasswd")
        sizePolicy2.setHeightForWidth(self.label_ssh_userpasswd.sizePolicy().hasHeightForWidth())
        self.label_ssh_userpasswd.setSizePolicy(sizePolicy2)
        self.label_ssh_userpasswd.setStyleSheet(u"font-size: 20px;\n"
"font-family: 'Arial';")

        self.gridLayout_4.addWidget(self.label_ssh_userpasswd, 7, 0, 1, 1)

        self.label_ssh_username = QLabel(self.row_4)
        self.label_ssh_username.setObjectName(u"label_ssh_username")
        sizePolicy2.setHeightForWidth(self.label_ssh_username.sizePolicy().hasHeightForWidth())
        self.label_ssh_username.setSizePolicy(sizePolicy2)
        self.label_ssh_username.setStyleSheet(u"font-size: 20px;\n"
"font-family: 'Arial';")

        self.gridLayout_4.addWidget(self.label_ssh_username, 4, 0, 1, 1)

        self.label_ssh_dir = QLabel(self.row_4)
        self.label_ssh_dir.setObjectName(u"label_ssh_dir")
        sizePolicy2.setHeightForWidth(self.label_ssh_dir.sizePolicy().hasHeightForWidth())
        self.label_ssh_dir.setSizePolicy(sizePolicy2)
        self.label_ssh_dir.setStyleSheet(u"font-size: 20px;\n"
"font-family: 'Arial';")

        self.gridLayout_4.addWidget(self.label_ssh_dir, 3, 0, 1, 1)

        self.label_ssh_IP = QLabel(self.row_4)
        self.label_ssh_IP.setObjectName(u"label_ssh_IP")
        sizePolicy2.setHeightForWidth(self.label_ssh_IP.sizePolicy().hasHeightForWidth())
        self.label_ssh_IP.setSizePolicy(sizePolicy2)
        self.label_ssh_IP.setStyleSheet(u"font-size: 20px;\n"
"font-family: 'Arial';")

        self.gridLayout_4.addWidget(self.label_ssh_IP, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.row_4)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy11.setHorizontalStretch(1)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy11)
        self.pushButton.setStyleSheet(u"background: transparent;/* \u8bbe\u7f6e\u6309\u94ae\u7684\u80cc\u666f\u4e3a\u900f\u660e */background-color: rgb(52, 59, 72);color: white; /* \u8bbe\u7f6e\u6587\u672c\u989c\u8272\u4e3a\u767d\u8272 */\n"
"    font-size: 16px; /* \u8bbe\u7f6e\u5b57\u4f53\u5927\u5c0f */\n"
"    font-weight: bold; /* \u8bbe\u7f6e\u5b57\u4f53\u4e3a\u7c97\u4f53 */\n"
"    border: 2px solid #324B58; /* \u8bbe\u7f6e\u8fb9\u6846\u5bbd\u5ea6\u548c\u989c\u8272 */\n"
"    border-radius: 5px; /* \u8bbe\u7f6e\u8fb9\u6846\u7684\u5706\u89d2\u5927\u5c0f */\n"
"    padding: 5px; /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */\n"
"    text-align: center; /* \u8bbe\u7f6e\u6587\u672c\u5c45\u4e2d\u5bf9\u9f50 */\n"
"font-size: 20px;\n"
"font-family: 'Arial';\n"
"font-weight: bold;")

        self.gridLayout_4.addWidget(self.pushButton, 2, 3, 3, 1)

        self.label_ssh_conda = QLabel(self.row_4)
        self.label_ssh_conda.setObjectName(u"label_ssh_conda")
        sizePolicy2.setHeightForWidth(self.label_ssh_conda.sizePolicy().hasHeightForWidth())
        self.label_ssh_conda.setSizePolicy(sizePolicy2)
        self.label_ssh_conda.setStyleSheet(u"font-size: 20px;\n"
"font-family: 'Arial';")

        self.gridLayout_4.addWidget(self.label_ssh_conda, 8, 0, 1, 1)

        self.ssh_save = QPushButton(self.row_4)
        self.ssh_save.setObjectName(u"ssh_save")
        sizePolicy11.setHeightForWidth(self.ssh_save.sizePolicy().hasHeightForWidth())
        self.ssh_save.setSizePolicy(sizePolicy11)
        self.ssh_save.setStyleSheet(u"background: transparent;/* \u8bbe\u7f6e\u6309\u94ae\u7684\u80cc\u666f\u4e3a\u900f\u660e */background-color: rgb(52, 59, 72);color: white; /* \u8bbe\u7f6e\u6587\u672c\u989c\u8272\u4e3a\u767d\u8272 */\n"
"    font-size: 16px; /* \u8bbe\u7f6e\u5b57\u4f53\u5927\u5c0f */\n"
"    font-weight: bold; /* \u8bbe\u7f6e\u5b57\u4f53\u4e3a\u7c97\u4f53 */\n"
"    border: 2px solid #324B58; /* \u8bbe\u7f6e\u8fb9\u6846\u5bbd\u5ea6\u548c\u989c\u8272 */\n"
"    border-radius: 5px; /* \u8bbe\u7f6e\u8fb9\u6846\u7684\u5706\u89d2\u5927\u5c0f */\n"
"    padding: 5px; /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */\n"
"    text-align: center; /* \u8bbe\u7f6e\u6587\u672c\u5c45\u4e2d\u5bf9\u9f50 */\n"
"font-size: 20px;\n"
"font-family: 'Arial';\n"
"font-weight: bold;")

        self.gridLayout_4.addWidget(self.ssh_save, 6, 3, 3, 1)

        self.lineEdit_2 = QLineEdit(self.row_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy12.setHorizontalStretch(3)
        sizePolicy12.setVerticalStretch(1)
        sizePolicy12.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy12)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.lineEdit_2, 2, 1, 1, 2)

        self.lineEdit_3 = QLineEdit(self.row_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy12.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy12)
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.lineEdit_3, 3, 1, 1, 2)

        self.lineEdit_4 = QLineEdit(self.row_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy12.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy12)
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.lineEdit_4, 4, 1, 1, 2)

        self.lineEdit_5 = QLineEdit(self.row_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy12.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy12)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.lineEdit_5.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.lineEdit_5.setEchoMode(QLineEdit.Password)

        self.gridLayout_4.addWidget(self.lineEdit_5, 7, 1, 1, 2)

        self.lineEdit_6 = QLineEdit(self.row_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy12.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy12)
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.lineEdit_6, 8, 1, 1, 2)


        self.verticalLayout_18.addLayout(self.gridLayout_4)


        self.verticalLayout_20.addWidget(self.row_4)

        self.row_5 = QFrame(self.new_page)
        self.row_5.setObjectName(u"row_5")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(3)
        sizePolicy13.setHeightForWidth(self.row_5.sizePolicy().hasHeightForWidth())
        self.row_5.setSizePolicy(sizePolicy13)
        self.verticalLayout_22 = QVBoxLayout(self.row_5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_key = QLabel(self.row_5)
        self.label_key.setObjectName(u"label_key")
        sizePolicy2.setHeightForWidth(self.label_key.sizePolicy().hasHeightForWidth())
        self.label_key.setSizePolicy(sizePolicy2)
        self.label_key.setStyleSheet(u"font-size: 20px;\n"
"font-family: 'Arial';")

        self.gridLayout_5.addWidget(self.label_key, 3, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.row_5)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy14.setHorizontalStretch(5)
        sizePolicy14.setVerticalStretch(1)
        sizePolicy14.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy14)
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.lineEdit_7.setEchoMode(QLineEdit.Normal)

        self.gridLayout_5.addWidget(self.lineEdit_7, 0, 1, 1, 1)

        self.label_dir = QLabel(self.row_5)
        self.label_dir.setObjectName(u"label_dir")
        sizePolicy2.setHeightForWidth(self.label_dir.sizePolicy().hasHeightForWidth())
        self.label_dir.setSizePolicy(sizePolicy2)
        self.label_dir.setStyleSheet(u"font-size: 20px;\n"
"font-family: 'Arial';")

        self.gridLayout_5.addWidget(self.label_dir, 2, 0, 1, 1)

        self.local_save = QPushButton(self.row_5)
        self.local_save.setObjectName(u"local_save")
        sizePolicy11.setHeightForWidth(self.local_save.sizePolicy().hasHeightForWidth())
        self.local_save.setSizePolicy(sizePolicy11)
        self.local_save.setStyleSheet(u"background: transparent;/* \u8bbe\u7f6e\u6309\u94ae\u7684\u80cc\u666f\u4e3a\u900f\u660e */background-color: rgb(52, 59, 72);color: white; /* \u8bbe\u7f6e\u6587\u672c\u989c\u8272\u4e3a\u767d\u8272 */\n"
"    font-size: 16px; /* \u8bbe\u7f6e\u5b57\u4f53\u5927\u5c0f */\n"
"    font-weight: bold; /* \u8bbe\u7f6e\u5b57\u4f53\u4e3a\u7c97\u4f53 */\n"
"    border: 2px solid #324B58; /* \u8bbe\u7f6e\u8fb9\u6846\u5bbd\u5ea6\u548c\u989c\u8272 */\n"
"    border-radius: 5px; /* \u8bbe\u7f6e\u8fb9\u6846\u7684\u5706\u89d2\u5927\u5c0f */\n"
"    padding: 5px; /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */\n"
"    text-align: center; /* \u8bbe\u7f6e\u6587\u672c\u5c45\u4e2d\u5bf9\u9f50 */\n"
"font-size: 20px;\n"
"font-family: 'Arial';\n"
"font-weight: bold;")

        self.gridLayout_5.addWidget(self.local_save, 3, 2, 1, 1)

        self.lineEdit_9 = QLineEdit(self.row_5)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy14.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy14)
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.lineEdit_9.setEchoMode(QLineEdit.Password)

        self.gridLayout_5.addWidget(self.lineEdit_9, 3, 1, 1, 1)

        self.model_view = QPushButton(self.row_5)
        self.model_view.setObjectName(u"model_view")
        sizePolicy11.setHeightForWidth(self.model_view.sizePolicy().hasHeightForWidth())
        self.model_view.setSizePolicy(sizePolicy11)
        self.model_view.setStyleSheet(u"background: transparent;/* \u8bbe\u7f6e\u6309\u94ae\u7684\u80cc\u666f\u4e3a\u900f\u660e */background-color: rgb(52, 59, 72);color: white; /* \u8bbe\u7f6e\u6587\u672c\u989c\u8272\u4e3a\u767d\u8272 */\n"
"    font-size: 16px; /* \u8bbe\u7f6e\u5b57\u4f53\u5927\u5c0f */\n"
"    font-weight: bold; /* \u8bbe\u7f6e\u5b57\u4f53\u4e3a\u7c97\u4f53 */\n"
"    border: 2px solid #324B58; /* \u8bbe\u7f6e\u8fb9\u6846\u5bbd\u5ea6\u548c\u989c\u8272 */\n"
"    border-radius: 5px; /* \u8bbe\u7f6e\u8fb9\u6846\u7684\u5706\u89d2\u5927\u5c0f */\n"
"    padding: 5px; /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */\n"
"    text-align: center; /* \u8bbe\u7f6e\u6587\u672c\u5c45\u4e2d\u5bf9\u9f50 */\n"
"font-size: 20px;\n"
"font-family: 'Arial';\n"
"font-weight: bold;\n"
"")

        self.gridLayout_5.addWidget(self.model_view, 0, 2, 3, 1)

        self.lineEdit_8 = QLineEdit(self.row_5)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy15.setHorizontalStretch(4)
        sizePolicy15.setVerticalStretch(1)
        sizePolicy15.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy15)
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.lineEdit_8, 2, 1, 1, 1)

        self.label_python = QLabel(self.row_5)
        self.label_python.setObjectName(u"label_python")
        sizePolicy2.setHeightForWidth(self.label_python.sizePolicy().hasHeightForWidth())
        self.label_python.setSizePolicy(sizePolicy2)
        self.label_python.setStyleSheet(u"font-size: 20px;\n"
"font-family: 'Arial';")

        self.gridLayout_5.addWidget(self.label_python, 0, 0, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout_5)


        self.verticalLayout_20.addWidget(self.row_5)

        self.row_6 = QFrame(self.new_page)
        self.row_6.setObjectName(u"row_6")
        sizePolicy13.setHeightForWidth(self.row_6.sizePolicy().hasHeightForWidth())
        self.row_6.setSizePolicy(sizePolicy13)
        self.verticalLayout_23 = QVBoxLayout(self.row_6)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.setting_log = QPlainTextEdit(self.row_6)
        self.setting_log.setObjectName(u"setting_log")
        sizePolicy13.setHeightForWidth(self.setting_log.sizePolicy().hasHeightForWidth())
        self.setting_log.setSizePolicy(sizePolicy13)
        self.setting_log.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_23.addWidget(self.setting_log)


        self.verticalLayout_20.addWidget(self.row_6)

        self.stackedWidget.addWidget(self.new_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy1.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy1)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy1.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy1)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        self.creditsLabel.setFont(font3)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
                        "o Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u5343\u6620\uff1a\u57fa\u4e8e\u9ad8\u65af\u55b7\u6e85\u7684\u7aef\u8fb9\u4e91\u7530\u91ce\u8003\u53e4\u4e09\u7ef4\u91cd\u5efa\u7cfb\u7edf", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.start_setting.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u8bbe\u7f6e", None))
        self.start_train.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u91cd\u5efa", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u8bad\u7ec3\u7167\u7247/\u89c6\u9891", None))
        self.select_file.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u8bad\u7ec3\u7167\u7247/\u89c6\u9891\u7684\u8def\u5f84", None))
        self.labelVersion_3.setText("")
        self.cloud_rebuid.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u7aef\u91cd\u5efa", None))
        self.model_select_label.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u5efa\u6a21\u578b\u9009\u62e9", None))
        self.photo_count_label.setText(QCoreApplication.translate("MainWindow", u"\u7167\u7247\u8ba1\u6570", None))
        self.local_rebuid.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u91cd\u5efa", None))
        self.model_select.setItemText(0, QCoreApplication.translate("MainWindow", u"Mip_Gaussian_splaating", None))
        self.model_select.setItemText(1, QCoreApplication.translate("MainWindow", u"Gaussian_splaating", None))
        self.model_select.setItemText(2, QCoreApplication.translate("MainWindow", u"Instant-NGP", None))
        self.model_select.setItemText(3, QCoreApplication.translate("MainWindow", u"Mip_NeRF_360", None))

        self.photo_select.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u6700\u597d\u7684\u7167\u7247\u96c6\u5408", None))
        self.photo_select.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u6240\u6709\u7684\u7167\u7247\u96c6\u5408", None))

        self.photo_select_label.setText(QCoreApplication.translate("MainWindow", u"\u7167\u7247\u9009\u62e9", None))
        self.epoch_select_label.setText(QCoreApplication.translate("MainWindow", u"\u8fed\u4ee3\u6b21\u6570", None))
        self.epoch_select.setItemText(0, QCoreApplication.translate("MainWindow", u"30 [Ksteps]", None))
        self.epoch_select.setItemText(1, QCoreApplication.translate("MainWindow", u"10 [Ksteps]", None))
        self.epoch_select.setItemText(2, QCoreApplication.translate("MainWindow", u"60 [Ksteps]", None))

        self.start_construction.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u91cd\u5efa", None))
        self.label_ssh_userpasswd.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u5bc6\u7801\uff1a", None))
        self.label_ssh_username.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u7528\u6237\u540d\uff1a", None))
        self.label_ssh_dir.setText(QCoreApplication.translate("MainWindow", u"\u8fdc\u7a0b\u6587\u4ef6\u5b58\u50a8\u76ee\u5f55\uff1a", None))
        self.label_ssh_IP.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668IP\u5730\u5740\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u8fde\u63a5", None))
        self.label_ssh_conda.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668Conda\u73af\u5883\u76ee\u5f55\uff1a", None))
        self.ssh_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u670d\u52a1\u5668\u914d\u7f6e", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"10.147.17.109", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"/home/yuyang/gaussian-splatting/data", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"yuyang", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"yuyang", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"/home/yuyang/anaconda3/bin/activate", None))
        self.label_key.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u5bc6\u94a5\uff1a", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"C:/Users/Lenovo/.conda/envs/gaussian_splatting/python.exe", None))
        self.label_dir.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u6587\u4ef6\u5b58\u50a8\u76ee\u5f55\uff1a", None))
        self.local_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u672c\u5730\u914d\u7f6e", None))
        self.lineEdit_9.setText(QCoreApplication.translate("MainWindow", u"sh_sichuanuniversity_qianyin_001", None))
        self.model_view.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u89c2\u5bdf", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"F:/3D_gaussian_splatting/gaussian-splatting/Modern_GUI_PyDracula_PySide6_or_PyQt6-master/data", None))
        self.label_python.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730Python\u73af\u5883\u76ee\u5f55\uff1a", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"\u5343\u6620\u56e2\u961f", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.2.3", None))
    # retranslateUi

