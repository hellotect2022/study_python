import matplotlib.pyplot as plt
import re
import matplotlib.dates as mdates
from matplotlib.ticker import AutoLocator

file_path = './record.txt'

x_data=[]
y_data=[]

def read_file():
    with open(file_path,'r') as file:
        for line in file:
            #print(match_re(r'\[([0-9]+)\]',line.strip()))
            x_date.append(match_re(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]',line.strip()))
            y_count.append(match_re(r'\[([0-9]+)\]',line.strip()))
            #print(line.strip())
            with open('./write.txt','a') as file:
                file.write(match_re(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]',line.strip())+"|"+match_re(r'\[([0-9]+)\]',line.strip())+"\n")
            #print(match_re(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]',line.strip())+"|"+match_re(r'\[([0-9]+)\]',line.strip()))
    
    #paint_plot(x_date,y_count,"fuck")

def match_re(pattern,text):
    match = re.search(pattern,text)
    if match:
        return match.group(1)

def paint_plot():
    # |를 기준으로 문자열을 나누기
    with open('./write.txt','r') as file:
        for line in file:
            x_str, y_str = line.strip().split('|')
            x_data.append(x_str)
            y_data.append(int(y_str))
    # 선 그래프 그리기
    #plt.plot(x_date, y_count, marker='o', linestyle='-', color='b', label='test')
    plt.plot(x_data, y_data, linestyle='-', color='b', label='test')
    # 그래프에 제목과 축 레이블 추가
    plt.title('test1')
    plt.xlabel('X data')
    plt.ylabel('Y data')
    # 범례 추가
    plt.legend()
    # 그리드 추가
    plt.grid(True)
    # x 축 눈금 조절
    from matplotlib.ticker import MaxNLocator

    # X 축 눈금 갯수 제한
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=3))  # 5개의 눈금으로 제한

    # Y 축 눈금 갯수 제한
    plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=3))  # 3개의 눈금으로 제한
     # y축 뒤집기
    #plt.gca().invert_yaxis()
    #plt.locator_params(axis='x', nbins=3)
    # 그래프 표시
    plt.show()

paint_plot()

#read_file()