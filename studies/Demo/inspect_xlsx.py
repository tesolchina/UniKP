import pandas as pd

try:
    df = pd.read_excel('datasets/kcat_km_samples.xlsx')
    print("Columns:", df.columns)
    print("Shape:", df.shape)
    print("First few rows:")
    print(df.head())
    
    # Search for NeuAc or epimerase in string columns
    query = 'NeuAc'
    mask = df.apply(lambda x: x.astype(str).str.contains(query, case=False)).any(axis=1)
    if mask.any():
        print(f"Found {mask.sum()} entries for '{query}'")
        print(df[mask].head())
    else:
        print(f"No entries for '{query}'")

    query = 'epimerase'
    mask = df.apply(lambda x: x.astype(str).str.contains(query, case=False)).any(axis=1)
    if mask.any():
        print(f"Found {mask.sum()} entries for '{query}'")
        print(df[mask].head())
    else:
        print(f"No entries for '{query}'")

except Exception as e:
    print(f"Error: {e}")
