import random


class ChessPlayer:
    def __init__(self, name, age, elo_rating, tenacity, is_boring):
        self.name = name
        self.age = age
        self.elo_rating = elo_rating
        self.tenacity = tenacity
        self.is_boring = is_boring
        self.tournament_score = 0


def simulateMatch(player1,player2):
    elo_difference = abs(player1.elo_rating - player2.elo_rating)

    if elo_difference > 100:
        if player1.elo_rating > player2.elo_rating:
            player1.tournament_score += 1
        else:
            player2.tournament_score += 1

    elif elo_difference < 100 and elo_difference > 50:
        if player1.elo_rating > player2.elo_rating:
            player1.tournament_score += 1

        elif player2.elo_rating > player1.elo_rating:
            rand = random.randint(1, 10)
            player2.tenacity *= rand
            if player2.tenacity > player1.tenacity:
                player2.tournament_score += 1

            else:
                player1.tournament_score += 1


        elif elo_difference < 50:
            if player1.tenacity > player2.tenacity:
                player1.tournament_score += 1

            else:
                player2.tournament_score += 1



        elif player1.is_boring == "true" or player2.is_boring == "true":
            if elo_difference < 100:
                player1.tournament_score = 0.5
                player2.tournament_score = 0.5
                print("draw")

        if player1.tournament_score > 0.5 and player1.tournament_score <= 1:
            print(player1.name, " Won ", player2.name, " Lost")
        if player2.tournament_score > 0.5 and player2.tournament_score <= 1:
            print(player2.name, " Won ", player1.name, " Lost")


players = [ChessPlayer("Courage the Cowardly Dog", 25, 1000.39, 1000, "true"),
           ChessPlayer("Princess Peach", 23, 945.65, 50, "false"),
           ChessPlayer("Walter White", 50, 1650.73, 750, "false"),
           ChessPlayer("Rory Gilmore", 16, 1700.87, 500, "false"),
           ChessPlayer("Anthony Fantano", 37, 1400.45, 400, "true"),
           ChessPlayer("Beth Harmon", 20, 2500.34, 150, "false")]
for i in range(len(players)-1):
    simulateMatch(players[i],players[i+1])
    simulateMatch(players[i+1],players[i])








