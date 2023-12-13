import qrcode

name = input("사이트 이름을 입력하세요: ")
site = input("사이트 주소를 입력하세요: ")

# QR 코드로 변환할 데이터
data = site

# QR 코드 생성
qr = qrcode.QRCode(
version=1, # QR 코드 버전 설정 (1부터 40까지)
error_correction=qrcode.constants.ERROR_CORRECT_L, # 오류 정정 수준 설정
box_size=10, # 각 QR 코드 모듈의 크기 설정
border=4, # 테두리의 너비 설정
)

# 데이터 추가
qr.add_data(data)
qr.make(fit=True)

# 이미지 생성
img = qr.make_image(fill_color="black", back_color="white")

# 이미지 저장
img.save(f"{name}.png")
print("생성 완료.")