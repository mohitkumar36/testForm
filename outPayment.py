from PyQt6 import QtCore, QtGui, QtWidgets
from datamanage import doPayment


class Ui_completePay(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(203, 171)
        self.Pay = QtWidgets.QDialogButtonBox(Dialog)
        self.Pay.setGeometry(QtCore.QRect(10, 100, 181, 51))
        self.Pay.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.Pay.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Close|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.Pay.setCenterButtons(True)
        self.Pay.setObjectName("Pay")
        self.monthText = QtWidgets.QLabel(Dialog)
        self.monthText.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.monthText.setObjectName("monthText")
        self.monthSelect = QtWidgets.QComboBox(Dialog)
        self.monthSelect.setGeometry(QtCore.QRect(110, 30, 68, 22))
        self.monthSelect.setObjectName("monthSelect")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.monthSelect.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 70, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 70, 49, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.Pay.accepted.connect(Dialog.accept) # type: ignore
        self.Pay.rejected.connect(Dialog.reject) # type: ignore

        self.Pay.accepted.connect(lambda: self.complete())

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def complete(self):
        month = self.monthSelect.currentText()
        regNo = self.lineEdit.text()
        #print(month, regNo)
        done = doPayment(regNo, month)
        print(done)
        if done:
            dlg = CustomDialog("Success")
            dlg.exec()
        else:
            dlg = CustomDialog("Failed")
            dlg.exec()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.monthText.setText(_translate("Dialog", "Select Month:"))
        self.monthSelect.setItemText(0, _translate("Dialog", "JAN"))
        self.monthSelect.setItemText(1, _translate("Dialog", "FEB"))
        self.monthSelect.setItemText(2, _translate("Dialog", "APRIL"))
        self.monthSelect.setItemText(3, _translate("Dialog", "APRIL"))
        self.monthSelect.setItemText(4, _translate("Dialog", "MAY"))
        self.monthSelect.setItemText(5, _translate("Dialog", "JUN"))
        self.monthSelect.setItemText(6, _translate("Dialog", "JUL"))
        self.monthSelect.setItemText(7, _translate("Dialog", "AUG"))
        self.monthSelect.setItemText(8, _translate("Dialog", "SEPT"))
        self.monthSelect.setItemText(9, _translate("Dialog", "OCT"))
        self.monthSelect.setItemText(10, _translate("Dialog", "NOV"))
        self.monthSelect.setItemText(11, _translate("Dialog", "DECEM"))
        self.label.setText(_translate("Dialog", "Reg No:"))


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
    ui = Ui_completePay()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
