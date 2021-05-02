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

        # Normalization
        self.normalization = QCheckBox('Normalization', self)
        self.normalization.move(20, 100)
        self.normalization.toggle()

        # Patch to Save
        self.patch_to_save = QLabel('Enter patch to save data:', self)
        self.patch_to_save.move(20, 62)

        self.edit_patch_to_save = QLineEdit(self)
        self.edit_patch_to_save.move(150, 60)

        # Width
        self.width = QLabel('Width:', self)
        self.width.move(20, 140)

        self.edit_width = QLineEdit(self)
        self.edit_width.move(150, 140)

        # Height
        self.height= QLabel('Height:', self)
        self.height.move(20, 180)

        self.edit_height = QLineEdit(self)
        self.edit_height.move(150, 180)

        # Patch to Save
        self.patch_to_save = QLabel('Enter patch to save data:', self)
        self.patch_to_save.move(20, 62)

        self.edit_patch_to_save = QLineEdit(self)
        self.edit_patch_to_save.move(150, 60)

        # Slider
        self.img_value = QLabel('Count of pictures: ', self)
        self.img_value.move(20, 215)

        self.stop_value = QSlider(Qt.Horizontal, self)
        self.stop_value.setGeometry(20, 240, 200, 30)
        self.stop_value.valueChanged[int].connect(self.slider_change)

        self.img_value = QLabel('00', self)
        self.img_value.move(120, 215)

        # Button
        self.btn = QPushButton('Start', self)
        self.btn.move(115, 340)
        self.btn.clicked.connect(self.start)

        # Progress Bar
        self.status = QLabel('Starting' + '\n Errors: 0' + '\n Success: 0', self)
        self.status.move(20, 280)

        self.setGeometry(500, 400, 300, 400)
        self.setWindowTitle('Data Spider')
        self.show()

    def Color(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('Checked')
        else:
            self.setWindowTitle('UnChecked')

    def start(self):
        import parser_kurs as pk
        result, errors, success = pk.parsing(self.edit_site_link.text(), self.edit_patch_to_save.text(),
                                             self.normalization.checkState(), self.stop_value.value(),
                                             self.edit_width.text(), self.edit_height.text())
        if result:
            self.status.setText('Done!' + '\n Errors:' + str(errors) + '\n Success:' + str(success))

    def slider_change(self):
        self.img_value.setText(str(self.stop_value.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = DataSpider()
    sys.exit(app.exec_())

# https://macrosvit.com.ua/impressionizm/collections-43480/
# D:/Dataset/Impr