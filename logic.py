import requests as rq
import json

class fizz:
    def __init__(self):
        self.url = "https://api.noopschallenge.com"
        self.next = "/fizzbot"
        self.burl = self.url+self.next

    def get_question(self):
        noop = rq.get(self.burl).json() # get the response
        message = noop['message'] # message from response
        print(self.burl, noop)
        # self.next = noop['nextQuestion'] # next quesion link
        self.burl = "https://api.noopschallenge.com/fizzbot/questions/1"
        return message

    def send_answer(self, answer):
        data = json.dumps({'answer':answer}) # json-ify dict for post
        code = rq.post(self.burl, data=data).json() # post answer
        if code['result'] == 'correct':
            self.next = code['nextQuestion']
            self.burl = self.url + self.next
        return code # return json of response

    def clear(self):
        self.next = '/fizzbot' # reset var
