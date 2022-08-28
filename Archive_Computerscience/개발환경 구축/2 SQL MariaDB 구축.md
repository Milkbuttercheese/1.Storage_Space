# 2. SQL: MariaDB 구축

## 1.데이터 베이스란?

- 정보 관리 / 웹 관리
- 데이터베이스의 종류
    - 관계형 데이터 베이스: 현재 가장 많이 사용중인 데이터베이스 모델
- 데이터베이스 제품 업체
    - Oracle (유료)
    - MySQL (오픈소스)
    - MariaDB (오픈소스) :MySQL이 나중에 Oracle에 합병되면서 이해관계에서 자유롭고자 하는 MySQL의 원제작자들이 모여 만든 프로그램
        - 설치방법
            - ubuntu: apt-get install mariadb-server
            - centos: yum install mariadb-server
- 데이터베이스의 언어
    - 데이터 정의 언어 $DDL$
    - 데이터 조작 언어 $DML$
    - 데이터 제어 언어 $DCL$
- 데이터베이스의 구성
    - 데이터베이스는 기본적으로 2차원 표(행렬)의 형태로 표현된다
        - 필드 이름: $id/name/e-mail/phone$ 등 $id$의 의미를 나타내는 위치
        - 레코드 $record/row$ : 각 고객의 정보
        - 컬럼 $column$
        - 필드 값: 행렬의 원소
    

### 2. MarialDB 기본 설정/ 실행

- 리눅스의 명령창- 터미널
    - 터미널 글자 크기 확장: ctrl+ shfit
    - 터미널 글자 크기 축소: ctrl+ -
    - ls : 현재 작업중인 파일의 리스트를 보여준다
    - whoami: 사용자의 이름을 보여준다
    - date: 현재 시간과 날짜를 보여준다
- 데이터베이스 서비스 사용 시작
    - systemctl enable mariadb —now
    - 컴퓨터가 껐다 꺼도 실행이 되며 지금도 실행이 되도록 하라
- 데이터베이스 프로그램 실행
    - mysql -u root -p / enter / enter
    - 나갈시 exit /quit 으로 입력하면 된다
    - mysql -h localhost -u root -p 이 원문이나
        - "-h localhost"는 현지 작업자이기 때문에 생략 가능
- 데이터베이스 비밀번호 설정
    - mysql_secure_installation
    - 현재 비밀번호 입력
    - 새로 비밀번호 설정할 것인가 물음⇒ y 입력
    - 새로운 비밀번호 입력
    - 추후 질문에 y or n 입력
        - Remove anonymous users? [Y/n] y
        - Disallow root login remotely? [Y/n] y
        - Remove test database and access to it? [Y/n] y
        - Reload privilege tables now? [Y/n] y