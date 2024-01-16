from datetime import datetime
import pytz

# 아시아/서울 시간대
seoul_timezone = pytz.timezone('Asia/Seoul')

# 현재 날짜와 시간 가져오기
current_time = datetime.now(seoul_timezone)

# 출력
print("현재 날짜와 시간 (아시아/서울):", current_time)
