
place = (
    (0, 0, 0, -1, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, -9, 0, 0, 0, 0),
    (0, 0, -1, 0, 0, 0, 0),
    (0, -1, -1, 0, 0, 9, 0),
    (0, 0, 0, 0, 0, 0, 0),
)


def main():
    h = (2, 3)
    d = (5, 4)

    variants = ('up', 'done', 'left', 'right')
    steps = {
        'up': (h[0], h[1]-1),
        'done': (h[0], h[1]+1),
        'left': (h[0]-1, h[1]),
        'right': (h[0]+1, h[1]),
    }

    possible_steps = {}
    for k in steps.keys():
        if place[steps[k][0]][steps[k][1]] >= 0:
            possible_steps.update({k: steps[k]})



    # up
    next_step = h[0], h[1]-1
    cof_raznosti = d[0]-next_step[0] + d[1]-next_step[1]
    # left
    # done
    # right
    result = {
        'up': [(h[0], h[1]-1), d[0]-next_step[0] + d[1]-next_step[1]]
    }

if __name__ == '__main__':
    main()
