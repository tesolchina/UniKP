# Prerequisites

[(Back to top)](#table-of-contents)

Notice:

- You need download pretrained protein language modoel *ProtT5-XL-UniRef50* to generate enzyme representation, the link is provided on [ProtT5-XL-U50](https://zenodo.org/records/4644188).
- You also need download model *UniKP* for ***k*`<sub>`cat`</sub>`, *K*`<sub>`m`</sub>`** and ***k*`<sub>`cat`</sub>` / *K*`<sub>`m`</sub>`** to predict corresponding kinetic parameters, the link is provided on [UniKP_model](https://huggingface.co/HanselYu/UniKP/tree/main).

**Place these two downloaded models in the UniKP directory.**

- We have included pretrained molecular language modoel *SMILES Transformer* in this repository to generate substrate representation, the link is also provided on [SMILES Transformer](https://github.com/DSPsleeporg/smiles-transformer).