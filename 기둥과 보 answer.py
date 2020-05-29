def check(result):
    for x, y, building in result:
        if building == 0:  # 기둥
            if y == 0 or [x, y - 1, 0] in result or [x - 1, y, 1] in result or [x, y, 1] in result:
                continue
            else:
                return False
        elif building == 1:  # 보
            if [x, y - 1, 0] in result or [x + 1, y - 1, 0] in result or (
                    [x - 1, y, 1] in result and [x + 1, y, 1] in result):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, a, b = build

        if b == 1:
            answer.append([x, y, a])
            is_true = check(answer)
            if is_true:
                continue
            else:
                answer.remove([x, y, a])

        elif b == 0:
            answer.remove([x, y, a])
            is_true = check(answer)
            if is_true:
                continue
            else:
                answer.append([x, y, a])



