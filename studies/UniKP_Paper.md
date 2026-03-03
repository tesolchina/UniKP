# UniKP: a unified framework for the prediction of enzyme kinetic parameters

**DOI**: [10.1038/s41467-023-44113-1](https://doi.org/10.1038/s41467-023-44113-1)

## Abstract
Prediction of enzyme kinetic parameters is essential for designing and optimizing enzymes for various biotechnological and industrial applications, but the limited performance of current prediction tools on diverse tasks hinders their practical applications. UniKP is a unified framework based on pretrained language models for the prediction of enzyme kinetic parameters, including enzyme turnover number ($k_{cat}$), Michaelis constant ($K_m$), and catalytic efficiency ($k_{cat}/K_m$), from protein sequences and substrate structures. A two-layer framework derived from UniKP (EF-UniKP) has also been proposed to allow robust $k_{cat}$ prediction in considering environmental factors, including pH and temperature. In addition, four representative re-weighting methods are systematically explored to successfully reduce the prediction error in high-value prediction tasks. UniKP demonstrates application in several enzyme discovery and directed evolution tasks, leading to the identification of new enzymes and enzyme mutants with higher activity.

## Key Findings
- **Unified Prediction**: UniKP successfully predicts multiple kinetic parameters ($k_{cat}$, $K_m$, $k_{cat}/K_m$) using a consistent framework.
- **Environmental Factors**: The EF-UniKP variant incorporates environmental context (pH and temperature) to improve $k_{cat}$ prediction accuracy under specific conditions.
- **High-Value Prediction**: The framework employs re-weighting methods to enhance performance on high-value prediction tasks where data might be sparse or imbalanced.
- **Practical Application**: The tool has been validated in real-world scenarios, aiding in the discovery and engineering of enzymes with improved properties.

## Methods & Framework
The UniKP framework utilizes the power of pretrained language models to generate rich representations of biological entities:
- **Protein Representation**: Uses the **ProtT5-XL-UniRef50** model to embed enzyme protein sequences.
- **Substrate Representation**: Uses the **SMILES Transformer** model to embed substrate chemical structures.
- **Model Architecture**: These representations are combined to train predictive models for kinetic parameters.
- **EF-UniKP**: A two-layer extension that integrates environmental factors (pH and temperature) into the prediction pipeline for more context-aware $k_{cat}$ estimation.

## Specific Use Cases

### 1. High-efficiency NeuAc Biosynthesis
- **Goal**: Improve the biosynthesis of N-acetylneuraminic acid (NeuAc).
- **Enzymes**: N-acetylglucosamine 2-epimerase (AGE) and NeuAc synthase (NeuB).
- **Application**: UniKP was used to mine for enzymes with higher $k_{cat}$ values to enhance the efficiency of the biosynthetic pathway.

### 2. GABA Production at Neutral pH
- **Goal**: Enable the production of Gamma-aminobutyric acid (GABA) from monosodium glutamate (MSG) at neutral pH.
- **Enzyme**: Glutamate decarboxylase.
- **Application**: The tool assisted in enzyme evolution strategies to find variants that are active and stable at neutral pH, a condition often preferred for industrial fermentation but challenging for natural glutamate decarboxylases which typically work at acidic pH.

### 3. De novo Biosynthesis of 10-hydroxy-2-decenoic acid
- **Goal**: Establish the biosynthesis of Queen Bee Acid (10-hydroxy-2-decenoic acid) in *Escherichia coli*.
- **Enzyme**: CYP153AMaq (a cytochrome P450 monooxygenase).
- **Application**: UniKP facilitated the evolution of the enzyme to improve its kinetic properties ($k_{cat}/K_m$) for the target reaction, enabling efficient production in a heterologous host.
