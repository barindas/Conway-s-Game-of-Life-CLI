import config


def make_empty_board(size: tuple[int, int]) -> list[list[str]]:
    return [[config.none_icon for x in range(size[0])] for y in range(size[-1])]


class Cell:
    def __init__(self, coord_sys: list[list[str]], x: int, y: int):
        self.coord_sys: list[list[str]] = coord_sys
        self.row: int = y
        self.col: int = x

    def set_alive(self, alive: bool) -> None:
        self.coord_sys[self.row][self.col] = (
            config.alive_icon if alive else config.none_icon
        )

    def count_neighbors(self) -> int:
        count = 0
        rows, cols = len(self.coord_sys), len(self.coord_sys[0])

        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue

                r, c = self.col + dr, self.row + dc

                if (
                    0 <= r < rows
                    and 0 <= c < cols
                    and self.coord_sys[r][c] == config.alive_icon
                ):
                    count += 1
        return count
