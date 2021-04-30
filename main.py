#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QCheckBox, QLineEdit,
                             QApplication, QLabel, QSlider)


class DataSpider(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Site link
        self.site_link = QLabel('Enter site link:', self)
        self.site_link.move(20, 22)

        self.edit_site_link = QLineEdit(self)
        self.edit_site_link.move(150, 20)

        # Color Processing
        self.color_processing = QCheckBox('Color processing', self)
        self.color_processing.move(20, 100)
        self.color_processing.toggle()
        self.color_processing.stateChanged.connect(self.Color)

        # Normalization
        self.normalization = QCheckBox('Normalization', self)
        self.normalization.move(140, 100)
        self.normalization.toggle()
        self.normalization.stateChanged.connect(self.Normalization)

        # Patch to Save
        self.patch_to_save = QLabel('Enter patch to save data:', self)
        self.patch_to_save.move(20, 62)

        self.edit_patch_to_save = QLineEdit(self)
        self.edit_patch_to_save.move(150, 60)

        # Slider
        self.img_value = QLabel('Количество картин: ', self)
        self.img_value.move(20, 140)

        self.stop_value = QSlider(Qt.Horizontal, self)
        self.stop_value.setGeometry(20, 160, 200, 30)
        self.stop_value.valueChanged[int].connect(self.slider_change)

        self.img_value = QLabel('00', self)
        self.img_value.move(120, 200)

        # Button
        self.btn = QPushButton('Start', self)
        self.btn.move(115, 255)
        self.btn.clicked.connect(self.start)


        self.setGeometry(500, 400, 300, 300)
        self.setWindowTitle('Data Spider')
        self.show()

    def Color(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('Checked')
        else:
            self.setWindowTitle('UnChecked')

    def Normalization(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('Norma')
        else:
            self.setWindowTitle('UnNorma')

    def start(self):
        import parser_kurs as pk
        print(self.edit_site_link.text())
        print(self.edit_patch_to_save.text())
        result = pk.parsing(self.edit_site_link.text(), self.edit_patch_to_save.text(), 1, 1, self.stop_value.value())
        if result:
            self.setWindowTitle('OK')

    def slider_change(self):
        self.img_value.setText(str(self.stop_value.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = DataSpider()
    sys.exit(app.exec_())
