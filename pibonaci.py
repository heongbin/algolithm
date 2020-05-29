T = int(input())
test_case=[0 for _ in range(T)]
for i in range(T):
    test_case[i]=int(input())



def fibonaci():
    global d
    for i in range(2,41):
        d[i][0]=d[i-1][0]+d[i-2][0]
        d[i][1]=d[i-1][1]+d[i-2][1]


for test in test_case:
    d=[[0 for _ in range(2)] for _ in range(41)]
    d[0][0]=1
    d[1][1]=1

    answer=[]
    fibonaci()
    print("{} {}".format(answer.count(0),answer.count(1)))
