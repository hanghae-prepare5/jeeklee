1. 서버 실행
: 자신의 프로젝트 폴더에서
1) windows : .\run_server.ps1
2) ubuntu :
   shell) set FLASK_APP="./proj/__init__.py"
   shell) set FLASK_DEBUG="true"
   shell) flask run

2. python 모듈 관리
1) 모듈 다운로드
   venv) pip install -r -requirements.txt
2) 모듈 목록 최신화
   venv) pip freeze > requirements.txt

3. 서버 강제 종료
 : Stop-Process -name flask
