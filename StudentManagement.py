import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QFont, QColor, QPixmap
from PyQt5.QtCore import Qt
import pyodbc

server = 'DESKTOP-2NFPMCV'  # Thay đổi thành tên máy chủ SQL Server trên máy bản thân
database = 'QLSV'

class StudentInfoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initDB()

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

        # self.subjectLabel = QLabel('Môn:')
        # self.subjectLabel.setFont(QFont('Times New Roman', 14))
        # self.subjectLabel.setStyleSheet("color: black;")
        # self.subjectInput = QLineEdit()
        # self.subjectInput.setStyleSheet("background-color: white; color: black;")

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

        self.exitButton = QPushButton('Thoát')
        self.exitButton.setFont(QFont('Times New Roman', 14))
        self.exitButton.setStyleSheet("background-color: red; color: white;")
        self.exitButton.clicked.connect(self.close)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Tên', 'Mã sinh viên', 'Lớp'])
        self.table.setStyleSheet("background-color: white; color: black;")
        self.table.horizontalHeader().setStyleSheet("background-color: lightgray; color: black;")
        # self.table.cellClicked.connect(self.deleteStudent)

        # Chỉnh độ rộng cột "Tên"
        self.table.setColumnWidth(0, 150)  # Đặt độ rộng của cột "Tên" là 150 pixels

        # Sắp xếp giao diện
        formLayout = QHBoxLayout()
        formLayout.addWidget(self.nameLabel)
        formLayout.addWidget(self.nameInput)
        formLayout.addWidget(self.idLabel)
        formLayout.addWidget(self.idInput)
        formLayout.addWidget(self.classLabel)
        formLayout.addWidget(self.classInput)
        # formLayout.addWidget(self.subjectLabel)
        # formLayout.addWidget(self.subjectInput)
        formLayout.addWidget(self.addButton)
        formLayout.addWidget(self.loadButton)
        formLayout.addWidget(self.sortButton)
        formLayout.addWidget(self.exitButton)
        formLayout.addWidget(self.editButton)
        formLayout.addWidget(self.delButton)

        imageAndDescriptionLayout = QHBoxLayout()
        imageAndDescriptionLayout.addWidget(self.imageLabel)
        imageAndDescriptionLayout.addWidget(self.descriptionLabel)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(imageAndDescriptionLayout)
        mainLayout.addLayout(formLayout)
        mainLayout.addWidget(self.table)

        self.setLayout(mainLayout)
        self.setWindowTitle('Quản lý thông tin sinh viên')
        self.setStyleSheet("background-color: white;")
        self.setGeometry(100, 100, 1200, 600)

    def initDB(self):
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()
        # self.cursor.execute('''
        #     CREATE TABLE IF NOT EXISTS SinhVien (
        #         maSinhVien VARCHAR(10) PRIMARY KEY,
        #         tenSinhVien NVARCHAR(255),
        #         lop NVARCHAR(50)
        #     )
        # ''')
        self.conn.commit()

    def addStudent(self):
        maSinhVien = self.idInput.text()
        tenSinhVien = self.nameInput.text()
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
                self.cursor.execute('''
                    INSERT INTO SinhVien (maSinhVien, tenSinhVien, lop) VALUES (?, ?, ?)
                ''', (maSinhVien, tenSinhVien, lop))
                self.conn.commit()

                self.idInput.clear()
                self.nameInput.clear()
                self.classInput.clear()

    def loadStudents(self):
        self.cursor.execute('SELECT maSinhVien, tenSinhVien, lop FROM SinhVien')
        students = self.cursor.fetchall()

        self.table.setRowCount(0)
        for row_number, row_data in enumerate(students):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def sortStudentsByName(self):
        self.cursor.execute('SELECT maSinhVien, tenSinhVien, lop FROM SinhVien ORDER BY tenSinhVien ASC')
        students = self.cursor.fetchall()

        self.table.setRowCount(0)
        for row_number, row_data in enumerate(students):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def deleteStudent(self):
        selected_items = self.table.selectedItems()
        if len(selected_items) > 0:
            row = selected_items[0].row()
            maSinhVien_item = self.table.item(row, 0)
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
            maSinhVien_item = self.table.item(row, 0)
            tenSinhVien_item = self.table.item(row, 1)
            lop_item = self.table.item(row, 2)
            if maSinhVien_item and tenSinhVien_item and lop_item:
                maSinhVien = maSinhVien_item.text()
                tenSinhVien = tenSinhVien_item.text()
                lop = lop_item.text()

                new_tenSinhVien, new_lop, ok = self.editStudentDialog(tenSinhVien, lop)
                if ok:
                    self.cursor.execute('UPDATE SinhVien SET tenSinhVien = ?, lop = ? WHERE maSinhVien = ?',
                                        (new_tenSinhVien, new_lop, maSinhVien))
                    self.conn.commit()
                    self.loadStudents()

    def editStudentDialog(self, tenSinhVien, lop):
        dialog = QMessageBox()
        dialog.setText("Tên Sinh Viên:")
        edit_tenSinhVien = QLineEdit(tenSinhVien)
        dialog.layout().addWidget(edit_tenSinhVien)
        dialog.setText("Lớp:")
        edit_lop = QLineEdit(lop)
        dialog.layout().addWidget(edit_lop)
        ok = dialog.exec_()
        return edit_tenSinhVien.text(), edit_lop.text(), ok == QMessageBox.Ok

    def closeEvent(self, event):
        self.conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StudentInfoApp()
    ex.show()
    sys.exit(app.exec_())
