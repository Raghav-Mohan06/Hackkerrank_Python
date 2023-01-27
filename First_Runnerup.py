if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    lst = list(arr)
    scores = list()

    for score in lst:
        if score not in scores:
            scores.append(score)
        else :
            continue
    ordr = sorted(scores, reverse=True)
    print(ordr[1])
