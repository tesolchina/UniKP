
import os
from huggingface_hub import snapshot_download

def download_model():
    model_id = "HanselYu/UniKP"
    local_dir = "UniKP_model"
    
    if os.path.exists(local_dir):
        print(f"Directory {local_dir} already exists.")
        # Check if empty
        if os.listdir(local_dir):
            print(f"Directory {local_dir} is not empty. Skipping download.")
            return

    print(f"Downloading model {model_id} to {local_dir}...")
    try:
        snapshot_download(repo_id=model_id, local_dir=local_dir, local_dir_use_symlinks=False)
        print("Download complete.")
    except Exception as e:
        print(f"Error downloading model: {e}")

if __name__ == "__main__":
    download_model()
