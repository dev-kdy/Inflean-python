from datetime import datetime
import pytz

# 아시아/서울 시간대
seoul_timezone = pytz.timezone('Asia/Seoul')

# 현재 날짜와 시간 가져오기
current_time = datetime.now(seoul_timezone)

# 출력
print("현재 날짜와 시간 (아시아/서울):", current_time)

# class 구조 설계

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return f'브랜드명 : {self._company}\n차 상세 정보 : {self._details}'

    def __repr__(self):
        return (
                    f'field:\n'
                    f'_company: {self._company}\n'
                    f'_details: {self._details}\n'
                )


car1 = Car("Farrai", {"color": "white", "hoursepower": 400, "price" : 8000} )

print(car1)
print(car1.__repr__())
print(car1.__dict__)

print(dir(car1))