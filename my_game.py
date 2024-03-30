import sys
import random
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui',self)
        self.lines = list(open("base.txt","r",encoding="utf-8"))
        self.random_line = random.choice(self.lines)
        self.letters = list(self.random_line)
        self.file = open("score.txt", "r", encoding="utf-8")

        self.score = self.file.read()
        self.best_score = self.file.read()
        self.file.close()

        self.bukva = 0
        

        self.word_1 = self.letters[0]
        self.word_2 = self.letters[1]
        self.word_3 = self.letters[2]
        self.word_4 = self.letters[3]
        self.word_5 = self.letters[4]

        self.life = 6
        self.label_6.setText(str(self.life))
        print(self.letters)

        self.label_8.setVisible(False)
        self.label_11.setVisible(False)
        self.label_12.setVisible(False)
        self.label_13.setVisible(False)
        self.label_14.setVisible(False)
        self.label_9.setVisible(False)
        
        self.label_1.setText(str(self.word_1))
        self.label_1.setVisible(False)
        self.label_2.setText(str(self.word_2))
        self.label_2.setVisible(False)
        self.label_3.setText(str(self.word_3))
        self.label_3.setVisible(False)
        self.label_4.setText(str(self.word_4))
        self.label_4.setVisible(False)
        self.label_5.setText(str(self.word_5))
        self.label_5.setVisible(False)

        #if self.label_1.setVisible(True) and self.label_2.setVisible(True) and self.label_3.setVisible(True) and self.label_4.setVisible(True) and self.label_5.setVisible(True)

        self.pushButton_34.clicked.connect(self.start_game)        
        


    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
    
            # Встановити стильовий лист вікна
            self.setStyleSheet("background-color: white; color: black;")
            
    def hit_point(self):
        self.life -= 1
        self.label_6.setText(str(self.life))
        if self.life == 5:
            self.label_8.setVisible(True)
        if self.life == 4:
            self.label_9.setVisible(True)
        if self.life == 3:
            self.label_11.setVisible(True)
        if self.life == 2:
            self.label_12.setVisible(True)
        if self.life == 1:
            self.label_13.setVisible(True)
        if self.life == 0:
            self.label_14.setVisible(True) 
    def start_game(self):
        if self.life == 5:
            self.label_8.setVisible(True)
        if self.life == 4:
            self.label_9.setVisible(True)
        if self.life == 3:
            self.label_11.setVisible(True)
        if self.life == 2:
            self.label_12.setVisible(True)
        if self.life == 1:
            self.label_13.setVisible(True)
        if self.life == 0:
            self.label_14.setVisible(True)
            

        self.pushButton.clicked.connect(self.liter_1)
        self.pushButton_2.clicked.connect(self.liter_2)
        self.pushButton_3.clicked.connect(self.liter_3)
        self.pushButton_4.clicked.connect(self.liter_4)
        self.pushButton_5.clicked.connect(self.liter_5)
        self.pushButton_6.clicked.connect(self.liter_6)
        self.pushButton_7.clicked.connect(self.liter_7)
        self.pushButton_8.clicked.connect(self.liter_8)
        self.pushButton_9.clicked.connect(self.liter_9)
        self.pushButton_10.clicked.connect(self.liter_10)
        self.pushButton_11.clicked.connect(self.liter_11)
        self.pushButton_12.clicked.connect(self.liter_12)
        self.pushButton_13.clicked.connect(self.liter_13)
        self.pushButton_14.clicked.connect(self.liter_14)
        self.pushButton_15.clicked.connect(self.liter_15)
        self.pushButton_16.clicked.connect(self.liter_16)
        self.pushButton_17.clicked.connect(self.liter_17)
        self.pushButton_18.clicked.connect(self.liter_18)
        self.pushButton_19.clicked.connect(self.liter_19)
        self.pushButton_20.clicked.connect(self.liter_20)
        self.pushButton_21.clicked.connect(self.liter_21)
        self.pushButton_22.clicked.connect(self.liter_22)
        self.pushButton_23.clicked.connect(self.liter_23)
        self.pushButton_24.clicked.connect(self.liter_24)
        self.pushButton_25.clicked.connect(self.liter_25)
        self.pushButton_26.clicked.connect(self.liter_26)
        self.pushButton_27.clicked.connect(self.liter_27)
        self.pushButton_28.clicked.connect(self.liter_28)
        self.pushButton_29.clicked.connect(self.liter_29)
        self.pushButton_30.clicked.connect(self.liter_30)
        self.pushButton_31.clicked.connect(self.liter_31)
        self.pushButton_32.clicked.connect(self.liter_32)
        self.pushButton_33.clicked.connect(self.liter_33)

        if self.bukva == 5:
            self.score += 1
            self.random_line = random.choice(self.lines)
            self.letters = list(self.random_line)
            print(self.letters)
            self.word_1 = self.letters[0]
            self.word_2 = self.letters[1]
            self.word_3 = self.letters[2]
            self.word_4 = self.letters[3]
            self.word_5 = self.letters[4]
        
            self.label_1.setText(str(self.word_1))
            self.label_1.setVisible(False)
            self.label_2.setText(str(self.word_2))
            self.label_2.setVisible(False)
            self.label_3.setText(str(self.word_3))
            self.label_3.setVisible(False)
            self.label_4.setText(str(self.word_4))
            self.label_4.setVisible(False)
            self.label_5.setText(str(self.word_5))
            self.label_5.setVisible(False)
        if self.score > self.best_score:
            self.file = open("score.txt", "a", encoding="utf-8")
            self.life.write(self.best_score)
        self.label_10.setText("Найкращий рахунок: " + str(self.score))

    def liter_2(self):
        if "б" in self.letters:
            self.bukva += 1
            if "б" == self.letters[0]:
                self.label_1.setVisible(True)
            if "б" == self.letters[1]:
                self.label_2.setVisible(True)
            if "б" == self.letters[2]:
                self.label_3.setVisible(True)
            if "б" == self.letters[3]:
                self.label_4.setVisible(True)
            if "б" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_3(self):
        if "в" in self.letters:
            self.bukva += 1
            if "в" == self.letters[0]:
                self.label_1.setVisible(True)
            if "в" == self.letters[1]:
                self.label_2.setVisible(True)
            if "в" == self.letters[2]:
                self.label_3.setVisible(True)
            if "в" == self.letters[3]:
                self.label_4.setVisible(True)
            if "в" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_4(self):
        if "г" in self.letters:
            self.bukva += 1
            if "г" == self.letters[0]:
                self.label_1.setVisible(True)
            if "г" == self.letters[1]:
                self.label_2.setVisible(True)
            if "г" == self.letters[2]:
                self.label_3.setVisible(True)
            if "г" == self.letters[3]:
                self.label_4.setVisible(True)
            if "г" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_5(self):
        if "ґ" in self.letters:
            self.bukva += 1
            if "ґ" == self.letters[0]:
                self.label_1.setVisible(True)
            if "ґ" == self.letters[1]:
                self.label_2.setVisible(True)
            if "ґ" == self.letters[2]:
                self.label_3.setVisible(True)
            if "ґ" == self.letters[3]:
                self.label_4.setVisible(True)
            if "ґ" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_6(self):
        if "д" in self.letters:
            self.bukva += 1
            if "д" == self.letters[0]:
                self.label_1.setVisible(True)
            if "д" == self.letters[1]:
                self.label_2.setVisible(True)
            if "д" == self.letters[2]:
                self.label_3.setVisible(True)
            if "д" == self.letters[3]:
                self.label_4.setVisible(True)
            if "д" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_7(self):
        if "е" in self.letters:
            self.bukva += 1
            if "е" == self.letters[0]:
                self.label_1.setVisible(True)
            if "е" == self.letters[1]:
                self.label_2.setVisible(True)
            if "е" == self.letters[2]:
                self.label_3.setVisible(True)
            if "е" == self.letters[3]:
                self.label_4.setVisible(True)
            if "е" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_8(self):
        if "є" in self.letters:
            self.bukva += 1
            if "є" == self.letters[0]:
                self.label_1.setVisible(True)
            if "є" == self.letters[1]:
                self.label_2.setVisible(True)
            if "є" == self.letters[2]:
                self.label_3.setVisible(True)
            if "є" == self.letters[3]:
                self.label_4.setVisible(True)
            if "є" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_9(self):
        if "ж" in self.letters:
            self.bukva += 1
            if "ж" == self.letters[0]:
                self.label_1.setVisible(True)
            if "ж" == self.letters[1]:
                self.label_2.setVisible(True)
            if "ж" == self.letters[2]:
                self.label_3.setVisible(True)
            if "ж" == self.letters[3]:
                self.label_4.setVisible(True)
            if "ж" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_10(self):
        if "з" in self.letters:
            self.bukva += 1
            if "з" == self.letters[0]:
                self.label_1.setVisible(True)
            if "з" == self.letters[1]:
                self.label_2.setVisible(True)
            if "з" == self.letters[2]:
                self.label_3.setVisible(True)
            if "з" == self.letters[3]:
                self.label_4.setVisible(True)
            if "з" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_11(self):
        if "и" in self.letters:
            self.bukva += 1
            if "и" == self.letters[0]:
                self.label_1.setVisible(True)
            if "и" == self.letters[1]:
                self.label_2.setVisible(True)
            if "и" == self.letters[2]:
                self.label_3.setVisible(True)
            if "и" == self.letters[3]:
                self.label_4.setVisible(True)
            if "и" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_12(self):
        if "і" in self.letters:
            self.bukva += 1
            if "і" == self.letters[0]:
                self.label_1.setVisible(True)
            if "і" == self.letters[1]:
                self.label_2.setVisible(True)
            if "і" == self.letters[2]:
                self.label_3.setVisible(True)
            if "і" == self.letters[3]:
                self.label_4.setVisible(True)
            if "і" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_13(self):
        if "ї" in self.letters:
            self.bukva += 1
            if "ї" == self.letters[0]:
                self.label_1.setVisible(True)
            if "ї" == self.letters[1]:
                self.label_2.setVisible(True)
            if "ї" == self.letters[2]:
                self.label_3.setVisible(True)
            if "ї" == self.letters[3]:
                self.label_4.setVisible(True)
            if "ї" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_14(self):
        if "й" in self.letters:
            self.bukva += 1
            if "й" == self.letters[0]:
                self.label_1.setVisible(True)
            if "й" == self.letters[1]:
                self.label_2.setVisible(True)
            if "й" == self.letters[2]:
                self.label_3.setVisible(True)
            if "й" == self.letters[3]:
                self.label_4.setVisible(True)
            if "й" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_15(self):
        if "к" in self.letters:
            self.bukva += 1
            if "к" == self.letters[0]:
                self.label_1.setVisible(True)
            if "к" == self.letters[1]:
                self.label_2.setVisible(True)
            if "к" == self.letters[2]:
                self.label_3.setVisible(True)
            if "к" == self.letters[3]:
                self.label_4.setVisible(True)
            if "к" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_16(self):
        if "л" in self.letters:
            self.bukva += 1
            if "л" == self.letters[0]:
                self.label_1.setVisible(True)
            if "л" == self.letters[1]:
                self.label_2.setVisible(True)
            if "л" == self.letters[2]:
                self.label_3.setVisible(True)
            if "л" == self.letters[3]:
                self.label_4.setVisible(True)
            if "л" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_17(self):
        if "м" in self.letters:
            self.bukva += 1
            if "м" == self.letters[0]:
                self.label_1.setVisible(True)
            if "м" == self.letters[1]:
                self.label_2.setVisible(True)
            if "м" == self.letters[2]:
                self.label_3.setVisible(True)
            if "м" == self.letters[3]:
                self.label_4.setVisible(True)
            if "м" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_18(self):
        if "н" in self.letters:
            self.bukva += 1
            if "н" == self.letters[0]:
                self.label_1.setVisible(True)
            if "н" == self.letters[1]:
                self.label_2.setVisible(True)
            if "н" == self.letters[2]:
                self.label_3.setVisible(True)
            if "н" == self.letters[3]:
                self.label_4.setVisible(True)
            if "н" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_19(self):
        if "о" in self.letters:
            self.bukva += 1
            if "о" == self.letters[0]:
                self.label_1.setVisible(True)
            if "о" == self.letters[1]:
                self.label_2.setVisible(True)
            if "о" == self.letters[2]:
                self.label_3.setVisible(True)
            if "о" == self.letters[3]:
                self.label_4.setVisible(True)
            if "о" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_20(self):
        if "п" in self.letters:
            self.bukva += 1
            if "п" == self.letters[0]:
                self.label_1.setVisible(True)
            if "п" == self.letters[1]:
                self.label_2.setVisible(True)
            if "п" == self.letters[2]:
                self.label_3.setVisible(True)
            if "п" == self.letters[3]:
                self.label_4.setVisible(True)
            if "п" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_21(self):
        if "р" in self.letters:
            self.bukva += 1
            if "р" == self.letters[0]:
                self.label_1.setVisible(True)
            if "р" == self.letters[1]:
                self.label_2.setVisible(True)
            if "р" == self.letters[2]:
                self.label_3.setVisible(True)
            if "р" == self.letters[3]:
                self.label_4.setVisible(True)
            if "р" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_22(self):
        if "с" in self.letters:
            self.bukva += 1
            if "с" == self.letters[0]:
                self.label_1.setVisible(True)
            if "с" == self.letters[1]:
                self.label_2.setVisible(True)
            if "с" == self.letters[2]:
                self.label_3.setVisible(True)
            if "с" == self.letters[3]:
                self.label_4.setVisible(True)
            if "с" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_23(self):
        if "т" in self.letters:
            self.bukva += 1
            if "т" == self.letters[0]:
                self.label_1.setVisible(True)
            if "т" == self.letters[1]:
                self.label_2.setVisible(True)
            if "т" == self.letters[2]:
                self.label_3.setVisible(True)
            if "т" == self.letters[3]:
                self.label_4.setVisible(True)
            if "т" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_24(self):
        if "у" in self.letters:
            self.bukva += 1
            if "у" == self.letters[0]:
                self.label_1.setVisible(True)
            if "у" == self.letters[1]:
                self.label_2.setVisible(True)
            if "у" == self.letters[2]:
                self.label_3.setVisible(True)
            if "у" == self.letters[3]:
                self.label_4.setVisible(True)
            if "у" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_25(self):
        if "ф" in self.letters:
            self.bukva += 1
            if "ф" == self.letters[0]:
                self.label_1.setVisible(True)
            if "ф" == self.letters[1]:
                self.label_2.setVisible(True)
            if "ф" == self.letters[2]:
                self.label_3.setVisible(True)
            if "ф" == self.letters[3]:
                self.label_4.setVisible(True)
            if "ф" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_26(self):
        if "х" in self.letters:
            self.bukva += 1
            if "х" == self.letters[0]:
                self.label_1.setVisible(True)
            if "х" == self.letters[1]:
                self.label_2.setVisible(True)
            if "х" == self.letters[2]:
                self.label_3.setVisible(True)
            if "х" == self.letters[3]:
                self.label_4.setVisible(True)
            if "х" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_27(self):
        if "ц" in self.letters:
            self.bukva += 1
            if "ц" == self.letters[0]:
                self.label_1.setVisible(True)
            if "ц" == self.letters[1]:
                self.label_2.setVisible(True)
            if "ц" == self.letters[2]:
                self.label_3.setVisible(True)
            if "ц" == self.letters[3]:
                self.label_4.setVisible(True)
            if "ц" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_28(self):
        if "ч" in self.letters:
            self.bukva += 1
            if "ч" == self.letters[0]:
                self.label_1.setVisible(True)
            if "ч" == self.letters[1]:
                self.label_2.setVisible(True)
            if "ч" == self.letters[2]:
                self.label_3.setVisible(True)
            if "ч" == self.letters[3]:
                self.label_4.setVisible(True)
            if "ч" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_29(self):
        if "ш" in self.letters:
            self.bukva += 1
            if "ш" == self.letters[0]:
                self.label_1.setVisible(True)
            if "ш" == self.letters[1]:
                self.label_2.setVisible(True)
            if "ш" == self.letters[2]:
                self.label_3.setVisible(True)
            if "ш" == self.letters[3]:
                self.label_4.setVisible(True)
            if "ш" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_30(self):
        if "щ" in self.letters:
            self.bukva += 1
            if "щ" == self.letters[0]:
                self.label_1.setVisible(True)
            if "щ" == self.letters[1]:
                self.label_2.setVisible(True)
            if "щ" == self.letters[2]:
                self.label_3.setVisible(True)
            if "щ" == self.letters[3]:
                self.label_4.setVisible(True)
            if "щ" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_31(self):
        if "ь" in self.letters:
            self.bukva += 1
            if "ь" == self.letters[0]:
                self.label_1.setVisible(True)
            if "ь" == self.letters[1]:
                self.label_2.setVisible(True)
            if "ь" == self.letters[2]:
                self.label_3.setVisible(True)
            if "ь" == self.letters[3]:
                self.label_4.setVisible(True)
            if "ь" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_32(self):
        if "ю" in self.letters:
            self.bukva += 1
            if "ю" == self.letters[0]:
                self.label_1.setVisible(True)
            if "ю" == self.letters[1]:
                self.label_2.setVisible(True)
            if "ю" == self.letters[2]:
                self.label_3.setVisible(True)
            if "ю" == self.letters[3]:
                self.label_4.setVisible(True)
            if "ю" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_33(self):
        if "я" in self.letters:
            self.bukva += 1
            if "я" == self.letters[0]:
                self.label_1.setVisible(True)
            if "я" == self.letters[1]:
                self.label_2.setVisible(True)
            if "я" == self.letters[2]:
                self.label_3.setVisible(True)
            if "я" == self.letters[3]:
                self.label_4.setVisible(True)
            if "я" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    def liter_1(self):
        if "а" in self.letters:
            self.bukva += 1
            if "а" == self.letters[0]:
                self.label_1.setVisible(True)
            if "а" == self.letters[1]:
                self.label_2.setVisible(True)
            if "а" == self.letters[2]:
                self.label_3.setVisible(True)
            if "а" == self.letters[3]:
                self.label_4.setVisible(True)
            if "а" == self.letters[4]:
                self.label_5.setVisible(True)
        else:
            self.hit_point()
    
    
      

    
        
    

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
