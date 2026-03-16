import sys
from PySide6.QtWidgets import(
    QApplication, QWidget, QLabel, QHBoxLayout, QDateEdit,
    QPushButton, QLineEdit, QVBoxLayout, QFormLayout, QComboBox, QMessageBox
)
from PySide6.QtCore import Qt

class FormBioadata(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Form Biodata")
        self.resize(400,300)

        main_layout = QVBoxLayout()

        judul = QLabel("FORM BIODATA MAHASISWA")
        judul.setAlignment(Qt.AlignmentFlag.AlignCenter)
        judul.setStyleSheet("font-size: 20px; font-weight: bold; padding: 18px; background: #000580 ; color: white; border-radius: 5px")
        form_layout = QFormLayout()

        self.input_nama = QLineEdit()
        self.input_nama.setPlaceholderText("Masukkan Nama Lengkap")
        form_layout.addRow("Nama:", self.input_nama)
        
        self.nim = QLineEdit()
        self.nim.setPlaceholderText("Masukkan NIM")
        form_layout.addRow("NIM:", self.nim)

        self.kelas = QLineEdit()
        self.kelas.setPlaceholderText("Masukkan kelas")
        form_layout.addRow("Kelas:", self.kelas)

        self.kelamin = QComboBox()
        self.kelamin.setPlaceholderText("--Jenis Kelamin--")
        self.kelamin.addItems([
            "Perempuam",
            "Laki-laki"
        ])
        form_layout.addRow("Jenis Kelamin:", self.kelamin)

        btn_layout = QHBoxLayout()
        self.btn_submit = QPushButton("Tampilkan")
        self.btn_submit.setStyleSheet("padding: 10px; background: #27ae60; color: white; border:none; border-radius: 5px")
        self.btn_submit.clicked.connect(self.submit)
            
        self.btn_reset = QPushButton("Reset")
        self.btn_reset.setStyleSheet("padding: 10px; background: #E0474C; color: white; border:none; border-radius: 5px")
        self.btn_reset.clicked.connect(self.reset)

        btn_layout.addWidget(self.btn_submit)
        btn_layout.addWidget(self.btn_reset)

        self.label_hasil = QLabel("")
        self.label_hasil.setWordWrap(True)
        self.label_hasil.setStyleSheet("padding: 15px; font-size: 12px")

        
        main_layout.addWidget(judul)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(self.label_hasil)
        main_layout.addStretch()

        self.setLayout(main_layout)
    
    def submit(self):
        nama = self.input_nama.text().strip()
        nim = self.nim.text().strip()
        kelas = self.kelas.text().strip()
        jenis_kelamin = self.kelamin.currentText()

        if not nama or not nim or not kelas or not jenis_kelamin:
            QMessageBox.warning(self, "Error", "Isi semua field!")
            return
        
        self.label_hasil.setText(
            f"""Data Tersimpan:\n\nNama: {nama}\nNIM: {nim}\nKelas: {kelas}\nJenis Kelamin: {jenis_kelamin}"""
        )
        self.label_hasil.setStyleSheet("padding: 15px; background: #d5f4e6; border-left: 4px solid #27ae60;color: black")

    def reset(self):
        self.input_nama.clear()
        self.nim.clear()
        self.kelamin.setCurrentIndex(0)
        self.kelas.clear()
        self.label_hasil.clear()



app = QApplication(sys.argv)
window = FormBioadata()
window.show()
sys.exit(app.exec())