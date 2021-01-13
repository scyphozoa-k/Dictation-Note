def judge_the_answer(text, ans):
    full_score = len(ans)  - 1
    i = 0
    number_of_correct = 0

    for _ in range(len(text) - 1):
        t, a = text[i:i+2], ans[i:i+2]
        i += 1

        if t == a:
            number_of_correct += 1
            

    score = number_of_correct / full_score * 100
    return round(score, 2)
if __name__ == "__main__":
    pass


