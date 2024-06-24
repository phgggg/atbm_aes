import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QColor, QPixmap
from PyQt5.QtCore import Qt
import pyodbc
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Protocol.KDF import PBKDF2
from base64 import b64encode, b64decode
from login import *

status = 0

# Thông tin kết nối cơ sở dữ liệu
server = 'DESKTOP-2NFPMCV'  # Thay đổi thành tên máy chủ SQL Server trên máy bản thân
database = 'QLSV'

# Tạo hoặc đọc khóa AES từ tệp
key_file = 'key.bin'

if not os.path.exists(key_file):
    key = get_random_bytes(32)

    with open(key_file, 'wb') as f:
        f.write(key)

else:
    with open(key_file, 'rb') as f:
        key = f.read()


# Hàm mã hóa
def encrypt_data(plaintext):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
    return b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')


# Hàm giải mã
def decrypt_data(ciphertext):
    data = b64decode(ciphertext)
    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8')


class StudentInfoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initDB()
        self.loadStudents()

    def initUI(self):
        # Tạo các thành phần giao diện
        self.imageLabel = QLabel()
        self.imageLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.imageLabel.setPixmap(QPixmap("pic.jpeg").scaled(100, 100, Qt.KeepAspectRatio))

        self.descriptionLabel = QLabel("QUẢN LÍ THÔNG TIN SINH VIÊN ĐẠI HỌC CÔNG NGHIỆP HÀ NỘI")
        self.descriptionLabel.setFont(QFont('Times New Roman', 31))
        self.descriptionLabel.setAlignment(Qt.AlignCenter)

        self.nameLabel = QLabel('Tên:')
        self.nameLabel.setFont(QFont('Times New Roman', 14))
        self.nameLabel.setStyleSheet("color: black;")
        self.nameInput = QLineEdit()
        self.nameInput.setStyleSheet("background-color: white; color: black;")

        self.idLabel = QLabel('Mã sinh viên:')
        self.idLabel.setFont(QFont('Times New Roman', 14))
        self.idLabel.setStyleSheet("color: black;")
        self.idInput = QLineEdit()
        self.idInput.setStyleSheet("background-color: white; color: black;")

        self.classLabel = QLabel('Lớp:')
        self.classLabel.setFont(QFont('Times New Roman', 14))
        self.classLabel.setStyleSheet("color: black;")
        self.classInput = QLineEdit()
        self.classInput.setStyleSheet("background-color: white; color: black;")

        self.editButton = QPushButton('Sửa sinh viên')
        self.editButton.setFont(QFont('Times New Roman', 14))
        self.editButton.setStyleSheet("background-color: orange; color: white;")
        self.editButton.clicked.connect(self.editStudent)

        self.addButton = QPushButton('Thêm sinh viên')
        self.addButton.setFont(QFont('Times New Roman', 14))
        self.addButton.setStyleSheet("background-color: green; color: white;")
        self.addButton.clicked.connect(self.addStudent)

        self.loadButton = QPushButton('Xem sinh viên')
        self.loadButton.setFont(QFont('Times New Roman', 14))
        self.loadButton.setStyleSheet("background-color: blue; color: white;")
        self.loadButton.clicked.connect(self.loadStudents)

        self.sortButton = QPushButton('Sắp xếp theo tên')
        self.sortButton.setFont(QFont('Times New Roman', 14))
        self.sortButton.setStyleSheet("background-color: purple; color: white;")
        self.sortButton.clicked.connect(self.sortStudentsByName)

        self.delButton = QPushButton('Xóa')
        self.delButton.setFont(QFont('Times New Roman', 14))
        self.delButton.setStyleSheet("background-color: purple; color: white;")
        self.delButton.clicked.connect(self.deleteStudent)

        self.InpButton = QPushButton('Nhập điểm')
        self.InpButton.setFont(QFont('Times New Roman', 14))
        self.InpButton.setStyleSheet("background-color: green; color: white;")
        self.InpButton.clicked.connect(self.addRes)

        self.ResultButton = QPushButton('Xem điểm')
        self.ResultButton.setFont(QFont('Times New Roman', 14))
        self.ResultButton.setStyleSheet("background-color: blue; color: white;")
        self.ResultButton.clicked.connect(self.loadStudentsRes)

        self.exitButton = QPushButton('Thoát')
        self.exitButton.setFont(QFont('Times New Roman', 14))
        self.exitButton.setStyleSheet("background-color: red; color: white;")
        self.exitButton.clicked.connect(self.close)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Tên', 'Mã sinh viên', 'Lớp'])
        self.table.setStyleSheet("background-color: white; color: black;")
        self.table.horizontalHeader().setStyleSheet("background-color: lightgray; color: black;")
        self.table.setColumnWidth(0, 150)

        self.tableres = QTableWidget()
        self.tableres.setColumnCount(4)
        self.tableres.setHorizontalHeaderLabels(['Tên', 'Mã sinh viên', 'Tên môn học', 'Điểm'])
        self.tableres.setStyleSheet("background-color: white; color: black;")
        self.tableres.horizontalHeader().setStyleSheet("background-color: lightgray; color: black;")
        self.tableres.setColumnWidth(0, 150)

        formLayout = QHBoxLayout()
        formLayout.addWidget(self.nameLabel)
        formLayout.addWidget(self.nameInput)
        formLayout.addWidget(self.idLabel)
        formLayout.addWidget(self.idInput)
        formLayout.addWidget(self.classLabel)
        formLayout.addWidget(self.classInput)
        formLayout.addWidget(self.addButton)
        formLayout.addWidget(self.loadButton)
        formLayout.addWidget(self.sortButton)
        formLayout.addWidget(self.editButton)
        formLayout.addWidget(self.delButton)
        formLayout.addWidget(self.InpButton)
        formLayout.addWidget(self.ResultButton)
        formLayout.addWidget(self.exitButton)

        imageAndDescriptionLayout = QHBoxLayout()
        imageAndDescriptionLayout.addWidget(self.imageLabel)
        imageAndDescriptionLayout.addWidget(self.descriptionLabel)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(imageAndDescriptionLayout)
        mainLayout.addLayout(formLayout)
        mainLayout.addWidget(self.table)
        mainLayout.addWidget(self.tableres)

        self.setLayout(mainLayout)
        self.setWindowTitle('Quản lý thông tin sinh viên')
        self.setStyleSheet("background-color: white;")
        self.setGeometry(100, 100, 1200, 600)

    def initDB(self):
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                                   + server + ';DATABASE=' + database + ';Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()
        self.conn.commit()

    def addStudent(self):
        maSinhVien = self.idInput.text()
        print("masv " + maSinhVien)
        tenSinhVien = self.nameInput.text()
        print("tensv " + tenSinhVien)
        lop = self.classInput.text()

        if maSinhVien and tenSinhVien and lop:
            self.cursor.execute('SELECT * FROM SinhVien WHERE maSinhVien = ?', (maSinhVien,))
            existing_student_id = self.cursor.fetchone()
            if existing_student_id:
                msg = QMessageBox()
                msg.setText('Mã sinh viên đã tồn tại. Vui lòng nhập lại.')
                msg.setStyleSheet("color: black;")
                msg.exec_()
            else:
                encrypted_tenSinhVien = encrypt_data(tenSinhVien)
                encrypted_lop = encrypt_data(lop)
                self.cursor.execute('''
                    INSERT INTO SinhVien (maSinhVien, tenSinhVien, lop) VALUES (?, ?, ?)
                ''', (maSinhVien, encrypted_tenSinhVien, encrypted_lop))

                self.conn.commit()
                # self.idInput.clear()
                # self.nameInput.clear()
                # self.classInput.clear()

    def loadStudents(self):
        self.cursor.execute('SELECT maSinhVien, tenSinhVien, lop FROM SinhVien')
        students = self.cursor.fetchall()

        self.table.setRowCount(0)
        for row_number, row_data in enumerate(students):
            self.table.insertRow(row_number)
            maSinhVien, encrypted_tenSinhVien, encrypted_lop = row_data
            tenSinhVien = decrypt_data(encrypted_tenSinhVien)
            lop = decrypt_data(encrypted_lop)
            self.table.setItem(row_number, 0, QTableWidgetItem(tenSinhVien))
            self.table.setItem(row_number, 1, QTableWidgetItem(maSinhVien))
            self.table.setItem(row_number, 2, QTableWidgetItem(lop))

    def loadStudentsRes(self):
        selected_items = self.table.selectedItems()
        if len(selected_items) > 0:
            row = selected_items[0].row()
            maSV_item = self.table.item(row, 1)
            if maSV_item:
                msv = maSV_item.text()
                self.cursor.execute('select dbo.SinhVien.maSinhVien, tenSinhVien, tenMonHoc, diem from dbo.SinhVien '
                                    'join dbo.Diem on dbo.SinhVien.maSinhVien = dbo.Diem.maSinhVien '
                                    'join MonHoc on dbo.Diem.maMonHoc = dbo.MonHoc.maMonHoc '
                                    'where dbo.SinhVien.maSinhVien = ?', msv)
                res = self.cursor.fetchall()
                print(res)
                self.tableres.setRowCount(0)
                for row_number, row_data in enumerate(res):
                    self.tableres.insertRow(row_number)
                    maSinhVien, encrypted_tenSinhVien, tenMonHoc, Diem = row_data
                    tenSinhVien = decrypt_data(encrypted_tenSinhVien)
                    self.tableres.setItem(row_number, 0, QTableWidgetItem(tenSinhVien))
                    self.tableres.setItem(row_number, 1, QTableWidgetItem(maSinhVien))
                    self.tableres.setItem(row_number, 2, QTableWidgetItem(tenMonHoc))
                    self.tableres.setItem(row_number, 3, QTableWidgetItem(str(Diem)))

    def sortStudentsByName(self):
        self.cursor.execute('SELECT maSinhVien, tenSinhVien, lop FROM SinhVien')
        students = sorted(self.cursor.fetchall(), key=lambda x: decrypt_data(x[1]))

        self.table.setRowCount(0)
        for row_number, row_data in enumerate(students):
            self.table.insertRow(row_number)
            maSinhVien, encrypted_tenSinhVien, encrypted_lop = row_data
            tenSinhVien = decrypt_data(encrypted_tenSinhVien)
            lop = decrypt_data(encrypted_lop)
            self.table.setItem(row_number, 1, QTableWidgetItem(maSinhVien))
            self.table.setItem(row_number, 0, QTableWidgetItem(tenSinhVien))
            self.table.setItem(row_number, 2, QTableWidgetItem(lop))

    def deleteStudent(self):
        selected_items = self.table.selectedItems()
        if len(selected_items) > 0:
            row = selected_items[0].row()
            maSinhVien_item = self.table.item(row, 1)
            if maSinhVien_item:
                maSinhVien = maSinhVien_item.text()
                reply = QMessageBox.question(self, 'Xác nhận',
                                             f'Bạn có chắc chắn muốn xóa sinh viên có mã {maSinhVien} không?',
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    self.cursor.execute('DELETE FROM SinhVien WHERE maSinhVien = ?', (maSinhVien,))
                    self.conn.commit()
                    self.loadStudents()
        else:
            QMessageBox.information(self, 'Thông báo', 'Vui lòng chọn một sinh viên để xóa.', QMessageBox.Ok)

    def editStudent(self):
        selected_items = self.table.selectedItems()
        if len(selected_items) > 0:
            row = selected_items[0].row()
            maSinhVien_item = self.table.item(row, 1)
            tenSinhVien_item = self.table.item(row, 0)
            lop_item = self.table.item(row, 2)
            if maSinhVien_item and tenSinhVien_item and lop_item:
                maSinhVien = maSinhVien_item.text()
                tenSinhVien = tenSinhVien_item.text()
                lop = lop_item.text()

                new_tenSinhVien, new_lop, ok = self.editStudentDialog(tenSinhVien, lop)
                if ok:
                    encrypted_tenSinhVien = encrypt_data(new_tenSinhVien)
                    encrypted_lop = encrypt_data(new_lop)
                    self.cursor.execute('UPDATE SinhVien SET tenSinhVien = ?, lop = ? WHERE maSinhVien = ?',
                                        (encrypted_tenSinhVien, encrypted_lop, maSinhVien))
                    self.conn.commit()
                    self.loadStudents()

    def editStudentDialog(self, tenSinhVien, lop):
        dialog = QDialog(self)
        dialog.setWindowTitle('Chỉnh sửa thông tin sinh viên')

        tenSinhVienLabel = QLabel("Tên SV:")
        edit_tenSinhVien = QLineEdit(tenSinhVien)
        lopLabel = QLabel("Lớp:")
        edit_lop = QLineEdit(lop)

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        okButton.clicked.connect(dialog.accept)
        cancelButton.clicked.connect(dialog.reject)

        formLayout = QVBoxLayout()
        formLayout.addWidget(tenSinhVienLabel)
        formLayout.addWidget(edit_tenSinhVien)
        formLayout.addWidget(lopLabel)
        formLayout.addWidget(edit_lop)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(formLayout)
        mainLayout.addLayout(buttonLayout)

        dialog.setLayout(mainLayout)

        result = dialog.exec_()
        return edit_tenSinhVien.text(), edit_lop.text(), result == QDialog.Accepted

    def addRes(self):
        msv, maMH, diem, ok = self.InpDialog()
        if ok:
            try:
                # Chuyển đổi diem sang float nếu cần thiết
                diem = float(diem)
                self.cursor.execute("INSERT INTO dbo.diem (maSinhVien, maMonHoc, diem) VALUES (?, ?, ?)",
                                    (msv, maMH, diem))
                self.conn.commit()
                print("Dữ liệu đã được thêm thành công.")
            except ValueError:
                print("Điểm phải là một số hợp lệ.")
            except Exception as e:
                print(f"Đã xảy ra lỗi: {e}")
                try:
                    self.cursor.execute("UPDATE [dbo].[Diem] SET [diem] = ? WHERE dbo.Diem.maSinhVien = ? and dbo.Diem.maMonHoc = ?",
                                        (diem, msv, maMH))
                    self.conn.commit()
                except Exception as e:
                    print(f"Đã xảy ra lỗi: {e}")

    def InpDialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Nhập điểm')

        # Initialize values
        tenSinhVien = ""
        mh = ""
        diem = ""

        # Create labels and line edits
        msvLabel = QLabel("Mã SV:")
        edit_msv = QLineEdit(tenSinhVien)
        maMHLabel = QLabel("Mã môn học:")
        edit_maMH = QLineEdit(mh)
        DiemLabel = QLabel("Điểm:")
        edit_Diem = QLineEdit(diem)

        # Create buttons
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        # Connect buttons to dialog methods
        okButton.clicked.connect(dialog.accept)
        cancelButton.clicked.connect(dialog.reject)

        # Create layouts and add widgets
        formLayout = QVBoxLayout()
        formLayout.addWidget(msvLabel)
        formLayout.addWidget(edit_msv)
        formLayout.addWidget(maMHLabel)
        formLayout.addWidget(edit_maMH)
        formLayout.addWidget(DiemLabel)
        formLayout.addWidget(edit_Diem)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(formLayout)
        mainLayout.addLayout(buttonLayout)

        dialog.setLayout(mainLayout)

        # Execute dialog and return values
        result = dialog.exec_()
        return edit_msv.text(), edit_maMH.text(), edit_Diem.text(), result == QDialog.Accepted

    def closeEvent(self, event):
        self.conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    password_app = PasswordApp()
    password_app.show()
    app.exec_()

    if password_app.status == 1:
        key = password_app.key.encode('utf-8', 'ignore') + password_app.key.encode('utf-8', 'ignore')
        password_app.key = ""
        print(password_app.key)
        student_info_app = StudentInfoApp()
        student_info_app.show()
        sys.exit(app.exec_())
    else:
        sys.exit(0)
