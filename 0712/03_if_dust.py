dust = 359

if dust > 150:
    if dust > 300:
        print('실외 활동을 자제하세요.')
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    if dust < 0:
        print('음수 값입니다.')
    else:
        print('좋음')

# else 가 없으면 동시 출력, else가 있으면 동시 출력 되지 않음

#elif dust > 0:
#    print('좋음')
#else:
#    print('음수 값입니다.')