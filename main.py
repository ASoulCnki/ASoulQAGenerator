# coding:UTF-8
import json
import random


# 解析 json 语料
def read_json(file_name="data.json"):
    if file_name != "":
        str_list = file_name.split(".")
        if str_list[len(str_list) - 1].lower() == "json":
            with open(file_name, mode="r", encoding="utf-8") as file:
                return json.loads(file.read())


data = read_json("data.json")
# 永远以"小伙伴你好！"开始
always_starts_with = data["always_starts_with"]
# 直接回答
straightforward = data["straightforward"]
# 先道歉
humble = data["humble"]
# 再打太极
apology = data["apology"]


# 生成阿草太极回答
def generate_answer(key_word):
    is_humble = random.randint(0, 100) > 30
    if is_humble:
        humble_beginning = random.choice(humble).replace("q", key_word)
        apology_answer = random.choice(apology)
        return "%s%s%s。" % (always_starts_with, humble_beginning, apology_answer)
    straightforward_answer = random.choice(straightforward).replace("q", key_word)
    return "%s %s" % (always_starts_with, straightforward_answer)


if __name__ == '__main__':
    keyword = input("请输入问题关键词:")
    print("A:", generate_answer(keyword))
