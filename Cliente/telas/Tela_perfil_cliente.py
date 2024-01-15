# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\perfil_cliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class PerfilCliente(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line_nome = QtWidgets.QLineEdit(self.frame)
        self.line_nome.setReadOnly(True)
        self.line_nome.setObjectName("line_nome")
        self.horizontalLayout.addWidget(self.line_nome)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.line_cpf = QtWidgets.QLineEdit(self.frame)
        self.line_cpf.setReadOnly(True)
        self.line_cpf.setObjectName("line_cpf")
        self.horizontalLayout_2.addWidget(self.line_cpf)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.nascimento = QtWidgets.QDateEdit(self.frame)
        self.nascimento.setReadOnly(True)
        self.nascimento.setObjectName("nascimento")
        self.horizontalLayout_3.addWidget(self.nascimento)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.email = QtWidgets.QLineEdit(self.frame)
        self.email.setReadOnly(True)
        self.email.setObjectName("email")
        self.horizontalLayout_4.addWidget(self.email)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.line_enderco = QtWidgets.QLineEdit(self.frame)
        self.line_enderco.setReadOnly(True)
        self.line_enderco.setObjectName("line_enderco")
        self.horizontalLayout_6.addWidget(self.line_enderco)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.b_voltar = QtWidgets.QPushButton(self.frame)
        self.b_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/feather/arrow-left-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_voltar.setIcon(icon)
        self.b_voltar.setFlat(False)
        self.b_voltar.setObjectName("b_voltar")
        self.horizontalLayout_5.addWidget(self.b_voltar)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.b_editar = QtWidgets.QPushButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Icons/feather/pen-tool.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_editar.setIcon(icon1)
        self.b_editar.setObjectName("b_editar")
        self.horizontalLayout_5.addWidget(self.b_editar)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nome:"))
        self.label_2.setText(_translate("MainWindow", "CPF:"))
        self.label_3.setText(_translate("MainWindow", "Nascimento:"))
        self.label_4.setText(_translate("MainWindow", "E-mail:"))
        self.label_6.setText(_translate("MainWindow", "Endereço:"))
        self.b_voltar.setText(_translate("MainWindow", "Voltar"))
        self.b_editar.setText(_translate("MainWindow", "Editar perfil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PerfilCliente()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
