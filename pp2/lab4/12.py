import json

def serialize(val):
    if val == "<missing>": return "<missing>"
    return json.dumps(val, separators=(',', ':'))

def deep_diff(o1, o2, path=""):
    differences = []
    keys = set()
    if isinstance(o1, dict): keys.update(o1.keys())
    if isinstance(o2, dict): keys.update(o2.keys())
    
    for key in sorted(keys):
        new_path = f"{path}.{key}" if path else key
        val1 = o1.get(key, "<missing>") if isinstance(o1, dict) else "<missing>"
        val2 = o2.get(key, "<missing>") if isinstance(o2, dict) else "<missing>"
        
        if isinstance(val1, dict) and isinstance(val2, dict):
            differences.extend(deep_diff(val1, val2, new_path))
        elif val1 != val2:
            differences.append(f"{new_path} : {serialize(val1)} -> {serialize(val2)}")
    return differences

obj1 = json.loads(input())
obj2 = json.loads(input())
diffs = deep_diff(obj1, obj2)
if diffs:
    for d in sorted(diffs): print(d)
else:
    print("No differences")