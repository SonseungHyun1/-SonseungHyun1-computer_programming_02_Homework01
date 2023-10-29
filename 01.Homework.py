# 신차 출고 유지비 계산기
class CarExpensesCalculator:
    def __init__(self):   #클래스의 속성들을 초기화
        self.car_price = 0
        self.driver_age = 0
        self.fuel_type = ""
        self.annual_mileage = 0
        self.fuel_efficiency = 0
        self.down_payment = 0
        self.loan_duration = 0

    def get_car_price(self):  # 차량의 가격을 입력 받아 속성에 할당
        car_price_str = input("차량의 가격을 입력하세요 (백만원 단위로 예: 5000만원 -> 50 ): ")
        if not car_price_str.replace('.', '').isdigit():
            print("입력값은 숫자여야 합니다.")
            return False
        self.car_price = float(car_price_str) * 1000000
        return True

    def get_driver_age(self):   # 운전자의 나이를 입력 받아 속성에 할당
        self.driver_age = int(input("운전자의 나이를 입력하세요: "))

    def get_fuel_expenses(self):  # 차량의 연료 정보를 입력 받아 속성에 할당
        self.fuel_type = input("차량의 연료 유형을 입력하세요 (가솔린 또는 디젤): ")
        annual_mileage_str = input("연간 주행 예상 거리를 입력하세요 (km 단위로): ")
        fuel_efficiency_str = input("차량의 평균 연비를 입력하세요 (km/l 단위로): ")

        if not annual_mileage_str.isdigit() or not fuel_efficiency_str.replace('.', '').isdigit():
            print("입력값은 숫자여야 합니다.")
            return False

        self.annual_mileage = int(annual_mileage_str)
        self.fuel_efficiency = float(fuel_efficiency_str)
        return True

    def get_installment_payment(self):   # 차량의 할부 정보를 입력 받아 속성에 할당
        down_payment_str = input("선납금을 입력하세요 (백만원 단위로): ")
        loan_duration_str = input("할부 개월을 입력하세요: ")

        if not down_payment_str.replace('.', '').isdigit() or not loan_duration_str.isdigit():
            print("입력값은 숫자여야 합니다.")
            return False

        self.down_payment = float(down_payment_str) * 1000000
        self.loan_duration = int(loan_duration_str)
        return True

    def calculate_insurance_premium(self):  # 보험료를 계산 하는 함수
        base_premium = 1500000
        additional_fee = 0

        if self.car_price > 50000000:
            additional_fee += 0.1

        if self.driver_age < 25:
            additional_fee += 0.5
        elif 25 <= self.driver_age < 35:
            additional_fee += 0.4
        elif 35 <= self.driver_age < 45:
            additional_fee += 0.3
        elif self.driver_age > 60:
            additional_fee += 0.1

        total_premium = base_premium + (base_premium * additional_fee)
        monthly_premium = total_premium / 12

        return total_premium, monthly_premium

    def calculate_fuel_expenses(self):  # 연료비를 계산 하는 함수
        petrol_price = 1629
        diesel_price = 1638

        if self.fuel_type == "가솔린":
            fuel_consumption = self.annual_mileage / self.fuel_efficiency
            fuel_cost = fuel_consumption * petrol_price
        elif self.fuel_type == "디젤":
            fuel_consumption = self.annual_mileage / self.fuel_efficiency
            fuel_cost = fuel_consumption * diesel_price
        else:
            print("유효하지 않은 연료 유형입니다.")
            fuel_cost = 0

        monthly_fuel_cost = fuel_cost / 12
        return fuel_cost, monthly_fuel_cost

    def calculate_installment_payment(self):    # 할부 이자 및 월 할부금을 계산 하는 함수
        loan_amount = self.car_price - self.down_payment
        annual_interest_rate = 0.054
        monthly_interest_rate = annual_interest_rate / 12
        monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -self.loan_duration)

        return monthly_payment

    def calculate_taxes(self):  # 세금 및 등록비를 계산하는 함수
        individual_consumption_tax = self.car_price * 0.05
        education_tax = individual_consumption_tax * 0.3
        registration_tax = self.car_price * 0.07
        total_taxes = individual_consumption_tax + education_tax + registration_tax

        return total_taxes

    def calculate_total_expenses(self):   # 총 유지비를 계산하는 함수
        total_insurance_premium, monthly_insurance_premium = self.calculate_insurance_premium()
        total_fuel_cost, monthly_fuel_cost = self.calculate_fuel_expenses()
        monthly_installment_payment = self.calculate_installment_payment()
        total_taxes = self.calculate_taxes()

        # 월간 및 연간 유지비 계산
        monthly_expenses = monthly_insurance_premium + monthly_fuel_cost + monthly_installment_payment + total_taxes
        annual_expenses = monthly_expenses * 12

        return monthly_expenses, annual_expenses

# 메인 프로그램
calculator = CarExpensesCalculator()

while True:
    if not calculator.get_car_price():
        continue

    calculator.get_driver_age()
    if not calculator.get_fuel_expenses():
        continue

    if not calculator.get_installment_payment():
        continue

     # 각 비용 계산
    total_insurance_premium, monthly_insurance_premium = calculator.calculate_insurance_premium()
    total_fuel_cost = calculator.calculate_fuel_expenses()
    monthly_fuel_cost = total_fuel_cost[1] / 12  # 두 번째 값만 사용
    monthly_installment_payment = calculator.calculate_installment_payment()
    total_taxes = calculator.calculate_taxes()

    # 최종 결과 출력
    print("\n=== 최종 결과 ===")
    print(f"월간 유지비: {monthly_insurance_premium + monthly_fuel_cost + monthly_installment_payment:.2f} 원")
    print(f"연간 유지비: {(monthly_insurance_premium + monthly_fuel_cost + monthly_installment_payment) * 12 :.2f} 원")
    print("=================")
