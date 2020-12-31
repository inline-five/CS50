import pprint

voters2 = [['Lex Luthor', 'Brian J. Mason', 'Abelt Dessler', 'Daisuke Aramaki', 'Drake Luft'], 
          ['Lex Luthor', 'Daisuke Aramaki', 'Brian J. Mason', 'Abelt Dessler', 'Drake Luft'], 
          ['Drake Luft', 'Abelt Dessler', 'Lex Luthor', 'Brian J. Mason', 'Daisuke Aramaki'], 
          ['Drake Luft', 'Daisuke Aramaki', 'Brian J. Mason', 'Abelt Dessler', 'Lex Luthor'], 
          ['Lex Luthor', 'Drake Luft', 'Abelt Dessler', 'Daisuke Aramaki', 'Brian J. Mason'], 
          ['Daisuke Aramaki', 'Drake Luft', 'Brian J. Mason', 'Lex Luthor', 'Abelt Dessler']]
          
voters = [["dem", "ind", "rep"],
          ["rep", "ind", "dem"],
          ["ind", "dem", "rep"],
          ["ind", "rep", "dem"]]
        
    # tally first round votes

    
numVoters = len(voters)
totalVotes = len(voters[0])
winners = []
losers = []
firstround = []
    
for x in range(numVoters):
    for y in range(1):
        firstround.append(voters[x][0])

flag = 1
while (flag):
    cand = {}
    for x in range(numVoters):
        for y in range(1):
            if voters[x][0] not in firstround or any(voters[x][0] in sl for sl in losers):
                losers.append(voters[x][0])
                del voters[x][0]
                continue
    totalVotes -= 1

            
    for person in voters:
        for vote in range(1):
            if person[vote] in cand and person[vote]:
                cand[person[vote]] += 1
            elif person[vote] not in cand and person[vote]:
                cand[person[vote]] = 1
                    
    # return winner
    if len(cand) == numVoters:
        print("None")
        flag = 0
    else:
        for key, value in cand.items():
            if key not in losers and value >= int(numVoters / 2) + 1:
                print(key)
                flag = 0
                
                
        #remove losers
        
    num_minVote = min(cand.values())
    res = [key for key in cand if cand[key] == num_minVote] 
    losers.append(res)

    for x in range(numVoters):
        for y in range(1):
            if voters[x][0] in res:
                del voters[x][0]
    totalVotes -= 1
             