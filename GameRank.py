def full_star(rank):
    if 1 <= rank <= 10:
        return 5
    elif 11 <= rank <= 15:
        return 4
    elif 16 <= rank <= 20:
        return 3
    elif 21 <= rank <= 25:
        return 2
    return -1000

def check_rank(sequence):
    rank = 25
    stars = 0
    streak = 0

    for game in sequence:
        win = game == 'W'

        if win:
            streak += 1
            if streak >= 3 and 6 <= rank <= 25:
                stars += 2
            else:
                stars += 1

            if stars > full_star(rank):
                stars -= full_star(rank)
                rank -= 1

        else:
            streak = 0

            if rank < 20 or (rank == 20 and stars != 0):
                stars -= 1

            if stars < 0:
                rank += 1
                stars = full_star(rank) - 1

        if rank == 0:
            return "Legend"

    return rank

sequence = input().strip()
result = check_rank(sequence)
print(result)
