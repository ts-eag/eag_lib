## 도서관 예약 시스템 진행사항 및 향후 계획

### 목적

- 이미 개발된 도서관 예약 시스템이 존재하나 비용 부분 때문에 자체적으로 재개발
- 이미 개발된 도서관 예약 시스템의 기본 기능을 먼저 구현 후 Specific한 기능들은 추가 개발한다.
  - 하지만 너무 많은 Specific한 개발 사항들은 SI가 될 수 있기 때문에 지양한다.
  - **공용 플랫폼** 개념으로 가야한다.

### 전제 사항

- 그래픽 UI는 최대한 신경쓰지 않고 개발한다.
- 계획이 수정될시 이 문서에 **지속적**으로 추가한다.(현재 시스템상 유지 보수 기능 취약하기 때문)
- 질문이나 문제가 발생할시 Issue에 등록해 주면 된다.

### 완료된 사항

- 도서관 예약 시스템 DB 구조 완성(제일 중요)
  - 일단 현재까지 나온 기능을 구현하기 위한 DB는 충분하지만 로직상 문제가 발견시 변경해야 함
- 사용 불가 좌석, 사용중 좌석, 예약가능 좌석 표시
- 남자, 여자 현재 좌석 현황
- 로그인 기능 구현
  - 현재는 자체적인 로그인 시스템으로 구현
  - 향후 API로 연동하는 부분이 들어갈시 많은 부분 수정이 필요하게 됨
- 현재 로그인한 사용자가 자신의 예약을 확인 가능
- 각종 device에 따라 UI 변경(반응형 웹)

### 향후 계획

- 예약 기능 추가
- 연장 기능 추가
- 퇴실 기능 추가
- 예약 기능시 로직 버그 제거
  - 과거로 예약 가능
  - 1명이 오늘 예약하고, 내일 예약하고, 내일 모레를 동시에 예약할 수 있는 상황 제거해야 함
  - etc
- 반응형 웹 UI에 시각화 기능 추가
- 관리자 페이지 통계 기능 추가

### 문서 문제점?

- 이렇게 기능 추가라고만 써놓으면 일정 관리가 안되는데 좀 더 일정 관리를 잘할 수 있는 툴이 없을까?
  - 귀찮지 않으면서 내 일에 방해가 되지 않는? 그런 툴을 한 번 찾아보자.