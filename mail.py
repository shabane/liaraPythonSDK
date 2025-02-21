import requests


class BaseMail:
    def __init__(self, api="https://mail-service.iran.liara.ir/api/v1/mails/"):
        self.api = api


class Message(BaseMail):
    def __init__(self, iid, direction, ffrom, to, subject, isFree, isDev, isSpam, isBlockedByRule, isTrash, createdAt, smapScore, readAt, mailserverId: str, header: dict, text=""):
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

    def __str__(self):
        return self.idd + '->' + self.subject

    def get_text(self, idd):
        ...

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
