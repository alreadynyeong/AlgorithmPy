def solution(progresses, speeds):
    answer = []
    day, cnt = 0, 0

    while len(progresses) > 0:
        if (progresses[0] + speeds[0]*day) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            day += 1
    answer.append(cnt)
    return answer