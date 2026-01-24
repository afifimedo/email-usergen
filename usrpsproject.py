import sys
import random
import string
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QGraphicsDropShadowEffect)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor, QAction

class HandsomeGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pro Identity Generator")
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
        title = QLabel("Identity Generator")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        title.setObjectName("titleLabel")
        main_layout.addWidget(title)

        # Username Section
        user_label = QLabel("USERNAME")
        user_label.setObjectName("sectionLabel")
        main_layout.addWidget(user_label)

        user_row = QHBoxLayout()
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Generate to see username...")
        self.user_input.setReadOnly(True)
        user_row.addWidget(self.user_input)

        copy_user_btn = QPushButton("Copy")
        copy_user_btn.setFixedSize(80, 45)
        copy_user_btn.clicked.connect(lambda: self.copy_to_clipboard(self.user_input.text()))
        user_row.addWidget(copy_user_btn)
        main_layout.addLayout(user_row)

        # Password Section
        pass_label = QLabel("PASSWORD")
        pass_label.setObjectName("sectionLabel")
        main_layout.addWidget(pass_label)

        pass_row = QHBoxLayout()
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Generate to see password...")
        self.pass_input.setReadOnly(True)
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        
        # Eye Action integrated in QLineEdit using QAction to fix TypeError
        self.toggle_action = QAction("Show 👁", self)
        self.toggle_action.triggered.connect(self.toggle_password_visibility)
        self.pass_input.addAction(self.toggle_action, QLineEdit.ActionPosition.TrailingPosition)
        
        user_row.setContentsMargins(0, 0, 0, 0) # ensure alignment
        pass_row.addWidget(self.pass_input)

        copy_pass_btn = QPushButton("Copy")
        copy_pass_btn.setFixedSize(80, 45)
        copy_pass_btn.clicked.connect(lambda: self.copy_to_clipboard(self.pass_input.text()))
        pass_row.addWidget(copy_pass_btn)
        main_layout.addLayout(pass_row)

        # Generate Button
        self.gen_btn = QPushButton("GENERATE NEW")
        self.gen_btn.setFixedHeight(55)
        self.gen_btn.clicked.connect(self.generate_identity)
        
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
                background-color: #0F172A;
                color: #F8FAFC;
                font-family: 'Segoe UI', sans-serif;
            }
            #titleLabel {
                color: #FFFFFF;
                margin-bottom: 10px;
            }
            #sectionLabel {
                color: #94A3B8;
                font-size: 10px;
                font-weight: bold;
                letter-spacing: 1px;
            }
            QLineEdit {
                background-color: #1E293B;
                border: 1px solid #334155;
                border-radius: 8px;
                padding: 10px 15px;
                font-size: 14px;
                color: #FFFFFF;
            }
            QLineEdit:focus {
                border: 1px solid #38BDF8;
            }
            QPushButton {
                background-color: #334155;
                border: none;
                border-radius: 8px;
                color: #FFFFFF;
                font-weight: bold;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #475569;
            }
            QPushButton:pressed {
                background-color: #1E293B;
            }
            QMainWindow {
                background-color: #0F172A;
            }
            /* Special Generate Button Style */
            QPushButton:last-child {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                                            stop:0 #0EA5E9, stop:1 #2563EB);
                font-size: 15px;
                letter-spacing: 1px;
            }
            QPushButton:last-child:hover {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                                            stop:0 #38BDF8, stop:1 #3B82F6);
            }
        """)

    def generate_username(self, length=10):
        chars = string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def generate_password(self, length=12):
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def generate_identity(self):
        self.user_input.setText(self.generate_username())
        self.pass_input.setText(self.generate_password())

    def toggle_password_visibility(self):
        if self.pass_input.echoMode() == QLineEdit.EchoMode.Password:
            self.pass_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.toggle_action.setText("Hide 🙈")
        else:
            self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.toggle_action.setText("Show 👁")

    def copy_to_clipboard(self, text):
        if text:
            QApplication.clipboard().setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HandsomeGenerator()
    window.show()
    sys.exit(app.exec())
