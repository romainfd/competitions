import numpy as np
from tqdm.notebook import tqdm as tqdm


class Worker(object):

    def __init__(self, worker_id, info):
        self.id = worker_id
        self.domain = info['domain']
        self.morning_options = info['morningOptions']
        self.evening_options = info['eveningOptions']
        self.morning_transport_set = set([transport_id for option in self.morning_options for transport_id in option])
        self.evening_transport_set = set([transport_id for option in self.evening_options for transport_id in option])
        self.best_morning_option = -1
        self.best_evening_option = -1
        self.selected = False

    def select(self):
        self.selected = True

    def score(self, transport_morning_dic, transport_evening_dic):
        return self.score_morning(transport_morning_dic) + self.score_evening(transport_evening_dic)

    def score_aux(self, options, transport_dic):
        best_option = -1
        best_score = np.inf
        for i, option in enumerate(options):
            score = sum(map(lambda x: transport_dic[x].score, option))
            if score < best_score:
                best_score = score
                best_option = i
        return best_option, best_score

    def score_morning(self, transport_morning_dic):
        self.best_morning_option, score = self.score_aux(self.morning_options, transport_morning_dic)
        return score

    def score_evening(self, transport_evening_dic):
        self.best_evening_option, score = self.score_aux(self.evening_options, transport_evening_dic)
        return score

    def add_transport_to_dic(self, dic_morning, dic_evening):
        for transports in self.morning_options:
            for transport_id in transports:
                if transport_id not in dic_morning:
                    dic_morning[transport_id] = Transport(transport_id, True)
                dic_morning[transport_id].add_potential_worker(self.id)

        for transports in self.evening_options:
            for transport_id in transports:
                if transport_id not in dic_evening:
                    dic_evening[transport_id] = Transport(transport_id, False)
                dic_evening[transport_id].add_potential_worker(self.id)

    def __repr__(self):
        return str(self.id)

    def update_transports(self, transports_morning_dic, transports_evening_dic):
        morning_transports_remove_ids = self.morning_transport_set
        evening_transports_remove_ids = self.evening_transport_set
        if self.selected:
            morning_transports_remove_ids.difference_update(self.morning_options[self.best_morning_option])
            evening_transports_remove_ids.difference_update(self.evening_options[self.best_evening_option])
            for transport_id in self.morning_options[self.best_morning_option]:
                transports_morning_dic[transport_id].nb_actual_users += 1
            for transport_id in self.evening_options[self.best_evening_option]:
                transports_evening_dic[transport_id].nb_actual_users += 1
        self.update_transport_aux(transports_morning_dic, morning_transports_remove_ids)
        self.update_transport_aux(transports_evening_dic, evening_transports_remove_ids)

    def update_transport_aux(self, transports_dic, transports_remove_ids):

        for transports_remove_id in transports_remove_ids:
            transports_dic[transports_remove_id].remove_potential_worker(self.id)


class Transport(object):

    def __init__(self, id, is_morning):
        self.id = id
        self.is_morning = is_morning
        self.potential_users_id = set()
        self.nb_actual_users = 0

    def add_potential_worker(self, user_id):
        self.potential_users_id.add(user_id)

    def remove_potential_worker(self, user_id):
        self.potential_users_id.remove(user_id)

    @property
    def score(self):
        return len(self.potential_users_id) + self.nb_actual_users ** 2

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
    def num_workers_to_choose(self):
        return sum(self.quotas.values())

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

    def solution(self, loop_gap=1):
        nb_workers_to_choose = self.num_workers_to_choose
        solution = []
        pbar = tqdm(total=nb_workers_to_choose)
        while len(self.domain_worker_dic) > 0:
            domain_complete = set()
            if loop_gap == -1:
                loop_gap_ = min(max(int(10. ** (self.num_workers / 10000)), 1), 200)
            else:
                loop_gap_ = loop_gap

            if loop_gap_ == 1:
                workers_ids = [min(self.workers,
                                   key=lambda worker_id_: self.workers[worker_id_].score(self.transports_morning,
                                                                                         self.transports_evening))]

            else:
                workers_ids = sorted(self.workers,
                                     key=lambda worker_id_: self.workers[worker_id_].score(self.transports_morning,
                                                                                           self.transports_evening))[
                              :loop_gap_]
            for worker_id in workers_ids:
                worker = self.workers[worker_id]

                # don't add worker if quota is already met
                if self.quotas[worker.domain] == 0:
                    # update worker transports (he won't take any)
                    worker.update_transports(self.transports_morning, self.transports_evening)

                    del self.workers[worker_id]
                    continue

                morning_option = worker.best_morning_option
                evening_option = worker.best_evening_option
                solution.append({'name': worker_id, 'morningOptionIndex': morning_option,
                                 'eveningOptionIndex': evening_option})
                worker.select()

                # update transports which won't be taken by worker
                worker.update_transports(self.transports_morning, self.transports_evening)
                self.quotas[worker.domain] -= 1
                if self.quotas[worker.domain] == 0:
                    domain_complete.add(worker.domain)

                del self.workers[worker_id]
                pbar.update(1)

            for domain in domain_complete:
                for worker_id in self.domain_worker_dic[domain]:
                    if worker_id in self.workers:
                        self.workers[worker_id].update_transports(self.transports_morning, self.transports_evening)
                        del self.workers[worker_id]
                del self.domain_worker_dic[domain]

            pbar.set_description("w.: %d | dom.: %d | gap: %d" %
                                 (self.num_workers, len(self.domain_worker_dic), loop_gap_))

        return solution

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
        ax.set_xticklabels(transports.values(), rotation='vertical', fontsize='medium')

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
