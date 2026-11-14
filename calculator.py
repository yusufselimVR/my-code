import math
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QGridLayout, QLabel

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("calculator")
        self.label = QLabel(self)
        self.label.setGeometry(300, 50, 50, 50)
        self.setGeometry(300, 300, 300, 300)
        self.search = QLineEdit(self)
        self.search.setReadOnly(True)
        buttons = [
        ["7", "8", "9", "*"],
        ["4", "5", "6", "/"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"],
        ["√", "x²", "^", "."]
        ]

        self.label.setStyleSheet("font-size: 20px;")
        self.search.setStyleSheet("font-size: 20px;")
        vbox = QVBoxLayout()
        vbox.addWidget(self.search)

        grid = QGridLayout()

        for row, values in enumerate(buttons):
            for col, value in enumerate(values):
                button = QPushButton(value, self)

                button.setStyleSheet("font-size: 20px;")

                button.clicked.connect(lambda checked, v=value: self.button_clicked(v))

                grid.addWidget(button, row, col)

                vbox.addLayout(grid)
                self.setLayout(vbox)

                self.search.textChanged.connect(self.update_preview)

    def update_preview(self):
        try:
            equation = self.search.text()
            result = eval(equation)
            self.label.setText(str(result))
        except:
            self.label.setText("")
        if len(equation) == 1:
            self.label.setText("")


    def button_clicked(self, value):
        if value == "C":
            self.search.clear()
        elif value == "=":
            try:
                result = eval(self.search.text())
                self.search.setText(str(result))
                self.label.clear()
            except:
                self.search.setText("syntax error")
        elif value == "√":
            try:
                equation = float(self.search.text())
                result = math.sqrt(equation)
                self.search.setText(str(result))
            except:
                self.search.setText("syntax error")
        elif value == "x²":
            try:
                number = self.search.text()
                self.search.setText(str(number) + "** 2")
            except:
                self.search.setText("syntax error")
        elif value == "^":
            try:
                number = self.search.text()
                self.search.setText(str(number) + "**")
            except:
                self.search.setText("syntax error")
        else:
            self.search.setText(self.search.text() + value)

def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()