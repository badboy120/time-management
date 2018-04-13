# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
import math
from PyQt4.QtGui import *
from PyQt4.QtCore import *



class Timeschedule(QDialog):
    def __init__(self, parent):
        super(Timeschedule, self).__init__(parent)
        self.parent = parent
        self.resize(400,350)
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint)   
        self.setWindowOpacity(0.9)
        self.setWindowTitle('Time Mananger')

        self.headDict = {}
        self.headPostArrayKey = 0
        self.HeadGroupBox = QGroupBox('Time Schedule')
        self.HeadGroupBox.setMinimumHeight(100)  
        self.HeadGroupBox.scroll(100,2)
        self.HeadAddParam = QPushButton('+')
        self.HeadAddParam.setFixedSize(50,25)
        self.HeadRemoveParam = QPushButton('-')
        self.HeadRemoveParam.setFixedSize(50,25)
        self.headDict[str(self.headPostArrayKey)+'_from'] = QLineEdit()
        self.headDict[str(self.headPostArrayKey)+'_to'] = QLineEdit()
        self.HeadGroupBoxLayout = QGridLayout()
        self.HeadGroupBoxLayout.addWidget(self.HeadAddParam, 0, 0)
        self.HeadGroupBoxLayout.addWidget(self.HeadRemoveParam, 0, 1)
        self.HeadGroupBoxLayout.addWidget(QLabel('From'), 2, 0)
        self.HeadGroupBoxLayout.addWidget(self.headDict[str(self.headPostArrayKey)+'_from'], 2, 1)
        self.HeadGroupBoxLayout.addWidget(QLabel('To'), 2, 2)
        self.HeadGroupBoxLayout.addWidget(self.headDict[str(self.headPostArrayKey)+'_to'], 2, 3)
        worklabel = QLabel("Meeting", self)
        self.headDict[str(self.headPostArrayKey)+'_work']= worklabel
        self.HeadGroupBoxLayout.addWidget(QLabel('Work'), 2, 4) 
        self.HeadGroupBoxLayout.addWidget(self.combobox(worklabel),2,5)  
        self.HeadGroupBox.setLayout(self.HeadGroupBoxLayout)
        self.HeadAddParam.clicked.connect(self.addHeadParam) 
        self.HeadRemoveParam.clicked.connect(self.removeHeadParam)
        self.newline1,self.newline2,self.newline3,self.newline4,self.newline5,self.newline6 = [],[],[],[],[],[]

        
        self.hbLayout = QHBoxLayout()
        self.hbLayout.addStretch()

        self.btnPost = QPushButton('Submit')
        self.hbLayout.addWidget(self.btnPost)

        self.btnCal = QPushButton('Calculate')
        self.hbLayout.addWidget(self.btnCal)

        self.btnClear = QPushButton('Clear All')
        self.hbLayout.addWidget(self.btnClear)

        self.btnQuit = QPushButton('Quit')
        self.hbLayout.addWidget(self.btnQuit)
        self.connect(self.btnPost, SIGNAL('clicked()'), self.postData)
        self.countcal = 0
        self.connect(self.btnCal, SIGNAL('clicked()'), self.schedule_cal)
        self.connect(self.btnClear, SIGNAL('clicked()'), self.clearall)
        self.connect(self.btnQuit,SIGNAL('clicked()'),QCoreApplication.instance().quit)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.HeadGroupBox)
        main_layout.addLayout(self.hbLayout)
        main_layout.setSpacing(1)

        self.setLayout(main_layout)


    def combobox(self,worklabel):  
        combo = QComboBox(self)
        worklabel.move(400,400)
        f = open('list.txt','r')
        while True:
            line = f.readline()
            line = line.split('\n')[0]
            if line:
                combo.addItem(self.tr(line))  
            else:
                f.close()
                break  

     	def onActivated(text):	
			worklabel.setText(text) 
    
        self.connect(combo, SIGNAL('activated(QString)'), onActivated)

        return combo
      

    def postData(self):
        self.headdictdata={}
        for k, v in self.headDict.items():
            temp=k.split('_')
            if temp[1]=='from':
                if self.headdictdata.has_key(temp[0]):
                    self.headdictdata[temp[0]]['From'] =str(v.text())
                else:
                    self.headdictdata[temp[0]] = {'From':str(v.text())}

            elif temp[1]=='to':
                if self.headdictdata.has_key(temp[0]):
                    self.headdictdata[temp[0]]['To'] =str(v.text())
                else:
                    self.headdictdata[temp[0]] = {'To':str(v.text())}

            elif temp[1]=='work':
                if self.headdictdata.has_key(temp[0]):
                    self.headdictdata[temp[0]]['Work'] =str(v.text())
                else:
                    self.headdictdata[temp[0]] = {'Work':str(v.text())}
        
        f = open('data.txt','a')
        flag = 0
        for i in self.headdictdata:
            t1 = self.headdictdata[i]['From']
            t2 = self.headdictdata[i]['To']
            do = self.headdictdata[i]['Work']
            line = t1 + ' ' + t2 + ' ' + do
            if t1 == '' or t2 == '' or do == '':
                continue
            else:
                line = line + '\n'
                flag = 1
            f.write(line)
        if flag == 0:
            QMessageBox.about(self, 'Info', 'Submit fail, no input.')
        else:
            QMessageBox.about(self, 'Info', 'Submit Sccuess!')  
        f.close()



    def addHeadParam(self):
        sts=str(self.headPostArrayKey+1)
        self.headDict[sts+'_from'] = QLineEdit()
        self.headDict[sts+'_to'] = QLineEdit()
        self.newline1.append(QLabel('From'))
        self.newline2.append(self.headDict[sts+'_from'])
        self.newline3.append(QLabel('To'))
        self.newline4.append(self.headDict[sts+'_to'])
        worklabel = QLabel("Meeting", self)
        self.headDict[sts+'_work']= worklabel
        self.newline5.append(QLabel('Work'))   
        self.newline6.append(self.combobox(worklabel))  
        self.HeadGroupBoxLayout.addWidget(self.newline1[self.headPostArrayKey])
        self.HeadGroupBoxLayout.addWidget(self.newline2[self.headPostArrayKey])
        self.HeadGroupBoxLayout.addWidget(self.newline3[self.headPostArrayKey])
        self.HeadGroupBoxLayout.addWidget(self.newline4[self.headPostArrayKey])
        self.HeadGroupBoxLayout.addWidget(self.newline5[self.headPostArrayKey])
        self.HeadGroupBoxLayout.addWidget(self.newline6[self.headPostArrayKey])
        self.headPostArrayKey+=1

    def removeHeadParam(self):
        if self.headPostArrayKey==0:
            QMessageBox.about(self, 'Info', 'At least one input is needed.') 
            return
        self.headPostArrayKey-=1
        self.HeadGroupBoxLayout.removeWidget(self.newline1[self.headPostArrayKey])
        self.HeadGroupBoxLayout.removeWidget(self.newline2[self.headPostArrayKey])
        self.HeadGroupBoxLayout.removeWidget(self.newline3[self.headPostArrayKey])
        self.HeadGroupBoxLayout.removeWidget(self.newline4[self.headPostArrayKey])
        self.HeadGroupBoxLayout.removeWidget(self.newline5[self.headPostArrayKey])
        self.HeadGroupBoxLayout.removeWidget(self.newline6[self.headPostArrayKey])
        self.newline1[self.headPostArrayKey].deleteLater()
        self.newline1.pop()
        self.newline2[self.headPostArrayKey].deleteLater()
        self.newline2.pop()
        self.newline3[self.headPostArrayKey].deleteLater()
        self.newline3.pop()
        self.newline4[self.headPostArrayKey].deleteLater()
        self.newline4.pop()
        self.newline5[self.headPostArrayKey].deleteLater()
        self.newline5.pop()
        self.newline6[self.headPostArrayKey].deleteLater()
        self.newline6.pop()
        self.headDict.pop(str(self.headPostArrayKey+1)+'_from')
        self.headDict.pop(str(self.headPostArrayKey+1)+'_to')
        self.headDict.pop(str(self.headPostArrayKey+1)+'_work')



    def clearall(self):
        f = open('data.txt','w')
        f.close()
        QMessageBox.about(self, 'Info', 'Data all cleared.') 

    def schedule_cal(self):
        self.countcal += 1
        f = open('data.txt','r')
        n = 0
        schedule = []
        do = []
        count = []
        while True:
            line = f.readline()
            if line:
                t1,t2,t3 = line.split()
                t1 = t1.split(':')
                t2 = t2.split(':')
                if len(t1)==2:
                    t1 = float(t1[0])+float(t1[1])/60
                else:
                    t1 = float(t1[0])
                if len(t2)==2:
                    t2 = float(t2[0])+float(t2[1])/60
                else:
                    t2 = float(t2[0])
                schedule.append([t1,t2,t3])
                n+=1
            else:
                f.close()
                break

        for i in range(n):
            if schedule[i][2] in do:
                j = do.index(schedule[i][2])
                count[j]+=schedule[i][1]-schedule[i][0]
            else:
                do.append(schedule[i][2])
                count.append(schedule[i][1]-schedule[i][0])
        print 'Result No.'+str(self.countcal)+':\n'
        for i in range(len(do)):
            print do[i],str(int(math.floor(count[i])))+'h'+str(int(round((count[i]-math.floor(count[i]))*60)))+'m'
        QMessageBox.about(self, 'Info', 'Result is in next tab.') 
        print '\n'

class EmittingStream(QObject):  
        textWritten = pyqtSignal(str)  
        def write(self, text):  
            self.textWritten.emit(str(text))  

class MainWindow(QMainWindow):  
    def __init__(self,parent=None):  
        QMainWindow.__init__(self, parent)  

        tabs = QTabWidget(self)  

        tab1 = QWidget()      
        vbox = QVBoxLayout()  
        ts = Timeschedule(self)  
        vbox.addWidget(ts)  
        tab1.setLayout(vbox)  
          
        self.tab2 = QTextEdit()  
          
        tabs.addTab(tab1,"Schedule")  
        tabs.addTab(self.tab2,"Result")  
          
        tabs.resize(350,300)  
        self.resize(350,300)  
          
 
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)  
        sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)  
  
          
    def __del__(self):  
        sys.stdout = sys.__stdout__  
        sys.stderr = sys.__stderr__  
          
    def normalOutputWritten(self, text):  
        cursor = self.tab2.textCursor()  
        cursor.movePosition(QTextCursor.End)  
        cursor.insertText(text)  
        self.tab2.setTextCursor(cursor)  
        self.tab2.ensureCursorVisible()  


if __name__ == "__main__":
    app = QApplication(sys.argv) 
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())