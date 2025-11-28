import pyautogui
import time
import schedule

# 클릭할 좌표들
positions = [(628, 794), (964, 754),(1295,973)]
#positions = [(953,499)]

# 특정 위치들을 0.2초 간격으로 클릭하는 함수
def click_multiple_positions():
    for x, y in positions:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(0.01)  # 0.2초 간격

# 매일 특정 시각에 실행 (예: 15:12)
schedule.every().day.at("20:00:00").do(click_multiple_positions)

# 계속 대기하면서 스케줄 확인
while True:
    schedule.run_pending()
    time.sleep(1)