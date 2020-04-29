class Worker(object):

    def __init__(self, worker_id, info):
        self.id = worker_id
        self.domain = info['domain']
        self.morning_options = info['morningOptions']
        self.evening_options = info['eveningOptions']

    def score(self):
        pass

    def add_transport_to_dic(self, dic_morning, dic_evening):
        for transports in self.morning_options:
            for transport_id in transports:
                if transport_id not in dic_morning:
                    dic_morning[transport_id] = Transport(transport_id, True)
                dic_morning[transport_id].add_user(self.id)

        for transports in self.evening_options:
            for transport_id in transports:
                if transport_id not in dic_evening:
                    dic_evening[transport_id] = Transport(transport_id, False)
                dic_evening[transport_id].add_user(self.id)


class Transport(object):

    def __init__(self, id, is_morning):
        self.id = id
        self.is_morning = is_morning
        self.potential_users_id = []

    def add_user(self, user_id):
        self.potential_users_id.append(user_id)


class Dataset(object):

    def __init__(self, id_nb, quotas, workers):
        self.id = id_nb
        self.quotas = quotas
        self.workers = []
        self.transports_morning = {}
        self.transports_evening = {}
        for worker_id, worker_info in workers.items():
            self.workers.append(Worker(worker_id, worker_info))
            self.workers[-1].add_transport_to_dic(
                self.transports_morning, self.transports_evening)
