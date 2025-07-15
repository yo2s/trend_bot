import requests
import os
from datetime import datetime

def search_trends():
    """이커머스 트렌드 검색"""
    trends = []
    
    # 구글 트렌드 키워드들
    keywords = ["이커머스", "온라인쇼핑", "AI마케팅", "개인화마케팅", "카카오톡마케팅"]
    
    # 간단한 트렌드 시뮬레이션 (나중에 실제 크롤링으로 교체)
    for keyword in keywords:
        trends.append(f"🔥 {keyword}: 관심도 상승 중")
    
    return "\n".join(trends)

def send_to_slack(message):
    """슬랙으로 메시지 전송"""
    webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
    
    if not webhook_url:
        print("SLACK_WEBHOOK_URL이 설정되지 않았습니다!")
        return
    
    payload = {
        'text': message,
        'username': 'Trend Bot',
        'icon_emoji': ':chart_with_upwards_trend:'
    }
    
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        print("슬랙 전송 성공!")
    else:
        print(f"슬랙 전송 실패: {response.status_code}")

if __name__ == "__main__":
    # 트렌드 검색
    trends = search_trends()
    
    # 메시지 포맷팅
    today = datetime.now().strftime('%Y-%m-%d %H:%M')
    message = f"""🚀 **{today} 이커머스 트렌드 리포트**

{trends}

_그냥 헌팅말고 ㅡㅡ 트렌드 시그널 헌팅 가즈아! 💪_"""
    
    # 슬랙으로 전송
    send_to_slack(message)
    print("트렌드 검색 및 전송 완료!")
