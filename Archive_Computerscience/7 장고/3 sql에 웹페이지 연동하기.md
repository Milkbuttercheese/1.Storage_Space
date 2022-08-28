# 3. sql에 웹페이지 연동하기

$querySet$

- 하나의 모델객체가 원소가 되는 리스트

- 데이터베이스는 최신 데이터가 아래에 저장되는데 보통의 웹페이지는 최신 글이 위에 적히는 $UI$를 갖는다. 그렇기 때문에 `.order_by('-id')` 를 사용하면 $id$ 기준 내림차순으로 배열된다
- $insert.html$ 에서 $tag$를 $id$대신 $name$을 쓴다 왜?

- 보통 $sql$에 저장된 $row$ $data$를 꺼내는데에 $primary\,\,key$를 주로 쓴다
- $dto$: $data\,\,transfer\,\,object$의 약자
- $urls.py$ 에서 $<ind:id>$은 $index.html$에서 들어오는 변수로, $views.py$로 넘긴다
- `#{% url 'detail' data.id %}` : `{{data.id}}` 가 아닌이유: 이미 % %로 파이썬 명령어임을 표시했기에

- $name_{model}.objects.get$ 과 $name_{model}.objects.filter$의 차이는 하나의 $row$를 받아올 것인가, 조건의 맞는 여러개의 $row$를 받아오느냐의 차이가 있다

- 슈퍼유저 만들기
    - $python\,\,manage.py\,\,createsuperuser$
    - $myweb$ 가상환경에서 만드는 프로젝트 전체의 슈퍼유저가 된다
    - 
    

$admin.site$에 나의 $model$ 등록시키기

$admin.site.register(MyBoard)$