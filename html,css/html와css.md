## HTML과 인사하기

<h1>hello</h1>
<p>nice to meet you</p>

## 중앙에 배치하기

footer {
  text-align: center;
  background-color: #1e1e1e;
  color: #919191;
  font-size: 12px;
}

.mainbox {
  border: 5px groove #e6b3ff;
}

## 박스 쪼개기
.box1 {
  background-color: skyblue;
  width: 60px;
  height: 60px;
  border: 5px solid black;
  padding: 20px;
}

.box2 {
  background-color: violet;
  width: 100px;
  height: 100px;
  border: 5px solid purple;
}

footer {
  text-align: center;
  background-color: #1e1e1e;
  font-size: 12px;
  color: #919191;
}

.mainbox {
  width: 610px;
  margin-right: auto;
  margin-left: auto;
  border: 1px solid #ebebeb;
  text-align: right;
  padding: 30px;
  margin: 25px;
}

## 그림자 표현하기
 box-shadow: -100 1px 20px 0 rgba(0, 0, 0, 0.1);

 ## 구글 웹폰트 사용하기
 @import url('https://fonts.googleapis.com/css?family=Red+Hat+Mono:300,300,400,400,500,500,600,600,700,700&display=swap');

* {
  font-family: 'Red Hat Mono';
}
