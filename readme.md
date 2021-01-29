# Flood Fill
이미지에 색 채우기

## Build
#### 1. Install Python 3.5 or later and pip3
~~~
(ubuntu)$ sudo apt-get install python3
(ubuntu)$ python3 --version
(ubuntu)$ sudo apt-get install python3-pip
~~~

#### 2. Install OpenCV 4
~~~
(ubuntu)$ pip3 install opencv-contrib-python
~~~

#### 3. Usage
~~~
(ubuntu)$ python3 flood-fill.py --io --location --rgb
~~~
io: 입/출력 이미지 경로   
location: 좌표 (x, y)   
rgb(optional): RGB값 (255, 0, 0)   
ex. python3 main.py --io input.jpg output.jpg --location 300 500 --rgb 255 0 0

#### 4. Logs
정상적으로 작업을 수행하면 exit code로 0을, 오류가 발생했다면 1을 리턴한다.   
오류 발생시 커맨드라인에 다음과 같은 로그를 남긴다.
~~~
 flood-fill.py error: Image input failed
~~~
주어진 경로에 이미지파일이 없음
~~~
 flood-fill.py error: Image output failed
~~~
주어진 경로가 잘못되어 이미지파일을 저장할 수 없음
~~~
 flood-fill.py error: x or y out of image range
~~~
x 혹은 y 값이 입력이미지를 벗어남
~~~
 flood-fill.py error: Invalid RGB value
~~~
주어진 RGB 값이 0~255의 범위를 벗어남
