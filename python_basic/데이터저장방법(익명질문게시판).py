# 첫번째 데이터 저장 방법 - 딕셔너리 사용
total_dictionary = {} #질문은 key에, 답변은 value에 저장

#질문입력(key)
while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_dictionary[question] = ""

#답변입력(value)
for i in total_dictionary:
    print(i)
    answer = input("답변을 입력해주세요 : ")
    total_dictionary[i] = answer #key값에 해당하는 value 불러냄
print(total_dictionary)

# 두번째 데이터 저장 방법 - 리스트 사용
total_list = []

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question, "답변" : ""})

for i in total_list:
    print(i["질문"]) #질문을 key로 접근
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer
print(total_list)
    