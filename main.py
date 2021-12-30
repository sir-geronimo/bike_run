from src.core.game import Game

if __name__ == "__main__":
    game = Game()

    while game.is_running:
        game.loop()

    game.quit()
