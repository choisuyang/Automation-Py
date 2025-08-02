import time
import pyautogui
import os
import cv2
import numpy as np
from AppKit import NSScreen  # macOS에서 화면 해상도 감지를 위해 사용

class ImageSearch:
    def autoMouse(self, number):
        # Retina 디스플레이 좌표 보정
        pyautogui.PAUSE = 0.5  # 너무 빠르게 실행되지 않도록 조정
        pyautogui.FAILSAFE = False  # 에러 방지

        # 해상도 크기 확인
        screen_width, screen_height = pyautogui.size()  # 논리 픽셀 기준 화면 크기 출력
        print(f"화면 해상도: {screen_width} x {screen_height}")
        # 이미지 경로 설정
        current_dir = os.path.dirname(__file__)  
        img_path = os.path.join(current_dir, '..', 'img', f'{number}.png')

        # 상대 경로 -> 절대 경로로 변환
        img_path = os.path.abspath(img_path)
        print("-- 이미지 경로:", img_path)
        
        # locateOnScreen으로 화면에서 이미지 찾기
        location = pyautogui.locateOnScreen(img_path) 
        print('location--->',location)
        # pyautogui.center(location)
        pyautogui.moveTo(location, duration=0.6)
        pyautogui.click(location)
        if location:
            print(f"이미지 {number}.png 위치 발견: {location}")

            # 중앙 좌표 계산 및 배율 보정
            center_x, center_y = pyautogui.center(location)
            center_x = center_x // 2  # X좌표 보정
            center_y = center_y // 2  # Y좌표 보정
            print(f"보정된 좌표: ({center_x}, {center_y})")

            # 이동 및 클릭
            pyautogui.moveTo(center_x, center_y, duration=0.6)
            pyautogui.click(center_x, center_y)
            time.sleep(2)
            print(f"이미지 {number}.png 클릭 완료! ({center_x}, {center_y})")
        else:
            print(f"이미지 {number}.png 화면에서 찾을 수 없음.")
  