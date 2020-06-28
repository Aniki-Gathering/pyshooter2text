from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow, QMenu, QSystemTrayIcon
from Ui_setup import main2
from Ui_minimodel import main3
from Ui_main_screen import main1
from PyQt5.QtGui import QBrush, QIcon, QPalette, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
from system_hotkey import SystemHotkey
import search as sr
from configobj import ConfigObj
# import use.ScreenShooter as sct
import os
from use.OCR import GetText
from use.Translate import GetTranslation


class Ui_Dialog(QtWidgets.QWidget,main2):
    sig = pyqtSignal()
    sig1 = pyqtSignal(str)
    sig2 = pyqtSignal(str)
    def __init__(self):
        super(Ui_Dialog,self).__init__()
        self.setupUi(self)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(526, 439)
        self.label.adjustSize()
        self.initUI()
        
    def initUI(self):
        self.imshow.setPixmap(QPixmap('image/skin/'+self.comboBox.currentText()+'.png'))
        self.pushButton.clicked.connect(self.apply)
        self.pushButton_2.clicked.connect(self.cancel)
        config = ConfigObj("setup.ini",encoding='UTF8') 
        s1=config['keyboard_shortcut']['screenshot']
        s2=config['keyboard_shortcut']['minimodel']
        s3=config['background']['path']
        s4=config['setting']['minimize']
        s5=config['setting']['welcome']
        self.lineEdit.setText(s1)
        self.lineEdit_4.setText(s2)
        if(s4=='true'):
            self.radioButton.setChecked(True)
        else:
            self.radioButton_2.setChecked(True)
        if(s5=='true'):
            self.radioButton_3.setChecked(True)
        else:
            self.radioButton_4.setChecked(True) 
        self.comboBox.currentIndexChanged.connect(self.view)     
        #gview
    def apply(self):
        config = ConfigObj("setup.ini",encoding='UTF8')
        s1=config['keyboard_shortcut']['screenshot']
        s2=config['keyboard_shortcut']['minimodel']
        m1=str(self.lineEdit.text())
        m2=str(self.lineEdit_4.text())
        m3='image/skin/'+self.comboBox.currentText()+'.png'
        if m1!=m2:
            if m1!=config['keyboard_shortcut']['screenshot']:
                self.sig1.emit(s1)
                config['keyboard_shortcut']['screenshot'] = m1
            if m2!=config['keyboard_shortcut']['minimodel']:
                self.sig2.emit(s2)    
                config['keyboard_shortcut']['minimodel']= m2
        config['background']['path']=m3
        if self.radioButton.isChecked():
            config['setting']['minimize']='true'
        else:
            config['setting']['minimize']='false'
        if self.radioButton_3.isChecked():
            config['setting']['welcome']='true'
        else:
            config['setting']['welcome']='false'            
        config.write()
        self.sig.emit()
        self.close()
    def cancel(self):
        self.close()
    def view(self):
        self.imshow.setPixmap(QPixmap('image/skin/'+self.comboBox.currentText()+'.png'))
        
        

class MINI(QtWidgets.QWidget,main3):
    def __init__(self):
        super(MINI,self).__init__()
        self.setupUi(self)
        self.label.setAlignment(Qt.AlignTop)
        self.pushButton.clicked.connect(self.search_min)
    def search_min(self):
        self.label.setMaximumWidth(320)
        self.label.clear()
        self.resize(342,86)
        str1=self.lineEdit.text()
        result=[]
        tmpp=sr.analysis(sr.get_net(str(str1)))
        for word in tmpp:
            tmp=word
            if len(tmp)>21:
                while len(tmp)>21:
                    result.append(tmp[:21])
                    tmp=tmp[21:]
                result.append(tmp)    
            else:
                result.append(word)
        mean=('\n').join(result)
        
        
        self.label.setText(mean)  
    def closeEvent(self, event):
        event.ignore()
        self.hide()    

#主界面
class mainwindow(QtWidgets.QMainWindow,main1):
    hk = SystemHotkey()
    config = ConfigObj("setup.ini",encoding='UTF8')
    s1=config['keyboard_shortcut']['screenshot']
    s2=config['keyboard_shortcut']['minimodel']
    s3=config['background']['path']
    s4=config['setting']['minimize']
    s5=config['setting']['welcome']
    hotkey_sig = pyqtSignal()
    hotkey_sig0 = pyqtSignal()
    hotkey_sig1 = pyqtSignal()
    hotkey_sig2 = pyqtSignal()
    
    def __init__(self):
        super(mainwindow,self).__init__()
        self.hotkey_use()
        self.setFixedSize(757, 634)
        self.initUI()
    def initUI(self):
        self.config = ConfigObj("setup.ini",encoding='UTF8')
        self.s1=self.config['keyboard_shortcut']['screenshot']
        self.s2=self.config['keyboard_shortcut']['minimodel']
        self.s3=self.config['background']['path']
        self.s4=self.config['setting']['minimize']
        self.s5=self.config['setting']['welcome']
        #设置背景图片
        window_pale =QPalette()
        pix=QPixmap(self.s3)
        pix.scaled(self.width(),self.height()) 
        window_pale.setBrush(self.backgroundRole(), QBrush(pix)) 
        self.setPalette(window_pale)
        #
        self.hotkey_use_1(self.s1)
        self.hotkey_use_2(self.s2)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.prt_sc)
        self.pushButton_5.clicked.connect(self.translate)
        self.pushButton_4.clicked.connect(self.setup)
        self.pushButton_6.clicked.connect(self.search_single)
        self.pushButton_2.clicked.connect(self.open_min)
        self.pushButton_3.clicked.connect(self.copy)
        self.setWindowIcon(QIcon('image/ico.png')) 
        self.setWindowTitle("翻译软件测试版")
    #定义设置按钮的功能
    def setup(self):
        self.dia = Ui_Dialog()
        self.dia.sig.connect(self.initUI)
        self.dia.sig1.connect(lambda:self.hotkey_use_1)
        self.dia.sig2.connect(lambda:self.hotkey_use_2)
        self.dia.show()
    #定义min模式按钮    
    def open_min(self):
        self.mi=MINI()
        self.mi.show()
        self.tray_min()
        self.hide()
    #复制    
    def copy(self):
        strt=self.textBrowser_2.toPlainText()
        clipboard=QApplication.clipboard()
        clipboard.setText(str(strt))
    #截屏    
    def prt_sc(self):
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        self.showMinimized() 
        os.system("python ./use/ScreenShooter.py") # 改
        # strt2=GetText()
        # self.textBrowser.setText(strt2)
        # sct.prc()
        self.showNormal()
    #调用翻译函数    
    def translate(self):
        strt1=self.textBrowser.toPlainText()
        strt2=GetText()
        self.textBrowser.setText(strt2) # 改
        strt3=GetTranslation(strt2)
        self.textBrowser_2.setText(strt3)
        
    def search_single(self):
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        str1=self.lineEdit.text()
        self.textBrowser.setPlainText(str(str1))
        result=sr.analysis(sr.get_net(str(str1)))
        for i in result:
            self.textBrowser_2.append(i)
    #快捷键(全局热键)
    def hotkey_use(self):
        self.hotkey_sig.connect(self.MKey_pressEvent)
        self.hotkey_sig0.connect(self.open_min)
        m=self.s1.split('+')
        self.hk.register((m[0],m[1]),callback=lambda x:self.h_emit())
        n=self.s2.split('+')
        self.hk.register((n[0],n[1]),callback=lambda x:self.h0_emit())
    def hotkey_use_1(self,first):
        self.hotkey_sig1.connect(self.MKey_pressEvent)
        n=first.split('+')
        self.hk.unregister((n[0],n[1]))
        m=self.s1.split('+')
        self.hk.register((m[0],m[1]),callback=lambda x:self.h1_emit())
    def hotkey_use_2(self,second):
        self.hotkey_sig2.connect(self.open_min)
        n=second.split('+')
        self.hk.unregister((n[0],n[1]))
        m=self.s2.split('+')
        self.hk.register((m[0],m[1]),callback=lambda x:self.h2_emit())

    def MKey_pressEvent(self):
        # sct.prc()
        os.system("python ./use/ScreenShooter.py") # 改
    def h_emit(self):
        self.hotkey_sig.emit()
    def h0_emit(self):
        self.hotkey_sig0.emit()        
    def h1_emit(self):
        self.hotkey_sig1.emit()
    def h2_emit(self):
        self.hotkey_sig2.emit()    
    #托盘
    def tray_min(self):
        self.tray = QSystemTrayIcon() 
        self.icon = QIcon('image/ico.png')
        self.tray.activated.connect(self.iconActivated)
        self.tray.setIcon(self.icon)
        #气泡提示
        self.tray.setToolTip(u'翻译软件测试版')
        self.traymenu = QMenu()
        a1 =QAction(QIcon('image/re.png'), u'还原', self) #添加一级菜单动作选项(还原窗口程序)
        a1.triggered.connect(self.show)
        a2 =QAction(QIcon('image/exit.png'), u'退出', self) #添加一级菜单动作选项(退出程序)
        a2.triggered.connect(app.quit)
        self.traymenu.addAction(a2)
        self.traymenu.addAction(a1)
        self.tray.setContextMenu(self.traymenu)
        self.tray.show()
        self.tray.showMessage(u"", '应用已被最小化', icon=1)
    #点击托盘栏图标
    def iconActivated(self, ev):
        if ev == QSystemTrayIcon.Trigger:
            if self.isMinimized() or not self.isVisible():
                self.show()
            else: 
                self.hide()         
    #重写close事件    
    def closeEvent(self, event):
        if(self.s4=='true'):
            event.ignore() 
            self.hide()
            self.tray_min()
        else:
            pass     

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    first=mainwindow()
    first.show()
    sys.exit(app.exec_())

 