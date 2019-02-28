import csv

users = {}


class Mail:
    def __init__(self, _date, _to=None, _from=None):
        self.to = _to
        self.fr = _from
        self.date = _date

    def __str__(self):
        return "From {:>50} to {:>50} at {:>20}".format(
            self.fr if self.fr is not None else 'null',
            self.to if self.to is not None else 'null',
            self.date
        )


with open('mail_metadata_dataset.csv', 'r', encoding='utf8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    headers = next(spamreader, None)
    # print(headers)
    i = 0
    for fr, to, date in spamreader:
        if fr not in users:
            users[fr] = {'user': fr, 'mails': []}
        if to not in users:
            users[to] = {'user': to, 'mails': []}
        if "badguysgroup.com" not in fr:
            users[fr]['mails'].append(Mail(date, _to=to))
        if "badguysgroup.com" not in to:
            users[to]['mails'].append(Mail(date, _from=fr))
        i += 1

print(len(users))

users_s = list(users.values())
users_s.sort(key=lambda user: len(user['mails']))#, reverse=True)

for user in users_s[:10]:
    print(user['user'], len(user['mails']))
