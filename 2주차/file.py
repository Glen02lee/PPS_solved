import datetime

today_date = datetime.datetime.now().strftime("%Y%m%d")

for i in range(1, 5 + 1):  # 원하는 숫자 범위 설정하시면 됩니다~
    filename = f"B{i:03d}_이민석_{today_date}.py"  # 날짜는 자동으로 추가해드렸습니다~
    with open(filename, 'w') as f:
        f.write(f'#PPS "B{i:03d}"\n')
    print(f"Created {filename}")