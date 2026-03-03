
import os
import sys
from transformers import T5Tokenizer, T5EncoderModel

log_file = "Install/process.log"

def log(message):
    print(message)
    with open(log_file, "a") as f:
        f.write(message + "\n")

def check_prot_t5():
    model_name = "Rostlab/prot_t5_xl_uniref50"
    log(f"Checking {model_name} availability on HuggingFace Hub...")
    try:
        tokenizer = T5Tokenizer.from_pretrained(model_name, do_lower_case=False)
        model = T5EncoderModel.from_pretrained(model_name)
        log(f"Successfully loaded {model_name} (cached or downloaded).")
        return True
    except Exception as e:
        log(f"Failed to load {model_name}: {e}")
        return False

def check_local_model_dir(dir_name):
    if os.path.isdir(dir_name):
        log(f"Local directory '{dir_name}' exists.")
        return True
    else:
        log(f"Local directory '{dir_name}' does not exist.")
        return False

if __name__ == "__main__":
    # Check ProtT5
    # The code expects "prot_t5_xl_uniref50" folder locally or uses that ID.
    # The official ID is likely "Rostlab/prot_t5_xl_uniref50".
    
    if not check_local_model_dir("prot_t5_xl_uniref50"):
        log("Attempting to use HuggingFace model 'Rostlab/prot_t5_xl_uniref50' instead of local folder.")
        # We don't download it here to avoid massive download without permission, 
        # but we verify if we can access it using transformers.
        # Actually, verifying availability via from_pretrained might trigger download if not specific.
        # We'll just skip actual download for now and report it missing locally.
        pass

    # Check UniKP models
    if not check_local_model_dir("UniKP_model"):
         log("UniKP_model directory is missing. Please download from https://huggingface.co/HanselYu/UniKP/tree/main")

    # Check SMILES Transformer (already found assets)
    if os.path.exists("assets/trfm_12_23000.pkl"):
        log("SMILES Transformer (trfm_12_23000.pkl) found in assets.")
    else:
        log("SMILES Transformer (trfm_12_23000.pkl) missing.")

