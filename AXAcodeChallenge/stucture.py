import numpy as np


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

    def __repr__(self):
        return str(self.id)


class Transport(object):

    def __init__(self, id, is_morning):
        self.id = id
        self.is_morning = is_morning
        self.potential_users_id = []

    def add_user(self, user_id):
        self.potential_users_id.append(user_id)

    @property
    def score(self):
        return len(self.potential_users_id)

    def __repr__(self):
        return str(self.id)


class Dataset(object):

    def __init__(self, id_nb, quotas, workers):
        self.id = id_nb
        self.quotas = quotas
        self.domain_worker_dic = {}
        self.workers = {}
        self.transports_morning = {}
        self.transports_evening = {}
        for worker_id, worker_info in workers.items():
            worker = Worker(worker_id, worker_info)
            domain = worker.domain
            self.workers[worker_id] = worker
            if domain not in self.domain_worker_dic:
                self.domain_worker_dic[domain] = set()
            self.domain_worker_dic[domain].add(worker.id)
            worker.add_transport_to_dic(self.transports_morning, self.transports_evening)

    @property
    def num_workers(self):
        return len(self.workers)

    @property
    def num_domains(self):
        return len(self.domain_worker_dic)

    @property
    def num_transports_morning(self):
        return len(self.transports_morning)

    @property
    def num_transports_evening(self):
        return len(self.transports_evening)

    @property
    def num_by_domain(self):
        return {domain: len(workers) for domain, workers in self.domain_worker_dic.items()}

    def plot_domain(self, ax):
        nb_domains = len(self.domain_worker_dic)
        ax.bar(np.arange(nb_domains), self.quotas.values(), alpha=0.7, label='quotas')
        ax.bar(np.arange(nb_domains), self.num_by_domain.values(), alpha=0.7, label='Available workers')
        ax.set_xticks(np.arange(nb_domains))
        ax.set_xticklabels(list(self.quotas.keys()), rotation='vertical', fontsize='medium')
        ax.legend()

    def plot_transport(self, ax, color, transports, label):
        num_transport = len(transports)
        num_workers_transport = [len(transport.potential_users_id) for transport in transports.values()]
        ax.bar(np.arange(num_transport), num_workers_transport, color=color, label=label, alpha=0.7)
        ax.set_xticks(np.arange(num_transport))
        ax.set_xticklabels(transports.values, rotation='vertical', fontsize='medium')

    def plot_transport_morning(self, ax, color='r'):
        self.plot_transport(ax, color, self.transports_morning, label='morning')

    def plot_transport_evening(self, ax, color='b'):
        self.plot_transport(ax, color, self.transports_evening, label='evening')

    @property
    def str_stats(self):
        stats_string = f'id: {self.id}\n'
        stats_string += f'  - Number of workers: {self.num_workers}\n'
        stats_string += f'  - Number of domains: {self.num_domains}\n'
        stats_string += f'  - Number of transports morning: {self.num_transports_morning}\n'
        stats_string += f'  - Number of transports evening: {self.num_transports_evening}\n'
        return stats_string

    def __repr__(self):
        return f'Dataset({str(self.id)})'
