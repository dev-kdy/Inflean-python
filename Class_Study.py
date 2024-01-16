class Car():
    """
    Car class
    Author : KDY
    Date : 2024-01-16
    """

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

    def detail_info(self):
        print("Id : {}\nprice_info : {}".format(id(self), self._details.get('price')))


car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

print(id(car1))
print(id(car2))
print(id(car3))

print(car1 is car2)

car2.detail_info()

# Magic method __doc__을 출력 시 클래스 설명 주석이 나온다.
print(car1.__doc__)

