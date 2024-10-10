import os
import json

# 현재 파일의 디렉토리의 파일 목록을 JSON 파일에 저장하는 함수
def save_file_list_to_json(output_file):
    # 현재 스크립트 파일의 디렉토리 경로
    directory_path = os.path.dirname(os.path.realpath(__file__))

    # 디렉토리 내 모든 파일을 리스트로 저장
    file_list = []
    for root, dirs, files in os.walk(directory_path):
        # '.git' 디렉토리를 건너뛰기
        if '.git' in dirs:
            dirs.remove('.git')  # 해당 디렉토리를 검색 대상에서 제외

        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)

    output_path = os.path.join(directory_path, output_file)

    # 파일 목록을 JSON 파일로 저장
    with open(output_path, 'w') as json_file:
        json.dump(file_list, json_file, indent=4)

# 사용 예제
output_file = 'files.json'
save_file_list_to_json(output_file)
