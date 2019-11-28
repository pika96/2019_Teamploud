# 2019_Teamploud(2019.09 - 2019.12)

## 프로젝트 개요
클라우드 컴퓨팅 기술은 이제 우리 주변에서 널리 사용되고 있는 기술입니다. 실제로 클라우드는 저희 주변에서 쉽게 볼 수 있는 메일, 구글 드라이브, AWS 등 다양한 분야에서 사용되고 있습니다.
저희 프로젝트는 기존 주제에 클라우드를 접목시켜 만드는 것을 목표로 하였습니다. 저희가 기획한 프로젝트는 캘린더에 일정을 메모하고 해당 날짜에 필요한 문서를 첨부하는 등 팀 단위의 일정을 관리 할 수 있는 프로그램입니다.

저희는 AWS 같은 다른 클라우드 서비스를 이용하지 않고, 노트북으로 리눅스 서버를 구축하여 모든 데이터가 저희가 만든 서버에 저장될 수 있도록 구현하였습니다.

## 개발 환경
 - Server : ubuntu-18.04.1-live-server-amd64
 - Client : Windows 10
 - 개발 언어 : Python
 - 네트워크 통신 : socket 통신
 - DB : Mongo DB
 - 암호화
   - 키 교환 : RSA 암호
   - 파일 암호화 : pyCryptodome modules
   - DB 암호화 : SHA-256


## Teamploud 기능
 - 회원가입
 - 로그인
 - 그룹 생성
 - 캘린더
 - 날짜에 파일 첨부 및 메모
 - 그룹끼리 일정 및 파일 공유

## 느낀 점
 - 클라우드 서버를 직접 구현해봄으로써 클라우드 작동 방식을 이해할 수 있었다.
 - 파일 암호화, RSA 암호화, DB 암호화 등 암호화를 적용시켜보며 암호화 과정을 다시 한번 공부하고 이해할 수 있었다.
 - 여러 사람이 한꺼번에 접속할 수 있도록 멀티 스레딩을 이용하여 구현하였는데 완벽하지는 않았지만 멀티 스레딩에 대해 공부할 수 있었다.
 - socket 통신을 이용해 직접 연결해보며 네트워크 통신에 대해 공부할 수 있었다.

## 발표 자료
