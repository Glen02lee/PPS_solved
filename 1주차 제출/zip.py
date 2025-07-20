import zipfile
import glob
from datetime import datetime

# 이름과 날짜 설정
name = "이민석"
date_str = datetime.today().strftime('%Y%m%d')  # '20250713' 형식
zip_filename = f"{name}_{date_str}.zip"

# zip 파일 생성
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for file in glob.glob("*.py"):
        zipf.write(file)

print(f"{zip_filename} 생성 완료!")