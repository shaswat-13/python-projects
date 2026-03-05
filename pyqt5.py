import pyqt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys

def main():

    # start the application
    app = QApplication([])
    app.exec_()

    # ceate a window
    window = QWidget()
    window.setWindowTitle("Tiddies")
    window.setGeometry(100, 100, 300, 200)

    # create a label
    label = QLabel("Hello, PyQt5!", window)
    label.move(50, 50)

    # show the window
    window.show()
    print("Application has started successfully.")
    input("Press Enter to exit...")  # Keep the console open until user presses Enter
    sys.exit(app.exec_())

    
    

main()
