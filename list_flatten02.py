def flatten(data):
    output=[]
    for item in data:
        if type(item)==list:
            output+=flatten(item) #재귀 사용
        else:
            output.append(item)
    return output
example=[[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본: ", example)
print("변환: ", flatten(example))
#리스트가 몇 차원이든 평탄화할 수 있다.