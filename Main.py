from pdf2image import convert_from_path
from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib
from pdfreader import SimplePDFViewer,PageDoesNotExist

pdfpath = pathlib.Path(pathlib.Path(__file__).parent,f'test1.pdf')
tempath = pathlib.Path(pathlib.Path(__file__).parent,f'temp')

class Ui_Dialog(object):
    def __init__(self) -> None:
        super().__init__()
        win = None
    
    def setupUi(self, Dialog):
        self.win = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 492)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.image_label = QtWidgets.QLabel(Dialog)
        self.image_label.setObjectName("image_label")
        self.verticalLayout_2.addWidget(self.image_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previous_btn = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previous_btn.sizePolicy().hasHeightForWidth())
        self.previous_btn.setSizePolicy(sizePolicy)
        self.previous_btn.setObjectName("previous_btn")
        self.horizontalLayout.addWidget(self.previous_btn)
        self.next_btn = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_btn.sizePolicy().hasHeightForWidth())
        self.next_btn.setSizePolicy(sizePolicy)
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout.addWidget(self.next_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.Startup()

        self.next_btn.clicked.connect(self.action)

    def action(self):
        self.win.close()

    def Startup(self):
        global pdfpath,tempath

        file = open(pdfpath,'rb')
        viewer = SimplePDFViewer(file)

        images = []
        try:
            while True:
                viewer.render()
                images.extend(viewer.canvas.inline_images)
                images.extend(viewer.canvas.images.values())
                viewer.next()
        except PageDoesNotExist:
            pass

        for i, img in enumerate(images):
            img.to_Pillow().save(f"{i}.png")

    def Startup1(self):
        global pdfpath,tempath,fname
        
        # print(fname)

        print(pdfpath)

        doc = convert_from_path(pdfpath,output_folder=str(tempath),fmt='jpeg',first_page=1,last_page=1,use_cropbox=True)

        # i=0

        # for image in doc:
        #     tempath = pathlib.Path(tempath,f'{i}.png')
        #     print(i)
        #     image.save(str(tempath),'PNG')
        #     tempath = tempath.parent
        #     i+=1

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.image_label.setText(_translate("Dialog", "TextLabel"))
        self.previous_btn.setText(_translate("Dialog", "Previous"))
        self.next_btn.setText(_translate("Dialog", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
