def coordinatesInSameQuadrant(x1, y1, x2, y2):
    if x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0:
        return True
    elif x1 < 0 and y1 > 0 and x2 < 0 and y2 > 0:
        return True
    elif x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0:
        return True
    elif x1 > 0 and y1 < 0 and x2 > 0 and y2 < 0:
        return True
    else:
        return False