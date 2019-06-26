import requests as rq
import json

class fizz:
    def __init__(self):
        self.url = "https://api.noopschallenge.com"
        self.next = "/fizzbot"
        self.burl = self.url+self.next

    async def get_question(self):
        noop = rq.get(self.burl).json() # get the response
        # message = noop['message'] # message from response
        # rules = noop['rules']
        # numbers = noop['numbers']
        # self.next = noop['nextQuestion'] # next quesion link
        self.burl = "https://api.noopschallenge.com/fizzbot/questions/1"
        return noop # return question ?
        # await noop # return question ?

    async def send_answer(self, answer):
        data = json.dumps({'answer':answer}) # json-ify dict for post
        code = rq.post(self.burl, data=data).json() # post answer
        if code['result'] == 'correct':
            self.next = code['nextQuestion']
            self.burl = self.url + self.next
        return code # return json of response
        # await code # return json of response

    async def clear(self):
        self.next = '/fizzbot' # reset var
