import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QPixmap
from PyQt5.QtCore import QTimer
from random import randint


textFont = QFont("Times", 14)
buttonFont = QFont("Arial", 12)
computerScore = 0
playerScore = 0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors Game")
        self.setGeometry(350, 150, 550, 500)
        self.ui()

    def ui(self):
        # ############################Scores####################
        self.score_computer_text = QLabel("Computer Score : ", self)
        self.score_computer_text.move(30, 20)
        self.score_computer_text.setFont(textFont)
        self.score_player_text = QLabel("Your Score : ", self)
        self.score_player_text.setFont(textFont)
        self.score_player_text.move(330, 20)

        # #########################Images########################
        self.image_computer = QLabel(self)
        self.image_computer.setPixmap(QPixmap("images/rock.png"))
        self.image_computer.move(50, 100)

        self.image_player = QLabel(self)
        self.image_player.setPixmap(QPixmap("images/rock.png"))
        self.image_player.move(330, 100)

        self.image_game = QLabel(self)
        self.image_game.setPixmap(QPixmap("images/game.png"))
        self.image_game.move(230, 160)

        # ###################Buttons######################
        btn_start = QPushButton("Start", self)
        btn_start.setFont(buttonFont)
        btn_start.move(180, 250)
        btn_start.clicked.connect(self.start)
        btn_stop = QPushButton("Stop", self)
        btn_stop.setFont(buttonFont)
        btn_stop.clicked.connect(self.stop)
        btn_stop.move(270, 250)

        # #########################Timer##################

        self.timer = QTimer(self)
        self.timer.setInterval(280)
        self.timer.timeout.connect(self.play_game)

        self.show()

    def start(self):
        self.timer.start()

    def play_game(self):
        self.rnd_computer = randint(1, 3)
        self.rnd_player = randint(1, 3)
        print(self.rnd_player, self.rnd_computer)

        if self.rnd_computer == 1:
            self.image_computer.setPixmap(QPixmap("images/rock.png"))
        elif self.rnd_computer == 2:
            self.image_computer.setPixmap(QPixmap("images/paper.png"))
        else:
            self.image_computer.setPixmap(QPixmap("images/scissors.png"))

        if self.rnd_player == 1:
            self.image_player.setPixmap(QPixmap("images/rock.png"))

        elif self.rnd_player == 2:
            self.image_player.setPixmap(QPixmap("images/paper.png"))
        else:
            self.image_player.setPixmap(QPixmap("images/scissors.png"))

    def stop(self):
        global computerScore
        global playerScore
        self.timer.stop()

        if self.rnd_computer == 1 and self.rnd_player == 1:
            mbox = QMessageBox.information(self, "Information", "Draw Game")

        elif self.rnd_computer == 1 and self.rnd_player == 2:
            mbox = QMessageBox.information(self, "Information", "You Win")
            playerScore += 1
            self.score_player_text.setText("Your Score:{}".format(playerScore))
        elif self.rnd_computer == 1 and self.rnd_player == 3:
            mbox = QMessageBox.information(self, "Information", "Computer Wins")
            computerScore += 1
            self.score_computer_text.setText("Computer Score:{}".format(computerScore))

        elif self.rnd_computer == 2 and self.rnd_player == 1:
            mbox = QMessageBox.information(self, "Information", "Computer Wins")
            computerScore += 1
            self.score_computer_text.setText("Computer Score:{}".format(computerScore))
        elif self.rnd_computer == 2 and self.rnd_player == 2:
            mbox = QMessageBox.information(self, "Information", "Draw Game")

        elif self.rnd_computer == 2 and self.rnd_player == 3:
            mbox = QMessageBox.information(self, "Information", "You Win")
            playerScore += 1
            self.score_player_text.setText("Your Score:{}".format(playerScore))

        elif self.rnd_computer == 3 and self.rnd_player == 1:
            mbox = QMessageBox.information(self, "Information", "You Win")
            playerScore += 1
            self.score_player_text.setText("Your Score:{}".format(playerScore))
        elif self.rnd_computer == 3 and self.rnd_player == 2:
            mbox = QMessageBox.information(self, "Information", "Computer Wins")
            computerScore += 1
            self.score_computer_text.setText("Computer Score:{}".format(computerScore))
        elif self.rnd_computer == 3 and self.rnd_player == 3:
            mbox = QMessageBox.information(self, "Information", "Draw Game")

        if computerScore == 3 or playerScore == 3:
            mbox = QMessageBox.information(self, "Information", "Game Over")
            sys.exit()


def main():
    app = QApplication(sys.argv)
    window = Window()
    # window.start()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
