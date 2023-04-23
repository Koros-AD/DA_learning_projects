#7) Создайте класс для игры с атрибутами для имени игрока, очков, жизней и уровня
class Game:
    def __init__(self, name, score, lives, level):
        self.name = name
        self.score = 0
        self.lives = 5
        self.level = 1
        self.is_running = False
#Класс должен содержать методы для
    # a) Запуска, завершения и перезапуска игры
    def start(self):
        if self.is_running:
            print("Game is already running!")
        else:
            self.is_running = True
            print("Game started")

    def restart(self):
        self.score = 0
        self.lives = 5
        self.level = 1
        print("Game restarted")

    def endgame(self):
        self.is_running = False
        print("Game ended")

    # b) Получения очков
    def add_points(self, points):
        self.score += points
        if self.score >= self.level * 10:
            self.level += 1
            print("Level up!")

    # c) Потери жизней
    def lose_life(self):
        self.lives -= 1
        if self.lives == 0:
            print("Game Over")
            self.endgame()

    def get_info(self):
        return f"Name: {self.name}, Score: {self.score}, Lives: {self.lives}, Level: {self.level}"


game1 = Game("Sonic", 0, 5, 1)
game1.start()
game1.start()

game1.add_points(5)
game1.add_points(5)
game1.add_points(5)
game1.add_points(5)
print(game1.get_info())

game1.lose_life()
game1.lose_life()
game1.lose_life()
print(game1.get_info())

game1.restart()
print(game1.get_info())

game1.endgame()
