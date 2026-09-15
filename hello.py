# Ruff 작동하는지 테스트

name = "CNU"
numbers = [1, 2, 3, 4, 5]


def greet(name):
    print("Hello, " + name)


greet(name)

# CNU-202404659-/
# │
# ├── .vscode/
# │   └── settings.json
# │       → VS Code 설정
# │       → 저장할 때 Ruff 실행
# │
# ├── pyproject.toml
# │       → Python 프로젝트/도구 설정
# │       → 현재는 Ruff의 규칙 설정
# │
# ├── .gitignore
# │       → GitHub에 올리지 않을 파일 지정
# │       → .venv/, __pycache__/ 등
# │
# └── hello.py
#         → 실제 Python 소스 코드

# Python       → #
# TOML         → #
# C++          → //
# JavaScript   → //
# JSONC        → //
