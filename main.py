from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import time
from slack.Notification import Noti


def parse_list(driver: webdriver.Chrome):
    lis = driver.find_elements(By.CLASS_NAME, 'pIav2d')
    idx = 0
    for li in lis:
        print('li : ', idx)
        idx += 1

    return lis


def parse_costs(driver: webdriver.Chrome):
    print('parsing start!')
    lis = driver.find_elements(By.CLASS_NAME, 'pIav2d')
    idx = 0
    costs = []
    for li in lis:
        spans = li.find_elements(By.TAG_NAME, 'span')
        for span in spans:
            if span.get_attribute("data-gs") is not None:
                if span.text == '':
                    continue
                print(idx, span.text[1:].replace(',', ''))
                costs.append(span.text)
                idx += 1

    return costs


def main():
    driver = webdriver.Chrome()

    # 크롬 드라이버에 url 주소 넣고 실행
    # driver.get('https://www.google.co.kr/')

    # 페이지가 완전히 로딩되도록 3초동안 기다림
    # time.sleep(3)
    # WebDriverWait(driver, 40)

    path = {
        # "15-BER-AMS": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE1YLAJagcIARIDSUNOcgcIARIDQkVSGh4SCjIwMjQtMDMtMDJqBwgBEgNBTVNyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko",
        # "15-BER-BER": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE1YLAJagcIARIDSUNOcgcIARIDQkVSGh4SCjIwMjQtMDMtMDJqBwgBEgNCRVJyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko",
        # "15-BER-BRU": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE1YLAJagcIARIDSUNOcgcIARIDQkVSGh4SCjIwMjQtMDMtMDJqBwgBEgNCUlVyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko",
        # "15-BER-WAW": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE1YLAJagcIARIDSUNOcgcIARIDQkVSGh4SCjIwMjQtMDMtMDJqBwgBEgNXQVdyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko",
        # "15-BER-VIE": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE1YLAJagcIARIDSUNOcgcIARIDQkVSGh4SCjIwMjQtMDMtMDJqBwgBEgNWSUVyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko",
        # "16-BER-AMS": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE2YLAJagcIARIDSUNOcgcIARIDQkVSGh4SCjIwMjQtMDMtMDJqBwgBEgNBTVNyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko",
        # "16-BER-BER": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE2YLAJagcIARIDSUNOcgcIARIDQkVSGh4SCjIwMjQtMDMtMDJqBwgBEgNCRVJyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko",
        # "16-BER-BRU": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE2YLAJagcIARIDSUNOcgcIARIDQkVSGh4SCjIwMjQtMDMtMDJqBwgBEgNCUlVyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko",
        # "16-BER-WAW": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE2YLAJagcIARIDSUNOcgcIARIDQkVSGh4SCjIwMjQtMDMtMDJqBwgBEgNXQVdyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko",
        # "16-BER-VIE": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE2YLAJagcIARIDSUNOcgcIARIDQkVSGh4SCjIwMjQtMDMtMDJqBwgBEgNWSUVyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko"
        "15-BER-AMS": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE1YLAJagcIARIDSUNOcgcIARIDQkVSGh4SCjIwMjQtMDMtMDJqBwgBEgNBTVNyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko",
        "15-BER-BRU": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE1YLAJagcIARIDSUNOcgcIARIDQkVSGh4SCjIwMjQtMDMtMDJqBwgBEgNCUlVyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko",
        "16-BER-AMS": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE2YLAJagcIARIDSUNOcgcIARIDQkVSGh4SCjIwMjQtMDMtMDJqBwgBEgNBTVNyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko",
        "16-BER-BRU": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE2YLAJagcIARIDSUNOcgcIARIDQkVSGh4SCjIwMjQtMDMtMDJqBwgBEgNCUlVyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko",
        "15-AMS-BER": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE1YLAJagcIARIDSUNOcgcIARIDQU1TGh4SCjIwMjQtMDMtMDJqBwgBEgNCRVJyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko",
        "15-BRU-BER": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE1YLAJagcIARIDSUNOcgcIARIDQlJVGh4SCjIwMjQtMDMtMDJqBwgBEgNCRVJyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko",
        "16-AMS-BER": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE2YLAJagcIARIDSUNOcgcIARIDQU1TGh4SCjIwMjQtMDMtMDJqBwgBEgNCRVJyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko",
        "16-BRU-BER": "https://www.google.com/travel/flights/search?tfs=CBwQAhohEgoyMDI0LTAyLTE2YLAJagcIARIDSUNOcgcIARIDQlJVGh4SCjIwMjQtMDMtMDJqBwgBEgNCUlVyBwgBEgNJQ05AAUgBcAGCAQsI____________AZgBAw&tfu=EgIIASIDCgEw&hl=ko"
    }
    last_value = {}
    for key in path:
        last_value[key] = 1e100

    updated = False
    slack_noti = Noti()
    while True:
        try:
            message = ''
            diff = False
            for key in path:
                login_url = path[key]
                driver.get(login_url)
                time.sleep(5)
                driver.implicitly_wait(40)
                # parse_list(driver)
                costs = parse_costs(driver)
                message += key + ": "
                for cost in costs[:2]:
                    message += cost[1:][:-5] + "\t"

                if last_value[key] != costs[0][1:][:-5]:
                    diff = True
                last_value[key] = costs[0][1:][:-5]

                message += "\n"

            if diff == True:
                slack_noti.send(message)
            time.sleep(3*60*60)
        except:
            print("Error!")
            time.sleep(3)


if __name__ == "__main__":
    main()
