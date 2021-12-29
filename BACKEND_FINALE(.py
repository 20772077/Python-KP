from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QTextEdit, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Window2')
        self.label_info = QtWidgets.QLabel(self)
        pixmap = QPixmap('sprav_info.jpg')
        self.label_info.setPixmap(pixmap)
        self.label_info.resize(1177,438)
        self.label_info.move(0, 0)
        self.label_info.show()
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.clicked.connect(self.btnClosed)
        self.pushButton.setText("Закрыть")
        self.pushButton.move(0, 470)
        
    def btnClosed(self):
        self.close()        

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('MainWindow')
        self.button = QPushButton(self)
        self.button.show()
        self.button.clicked.connect(self.show_window_2)
        self.resize(1024,600)
        self.new_text = QtWidgets.QLabel(self)
        self.label = QtWidgets.QLabel(self)
        self.label1 = QtWidgets.QLabel(self)
        self.pushButton = QtWidgets.QPushButton(self)
        self.label_border = QtWidgets.QLabel(self)
        self.btn = QtWidgets.QPushButton(self)
        self.input_h = QtWidgets.QLineEdit(self)
        self.input_H = QtWidgets.QLineEdit(self)
        self.input_Eb = QtWidgets.QLineEdit(self)        
        self.input_Rb = QtWidgets.QLineEdit(self)
        self.input_N = QtWidgets.QLineEdit(self)
        self.input_Na = QtWidgets.QLineEdit(self)
        
        self.output = QTextEdit(self)
        self.save_result = QPushButton(self)
        
        self.UI(self)
    def UI(self, Window):
        
        self.setWindowTitle("Курсовая работа")
        self.setGeometry(100, 100, 100, 100)
        self.resize(1024,600)

        self.label.setText("Введите \n данные")
        self.label.move(25, 282)

        self.button.setText("Справочная информация")
        self.button.move(10, 480)
        self.button.resize(400, 100)
        self.button.setFont(QFont('Times', 15))

        self.label_border.setText("_________________")
        self.label_border.move(0, 430)

        self.btn.move(10, 347)
        self.btn.setText("Рассчитать")
        self.btn.setFixedWidth(75)
        self.btn.clicked.connect(self.add_label)

        self.input_h.move(100, 272)
        self.input_h.resize(300,30)
        self.input_h.setPlaceholderText("h, мм")

        self.input_H.move(100, 302)
        self.input_H.resize(300,30)
        self.input_H.setPlaceholderText("H, м")

        self.input_Eb.move(100, 332)
        self.input_Eb.resize(300,30)
        self.input_Eb.setPlaceholderText("Eb, МПа")

        self.input_Rb.move(100, 362)
        self.input_Rb.resize(300,30)
        self.input_Rb.setPlaceholderText("Rb, МПа")

        self.input_N.move(100, 392)
        self.input_N.resize(300,30)
        self.input_N.setPlaceholderText("N, кН")

        self.input_Na.move(100, 422)
        self.input_Na.resize(300,30)
        self.input_Na.setPlaceholderText("Nl, кН")
        
        self.label_img = QtWidgets.QLabel(self)
        self.pixmap = QPixmap('image for KR.jpg')
        self.label_img.setPixmap(self.pixmap)
        self.label_img.resize(409,272)
        self.label_img.move(0, 0)
        
        self.output.move(420, 5)
        self.output.resize(600,535)
        self.output.setAlignment(QtCore.Qt.AlignTop)
        

        
#эта функция должна производить рассчёты
    def add_label(self):
        self.new_text.setText("Вычисления")
        self.new_text.move(420, 5)
        self.new_text.adjustSize() 
        

        

        h = float(self.input_h.text())

        H =float(self.input_H.text())

        Eb = float(self.input_Eb.text())

        Rb = float(self.input_Rb.text())

        N = float(self.input_N.text())

        Nl = float(self.input_Na.text())
        
        self.output.append('В данной задаче осуществляется проверка прочности панели.')
        ea = 0.
        l0 = 0.
        self.output.append('Расчет производим согласно 3.1.8 на действие продольной силы,' 
              'приложенной со случайным эксцентриситетом еа, определенным согласно 3.1.6.')
        self.output.append('Поскольку h/30 = '+ str(h/30.)+ 'и H/600 = '+ str(H/0.6))
        if h/30 < 10 and H/0.6 <10:
            self.output.append('принимаем еа = е0 = 10мм')
            ea = 10.
        else:
            self.output.append('принимаем еа = е0 = '+ str(h/30.))
            ea = h/30.
        self.output.append('Закрепление панели сверху и снизу принимаем шарнирным, следовательно,'
              'расчётная длина l0, согласно таблице 3.2, равна l0 = Н')
        ###### 
        l0 = H
        self.output.append('Так как отношение l0/h = '+ str(l0/(h*0.001)))
        self.output.append('расчет производим с учетом влияния прогиба согласно 3.1.12')
        #################################################################################
        fl = 0.
        e0 = 10.
        be = 0.
        b = 1000.
        self.output.append('По формуле (3.11) определяем коэффициент фl, принимая M1l/Ml = Nl/N = '+ str(Nl/N))
        self.output.append(' фl = 1 + M1l/Ml = 1 + '+ str((1. + Nl/N)))
        fl = 1. + Nl/N
        self.output.append('Поскольку бе = е0/h = '+str( e0/h))
        if e0/h < 0.15:
            self.output.append('Принимаем бе = 0,15')
            be = 0.15
        else:
            self.output.append('Принимаем бе = '+ str(e0/h))
            be = e0/h
        self.output.append('Жесткость D определим по формуле (3.10), принимая ширину сечения' 
              'b = 1 м = = 1000 мм')
        self.output.append('D = (Eb * b * h^3)/(80*фl*(0.3*бе))= '+ str((Eb * b * h*h*h)/(80*fl*(0.3*be))))
        D = (Eb * b * h*h*h)/(80.*fl*(0.3*be))
        self.output.append('Тогда')
        #################################################################################
        pi = 3.1415
        Ncr = 0.
        n = 0.
        yb2 = 0.
        self.output.append('Ncr = (pi^2*D)/l0^2 = '+ str((pi*pi*D)/(l0*l0)))
        Ncr = (pi*pi*D)/(l0*l0)
        self.output.append('n = 1/(1 - N/Ncr) = '+ str(1./(1. - N/(Ncr * 0.0000000001))))
        n = 1./(1. - N/(Ncr * 0.0000000001))
        self.output.append('Расчетное сопротивление бетона Rb согласно 2.1.9 принимаем с учётом '
              'коэффициента ?b2 = 0,9.')
        yb2 = 0.9
        self.output.append('Тогда Rb = '+str( Rb * yb2))
        Rb = Rb * yb2
        self.output.append('Проверим условие (3.1), используя формулу (3.2)')
        ################################################################################
        y = 0.
        self.output.append('RbAb = Rb*b*h*(1-(2*e0*n)/h) = '+ str(Rb * b * h * (1. - ((2. * e0 * n) / h)) * 0.001))
        y = Rb * b * h * (1. - ((2. * e0 * n) / h)) * 0.001
        if y > N:
            self.output.append(str(y)+ '> N = '+ str(N)+',')
            self.output.append('т.е. прочность панели на действие полной нагрузки обеспечена.')
            bool1 = True
        else:
            self.output.append('т.е. прочность панели на действие полной нагрузки НЕ обеспечена.')
            bool1 = False
          
        self.output.append('Поскольку Nl/N = '+ str(Nl/N))
        ysl_ = 0.
        self.output.append('> 0,9, согласно 3.3 проверим прочность панели на действие только '
              'постоянных и длительных нагрузок, т.е. при Nl ='+ str(N) + 'кН.'
              ' В этом случае ?l = 2, и тогда') 
        fl_ = 2.
        self.output.append('Ncr = '+ str(Ncr* (fl/fl_ )))
        Ncr = Ncr * (fl/fl_)
        self.output.append('n = '+ str(1./(1.-(Nl/Ncr))))
        n = 1./(1. - N/(Ncr * 0.0000000001))
        self.output.append('Расчетное сопротивление Rb принимаем с учётом ybl = 0.9')
        ybl = 0.9
        self.output.append('Rb = '+ str(Rb*ybl))
        Rb = Rb*ybl
        self.output.append('RbAb = '+ str(Rb * b * h * (1. - ((2. * e0 * n) / h)) * 0.001))
        ysl_ = Rb * b * h * (1. - ((2. * e0 * n) / h)) * 0.001
        if ysl_ > Nl:
            self.output.append('т.е. прочность панели обеспечена при любых сочетаниях нагрузок.')
            bool2 = True
        else:
            self.output.append('т.е. прочность панели НЕ обеспечена при любых сочетаниях нагрузок.')
            bool2 = False
        
      
        self.save_result.move(420, 550)
        self.save_result.setText("Сохранить результат")
        self.save_result.resize(600,30)
        self.save_result.clicked.connect(lambda: self.saving(h, H, Eb, Rb, N, Nl, bool1, bool2))
      
    def saving(self, h, H, Eb, Rb, N, Nl, bool1, bool2):
        fileTXT = open('Результаты.txt','w')
        
        fileTXT.write('h = ' + str(h) + '\n')
        fileTXT.write('H = '+ str(H) + '\n')
        fileTXT.write('Eb = '+ str(Eb) + '\n')
        fileTXT.write('Rb = '+ str(Rb) + '\n')
        fileTXT.write('N = '+ str(N) + '\n')
        fileTXT.write('Nl = '+ str(Nl) + '\n')
        
        if bool1 == True:
            fileTXT.write('прочность панели на действие полной нагрузки обеспечена\n')
        else:
            fileTXT.write('прочность панели на действие полной нагрузки НЕ обеспечена\n')
            
        if bool2 == True:
            fileTXT.write('прочность панели обеспечена при любых сочетаниях нагрузок\n')
        else:
            fileTXT.write('прочность панели НЕ обеспечена при любых сочетаниях нагрузок\n')
            
        fileTXT.close
        
    def show_window_2(self):
        self.w2 = Window2()
        self.w2.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())