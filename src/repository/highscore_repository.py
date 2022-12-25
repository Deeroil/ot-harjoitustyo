from db_connection import get_db_connection


class HighscoreRepository:
    """Manages highscore database.

      High score is the amount of consecutive wins.

    """

    def __init__(self, connection):
        self._connection = connection

    def add(self, user, score):
        """Adds user and score to database.

          Args:
            user: name of the user
            score: amount of wins in a row
        """
        cursor = self._connection.cursor()

        sql = "INSERT INTO HIGHSCORES(user, wins) VALUES (?,?)"
        cursor.execute(sql, (user, score))
        self._connection.commit()

    def find_top_3(self):
        """Returns top 3 rows on the highscore.

            Returns:
              a list of tuples, (user, wins).

        """
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM HIGHSCORES ORDER BY WINS DESC LIMIT 3")

        rows = cursor.fetchall()

        return [(row["user"], row["wins"]) for row in rows]

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM HIGHSCORES ORDER BY WINS DESC")

        rows = cursor.fetchall()

        return [(row["user"], row["wins"]) for row in rows]


highscore_repository = HighscoreRepository(get_db_connection())
