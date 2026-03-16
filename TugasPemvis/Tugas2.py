# NAMA: MUHAMMAD IZZUL ISLAM
# NIM: F1D02410077
# KELAS: D

import sys
from PySide6.QtWidgets import(
    QApplication, QWidget, QLabel,QPushButton, 
    QLineEdit, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt

class KonversiSuhu(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Konversi Suhu")
        self.resize(400,300)

        layout = QVBoxLayout()

        judul = QLabel("KONVERSI SUHU")
        judul.setAlignment(Qt.AlignmentFlag.AlignCenter)
        judul.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px; background: #34495e; color: white; border-radius: 5px")

        self.input = QLineEdit()
        self.label_input = QLabel("Masukkan Suhu (Celsius):")
        self.input.setPlaceholderText("Masukkan angka")
        self.input.setStyleSheet("padding: 10px; font-size: 14px;")

        tombol_layout = QHBoxLayout()

        self.btn_Fahrenheit = QPushButton("Fahrenheit")
        self.btn_Kelvin = QPushButton("Kelvin")
        self.btn_Reamur = QPushButton("Reamur")

        for btn in [self.btn_Fahrenheit, self.btn_Kelvin, self.btn_Reamur]:
            btn.setStyleSheet("""
                              padding: 15px;
                              font-size:20px;
                              background-color: #3498db;
                              color: white;
                              border: none;
                              border-radius: 5px;
            """)

        tombol_layout.addWidget(self.btn_Fahrenheit)
        tombol_layout.addWidget(self.btn_Kelvin)
        tombol_layout.addWidget(self.btn_Reamur)

        self.btn_Fahrenheit.clicked.connect(self.konversi_fahrenheit)
        self.btn_Kelvin.clicked.connect(self.konversi_kelvin)
        self.btn_Reamur.clicked.connect(self.konversi_reamur)

        self.label_hasil = QLabel("Hasil Konversi")
        self.label_hasil.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_hasil.setStyleSheet("color:black; font-size: 18px; padding: 20px; background: #ecf0f1; border-radius: 5px")

        layout.addWidget(judul)
        layout.addWidget(self.label_input)
        layout.addWidget(self.input)
        layout.addLayout(tombol_layout)
        layout.addWidget(self.label_hasil)

        self.setLayout(layout)

    def get_numbers(self):
        try: 
            a = float(self.input.text())
            return a
        except ValueError:
            QMessageBox.warning(self, "Error", "Input harus angka!!")
            return

    def tampil_hasil(self, hasil):
        a = self.get_numbers()
        self.label_hasil.setText(f"Hasil Konversi: \n\n {a} Celsius = {hasil}")
        self.label_hasil.setStyleSheet("border-left: 4px solid #2eaa71; font-size: 18px; padding: 20px; background: #2ecc71; border-radius: 5px")
        return hasil

    def konversi_fahrenheit(self):
        a = self.get_numbers()
        if a is not None:
            hasil = (a * 9/5) + 32
            self.tampil_hasil(f"{hasil:.2f} Fahrenheit")

    def konversi_kelvin(self):
        a = self.get_numbers()
        if a is not None:
            hasil = a + 273.15
            self.tampil_hasil(f"{hasil:.2f} Kelvin")

    def konversi_reamur(self):
        a = self.get_numbers()
        if a is not None:
            hasil = a * 4/5
            self.tampil_hasil(f"{hasil:.2f} Reamur")

app = QApplication(sys.argv)
window = KonversiSuhu()
window.show()
sys.exit(app.exec())
