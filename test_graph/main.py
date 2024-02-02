import matplotlib.pyplot as plt
import re
import matplotlib.dates as mdates
from matplotlib.ticker import AutoLocator
import os

file_path = './record.txt'

x_tmp=[]
y_tmp=[]

x_data=[]
y_data=[]

def match_re(pattern,text):
    match = re.search(pattern,text)
    if match:
        return match.group(1)

def read_file():
    if os.path.exists("./write.txt"):
        os.remove("./write.txt")
    with open(file_path,'r') as file:
        for line in file:
            x_tmp.append(match_re(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]',line.strip()))
            y_tmp.append(match_re(r'\[([0-9]+)\]',line.strip()))
            with open('./write.txt','a') as file:
                file.write(match_re(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]',line.strip())+"|"+match_re(r'\[([0-9]+)\]',line.strip())+"\n")

def paint_plot():
    # |를 기준으로 문자열을 나누기
    with open('./write.txt','r') as file:
        for line in file:
            x_str, y_str = line.strip().split('|')
            x_data.append(x_str.replace(" ","\n"))
            y_data.append(int(y_str))
    # 선 그래프 그리기

    plt.plot(x_data, y_data, linestyle='-', color='b', label='test')
    # 그래프에 제목과 축 레이블 추가
    plt.title("Hoban worker thread")
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
    
     # 마지막 데이터 값 표시
    last_x = x_data[-1]
    last_y = y_data[-1]
    plt.text(last_x, last_y, f'{last_y}', ha='right', va='bottom', color='r')

    # 마지막 데이터의 x 위치에 눈금 추가
     # 현재 눈금 가져오기
    current_ticks = [tick.get_text() for tick in plt.gca().get_xticklabels() if tick.get_text() != '']
    
    # for tick in plt.gca().get_xticklabels():
    #     print("tick",tick)
    
    current_ticks.append(last_x)
    # 마지막 데이터의 x 위치에 눈금 추가
    plt.xticks(current_ticks, rotation=0)
  

    # 그래프 표시
    plt.show()

#read_file()
paint_plot()

#