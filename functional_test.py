from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000/library/')

        self.assertIn('Home Title', self.browser.title)

        # 그는 현재 3층 도서관의 여유좌석을 확인한다.
        status = self.browser.find_element_by_id('man_room_available')
        self.assertEqual(int(status.text), 10)

        # # 예약하기 위해 3층 도서관 버튼을 클릭한다.
        # button = self.browser.find_element_by_id('3d_button')
        # button.click()
        #
        # # 3층의 현재 좌석 상황이 보인다. 90개 좌석이 있는 것을 확인한다.
        # table = self.browser.find_element_by_id('id_list_table')
        # digit = table.find_element_by_tag_name('td')
        # self.assertEqual(len(digit), 10)
        #
        # # 1번 좌석을 예약한다.
        # rows = table.find_element_by_tag_name('tr')[1-1] # 사람이 이해하기 쉽게
        # column = rows.find_element_by_tag_name('td')[1-1] # 사람이 이해하기 쉽게
        # column

        # 로그인을 한다.
        # 남자, 여자를 선택할 수 있도록 한다.
        # 남자를 선택하면 90개의 좌석의 예약 현황을 볼 수 있다.
        # 예약된 자리와 예약할 수 있는 자리의 css를 다르게 보여준다.
        # 1번 자리를 선택하면 예약


if __name__ == '__main__':
    unittest.main(warnings='ignore')


######## First
# 로그인이 되어 있지 않으면 로그인 페이지로 이동시킴
# 디지털 열람실
## 이용안내, 이용예약, 예약확인 및 취소 버튼 3개 만들어놓기



# 좌석 버튼 위에 마우스를 올리면 현재 예약한 사람(x)과 예약 종료 시간을 보내준다.
# 좌석이 예약되어 있으면 x 표시, 좌석이 예약 가능하다면 seat_number를 보여준다.
# 좌석을 클릭하면 '예약' 과 '취소' 버튼이 2개가 뜬다.
# 예약 버튼을 누르면 다시 한 번 예약하는 사람 이름, 시작 시간, 종료 시간을 보여주면서
# '확인' 버튼과 '취소' 버튼을 보여준다.



# 예약, 퇴실, 연장
#

## 현재 좌석 현황
# 1안
# 종료시간 > 현재시간 ---> 사용중
# 종료시간 < 현재시간 ---> 예약가능

# 2안
# seat table을 따로 만들고 여기에 available 컬럼에 3가지 타입을 넣는다.
# available 컬럼을 종료 시간이 지나게 되면 다시 업데이트를 해준다??


## CFV field 설명
# reservation: Yes, No
# class: pointer available, yesok, pass
# x: 가로
# y: 세로
# seatcd:
# seatname: 가로세로
# rating_nm: 등급 이름
# seat_relation_code:
# kind_cd:
# rating_cd:
# seat_area_cd:
# locynm: y열 이름
# locxnm: 가로 번호



### 연재 계획

# 좌석 예약할 때 생성되는 정보: 사용자 ID,
# 좌석 예약할 때 추가되는 정보

# 좌석 현황표: /library/
# 개별 좌석 보기: /library/<좌석 ID>/
# 좌석 예약: /library/<좌석 ID>/reserve
# 좌석 예약 취소: /library/<좌석 ID>/cancel





