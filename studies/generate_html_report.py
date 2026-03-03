
import pandas as pd
import markdown
import os
import base64
from io import BytesIO
import matplotlib.pyplot as plt

# File Paths
REPORT_MD_PATH = 'studies/report.md'
PROCESS_LOG_PATH = 'Install/process.log'
CSV_PATH = 'studies/Demo/demo_results.csv'
OUTPUT_HTML_PATH = 'studies/report.html'

def read_file(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def process_log_to_html(log_content):
    html = '<div class="process-log">'
    lines = log_content.strip().split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('==='):
            html += f'<h3>{line}</h3>'
        elif line.startswith('['):
            html += f'<h4>{line}</h4>'
        elif line.startswith('-'):
            html += f'<div class="log-item">{line}</div>'
        else:
            html += f'<div class="log-line">{line}</div>'
    html += '</div>'
    return html

def generate_plot_image(df):
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Log10 Actual'], df['Log10 Predicted'], color='blue', alpha=0.6)
    plt.plot([df['Log10 Actual'].min(), df['Log10 Actual'].max()], 
             [df['Log10 Actual'].min(), df['Log10 Actual'].max()], 
             'r--', lw=2, label='Ideal Prediction')
    plt.xlabel('Log10 Actual kcat')
    plt.ylabel('Log10 Predicted kcat')
    plt.title('Actual vs Predicted kcat (Mock Features)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    img = BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

def get_mermaid_diagram():
    return """graph TD
    %% Styling
    classDef file fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef lib fill:#fff9c4,stroke:#fbc02d,stroke-width:2px
    classDef asset fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    classDef script fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef external fill:#eeeeee,stroke:#616161,stroke-width:1px,stroke-dasharray:5,5

    subgraph External
        HF["HuggingFace Hub (ProtT5 Model)"]:::external
        SK["Scikit-Learn (ExtraTreesRegressor)"]:::external
    end

    subgraph Assets
        Vocab["vocab.pkl"]:::asset
        TrfmWeights["trfm_12_23000.pkl"]:::asset
        Dataset["datasets/*.json"]:::asset
    end

    subgraph Lib
        BV["build_vocab.py"]:::lib
        PT["pretrain_trfm.py (SMILES Transformer)"]:::lib
        Utils["utils.py"]:::lib
        DatasetLib["dataset.py"]:::lib
    end

    subgraph Main
        Kcat["UniKP_kcat.py"]:::script
        Km["UniKP_Km.py"]:::script
        KcatKm["UniKP_kcat_Km.py"]:::script
    end
    
    subgraph Studies
        Demo["studies/Demo/demo_replicate.py"]:::file
        Report["studies/report.html"]:::file
        Results["demo_results.csv"]:::file
    end

    %% Data Flow
    Vocab --> BV
    TrfmWeights --> PT
    Dataset --> Kcat
    
    %% Imports & Usage
    BV --> Kcat
    PT --> Kcat
    Utils --> Kcat
    DatasetLib --> PT

    %% Logic Flow
    HF -.->|Download/Cache| Kcat
    Kcat -->|Train/Predict| SK
    
    %% Demo Replicates
    Kcat -.->|Replicated Logic| Demo
    Demo -->|Generates| Results
    Results --> Report"""

def main():
    # 1. Read Content
    report_md_content = read_file(REPORT_MD_PATH)
    process_log_content = read_file(PROCESS_LOG_PATH)
    
    # 2. Convert Markdown to simple HTML
    try:
        html_report_body = markdown.markdown(report_md_content, extensions=['tables'])
    except:
        html_report_body = f"<pre>{report_md_content}</pre>"

    # 3. Process Log
    html_process_log = process_log_to_html(process_log_content)

    # 4. Process CSV Data
    plot_image_base64 = ""
    table_html = ""
    try:
        df = pd.read_csv(CSV_PATH)
        # Create Table (First 10 rows)
        table_html = df.head(10).to_html(classes='data-table', index=False)
        # Create Plot
        plot_image_base64 = generate_plot_image(df)
    except Exception as e:
        table_html = f"<p>Error loading CSV data: {e}</p>"

    # 5. Build Final HTML
    full_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UniKP Replication Report</title>
    
    <!-- MathJax Configuration -->
    <script>
        MathJax = {{
            tex: {{
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
            }},
            svg: {{
                fontCache: 'global'
            }}
        }};
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>

    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ startOnLoad: true }});
    </script>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 1000px; margin: 0 auto; padding: 20px; background-color: #f9f9f9; }}
        h1, h2, h3 {{ color: #2c3e50; }}
        .container {{ background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-bottom: 20px; }}
        .header {{ text-align: center; margin-bottom: 30px; border-bottom: 2px solid #eaeaea; padding-bottom: 20px; }}
        .section {{ margin-bottom: 40px; }}
        
        /* Mermaid Diagram */
        .mermaid {{ text-align: center; margin: 30px 0; background: white; padding: 10px; border-radius: 5px; }}

        /* Process Log Styles */
        .process-log {{ background: #f0f4f8; padding: 15px; border-radius: 5px; border-left: 4px solid #3498db; font-family: monospace; }}
        .process-log h3 {{ color: #2980b9; margin-top: 20px; margin-bottom: 10px; border-bottom: 1px solid #dcdcdc; }}
        .process-log h4 {{ color: #34495e; margin: 10px 0 5px 0; }}
        .log-item {{ margin-left: 20px; margin-bottom: 4px; color: #555; }}
        
        /* Table Styles */
        .data-table {{ width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 0.9em; }}
        .data-table th, .data-table td {{ padding: 12px 15px; border: 1px solid #ddd; text-align: left; }}
        .data-table th {{ background-color: #3498db; color: white; font-weight: bold; }}
        .data-table tr:nth-child(even) {{ background-color: #f2f2f2; }}
        
        /* Plot Styles */
        .plot-container {{ text-align: center; margin: 20px 0; }}
        .plot-container img {{ max-width: 100%; border: 1px solid #ddd; border-radius: 4px; padding: 5px; }}

    </style>
</head>
<body>

    <div class="container">
        <div class="header">
            <h1>UniKP Replication Status Report</h1>
            <p>Generated automatically based on workspace replication tasks.</p>
        </div>

        <div class="section">
            <h2>1. Replication Process Execution</h2>
            <p>The following steps were automatically executed to set up the environment, resolve dependencies, and run the demo.</p>
            {html_process_log}
        </div>

        <div class="section">
            <h2>2. Codebase Architecture</h2>
            <p>The following diagram illustrates the interaction between the core library modules, assets, and the main execution scripts.</p>
            <div class="mermaid">
                {get_mermaid_diagram()}
            </div>
        </div>

        <div class="section">
            <h2>3. Methodology & Findings</h2>
            {html_report_body}
        </div>

        <div class="section">
            <h2>4. Demo Results Visualization</h2>
            <p>Below is a visualization of the predicted vs actual kcat values (Log10 scale) from the demo run.</p>
            <div class="plot-container">
                <img src="data:image/png;base64,{plot_image_base64}" alt="Prediction Plot">
                <p><em>Note: If Mock Features were used, low correlation is expected.</em></p>
            </div>
            
            <h3>Sample Data Output</h3>
            <p>First 10 rows from <code>studies/Demo/demo_results.csv</code>:</p>
            {table_html}
        </div>
    </div>

</body>
</html>
    """
    
    with open(OUTPUT_HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Report generated at: {OUTPUT_HTML_PATH}")

if __name__ == '__main__':
    main()
