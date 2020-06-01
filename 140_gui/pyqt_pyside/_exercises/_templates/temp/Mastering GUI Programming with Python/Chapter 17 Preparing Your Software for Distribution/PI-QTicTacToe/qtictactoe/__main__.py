______ sys
____ ?.?W.. ______ QApplication
____ .mainwindow ______ MainWindow

___ main
    app _ QApplication(sys.argv)
    mainwindow _ MainWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
