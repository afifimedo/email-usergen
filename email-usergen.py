import sys
import random
import string
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QGraphicsDropShadowEffect)
from PyQt6.QtCore import Qt, QTimer, QPointF
from PyQt6.QtGui import QFont, QColor, QAction, QIcon, QPixmap, QPainter, QPen, QPainterPath

class email_usergen (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("email-usergen")
        self.resize(380, 410)
        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(14)

        # Title Header
        title = QLabel("email-usergen")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        title.setObjectName("titleLabel")
        main_layout.addWidget(title)
        main_layout.addSpacing(4)

        # --- Section 1: Username ---
        user_layout = QVBoxLayout()
        user_layout.setSpacing(5)
        user_label = QLabel("USERNAME")
        user_label.setObjectName("sectionLabel")
        user_layout.addWidget(user_label)

        user_row = QHBoxLayout()
        user_row.setSpacing(10)
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Generate to see username...")
        self.user_input.setReadOnly(True)
        self.user_input.setFixedHeight(38)
        user_row.addWidget(self.user_input)

        self.copy_user_btn = QPushButton("Copy")
        self.copy_user_btn.setFixedSize(70, 38)
        self.copy_user_btn.clicked.connect(lambda: self.copy_to_clipboard(self.user_input.text(), self.copy_user_btn))
        user_row.addWidget(self.copy_user_btn)
        user_layout.addLayout(user_row)
        main_layout.addLayout(user_layout)

        # --- Section 2: Email Address ---
        email_layout = QVBoxLayout()
        email_layout.setSpacing(5)
        email_label = QLabel("EMAIL ADDRESS")
        email_label.setObjectName("sectionLabel")
        email_layout.addWidget(email_label)

        email_row = QHBoxLayout()
        email_row.setSpacing(10)
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Generate to see email...")
        self.email_input.setReadOnly(True)
        self.email_input.setFixedHeight(38)
        email_row.addWidget(self.email_input)

        self.copy_email_btn = QPushButton("Copy")
        self.copy_email_btn.setFixedSize(70, 38)
        self.copy_email_btn.clicked.connect(lambda: self.copy_to_clipboard(self.email_input.text(), self.copy_email_btn))
        email_row.addWidget(self.copy_email_btn)
        email_layout.addLayout(email_row)
        main_layout.addLayout(email_layout)

        # --- Section 3: Secure Password ---
        pass_layout = QVBoxLayout()
        pass_layout.setSpacing(5)
        pass_label = QLabel("SECURE PASSWORD")
        pass_label.setObjectName("sectionLabel")
        pass_layout.addWidget(pass_label)

        pass_row = QHBoxLayout()
        pass_row.setSpacing(10)
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Generate to see password...")
        self.pass_input.setReadOnly(True)
        self.pass_input.setFixedHeight(38)
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Eye action toggle (pure white vector icon) - will be added when generate_all is called
        self.toggle_action = QAction(self)
        self.toggle_action.setIcon(self.create_eye_icon(visible=False))
        self.toggle_action.setToolTip("Show / Hide password")
        self.toggle_action.triggered.connect(self.toggle_password_visibility)

        pass_row.addWidget(self.pass_input)

        self.copy_pass_btn = QPushButton("Copy")
        self.copy_pass_btn.setFixedSize(70, 38)
        self.copy_pass_btn.clicked.connect(lambda: self.copy_to_clipboard(self.pass_input.text(), self.copy_pass_btn))
        pass_row.addWidget(self.copy_pass_btn)
        pass_layout.addLayout(pass_row)
        main_layout.addLayout(pass_layout)

        # --- Generate All Button ---
        self.gen_btn = QPushButton("GENERATE ALL")
        self.gen_btn.setFixedHeight(44)
        self.gen_btn.setObjectName("generateAllBtn")
        self.gen_btn.clicked.connect(self.generate_all)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 150))
        self.gen_btn.setGraphicsEffect(shadow)

        main_layout.addWidget(self.gen_btn)

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #000000;
                color: #FFFFFF;
                font-family: 'Segoe UI';
            }
            QMainWindow {
                background-color: #000000;
            }
            #titleLabel {
                color: #FFFFFF;
                font-weight: bold;
            }
            #sectionLabel {
                color: #7E7E84;
                font-size: 9px;
                font-weight: bold;
                letter-spacing: 1px;
            }
            QLineEdit {
                background-color: #121214;
                border: 1px solid #232326;
                border-radius: 8px;
                padding: 6px 12px;
                font-size: 13px;
                color: #FFFFFF;
            }
            QLineEdit:focus {
                border: 1px solid #3A3A40;
            }
            QPushButton {
                background-color: #1B1B1E;
                border: 1px solid #28282D;
                border-radius: 8px;
                color: #FFFFFF;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #26262B;
                border: 1px solid #36363D;
            }
            QPushButton:pressed {
                background-color: #121214;
            }
            QPushButton#generateAllBtn {
                background-color: #1B1B1E;
                border: 1px solid #28282D;
                border-radius: 8px;
                font-size: 12px;
                font-weight: bold;
                letter-spacing: 1px;
                color: #FFFFFF;
            }
            QPushButton#generateAllBtn:hover {
                background-color: #26262B;
                border: 1px solid #36363D;
            }
            QPushButton#generateAllBtn:pressed {
                background-color: #121214;
            }
        """)

    def generate_username(self, length=10):
        chars = string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def generate_email(self, length=10):
        chars = string.ascii_lowercase + string.digits
        local = ''.join(random.choice(chars) for _ in range(length))
        domains = ["proton.me", "skiff.com", "tutanota.com", "duck.com", "gmail.com"]
        return f"{local}@{random.choice(domains)}"

    def generate_password(self, length=16):
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(chars) for _ in range(length))

    def generate_all(self):
        self.user_input.setText(self.generate_username())
        self.email_input.setText(self.generate_email())
        self.pass_input.setText(self.generate_password())
        # Add eye icon action if not already added
        if self.pass_input.actions() == []:
            self.pass_input.addAction(self.toggle_action, QLineEdit.ActionPosition.TrailingPosition)

    def create_eye_icon(self, visible=True):
        pix = QPixmap(32, 32)
        pix.fill(Qt.GlobalColor.transparent)
        p = QPainter(pix)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        pen = QPen(QColor("#FFFFFF"))
        pen.setWidth(2)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
        p.setPen(pen)
        
        path = QPainterPath()
        path.moveTo(4, 16)
        path.cubicTo(10, 8, 22, 8, 28, 16)
        path.cubicTo(22, 24, 10, 24, 4, 16)
        p.drawPath(path)
        
        p.setBrush(QColor("#FFFFFF"))
        p.drawEllipse(QPointF(16, 16), 3.5, 3.5)
        
        if not visible:
            p.setBrush(Qt.BrushStyle.NoBrush)
            p.drawLine(6, 6, 26, 26)
            
        p.end()
        return QIcon(pix)

    def toggle_password_visibility(self):
        if self.pass_input.echoMode() == QLineEdit.EchoMode.Password:
            self.pass_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.toggle_action.setIcon(self.create_eye_icon(visible=True))
        else:
            self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.toggle_action.setIcon(self.create_eye_icon(visible=False))

    def copy_to_clipboard(self, text, button):
        if text:
            QApplication.clipboard().setText(text)
            original_text = button.text()
            button.setText("Copied!")
            button.setStyleSheet("background-color: #1E3322; border: 1px solid #355E3B; color: #5AF07A;")
            QTimer.singleShot(1200, lambda: self.reset_copy_button(button, original_text))

    def reset_copy_button(self, button, original_text):
        button.setText(original_text)
        button.setStyleSheet("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 10))
    window = email_usergen()
    window.show()
    sys.exit(app.exec())
