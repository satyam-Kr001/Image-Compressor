import sys
import PIL
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QFileDialog,QInputDialog, QWidget, QFrame,QMainWindow, QLabel, QLineEdit, QPushButton
from PIL import Image
from PyQt5.QtCore import Qt
import os
from huffman_tree import *

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Image Compressor'
        self.left = 10
        self.top = 10
        self.image_width = 0
        self.width = 400
        self.height = 600
        self.compress_width = 0;
        self.statusBar().showMessage("Message:")
        self.statusBar().setObjectName("status")
        self.setObjectName("main_window")
        stylesheet = ""
        with open("design.qss","r") as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)
        self.setFixedSize(self.width,self.height)
        self.initUI()

        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #--------------------------------------main_window---------------------------------------------
        self.single_bubble =QFrame(self)
        self.single_bubble.setObjectName("bubble")
        self.single_bubble.move(40,130)
        self.single_bubble.mousePressEvent = self.single_bubble_clicked

        self.single_bubble_heading = QLabel(self.single_bubble)
        self.single_bubble_heading.setText("Compress Image")
        self.single_bubble_heading.setObjectName("bubble_heading")
        self.single_bubble_heading.move(56,85)

        self.single_bubble_para = QLabel(self.single_bubble)
        self.single_bubble_para.setText("Click here to compress single Image!")
        self.single_bubble_para.setObjectName("bubble_para")
        self.single_bubble_para.move(35,125)


        #-----------------------------------Single_Bubble_Expanded--------------------------------------

        self.single_bubble_expanded = QFrame(self)
        self.single_bubble_expanded.setObjectName("bubble_expanded")
        self.single_bubble_expanded.move(25,100)
        self.single_bubble_expanded.setVisible(False) 

        self.back_arrow_s = QLabel(self.single_bubble_expanded)
        self.back_arrow_s.move(15,10)
        self.back_arrow_s.setObjectName("back_button")
        self.back_arrow_s.setTextFormat(Qt.RichText)
        self.back_arrow_s.setText("&#8592;")
        self.back_arrow_s.mousePressEvent = self.back_arrow_clicked

        self.single_bubble_heading = QLabel(self.single_bubble_expanded)
        self.single_bubble_heading.setText("Compress Image")
        self.single_bubble_heading.setObjectName("bubble_heading")
        self.single_bubble_heading.move(90,8)   

        self.select_image_label = QLabel(self.single_bubble_expanded)
        self.select_image_label.setText("Choose Image")
        self.select_image_label.setObjectName("bubble_para")
        self.select_image_label.move(30,50) 

        self.image_path = QLineEdit(self.single_bubble_expanded)
        self.image_path.setObjectName("path_text")
        self.image_path.move(60,85)

        self.browse_button = QPushButton(self.single_bubble_expanded)
        self.browse_button.setText("......")
        self.browse_button.setObjectName("browse_button")
        self.browse_button.clicked.connect(self.select_file)
        self.browse_button.move(240,80) 


        self.select_image_quality = QLabel(self.single_bubble_expanded)
        self.select_image_quality.setText("Dimension of the current Image")
        self.select_image_quality.setObjectName("bubble_para")
        self.select_image_quality.move(30,130) 
      


        self.quality_path = QLineEdit(self.single_bubble_expanded)
        self.quality_path.setObjectName("Quality_path_text")
        self.quality_path.move(80,160)

        self.compress_image = QPushButton(self.single_bubble_expanded)
        self.compress_image.setText("Compress")
        self.compress_image.setObjectName("compress_button")
        self.compress_image.clicked.connect(self.resize_pic)
        self.compress_image.move(100,260) 

        #------------------------------------end main_window---------------------------------------------

        self.show()
        #------------------------------------Functions---------------------------------------------------
    def single_bubble_clicked(self, event):
        print("Single bubble clicked")
        self.single_bubble.setVisible(False)
        self.single_bubble_expanded.setVisible(True) 

    

    def back_arrow_clicked(self,evenet):
        print("Single bubble clicked")
        self.single_bubble.setVisible(True)
        # self.dir_bubble.setVisible(True) 
        self.single_bubble_expanded.setVisible(False) 
        # self.dir_bubble_expanded.setVisible(False)


    def select_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;JPEG (*.jpeg)")
        if fileName:
            print(fileName)
            self.image_path.setText(fileName)
            img = Image.open(fileName)
            self.image_width = img.width
            self.compress_width = self.image_width
            self.quality_path.setText(str(self.image_width))


    def quality_current_value(self):
        if self.quality_combo.currentText() == "High":
            self.quality_path.setText(str(self.image_width))
            self.compress_width = self.image_width

        # if self.quality_combo.currentText() == "Medium":
        #     self.quality_path.setText(str(int(self.image_width/2)))
        #     self.compress_width = int(self.image_width/2) 

        # if self.quality_combo.currentText() == "Low":
        #     self.quality_path.setText(str(int(self.image_width/4)))
        #     self.compress_width = int(self.image_width/4) 


    def resize_pic(self):
        old_pic = self.image_path.text()
        print(old_pic)
        print(self.compress_width)
        # directories = self.image_path.text().split("/")
        # print(directories)
        new_pic = ""

        new_pic_name, okPressed = QInputDialog.getText(self, "Save Image as","Image Name:", QLineEdit.Normal, "")
        if okPressed and new_pic_name != '':
            print(new_pic_name)
            if(old_pic[-4:]) == "jpeg":
                new_pic_name += ".jpeg"

            if(old_pic[-4:]) == "png":
                new_pic_name += ".png"

            if(old_pic[-4:]) == "jpg":
                new_pic_name += ".jpg"
            else:
                new_pic_name += ".jpeg"

            # for dir in directories[:-1]:
            #     new_pic = new_pic+dir+"/"

            # new_pic += new_pic_name
            # print(new_pic)

        self.compression_code(old_pic)
        self.statusBar().showMessage("Message: Compressed")
    
    def compression_code(self, old_pic):
        try:
            img = Image.open(old_pic)
            picture = picture_convert(img,'new.bmp')
            Huffman_Coding(picture)
            print("Ended")
            # mywidth = self.compress_width
            # wpercent = (mywidth/float(img.size[0]))
            # hsize = int((float(img.size[1])*float(wpercent)))
            # img = img.resize((mywidth,hsize),PIL.Image.ANTIALIAS)
            # img.save(new_pic)
        except Exception as e:
            self.statusBar().showMessage("Message: "+e)



    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

