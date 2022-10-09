#데이터 전처리: Null값 처리/ 불필요 피처 제거/ 문자열-카테고리 인코딩을 일괄적으로 수행할 수 있겠끔 함수로 만들기
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 결측치 처리하기
def fillna(df):
    # 이 책에선 age는 열의 평균으로, 나머지 변수들은 'N'값으로 체우기로 결정한다
    df['Age'].fillna(df['Age'].mean(),inplace=True)
    df['Cabin'].fillna('N',inplace=True)
    df['Embarked'].fillna('N',inplace=True)
    return df

#불필요해보이는 피처 제거하기
def drop_features(df):
    df.drop(['PassengerId','Name','Ticket'],axis=1,inplace=True)
    return df

#문자열- 카테고리 피처 Sex,Cabin,Embarked를 인코딩하기
def encoding_features(df):
    #한번만 인코딩해야됨. 두번하면 안됨
    categories_backup=[]
    features=['Cabin','Sex','Embarked']
    for feature in features:
        LE= LabelEncoder()
        LE= LE.fit(df[feature])
        #카테고리 백업해두기
        categories_backup.append(list(LE.classes_))
        #인코딩하기
        df[feature]= LE.transform(df[feature])
    return df

#앞에서 정의한 전처리 함수들을 호출하여 한번에 전처리를 완료하기
def preprocessing_feature(df):
    df= fillna(df)
    df= drop_features(df)
    df= encoding_features(df)
    return df