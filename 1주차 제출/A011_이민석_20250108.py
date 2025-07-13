import pathlib

folder = pathlib.Path(r'C:\Users\USER\OneDrive\바탕 화면\pps\1주차\1번째 제출')
new_date = '20250711'

for p in folder.glob('A[0-9][0-9][0-9]_이민석_*.py'):
    parts = p.stem.split('_')
    if len(parts) != 3:
        continue
    new_name = f'{parts[0]}_{parts[1]}_{new_date}{p.suffix}'
    p.rename(p.with_name(new_name))
    print(f'{p.name} -> {new_name}')
