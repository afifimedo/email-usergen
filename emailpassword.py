import sys
import random
import string
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QFrame, QGraphicsDropShadowEffect)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QColor

class HandsomeGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secure Credentials Generator")
        self.setFixedSize(500, 400)
        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(20)

        # Title
        title = QLabel("Credentials Generator")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        title.setObjectName("titleLabel")
        main_layout.addWidget(title)

        # Email Section
        email_label = QLabel("EMAIL ADDRESS")
        email_label.setObjectName("sectionLabel")
        main_layout.addWidget(email_label)

        email_row = QHBoxLayout()
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Generate to see email...")
        self.email_input.setReadOnly(True)
        email_row.addWidget(self.email_input)

        copy_email_btn = QPushButton("Copy")
        copy_email_btn.setFixedSize(80, 45)
        copy_email_btn.clicked.connect(lambda: self.copy_to_clipboard(self.email_input.text()))
        email_row.addWidget(copy_email_btn)
        main_layout.addLayout(email_row)

        # Password Section
        pass_label = QLabel("SECURE PASSWORD")
        pass_label.setObjectName("sectionLabel")
        main_layout.addWidget(pass_label)

        pass_row = QHBoxLayout()
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Generate to see password...")
        self.pass_input.setReadOnly(True)
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        pass_row.addWidget(self.pass_input)

        copy_pass_btn = QPushButton("Copy")
        copy_pass_btn.setFixedSize(80, 45)
        copy_pass_btn.clicked.connect(lambda: self.copy_to_clipboard(self.pass_input.text()))
        pass_row.addWidget(copy_pass_btn)
        main_layout.addLayout(pass_row)

        # Generate Button
        self.gen_btn = QPushButton("GENERATE NEW")
        self.gen_btn.setFixedHeight(55)
        self.gen_btn.clicked.connect(self.generate_credentials)
        
        # Shadow effect for generate button
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QColor(0, 0, 0, 80))
        self.gen_btn.setGraphicsEffect(shadow)
        
        main_layout.addStretch()
        main_layout.addWidget(self.gen_btn)

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: #E0E0E0;
                font-family: 'Segoe UI', sans-serif;
            }
            #titleLabel {
                color: #FFFFFF;
                margin-bottom: 10px;
            }
            #sectionLabel {
                color: #888888;
                font-size: 10px;
                font-weight: bold;
                letter-spacing: 1px;
            }
            QLineEdit {
                background-color: #1E1E1E;
                border: 1px solid #333333;
                border-radius: 8px;
                padding: 10px 15px;
                font-size: 14px;
                color: #FFFFFF;
            }
            QLineEdit:focus {
                border: 1px solid #3D5AFE;
            }
            QPushButton {
                background-color: #2C2C2C;
                border: none;
                border-radius: 8px;
                color: #FFFFFF;
                font-weight: bold;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #3D3D3D;
            }
            QPushButton:pressed {
                background-color: #1A1A1A;
            }
            QPushButton#titleLabel {
                background-color: transparent;
            }
            QMainWindow {
                background-color: #121212;
            }
            /* Special Generate Button Style */
            QPushButton:last-child {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                                            stop:0 #3D5AFE, stop:1 #536DFE);
                font-size: 15px;
                letter-spacing: 1px;
            }
            QPushButton:last-child:hover {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                                            stop:0 #536DFE, stop:1 #6D83FF);
            }
        """)

    def generate_email(self, length=10):
        chars = string.ascii_lowercase + string.digits
        local = ''.join(random.choice(chars) for _ in range(length))
        domains = ["proton.me", "skiff.com", "tutanota.com", "duck.com"]
        return f"{local}@{random.choice(domains)}"

    def generate_password(self, length=16):
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(chars) for _ in range(length))

    def generate_credentials(self):
        self.email_input.setText(self.generate_email())
        self.pass_input.setText(self.generate_password())
        # Brief animation effect could go here, but keeping it simple and handsome

    def copy_to_clipboard(self, text):
        if text:
            QApplication.clipboard().setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HandsomeGenerator()
    window.show()
    sys.exit(app.exec())
