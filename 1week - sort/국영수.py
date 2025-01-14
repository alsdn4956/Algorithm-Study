N = int(input())
list = []

for i in range(N):
    #name, korea, english, math = input().split()
    #korea, english, math = int(korea), int(english), int(math)
    list.append(input().split())
    
    # 두 번째, 세 번째, 네 번째 원소를 기준으로 -면 내림차순, +면 오름차순
list.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))


    # x변수가 빠져 나왔으니까 name으로 변수 설정 해주고 name[0] 출력
for name in list:
    print(name[0])
    
