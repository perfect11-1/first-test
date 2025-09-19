
distance = 2 #距离2公里
time_abundant = 30 #时间充裕
weather_if_good = True #天气是否好

def how_to_go(distance, time_abundant, weather_if_good): # TODO: 为此函数编写单元测试
    if distance < 3 and time_abundant > 20 and weather_if_good:
        print('步行去')
    else:
        print('开车去')

how_to_go(distance, time_abundant, weather_if_good)
how_to_go(1, 20, True)