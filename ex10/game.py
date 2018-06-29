from linked_list import LinkedList
from queue import Queue
from stack import Stack
from wave import Wave
from non_plant import Non_Plant
from plant import Plant
from card import Card
from linked_list_node import Node
import random

class Game:
    def __init__(self, file):
        with open(file, 'r') as f:
            self.cash, self.height, self.width = [int(x) for x in f.readline().split(' ')]
            self.waves = LinkedList()
            self.waves_num = 0
            for line in iter(f.readline, ''):
                self.waves.add_head(Node(Wave(*[int(x) for x in line.split(' ')])))
                self.waves_num += 1
        self.board = [[Queue() for x in range(self.width)] for x in range(self.height)]
        self.gameOver = False
        self.turnNumber = 0
        self.nonPlants = 0
        self.powerDeck = Stack()
        for i in range(100):
            self.powerDeck.push(Card(random.randint(0,5)))

    def draw(self):
        print("Cash: $"+str(self.cash) + "\nWaves:",self.waves_num, sep = ' ')
        s = ' '.join([str(i) for i in range(self.width-1)])
        print(' ', s)
        for row in range(self.height):
            s = []
            for col in range(self.width):
                if self.is_plant(row, col):
                    char = 'P'
                elif self.is_nonplant(row, col):
                    size = self.board[row][col].size()
                    char = str(size) if size < 10 else "#"
                else:
                    char = '.'
                s.append(char)
            print(row, ' ', ' '.join(s), '', sep='')
        print()

    def is_nonplant(self, row, col):
        if self.board[row][col].front():
            if type(self.board[row][col].front().data) == Non_Plant:
                return True
        else:
            return False

    def is_plant(self, row, col):
        if self.board[row][col].front():
            if type(self.board[row][col].front().data) == Plant:
                return True
        else:
            return False

    def remove(self, row, col):
        if self.is_nonplant(row, col):
            self.cash += Non_Plant.worth
            self.nonPlants -= 1
        self.board[row][col].dequeue()

    def place_nonplant(self, row):
        self.board[row][self.width-1].enqueue(Non_Plant())
        self.nonPlants += 1

    def place_plant(self, row, col):
        if col < self.width-1 and self.board[row][col].isEmpty():
            if self.cash >= Plant.cost:
                self.board[row][col].enqueue(Plant())
                self.cash -= Plant.cost
            else:
                print("Bruh. You ain't got da dough for a plant")
        else:
            print("Nani deska? You can't place a plant there!")

    def place_wave(self):
        waveFinder = self.waves.head
        while waveFinder:
            if waveFinder.content.wave_num == self.turnNumber:
                for i in range(waveFinder.content.num):
                    self.place_nonplant(waveFinder.content.row)
                self.waves.remove(self.waves.head, waveFinder.content)
                self.waves_num -= 1
            waveFinder = waveFinder.next

    def plant_turn(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.is_plant(row, col):
                    if self.board[row][col].front().data.hp < 1:
                        self.remove(row, col)
                    else:
                        for atac in range(col, self.width):
                            if self.is_nonplant(row, atac):
                                self.board[row][col].front().data.attack(self.board[row][atac].front().data)
                                print("Plant at", str(row) + "," + str(col), "atacc nonPlant at", str(row) + "," + str(atac))
                                print("nonPlant at", str(row) + "," + str(atac), "has", self.board[row][atac].front().data.hp, "hp")
                                if self.board[row][atac].front().data.hp < 1:
                                    self.remove(row, atac)
                                break

    def nonplant_turn(self):
        for row in range(self.height):
            if self.is_nonplant(row, 0):
                self.gameOver = True
                print("YOU LOSED HAHAHAHAHA!")
                return
        for row in range(self.height):
            for col in range(1, self.width):
                if self.is_nonplant(row, col):
                    if self.is_plant(row, col-1):
                        for i in range(self.board[row][col].size()):
                            self.board[row][col].front().data.attack(self.board[row][col-1].front().data)
                            self.board[row][col].enqueue(self.board[row][col].front().data)
                            self.board[row][col].dequeue()
                        if self.board[row][col-1].front().data.hp < 1:
                            self.remove(row, col-1)
                    if self.board[row][col-1].isEmpty():
                        for i in range(self.board[row][col].size()):
                            self.board[row][col-1].enqueue(self.board[row][col].front().data)
                            self.board[row][col].dequeue()

    def run_turn(self):
        self.turnNumber += 1
        for row in range(self.height):
            for col in range(self.width-1):
                if self.is_plant(row, col):
                    self.board[row][col].front().data.weaken_powerup()
        self.plant_turn()
        self.nonplant_turn()
        self.place_wave()
        if self.nonPlants == 0 and self.waves_num == 0:
            self.draw()
            self.gameOver = True
            print("congratulations. you won. go pat yourself on the back or something I suppose")

    def draw_card(self):
        if(self.cash >= Card.cost):
            card = self.powerDeck.pop().data
            self.cash -= Card.cost
            for row in range(self.height):
                for col in range(self.width):
                    if self.is_plant(row, col):
                        self.board[row][col].front().data.apply_powerup(card)
        else:
            print("SHOW ME THE MONEY!!! NO CARD FOR YOU!")

    def get_input(self):
        while True:
            ui = input("Action?\n\t[ROW COL] to place plant ($" + str(Plant.cost) + ")\n\t[C] to draw a powerup card ($" + str(Card.cost) + ")\n\t[Q] to quit\n\t[ENTER] to do nothing?\n")
            if (len(ui) > 0):
                if (len(ui) == 1):
                    if (ui.lower() == 'c'):
                        self.draw_card()
                        break
                    elif (ui.lower() == 'q'):
                        self.gameOver = True
                        break
                    else:
                        print("Invalid Input \"" + ui + "\"")
                else:
                    try:
                        row, col = [int(x) for x in ui.split(' ')]
                        self.place_plant(row, col)
                        break
                    except:
                        print("Invalid Input \"" + ui + "\"")
            else:
                break
