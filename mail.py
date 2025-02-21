import requests
from os import path

class BaseMail:
    def __init__(self, api="https://mail-service.iran.liara.ir/api/v1/mails/"):
        self.api = api


class Message(BaseMail):
    def __init__(self, iid, direction, ffrom, to, subject, isFree, isDev, isSpam, isBlockedByRule, isTrash, createdAt, smapScore, readAt, mailserverId: str, header: dict, text=None):
        super().__init__()
        self.iid = iid
        self.direction = direction
        self.ffrom = ffrom
        self.to = to
        self.subject = subject
        self.isFree = isFree
        self.isDev = isDev
        self.isSpam = isSpam
        self.isBlockedByRule = isBlockedByRule
        self.isTrash = isTrash
        self.createdAt = createdAt
        self.smapScore = smapScore
        self.readAt = readAt
        self.mailserverId = mailserverId
        self.text = text
        self.header = header

    def __str__(self):
        return self.idd + '->' + self.subject

    def __repr__(self):
        return self.idd + '->' + self.subject

    def get_text(self):
        if self.text:
            return self.text

        msg = requests.get(path.join(self.api, self.mailserverId, "messages", self.iid), headers=self.header)
        if msg.status_code != 200:
            return False
        msg = msg.json()
        self.text = msg.get('data').get('message').get('text')
        return self.text


    def from_dict(self):
        ...


class MailServer(BaseMail):
    def __init__(self, mailserverId: str, liaraToken: str):
        super().__init__()
        self.mailserverId = mailserverId
        self.api = f"{self.api}{mailserverId}/messages?direction=incoming&isTrash=false"
        self.header = {"Authorization": f"Bearer {liaraToken}"}
        self.messages = []

    def list_income(self):
        mails = requests.get(self.api, headers=self.header)
        if mails.status_code != 200 or mails.json().get("status") != 'success':
            return False
        mails = mails.json()
        for mail in mails.get('data').get('messages'):
            self.messages.append(Message(
                mail.get('_id'),
                mail.get('direction'),
                mail.get('from'),
                mail.get('to'),
                mail.get('subject'),
                mail.get('isFree'),
                mail.get('isDev'),
                mail.get('isSpam'),
                mail.get('isBlockedByRule'),
                mail.get('isTrash'),
                mail.get('createdAt'),
                mail.get('smapScore'),
                mail.get('readAt'),
                self.mailserverId,
                self.header,
            ))
        return self.messages

    def __str__(self):
        return self.mailserverId
