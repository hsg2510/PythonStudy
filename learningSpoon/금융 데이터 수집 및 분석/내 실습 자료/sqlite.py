

"""
데이터 타입
- NULL, INTEGER, REAL(실수) TEXT(문자열), BLOB(바이너리 파일)

기본 명령어들
- create table if not exists 회계사 ( aid INTEGER PRIMARY KEY, 감사인 TEXT, 등록번호 TEXT);
- insert into 회계사 values(0, "삼일회계법인", "106-81-19621");
- select * from 회계사 where 감사인 = "삼일회계법인";
- select * from 회계사 where length(감사인) = 6;
- select * from 회계사 where substr(감사인, 1, 2) = "삼일"; #1번 위치로부터 2개 가져옴.
- alter table user add 비고 text; ("비고" 라는 column 추가)
- update user set 비고="진상" where  name = "홍성곤";
- drop table 테이블이름;

기존에 있던 컬럼을 지우는 명령어는 없다. 이런 경우 새로 테이블을 만들고 기존 테이블 데이터를 모두 옮겨야 한다.
- create table modified_user (name text);
- insert into modified_user SELECT name from user;
- drop table user;

테이블 병합
-SELECT 회사.종목명, 회사.주요주주, 회계사.감사인 from 회사 left join 회계사 on 회사.aid = 회계사.aid; #회계사 테이블을 회사 테이블로 합친다(aid 기준으로)
-select 회사.종목명, 회계사.등록번호 from 회사 left join 회계사 on 회사.aid = 회계사.aid where 회계사.감사인 = "삼일회계법인";
"""

import sqlite3

#DB 연결
conn = sqlite3.connect("test.db")
cur = conn.cursor()
query = "select * from 회계사"
cur.execute(query) # 명령어 실행

# 1) cursor
#rows = cur.fetchall() #모든행을 한번에 가져와서 rows에 저장

#for row in rows:
#    print(row)득

# 2)
for result in cur: #모든행을 변수에 저장한 뒤 출력하는 것이 아니라 for문 에서 cur로 부터 한행씩 받아와서 출력(성능상 이)
    print(result)

conn.commit() #save the change
conn.close()