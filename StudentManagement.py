import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QFont, QColor, QPixmap
from PyQt5.QtCore import Qt

class StudentInfoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initDB()

    def initUI(self):
        # Tạo các thành phần giao diện
        self.imageLabel = QLabel()
        self.imageLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.imageLabel.setPixmap(QPixmap("/Users/lengocquyen/Downloads/btl/ảnh.jpeg").scaled(200, 200, Qt.KeepAspectRatio))

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

        self.subjectLabel = QLabel('Môn:')
        self.subjectLabel.setFont(QFont('Times New Roman', 14))
        self.subjectLabel.setStyleSheet("color: black;")
        self.subjectInput = QLineEdit()
        self.subjectInput.setStyleSheet("background-color: white; color: black;")

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

        self.exitButton = QPushButton('Thoát')
        self.exitButton.setFont(QFont('Times New Roman', 14))
        self.exitButton.setStyleSheet("background-color: red; color: white;")
        self.exitButton.clicked.connect(self.close)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Tên', 'Mã sinh viên', 'Lớp', 'Môn'])
        self.table.setStyleSheet("background-color: white; color: black;")
        self.table.horizontalHeader().setStyleSheet("background-color: lightgray; color: black;")
        self.table.cellClicked.connect(self.deleteStudent)

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
        formLayout.addWidget(self.subjectLabel)
        formLayout.addWidget(self.subjectInput)
        formLayout.addWidget(self.addButton)
        formLayout.addWidget(self.loadButton)
        formLayout.addWidget(self.sortButton)
        formLayout.addWidget(self.exitButton)

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
        self.conn = sqlite3.connect('students.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                name TEXT,
                student_id TEXT PRIMARY KEY,
                class_name TEXT,
                subject TEXT
            )
        ''')
        self.conn.commit()

    def addStudent(self):
        name = self.nameInput.text()
        student_id = self.idInput.text()
        class_name = self.classInput.text()
        subject = self.subjectInput.text()

        if name and student_id and class_name and subject:
            self.cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
            existing_student_id = self.cursor.fetchone()

            if existing_student_id:
                msg = QMessageBox()
                msg.setText('Mã sinh viên đã tồn tại. Vui lòng nhập lại.')
                msg.setStyleSheet("color: black;")
                msg.exec_()
            else:
                self.cursor.execute('''
                    INSERT INTO students (name, student_id, class_name, subject) VALUES (?, ?, ?, ?)
                ''', (name, student_id, class_name, subject))
                self.conn.commit()

                self.nameInput.clear()
                self.idInput.clear()
                self.classInput.clear()
                self.subjectInput.clear()

    def loadStudents(self):
        self.cursor.execute('SELECT name, student_id, class_name, subject FROM students')
        students = self.cursor.fetchall()

        self.table.setRowCount(0)
        for row_number, row_data in enumerate(students):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def sortStudentsByName(self):
        self.cursor.execute('SELECT name, student_id, class_name, subject FROM students ORDER BY name ASC')
        students = self.cursor.fetchall()

        self.table.setRowCount(0)
        for row_number, row_data in enumerate(students):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def deleteStudent(self, row, column):
        reply = QMessageBox.question(self, 'Xác nhận', 'Bạn có chắc chắn muốn xóa sinh viên này không?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            student_id_item = self.table.item(row, 1)
            if student_id_item:
                student_id = student_id_item.text()
                self.cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
                self.conn.commit()
                self.loadStudents()

    def closeEvent(self, event):
        self.conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StudentInfoApp()
    ex.show()
    sys.exit(app.exec_())
