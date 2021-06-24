p = input('shengao:')
w = input('tizhong:')
height = float(p)
weight = int(w)
bmi = weight/(height*height)
if bmi < 18.5 :
    print('您太轻了')
elif 18.5 <= bmi < 25 :
    print('正常')
elif 25 <= bmi < 28 :
    print('过重')
elif 28 <= bmi < 32 :
    print('肥胖')
elif 32 <= bmi :
    print('超重')