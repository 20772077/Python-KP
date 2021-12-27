from PyQt5.QtGui import QIcon, QPixmap
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
        
        
        self.UI(self)
    def UI(self, Window):
        
        self.setWindowTitle("Курсовая работа")
        self.setGeometry(100, 100, 100, 100)
        self.resize(1024,600)

        self.label.setText("Введите \n данные")
        self.label.move(25, 282)

        self.label1.setText("Справочная \n информация")
        self.button.setText("Справочная инф-я")
        self.button.move(10, 472)
        self.label1.move(5, 392)
        #self.pushButton.clicked.connect(self)

        self.label_border.setText("_________________")
        self.label_border.move(0, 370)

        self.btn.move(10, 347)
        self.btn.setText("Рассчитать")
        self.btn.setFixedWidth(75)
        self.btn.clicked.connect(self.add_label)

        self.input_h.move(100, 272)
        self.input_h.resize(100,20)
        self.input_h.setPlaceholderText("h, мм")

        self.input_H.move(100, 292)
        self.input_H.resize(100,20)
        self.input_H.setPlaceholderText("H, м")

        self.input_Eb.move(100, 312)
        self.input_Eb.resize(100,20)
        self.input_Eb.setPlaceholderText("Eb, МПа")

        self.input_Rb.move(100, 332)
        self.input_Rb.resize(100,20)
        self.input_Rb.setPlaceholderText("Rb, МПа")

        self.input_N.move(100, 352)
        self.input_N.resize(100,20)
        self.input_N.setPlaceholderText("N, кН")

        self.input_Na.move(100, 372)
        self.input_Na.resize(100,20)
        self.input_Na.setPlaceholderText("Na, кН")
        
        self.label_img = QtWidgets.QLabel(self)
        self.pixmap = QPixmap('image for KR.jpg')
        self.label_img.setPixmap(self.pixmap)
        self.label_img.resize(409,272)
        self.label_img.move(0, 0)
        
#эта функция должна производить рассчёты
    def add_label(self):
        self.new_text.setText("Вычисления")
        self.new_text.move(420, 5)
        self.new_text.adjustSize() 
        
        
        print('Толщина, mm: ') 
        h = float(self.input_h.text())
        print('Высота, m: ')
        H = float(self.input_H.text())
        print('Eb, МПа:')
        Eb = float(self.input_Eb.text())
        print('Rb, МПа:')
        Rb = float(self.input_Rb.text())
        print('N, кН (полная нагрузка на 1 м стены)')
        N = float(self.input_N.text())
        print('Nl, кН (постоянная и длительная нагрузка)')
        Nl = float(self.input_Na.text())
        
        print('В данной задаче осуществляется проверка прочности панели.')
        ea = 0
        l0 = 0
        print('Расчет производим согласно 3.1.8 на действие продольной силы,' 
              'приложенной со случайным эксцентриситетом еа, определенным согласно 3.1.6.')
        print('Поскольку h/30 = ', h/30, 'и H/600 = ', H/600)
        if h/30 < 10 and H/0.6 <10:
          print('принимаем еа = е0 = 10мм')
          ea = 10
        else:
          pass
        print('Закрепление панели сверху и снизу принимаем шарнирным, следовательно,'
              'расчётная длина l0, согласно таблице 3.2, равна l0 = Н = 2,7 м.')
        ###### Clt
        l0 = 2700
        print('Так как отношение l0/h = ', l0/h)
        if l0/h > 4:
          print('расчет производим с учетом влияния прогиба согласно 3.1.12')
        else:
          pass
        #################################################################################
        fl = 0
        e0 = 10
        be = 0
        b = 1000
        print('По формуле (3.11) определяем коэффициент фl, принимая M1l/Ml = Nl/N = ', Nl/N)
        print(' фl = 1 + M1l/Ml = 1 + ', 1 + Nl/N)
        fl = 1 + Nl/N
        print('Поскольку бе = е0/h = ', e0/h)
        if e0/h < 0.15:
          print('Принимаем бе = 0,15')
          be = 0.15
        else:
          pass
        print('Жесткость D определим по формуле (3.10), принимая ширину сечения' 
              'b = 1 м = = 1000 мм')
        print('D = (Eb * b * h^3)/(80*фl*(0.3*бе))= ', (Eb * b * h*h*h)/(80*fl*(0.3*be)))
        D = (Eb * b * h*h*h)/(80*fl*(0.3*be))
        print('Тогда')
        #################################################################################
        pi = 3.1415
        Ncr = 0
        n = 0
        yb2 = 0
        print('Ncr = (pi^2*D)/l0^2 = ', (pi*pi*D)/(l0*l0))
        Ncr = (pi*pi*D)/(l0*l0)
        print('n = 1/(1 - N/Ncr) = ', 1/(1 - N/Ncr))
        n = 1/(1 - N/Ncr)
        print('Расчетное сопротивление бетона Rb согласно 2.1.9 принимаем с учётом '
              'коэффициента ?b2 = 0,9.')
        yb2 = 0.9
        print('Тогда Rb = ', Rb * yb2)
        Rb = Rb * yb2
        print('Проверим условие (3.1), используя формулу (3.2)')
        ################################################################################
        y = 0
        print('RbAb = Rb*b*h*(1-(2*e0*n)/h) = ', Rb*b*h*(1* (2*e0*n)/h))
        y = Rb * b * h * (1-((2* e0 * n) / h))
        if y > N:
          print(y, '> N = ', N,',')
          print('т.е. прочность панели на действие полной нагрузки обеспечена.')
        else:
          print('т.е. прочность панели на действие полной нагрузки НЕ обеспечена.')
        print('Поскольку Nl/N = ', Nl/N)
        if Nl/N > 0.9:
          ysl_ = 0
          print('> 0,9, согласно 3.3 проверим прочность панели на действие только '
                'постоянных и длительных нагрузок, т.е. при Nl =', N , 'кН.'
                ' В этом случае ?l = 2, и тогда') 
          fl_ = 2
          print('Ncr = ', Ncr* fl/fl_ )
          Ncr = Ncr * (fl/fl_)
          print('n = ', 1/(1-(Nl/Ncr))) 
          n = 1/(1-(Nl/Ncr))
          print('Расчетное сопротивление Rb принимаем с учётом ybl = 0.9')
          ybl = 0.9
          print('Rb = ', Rb*ybl)
          Rb = Rb*ybl
          print('RbAb = ', Rb*b*h*(1* (2*e0*n)/h))
          ysl_ = Rb*b*h*(1* (2*e0*n)/h)
          if ysl_ > Nl:
            print('т.е. прочность панели обеспечена при любых сочетаниях нагрузок.')
          else:
            print('т.е. прочность панели НЕ обеспечена при любых сочетаниях нагрузок.')
        else:
          pass
    def show_window_2(self):
        self.w2 = Window2()
        self.w2.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())