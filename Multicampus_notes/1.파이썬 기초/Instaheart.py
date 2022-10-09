import sys
#인스타 하트 누르는 모듈
import insta_bot_heart as ib

#인자받기
id= sys.argv[1]
pw = sys.argv[2]
tag= sys.argv[3]
#4번 인자는 숫자로 바꾸고 공백을 제거한다
num= int(sys.argv[4].strip())

#ib 모듈서 Captrue봇을 Bot 객체 저장
Bot= ib.CaptureBot()
#Bot 객체에 log인 함수 호출, 로그인, (id,pw) 필요
Bot.login(id,pw)
#Bot 객체 search_tag 함수 호출, 검색하기 (tag) 필요
# Bot.search_tag(tag)
# #Bot 객체 select_pic 함수 호출, 최근 검색물 클릭
# Bot.select_pic()
# #Bot 객체 capture_pics 함수 호출,(num )필요
#Bot.click_heart(num)
Bot.insta_like_auto(tag,num)

#봇 객체의 kill() 함수 호출
Bot.kill()