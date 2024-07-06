def election_results(votes):
    vote_count = {}
    for name, vote in votes.items():
        if vote == 1:
            if name in vote_count:
                vote_count[name] += 1
            else:
                vote_count[name] = 1
        else:
            vote_count[name] = vote_count.get(name, 0)

    max_votes = max(vote_count.values())
    

    winners = [name for name, count in vote_count.items() if count == max_votes]
    
    return max_votes, winners


inputs = [
    {'Anvar': 1, 'Lobar': 1, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1},
    {'Anvar': 0, 'Lobar': 1, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1},
    {'Anvar': 0, 'Lobar': 0, 'Asror': 0, 'Vali': 0, 'Surayyo': 0, 'Baxtiyor': 1}
]

for votes in inputs:
    max_votes, winners = election_results(votes)
    print(max_votes)
    for winner in winners:
        print(winner, end=" ")
    print()  
