# notification using slack
import requests
import os


class Noti:
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, 'token.txt')
        if os.path.exists(file_path) == False:
            raise FileNotFoundError("File not found")

        with open(file_path, "r") as fo:
            self.token = fo.readline()

    def send(self, message='message', label='#autobot'):
        response = requests.post("https://slack.com/api/chat.postMessage",
                                 headers={
                                     "Authorization": "Bearer " + self.token},
                                 data={"channel": label, "text": message}
                                 )
        print(message)
        # print(response)


def test():
    noti = Noti()
    noti.send(label='#autobot', message='hello here is rockjoon!')


if __name__ == "__main__":
    test()
