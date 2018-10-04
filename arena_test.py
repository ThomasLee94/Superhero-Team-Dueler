if __name__ == "__main__":

    team_A = Team("A")
    team_B = Team("B")
    arena = Arena(team_A, team_B)
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()