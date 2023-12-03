def points(games):
    point = 0
    for i in games:
        x = i[0]
        y = i[2]
        if x>y:
            point +=3 
        elif x==y:
            point += 1
        else:
            continue
    return point

points([])