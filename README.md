# 클라우드 업로드 전 로컬 테스트

1. 가상 환경을 생성하고 source 명령으로 활성화
```
python3.10 -m venv .venv
source .venv/bin/activate
```
2. make install 명령 실행
```
make install
```
3. python app.py 명령 실행
```
python app.py
```
4. 새로운 터미널 열고 작업 경로로 이동하여 ./make_prediction.sh 명령 실행
```
./make_prediction.sh
```

# Azure 업로드 

* [[Azure 공식 문서]](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops&tabs=linux)

1. 애저 클라우드 셸 실행
2. 애저 클라우드 셸에서 깃허브 저장소 클론
```
git clone https://github.com/<GitHub-사용자이름>/<저장소이름>.git
```
3. 가상 환경을 생성하고 source 명령으로 활성화
```
python3.10 -m venv .venv
source .venv/bin/activate
```
4. make install 명령 실행
```
make install
```
5. 클라우드 셸에서 앱을 배포
```
az webapp up -n <your-appservice>
```
6. URL(https://<your-appservice>.azurewebsite.net/)에 접속하여 배포된 애플리케이션이 잘 작동하는지 확인

