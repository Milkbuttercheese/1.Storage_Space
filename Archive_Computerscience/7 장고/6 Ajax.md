## 1. Ajax의 사용목적은 무엇인가?
-  하나의 HTML 페이지가 대용량인데에 반해, 변경되야 할 요소요소들이 작은 부분들만 차지한다면, 홈페이지 전체를 다시 생성하여 클라이언트에게 다시 주기보단, 일부 변경요소만 제공해주는 편이 낫다

## 2. Ajax의 원리
-  서버: 데이터를 요구하면 요구한 데이터를 보내주는 프로그램
-   url: 데이터를 서버에게 요청할 때 사용하는 특별한 양식의 데이터 위치값. 요청방식이 get/post/그 외로 나뉜다
	-   get 방식 
		-   주소 직접입력
		-   버튼 입력(폼 태그)
		-   Ajax 요청: 위의 두 방식과 다르게 새로고침없이 필요한 일부 정보만 요청한다
	-   post 방식	
-   콜백함수
	-   정의: 함수에 파라미터로 들어가는 함수
	-   용도: 함수들을 순차적으로 실행하고 싶을 때 사용한다
	-   예시)
		-   버튼 클릭 후 실행: `document.querySelector('.button').addEventListener('click',function(){})`
		-  시간 경과 후 실행: `setTimeout(function(){},time_interval)` 

## 3. Ajax를 어떻게 사용할 수 있는가?
-  바뀌지 않는 부분은 메인 파일에 입력해두고, 바뀌지 부분은 메인 파일에서 비워둔다.
-  바뀌는 부분은 ajax를 통하여 정보를 전달한다
```
<input type="button" value="fetch" onclick="  
fetch('html').then(function (response){  
    response.text().then(function(text){  
        alert(text);  
            })  
          })  
    ">
```
-  메커니즘
	-  html 이란 파일을 찾는다
	-  text에 서버가 응답한 데이터가 들어간다
	-  alert를 통해 데이터가 출력된다
	
-  원리
	-  `fetch('file_name')`: 웹브라우저에게 서버의 응답을 받아오라고 명령을 내림
	-  `fetch('file_name').then(function_name  or  function(){})` :서버의 응답을 받아온 후 함수를 시행시키라고 명령을 내림
	
-  용어:동기와 비동기
	-  동기 synchronous: 서버에 문서를 요청request하면 그에 대한 응답response가 오기 전까지 다른 요청을 하지 않는 통신방식
	-  비동기 asynchronous:서버에 문서를 요청request하고 그에 대한 응답request가 오기전에도 다른 요청을 하는 통신 방식
	-  비유- 짜장면 배달부: 짜장면 배달부는 1.짜장면 배달 2.주문자가 짜장면을 먹고 빈그릇을 내놓음 3. 짜장면 빈그릇 수거 3개의 일을 처리한다고 하자. 동기과정은 손님 A에게 배달 후 손님이 먹고 빈그릇을 내놓은것을 가져갈 때 까지 문앞에 서서 기다리는, 1>2>3 일련의 과정이 마쳐서야 손님 B에게로 가는 방식이고, 비동기과정은 손님A에게 배달을 하고 손님A가 식사를 하는 도중 다른 손님 B에게 가는 방식이다 / 또한 비동기의 경우 음식을 다먹고 그릇을 내놓으면 그 사실을 배달부에게 알리는 과정(콜백)이 존재한다
	
- 익명함수 annonymous function:
	- 일회성으로 사용될 함수인 경우 function(response){실행할 문장}의 형태로 정의한다.
	- 여기선 response란 객체를 parameter로 준다. 이때 이름은 꼭 response라고 할 필요는 없다
	- 객체를 console.log(response)를 통해 출력하면 `response: {type: 'basic', url: 'http://localhost:63342/5.%EC%9E%A5%EA%B3%A0/web2_javascript-master/html', redirected: false, status: 200, ok: true, …}`  가 출력된다 이때 정상적으로 서버에서 응답받으면 `status:200` , 파일이 없어서 응답을 못받으면 `status:404` 	로 받는다
	- 
	

### 3-1. 빈 태그에 내용 넣기

```
<article></article>
<input type="button" value="fetch" onclick="  
fetch('html').then(function (response){  
    response.text().then(function(text){  
        document.querySelector('article').innerHTML=text;
            })  
          })  
    ">
```

