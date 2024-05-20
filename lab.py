import sys
import random

import matplotlib
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6 import QtCharts

import algo
import numpy as np

from svekla import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from tkinter import filedialog

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=10, height=8, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Svekla_GUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.maxim_ind = None
        self.max_ind = None
        self.names = None
        self.allSolution = None
        self.solution = None
        self.matrix = None
        self.setupUi(self)
        self.setFixedSize(800, 600)
        # Программный модуль
        self.programStartButton.clicked.connect(self.switch_to_program)
        self.backToWelcomeButton.clicked.connect(self.switch_to_welcome)
        self.backToWelcomeButton_2.clicked.connect(self.switch_to_welcome)
        self.readMatrixFileButton.clicked.connect(self.readMatrix)
        self.runProcessProgramModule.clicked.connect(self.runDemo)
        self.plusButtonHist.clicked.connect(self.showHist)
        self.plusButtonLine.clicked.connect(self.showLine)

        # Модуль тестирования
        self.testStartButton.clicked.connect(self.switch_to_test)
        self.runProcessTest.clicked.connect(self.run)
        self.label_13.setVisible(False)
        self.nu.setVisible(False)
        self.label_14.setVisible(False)
        self.b_min_2.setVisible(False)
        self.label_15.setVisible(False)
        self.b_max_2.setVisible(False)

    def calculateFunc(self, matrix, indexes):
        s = 0
        for par in indexes:
            s += matrix[par[0]][par[1]]
        return s

    def runDemo(self):
        strategy = str(self.chooseStrategy.currentText())
        indexes = None
        font = QFont("Open Sans Condensed", 14)
        font.setBold(True)
        if strategy == "Венгерский алгоритм":
            indexes = algo.get_max_solution(self.matrix)
        if strategy == "Жадный алгоритм":
            indexes = algo.get_greedy_solution(self.matrix)
        if strategy == "Бережливый алгоритм":
            indexes = algo.get_provident_solution(self.matrix)
        if strategy == "Жадно-бережливый алгоритм":
            indexes = algo.get_greedy_provident_solution(self.matrix)
        if strategy == "Бережливо-жадный алгоритм":
            indexes = algo.get_provident_greedy_solution(self.matrix)
        if strategy == "G(k)":
            indexes = algo.get_greedy_solution_upgrade(self.matrix, 3)
        if strategy == "T(k)G":
            indexes = algo.get_provident_greedy_solution_upgrade(self.matrix, 5, 3)
        if strategy == "CTG":
            indexes = algo.CTG(self.matrix, 5)
        for par in indexes:
            self.tableWidget.item(par[0], par[1]).setFont(font)

    def run(self):
        maxes = [0] * 7
        self.allSolution = []
        if self.ripeningCheck.isChecked():
            nu = int(self.nu.text())
        else:
            nu = int(int(self.n.text()) / 2)
        for i in range(50):
            matrix = self.generateMatrix()

            solution = [self.calculateFunc(matrix, algo.get_greedy_solution(matrix)),
                        self.calculateFunc(matrix, algo.get_provident_solution(matrix)),
                        self.calculateFunc(matrix, algo.get_greedy_provident_solution(matrix, nu)),
                        self.calculateFunc(matrix, algo.get_provident_greedy_solution(matrix, nu)),
                        self.calculateFunc(matrix, algo.CTG(matrix, nu)),
                        self.calculateFunc(matrix, algo.get_provident_greedy_solution_upgrade(matrix, nu, 10)),
                        self.calculateFunc(matrix, algo.get_greedy_solution_upgrade(matrix, 8))
                        ]
            self.allSolution.append(solution)

            # print(solution)
            maxes[solution.index(max(solution))] += 1
        # print(maxes)

        k_for_tkg = []
        k_for_gk = []

        matrix = self.generateMatrix()

        for i in range(0, len(matrix)):
            k_for_gk.append(self.calculateFunc(matrix, algo.get_greedy_solution_upgrade(matrix, i + 1)))
            k_for_tkg.append(self.calculateFunc(matrix, algo.get_provident_greedy_solution_upgrade(matrix, nu, i + 1)))
        max_k_for_tkg = k_for_tkg.index(max(k_for_tkg))
        max_k_for_gk = k_for_gk.index(max(k_for_gk))

        # print(matrix)
        self.solution = [self.calculateFunc(matrix, algo.get_max_solution(matrix)),
                    self.calculateFunc(matrix, algo.get_greedy_solution(matrix)),
                    self.calculateFunc(matrix, algo.get_provident_solution(matrix)),
                    self.calculateFunc(matrix, algo.get_greedy_provident_solution(matrix, nu)),
                    self.calculateFunc(matrix, algo.get_provident_greedy_solution(matrix, nu)),
                    self.calculateFunc(matrix, algo.CTG(matrix, nu)),
                    self.calculateFunc(matrix,
                                       algo.get_provident_greedy_solution_upgrade(matrix, nu, max_k_for_tkg + 1)),
                    self.calculateFunc(matrix, algo.get_greedy_solution_upgrade(matrix, max_k_for_gk + 1))
                    ]
        self.allSolution.append(self.solution[1:])

        # print(solution)
        self.max_ind = self.solution.index(max(self.solution[1:]))
        # print(max_ind)
        min_value = min(self.solution[1:])
        self.names = ["Максимальная", "Жадная", "Бережливая", "Жадно-\nБережливая", "Бережливо-\nЖадная", "CTG",
                 "T(k)G\nk=10",
                 "G(k)\nk=8"]
        self.maxim_ind = maxes.index(max(maxes)) + 1

        self.MplLine.canvas.axes.clear()
        for j in range(0, 7):
            x = []
            y = []
            for i in range(len(self.allSolution)):
                x.append(i)
                y.append(self.allSolution[i][j])
            self.MplLine.canvas.axes.plot(x, y, label=self.names[j + 1], marker='o', markersize=3)
        self.MplLine.canvas.axes.set_title("Результаты стратегий по годам")
        self.MplLine.canvas.draw()

        names_short = ["М", "Ж", "Б", "Ж-Б", "Б-Ж", "CTG",
                 "T(k)G",
                 "G(k)"]
        self.MplHist.canvas.axes.clear()
        for i in range(8):
            if i == self.max_ind and i == self.maxim_ind:
                self.MplHist.canvas.axes.bar(names_short[i], self.solution[i], width=0.6, color="red", label=names_short[i], edgecolor="green", linewidth=2,
                        hatch='\\\\\\')
            elif i == self.max_ind:
                self.MplHist.canvas.axes.bar(names_short[i], self.solution[i], width=0.6, color="red", label=names_short[i])
            elif i == self.maxim_ind:
                self.MplHist.canvas.axes.bar(names_short[i], self.solution[i], width=0.6, color="blue", label=names_short[i], edgecolor="green", linewidth=2,
                        hatch='\\\\\\')
            else:
                self.MplHist.canvas.axes.bar(names_short[i], self.solution[i], width=0.6, color="blue", label=names_short[i])
        self.MplHist.canvas.axes.set_title("Результаты стратегий по годам")
        self.MplHist.canvas.draw()

    def showHist(self):
        min_value = min(self.solution[1:])
        plt.figure()
        for i in range(8):
            if i == self.max_ind and i == self.maxim_ind:
                plt.bar(self.names[i], self.solution[i], width=0.6, color="red", label=self.names[i], edgecolor="green",
                        linewidth=2,
                        hatch='\\\\\\')
            elif i == self.max_ind:
                plt.bar(self.names[i], self.solution[i], width=0.6, color="red", label=self.names[i])
            elif i == self.maxim_ind:
                plt.bar(self.names[i], self.solution[i], width=0.6, color="blue", label=self.names[i], edgecolor="green",
                        linewidth=2,
                        hatch='\\\\\\')
            else:
                plt.bar(self.names[i], self.solution[i], width=0.6, color="blue", label=self.names[i])
        plt.ylim(min_value - (min_value * 0.1))
        plt.title("Результаты стратегий в последний год")
        plt.xlabel("Стратегия")
        plt.ylabel("Целевая функция")
        plt.show()

    def showLine(self):
        plt.figure()
        for j in range(0, 7):
            x = []
            y = []
            for i in range(len(self.allSolution)):
                x.append(i)
                y.append(self.allSolution[i][j])
            plt.plot(x, y, label=self.names[j + 1], marker='o', markersize=3)
        plt.title("Результаты стратегий по годам")
        plt.xlabel("Год")
        plt.ylabel("Целевая функция")
        plt.legend()
        plt.show()

    def switch_to_welcome(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_program(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_test(self):
        self.stackedWidget.setCurrentIndex(2)

    def readMatrix(self):
        filepath = filedialog.askopenfilename()
        data = self.getInput(filepath)
        N = data[0]
        self.tableWidget.setColumnCount(N)
        self.tableWidget.setRowCount(N)
        self.matrix = data[1]
        for i in range(0, N):
            self.tableWidget.setColumnWidth(i, 50)
            for j in range(0, N):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.matrix[i][j])))
                self.tableWidget.item(i, j).setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

    def getInput(self, filepath):
        file = open(filepath)
        inp = file.read()
        tmp = ""
        N = -1
        a = []
        can_have = "0123456789."
        for i in inp:
            if can_have.count(i) == 0:
                if N == -1:
                    N = int(tmp)
                else:
                    number = float(tmp)
                    a.append(number)
                tmp = ""
            else:
                tmp += i
        number = float(tmp)
        a.append(number)
        matr = []
        for i in range(N):
            matr.append([])
            for j in range(N):
                matr[i].append(a[i * N + j])
        return [N, matr]

    def generateMatrix(self):
        a = []
        b = []
        n = int(self.n.text())
        a_min = int(self.a_min.text())
        a_max = int(self.a_max.text())
        b_min = float(self.b_min.text())
        b_max = float(self.b_max.text())
        for i in range(n):
            a.append(random.uniform(a_min, a_max))
        matrix = []
        if self.ripeningCheck.isChecked():
            b_min_2 = float(self.b_min_2.text())
            b_max_2 = float(self.b_max_2.text())
            nu = int(self.nu.text())
            for i in range(n):
                b.append([])
                matrix.append([])
                for j in range(n):
                    if j < nu:
                        b[i].append(random.uniform(b_min_2, b_max_2))
                        matrix[i].append(0)
                    else:
                        b[i].append(random.uniform(b_min, b_max))
                        matrix[i].append(0)
        else:
            for i in range(n):
                b.append([])
                matrix.append([])
                for j in range(n):
                    b[i].append(random.uniform(b_min, b_max))
                    matrix[i].append(0)
        for i in range(n):
            matrix[i][0] = a[i]
        for i in range(n):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j - 1] * b[i][j - 1]
        return matrix


if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcomeWindow = Svekla_GUI()
    welcomeWindow.show()
    sys.exit(app.exec())
