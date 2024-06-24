import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QLabel, QPushButton, QMessageBox
# from StudentManagement import *


class PasswordApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.status = 0  # Khởi tạo status mặc định là 0
        self.key = ""

    def initUI(self):

        # Thiết lập cửa sổ
        self.setWindowTitle('Password Checker')
        self.setGeometry(100, 100, 300, 150)

        # Layout chính
        layout = QVBoxLayout()

        # Nhãn hướng dẫn
        self.label = QLabel('Please enter your password:', self)
        layout.addWidget(self.label)

        # Ô nhập mật khẩu
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # Nút kiểm tra mật khẩu
        self.check_button = QPushButton('Check Password', self)
        self.check_button.clicked.connect(self.check_password)
        layout.addWidget(self.check_button)

        self.setLayout(layout)

    def check_password(self):
        entered_password = self.password_input.text()
        self.key = entered_password
        entered_password = 0
        self.correct_password = 0
        # QMessageBox.information(self, 'Success', 'Password is correct!')
        self.status = 1
        self.close()



# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     password_app = PasswordApp()
#     password_app.show()
#     app.exec_()
#
#     if password_app.status == 1:
#         student_info_app = StudentInfoApp()
#         student_info_app.show()
#         sys.exit(app.exec_())
#     else:
#         sys.exit(0)
