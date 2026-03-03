import json

def search_json(filepath, query):
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    results = []
    print(f"Total entries: {len(data)}")
    for entry in data:
        s = str(entry).lower()
        if query.lower() in s:
            results.append(entry)
            if len(results) >= 5:
                break
    return results

filepath = 'datasets/Kcat_combination_0918_wildtype_mutant.json'
query = 'N-acetylglucosamine 2-epimerase'
res = search_json(filepath, query)
print(f"Found {len(res)} entries for '{query}':")
for r in res:
    print(r)

query2 = 'NeuAc synthase'
res2 = search_json(filepath, query2)
print(f"Found {len(res2)} entries for '{query2}':")
for r in res2:
    print(r)
