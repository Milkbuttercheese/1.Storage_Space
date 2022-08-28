# 4. DB저장을 위해 변경해야 할점

### 1. $models.py$

- `phone_numbers = models.CharField(max_length=128,blank=True)`
    - (길이 부족으로 기존 길이 15에서 128로 늘림)
    - ($blank=True$ 는 공백이 있는 원소를 허락하는 조건)
    - 0001_initial.py를 삭제합니다
    - 테이블을 삭제합니다
        - mysql>visual로 들어가 $drop\,\,table\,\,table_{name}$ 명령어로 5개의 테이블을 삭제합니다. 이때 어떤 테이블은 다른 테이블을 참조해서 삭제를 못한다고 할텐데 그땐 참조 테이블을 먼저 삭제하고 다음에 삭제해주시면 됩니다
        | member_board                                      |
        | metal_board                                           |
        | visualization_mentalservicelocation   | 
        | visualization_myboard                          |
        | visualization_mymembers                    |
    - 다시 makesmigrations을 통해 모델을 만듭니다  ([https://wikidocs.net/9926](https://wikidocs.net/9926) 참조)
        - `python manage.py makemigrations`
        - `python manage.py migrate --fake visualization zero`
        - `python manage.py migrate --fake-initial`
        - `python manage.py migrate`
            
            

### 2.$views.py$

- $views.py$는 각자 다 파일내용이 달라서 제 파일을 업로드합니다
- 첫번째 visualization 폴더에 여기에 있는 전국_정신건강관련기관_위치정보.json 파일을 넣습니다

[전국_정신건강관련기관_위치정보.json](전국_정신건강관련기관_위치정보.json)

- `def update_json` 과 모듈을 복붙하고 경로를 본인 컴퓨터에 맞게 수정합니다
- templates>main.html 파일 <body>영역에 `<a href="{% url 'mental_service_location' %}">진료/의료기관 정보 데이터베이스에 불러오기</a>` 을 추가합니다
- [urls.py](http://urls.py)파일에 `path('mental_service_location/',views.update_json,name='mental_service_location'),` 을 추가합니다
- python [manage.py](http://manage.py) runserver를 통해 페이지를 열고 `진료/의료기관 정보 데이터베이스에 불러오기` 를 클릭합니다
- 1번 클릭한 후 로딩후 제자리에 있으면 데이터가 저장된 것입니다. mysql을 통해 데이터를 확인해보시면 됩니다. 또 다시 클릭하면 또 데이터가 저장되므로 그럴 경우 데이터를 삭제하고 다시 담아야합니다

		
python
from django.shortcuts import render, redirect

#맵제작에 필요한 모듈
from .models import MyBoard, MyMembers, MentalServiceLocation
import json
import folium
from folium.plugins import MarkerCluster
from folium import IFrame
from folium.plugins import MousePosition
from folium.plugins import FeatureGroupSubGroup
from folium.plugins import LocateControl
from folium import plugins

#현재위치 탐색에 사용될 모듈
import geocoder
import js2py

#기타
import re
import json
from urllib.request import urlopen
from time import time

def main_page(request):
    return render(request, 'main.html')

# Create your views here.
def update_json(request):

    with open('/Users/wooseongkyun/5.장고/visualization/전국_정신건강관련기관_위치정보.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    # json에서 정보 불러오기
    for i in range(len(json_data['data'])):
        public_or_privates=(json_data['data'][i]['공공/민간'])
        categories=(json_data['data'][i]['기관구분'])
        agency=(json_data['data'][i]['기관명'])
        address=(json_data['data'][i]['주소'])
        latitude=(json_data['data'][i]['위도'])
        longitude=(json_data['data'][i]['경도'])
        phone_numbers=(json_data['data'][i]['전화번호'])
        introductions='안녕하세요. 자기소개글을 준비중입니다.'
        result= MentalServiceLocation.objects.create(public_or_privates=public_or_privates, categories=categories, agency= agency, address=address, latitude=latitude, longitude=longitude,phone_numbers=phone_numbers,introductions=introductions)
    return redirect('/')

def make_map(request,my_location=[37.5, 126.98],radius=5000):
    #기능1. 장고데이터베이스에서 정보 가져오기
    #상담소/공공/민간데이터 정보로 구분하기
    counseling_data= MentalServiceLocation.objects.filter(categories='상담소')
    public_data= MentalServiceLocation.objects.filter(public_or_privates='공공').exclude(categories='상담소')
    private_data= MentalServiceLocation.objects.filter(public_or_privates='민간').exclude(categories='상담소')

    #상담소/민간의료기관/공공의료기관으로 구분
    #상담소
    counseling_agency=[]
    counseling_address=[]
    counseling_latitude=[]
    counseling_longitude=[]
    counseling_phone_numbers=[]
    #공공의료기관
    public_agency=[]
    public_address=[]
    public_latitude=[]
    public_longitude=[]
    public_phone_numbers=[]
    #민간의료기관
    private_agency=[]
    private_address=[]
    private_latitude=[]
    private_longitude=[]
    private_phone_numbers=[]

    #데이터 삽입
    for c_data in counseling_data:
        counseling_agency.append(c_data.agency)
        counseling_address.append(c_data.address)
        counseling_latitude.append(c_data.latitude)
        counseling_longitude.append(c_data.longitude)
        counseling_phone_numbers.append(c_data.phone_numbers)

    for pu_data in public_data:
        public_agency.append(pu_data.agency)
        public_address.append(pu_data.address)
        public_latitude.append(pu_data.latitude)
        public_longitude.append(pu_data.longitude)
        public_phone_numbers.append(pu_data.phone_numbers)

    for pr_data in public_data:
        private_agency.append(pr_data.agency)
        private_address.append(pr_data.address)
        private_latitude.append(pr_data.latitude)
        private_longitude.append(pr_data.longitude)
        private_phone_numbers.append(pr_data.phone_numbers)

    #지도 만들기

    my_map = folium.Map(location =my_location, zoom_start = 12.0,
                        tiles = 'Open street map',control_scale=True)

    # #선택 카테고리 추가하기
    groups=folium.FeatureGroup(name='진료/상담 기관')
    my_map.add_child(groups)
    counseling_group=FeatureGroupSubGroup(groups,name='상담소')
    my_map.add_child(counseling_group)
    public_group=FeatureGroupSubGroup(groups,name='공공 의료기관(보건소/정신건강보건센터/대학병원 외)')
    my_map.add_child(public_group)
    private_group=FeatureGroupSubGroup(groups,name='민간 의료기관')
    my_map.add_child(private_group)

    #MarkerCluster함수를 통해 특정 수 이상의 마커는 뭉쳐서 보이도록 표시함

    #상담소 마커
    MC_conseling= MarkerCluster()
    for name, lat, long, address_ in zip(counseling_agency,counseling_latitude,counseling_longitude,counseling_address):
        text=f"""<h4 align='center'>{name}</h4><p align='center'>{address_}</p>"""
        iframe = folium.IFrame(text, width=100, height=100)
        popup = folium.Popup(iframe, max_width=3000)
        MC_conseling.add_child(
            folium.Marker([lat, long], popup = popup)).add_to(counseling_group)

    #공공 의료기관 마커
    MC_public=MarkerCluster()
    for name, lat, long, address_ in zip(public_agency,public_latitude,public_longitude,public_address):
        text=f"""<h4 align='center'>{name}</h4><p align='center'>{address_}</p>"""
        iframe = folium.IFrame(text, width=100, height=100)
        popup = folium.Popup(iframe, max_width=3000)
        MC_public.add_child(
            folium.Marker([lat, long], popup = popup)).add_to(public_group)

    #민간 의료기관 마커
    MC_private=MarkerCluster()
    for name, lat, long, address_ in zip(private_agency,private_latitude,private_longitude,private_address):
        text=f"""<h4 align='center'>{name}</h4><p align='center'>{address_}</p>"""
        iframe = folium.IFrame(text, width=100, height=100)
        popup = folium.Popup(iframe, max_width=3000)
        MC_private.add_child(
            folium.Marker([lat, long], popup = popup)).add_to(private_group)
    folium.LayerControl(position='bottomright',collapsed=False).add_to(my_map)
    LocateControl(position='bottomright',drawCircle=False,keepCurrentZoomLevel=True).add_to(my_map)
    # if my_location !=[37.5, 126.98]:
    #     folium.Circle(
    #         my_location,
    #         radius=radius,
    #         tooltip=folium.Tooltip,
    #         color='#ffffgg',
    #         fill_color='#3186cc',
    #         popup='내 중심 반경 5km',).add_to(my_map)

    # 지도 저장(seoul_colleges.html)
    my_map.save('./templates/mental_service.html')
    return render(request,'mental_service.html')

# def where_am_i(request):
#     my_location = geocoder.ipinfo('me')
#     make_map(request,my_location.latlng)
#     return render(request, 'mental_service.html')
```