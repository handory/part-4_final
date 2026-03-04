# Python 3.11 기반의 경량(slim) 이미지 사용
FROM python:3.11-slim

# 컨테이너 내부 작업 디렉토리를 /app으로 설정
WORKDIR /app

# 의존성 목록 파일을 컨테이너로 복사
COPY requirements.txt .

# requirements.txt 기준으로 라이브러리 설치 (캐시 미사용)
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 메인 파일 복사
COPY main.py .

# 컨테이너가 사용할 포트(8000) 명시
EXPOSE 8000

# uvicorn으로 FastAPI 서버 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]