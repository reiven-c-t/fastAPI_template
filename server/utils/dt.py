from datetime import datetime, timedelta, timezone


class DateTime:
    def __init__(self):
        self.JST = timezone(timedelta(hours=9), "JST")

    def now(self):
        return datetime.now(self.JST)


dt = DateTime()
