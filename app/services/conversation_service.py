from collections import defaultdict
_data=defaultdict(list)
def get_history(cid): return list(_data.get(cid,[]))
def add_message(cid,role,content): _data[cid].append({'role':role,'content':content})
def delete_conversation(cid): _data.pop(cid,None)
