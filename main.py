import config
import coords
import engine
import time


def clear() -> None:
    print("\033[2J\033[H", end="", flush=True)


def main() -> None:
    board = coords.make_empty_board(config.aspect)
    for x, y in config.alive_at_start:
        coords.Node(
            board, x + config.offset_at_start, y + config.offset_at_start
        ).set_alive(True)

    while True:
        clear()
        engine.render(board)
        engine.apply(board, engine.calculate(board))
        time.sleep(1 / config.fps)


if __name__ == "__main__":
    pass
