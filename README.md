<h2>Video Cartoonizer</h2>
<p>이 프로그램은 Python과 OpenCV를 이용하여 만든 동영상 만화화 프로그램 입니다..</p>

<h2>Preparation</h2>
이 프로그램을 사용하기 위해서 python과 OpenCV가 필요합니다.
<p>pip install opencv-python opencv-contrib-python</p>

<h2>설명</h2>
Python 파일을 실행하면 위에는 원본 영상, 아래에는 만화화된 영상이 재생됩니다.<br>

<h2>ChatGPT코드와 비교</h2>
ChatGPT가 작성한 코드에서는 사물의 테두리가 불완전한 경우가 있습니다.<br>
Canny Edge Detection을 병행함으로써 사물의 테두리를 잘 표현할 수 있습니다.

<h2>실행 화면(위 : 기본, 아래 : 기본 + Canny Edge Detection)</h2>
<img src="https://user-images.githubusercontent.com/5174517/226780452-cd065b99-1367-4911-b256-138f1fe59848.png" width="642" height="752">
<img src="https://user-images.githubusercontent.com/5174517/226848584-ea2a01d6-0cbc-4e8b-8b0d-09d4a4ee3b5b.png" width="642" height="752">