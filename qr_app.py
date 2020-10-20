import os
import sys

import qrcode
from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QStatusBar, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap, QImage
from PyQt5.QtCore import Qt

class QRCodeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 550) # works best for the pictogram
        self.setWindowTitle('QR Code Generator')
        self.initUI()

    def initUI(self):
        font = QFont('Helvetica', 16)

        mainLayout = QVBoxLayout()
        entryLayout = QHBoxLayout()
        buttonLayout = QHBoxLayout()
        imageLayout = QVBoxLayout()
        imageLayout.addStretch()

        label = QLabel('Enter text:')
        label.setFont(font)

        self.textEntry = QLineEdit()
        self.textEntry.setFont(font)
        entryLayout.addWidget(label)
        entryLayout.addWidget(self.textEntry)
        mainLayout.addLayout(entryLayout)

        self.buttonGenerate = QPushButton('Generate QR Code')
        buttonLayout.addWidget(self.buttonGenerate)
        self.buttonGenerate.clicked.connect(self.generate_qr_code)
        self.buttonSaveImage = QPushButton('Save QR image')
        buttonLayout.addWidget(self.buttonSaveImage)
        self.buttonSaveImage.clicked.connect(self.save_qr_code)
        self.buttonClear = QPushButton('Clear')
        buttonLayout.addWidget(self.buttonClear)
        self.buttonClear.clicked.connect(self.clear)
        mainLayout.addLayout(buttonLayout)

        self.imageLabel = QLabel()
        self.imageLabel.setAlignment(Qt.AlignCenter)
        imageLayout.addWidget(self.imageLabel)
        mainLayout.addLayout(imageLayout)

        self.statusBar = QStatusBar()
        mainLayout.addWidget(self.statusBar)


        self.setLayout(mainLayout)

    def generate_qr_code(self):
        ## TODO: 
        # if text area is cleared, it still generates code for previous text
        text = self.textEntry.text()
        img = qrcode.make(text)
        qr = ImageQt(img)
        pix = QPixmap.fromImage(qr)
        self.imageLabel.setPixmap(pix)

    def save_qr_code(self):
        current_dir = os.getcwd()
        filename = self.textEntry.text()

        if filename:
            filename = os.path.join(current_dir, filename + '.png')
            self.imageLabel.pixmap().save(filename)
            self.statusBar.showMessage('Image saved at {}'.format(filename))

    def clear(self):
        self.textEntry.clear()
        self.imageLabel.clear()
        self.statusBar.clearMessage()



def main():
    app = QApplication(sys.argv)
    app.setStyleSheet('QPushButton{Height: 50px; font-size: 26px}')

    demo = QRCodeApp()
    demo.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
