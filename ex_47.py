def computegrade(s):
    if s > 1.0 or s < 0.0:
        print('Bad score')
    elif s <= 1.0 and s >= 0.9:
        print('A')
    elif s < 0.9 and s >= 0.8:
        print('B')
    elif s < 0.8 and s >= 0.7:
        print('C')
    elif s < 0.7 and s >= 0.6:
        print('D')
    elif s < 0.6:
        print('F')


try:
    score = float(input('Enter score: '))
    computegrade(score)
except:
    print('Bad score')
