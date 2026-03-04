# 경량 Alpine 기반 Nginx 이미지 사용
FROM nginx:alpine

# Nginx 기본 서버 설정 파일 교체
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 정적 웹 페이지(index.html)를 Nginx 기본 경로에 복사
COPY index.html /usr/share/nginx/html/index.html