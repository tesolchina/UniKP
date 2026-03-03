import json
import traceback

def search_json(filepath, query):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return []
    
    results = []
    print(f"Total entries: {len(data)}")
    for entry in data:
        s = str(entry).lower()
        if query.lower() in s:
            results.append(entry)
            if len(results) >= 5:
                break
    return results

if __name__ == '__main__':
    filepath = 'datasets/Kcat_combination_0918_wildtype_mutant.json'
    
    # Search for NeuAc
    query = 'NeuAc'
    print(f"Searching for '{query}'...")
    res = search_json(filepath, query)
    print(f"Found {len(res)} entries for '{query}'")
    for r in res:
        print(r)

    # Search for epimerase
    query = 'epimerase'
    print(f"Searching for '{query}'...")
    res = search_json(filepath, query)
    print(f"Found {len(res)} entries for '{query}'")
    for r in res:
        print(r)
