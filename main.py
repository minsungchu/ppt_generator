import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QGridLayout, QLabel, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """툴팁 설정"""
        QToolTip.setFont(QFont('SansSerif', 10))

        """위젯 아이템"""
        labelTitle = QLabel("찬양 제목")
        texteditTitle = QTextEdit()
        labelLyrics = QLabel("찬양 가사")
        texteditLyrics = QTextEdit()
        btnConvert = QPushButton("Save Contents to Presentation")

        """그리드 레이아웃 설정"""
        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(labelTitle, 0, 0)
        grid.addWidget(texteditTitle, 1, 0)
        grid.addWidget(labelLyrics, 2, 0)
        grid.addWidget(texteditLyrics, 3, 0)
        grid.addWidget(btnConvert, 4, 0)

        """Stylesheet"""
        self.setStyleSheet(
            "background-color : #303745;"
            "color : #CFD6C9;"
        )

        texteditTitle.setStyleSheet(
            """
            QTextEdit{
                min-height : 50px;
                max-height : 50px;
            }
            """
        )

        btnConvert.setStyleSheet(
            """
            QPushButton{
                min-height : 50px;
                max-height : 50px;
                font-size  : 20px;
            }
            """
        )

        """다이얼로그 제목,아이콘,위치,크기 설정"""
        self.setWindowTitle('스트리밍용 가사 PPT 생성 프로그램')
        self.setWindowIcon(QIcon('schana_icon.jpg'))
        self.move(200, 100)
        self.resize(1400, 800)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
