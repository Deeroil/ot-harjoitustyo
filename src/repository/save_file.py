import pickle
import os

FILENAME = "save.bin"


class SaveFile:
    """Manages save file.

      Attributes:
        minesweeper: Minesweeper object with the current state
        wins: amount of current wins

    """

    def __init__(self, minesweeper, wins):
        self.minesweeper = minesweeper
        self.wins = wins

    def save(self):
        """Saves game state as a binary file to save.bin.

        """
        with open(FILENAME, "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def load():
        """Returns saved file.

        Doesn't raise error if save file doesn't exist.

        """
        try:
            with open(FILENAME, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            pass

    @staticmethod
    def remove():
        """Removes the save file.

        Doesn't raise error if save file doesn't exist.

        """
        try:
            os.unlink(FILENAME)
        except FileNotFoundError:
            pass
