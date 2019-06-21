import requests as rq
import json

class fizz:
    def __init__(self):
        self.url = "https://api.noopschallenge.com"
        self.next = "/fizzbot"
        self.burl = self.url+self.next

    def get_question(self):
        self.burl = self.url+self.next
        noop = rq.get(self.burl).json()
        message = noop['message']
        self.next = noop['nextQuestion']
        return message, self.next

    def send_answer(self, answer):
        data = json.dumps({'answer':answer})
        code = rq.post(self.burl, data=data)
        return code
