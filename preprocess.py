
from previous_pairs import previous_pairs

def initialize_dicts(full_list):
    candidates = {}

    user_list = [user.get_username() for user in full_list]

    # prepare potential matches list
    for user in user_list:
        candidates[user] = user_list.copy()
        # remove self from possible candidaes
        candidates[user].remove(user)

        #if user in previous_pairs.keys():
        #    orig_set = set(candidates[user])
        #    remove_set = set(previous_pairs[user])
        #    candidates[user] = list(orig_set - remove_set)

    return candidates

def create_object_list(participants, ss_map):
    participant_map = {}
    for p in participants:
        participant_map[p.get_username()] = p

    ss_list = [(key, value) for key, value in ss_map.items()]
    
    ss_object_list = []
    for (santa, recp) in ss_list:
        ss_object_list.append((participant_map[santa], participant_map[recp]))
    
    return ss_object_list