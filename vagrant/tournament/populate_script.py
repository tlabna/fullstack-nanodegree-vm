import random

from tournament import connect, deletePlayers, deleteMatches
from tournament import reportMatch


the_players = [
    (1, 'T'),
    (2, 'R'),
    (3, 'C'),
    (4, 'N'),
    (5, 'V'),
    (6, 'S')
]


def registerPlayerUpdated(player_id, name):
    """Add a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    db_cursor = db.cursor()
    query = "INSERT INTO players (id, name) VALUES (%s, %s)"
    db_cursor.execute(query, (player_id, name))
    db.commit()
    db.close()


def createRandomMatches(player_list, num_matches):
    num_players = len(player_list)
    for i in xrange(num_matches):
        print 'match1'
        player1_index = random.randint(0, num_players - 1)
        player2_index = random.randint(0, num_players - 1)
        if player2_index == player1_index:
            player2_index = (player1_index + 1) % num_players
        winner_id = player_list[player1_index][0]
        winner_name = player_list[player1_index][1]
        loser_id = player_list[player2_index][0]
        loser_name = player_list[player2_index][1]
        reportMatch(winner_id, loser_id)
        print "%s (id=%s) beat %s (id=%s)" % (
            winner_name,
            winner_id,
            loser_name,
            loser_id)


def setup_players_and_matches():
    deleteMatches()
    deletePlayers()
    for player in the_players:
        registerPlayerUpdated(player[0], player[1])

    createRandomMatches(the_players, 12)


if __name__ == '__main__':
    setup_players_and_matches()
