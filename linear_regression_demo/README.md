# 선형회귀 데모 (linear_regression_demo)
이 코드는 Siraj Raval의 유튜브 영상 ["딥러닝 시작하기 #1 - 예측 하는 방법"](https://youtu.be/vOppzHpvTiQ)에 관한 것이며, 이는 "딥러닝 시작하기" 시리즈의 첫번째 에피소드로 동물들의 몸무게가 주어졌을 때, 뇌의 무게를 예측하기 위한 작성되었습니다. 

여기서는 [선형회귀](http://www.statisticssolutions.com/what-is-linear-regression/) 모델을 사용하며, 학습을 위한 데이터셋은 다양한 동물들의 뇌와 몸무게를 측정한 값들로 이루어져있습다. 데이타에 맞게 "선긋기"를 하기 위해 scikit-learn 이라는 머신러닝 라이브라리를 사용할 것이며, matplotlib을 써서 차트에 그래프를 그려볼 것입니다.

## 종속성

* pandas
* scikit-learn
* matplotlib

터미널창에서 다음 명령을 실행하여 위의 필수 라이브리들을 설치할 수 있습니다.

`pip install -r requirements.txt` 
 
pip가 없다면 [pip](https://pip.pypa.io/en/stable/installing/)에서 다운받으세요. 

## 사용법

터미널창에서 다음 명령을 실행하시면, scatter 차트와 최적 선이 그어진 것을 확인하실 수 있습니다.

`python demo.py`

## 도전과제

scikit-learn을 사용하여 'challenge_dataset'의 최적 선을 찾아보세요! 그리고 기존 데이터들의 예측값을 만들어보고 실제 값과 얼마나 비슷한 지 확인해보시고, 오차를 출력해보세요. 
scikit-learn [문서](http://scikit-learn.org/stable/documentation.html)도 참고하시면 도움이 될 것입니다.

* 이 주간 도전과제는  Udacity의 nanodegree 프로젝트와는 관련이 없습니다.
* 선형회귀를 3가지의 다른 변수들을 사용하여 수행한다면 보너스 점수가 있습니다.

## 저작권

원본 코드의 저작권은 [gcrowder](https://github.com/gcrowder)에게 있습니다. 저는 단지 더 많은 사람들이 시작할 수 있도록 풀어썼을 뿐입니다.
