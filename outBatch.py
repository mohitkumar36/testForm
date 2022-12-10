from PyQt6 import QtCore, QtGui, QtWidgets
from datamanage import changeBatch

class Ui_BatchUpdate(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(248, 187)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 120, 221, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.regLabel = QtWidgets.QLabel(Dialog)
        self.regLabel.setGeometry(QtCore.QRect(30, 40, 49, 16))
        self.regLabel.setObjectName("regLabel")
        self.batchLabel = QtWidgets.QLabel(Dialog)
        self.batchLabel.setGeometry(QtCore.QRect(40, 80, 49, 16))
        self.batchLabel.setObjectName("batchLabel")
        self.regText = QtWidgets.QLineEdit(Dialog)
        self.regText.setGeometry(QtCore.QRect(90, 40, 131, 21))
        self.regText.setObjectName("regText")
        self.batchSelect = QtWidgets.QComboBox(Dialog)
        self.batchSelect.setGeometry(QtCore.QRect(90, 80, 68, 22))
        self.batchSelect.setObjectName("batchSelect")
        self.batchSelect.addItem("")
        self.batchSelect.addItem("")
        self.batchSelect.addItem("")
        self.batchSelect.addItem("")

        self.retranslateUi(Dialog)


        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore

        self.buttonBox.accepted.connect(lambda: self.update())
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def update(self):
        regNo = self.regText.text()
        batch = self.batchSelect.currentText()
        
        done = changeBatch(regNo, batch)
        if done:
            dlg = CustomDialog("Success")
            dlg.exec()
        else:
            dlg = CustomDialog("Failed")
            dlg.exec()
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Update Batch"))
        self.regLabel.setText(_translate("Dialog", "Reg No:"))
        self.batchLabel.setText(_translate("Dialog", "Batch:"))
        self.batchSelect.setItemText(0, _translate("Dialog", "6-7AM"))
        self.batchSelect.setItemText(1, _translate("Dialog", "7-8AM"))
        self.batchSelect.setItemText(2, _translate("Dialog", "8-9AM"))
        self.batchSelect.setItemText(3, _translate("Dialog", "5-6PM"))

class CustomDialog(QtWidgets.QDialog):
    def __init__(self, s, regNo = ''):
        super().__init__()

        self.setWindowTitle("Success")

        QBtn = QtWidgets.QDialogButtonBox.StandardButton.Ok

        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        

        self.layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel(regNo + s)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_BatchUpdate()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
