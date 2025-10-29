# AIToolMaker
[![PyPI version](https://badge.fury.io/py/aitoolmaker.svg)](https://badge.fury.io/py/aitoolmaker)
[![PyPI version](https://img.shields.io/pypi/v/datacmp.svg)](https://pypi.org/project/datacmp/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**AIToolMaker** is a powerful Python framework that automatically generates and runs Streamlit-based AI tools and chatbots, or exports them as full HTML/CSS/JS websites.

* **PyPI** : https://pypi.org/project/aitoolmaker/

## Features

- **Instant Tool Generation**: Create AI-powered tools with a single command
- **Multiple Output Formats**: Generate Streamlit apps or standalone websites
- **6 Pre-built Tools**: Chatbot, Blog Generator, Data Analyzer, SQL Generator, Document Summarizer, Web Summarizer
- **Run Immediately**: Option to run tools instantly without exporting code
- **Auto-branding**: Automatic name and logo generation
- **Multi-API Support**: Works with Gemini, OpenAI, and Anthropic APIs

## Installation

```bash
pip install aitoolmaker
```

Or install from source:

```bash
git clone https://github.com/MoustafaMohamed01/aitoolmaker.git
cd aitoolmaker
pip install -e .
```

## Quick Start

### Python API

```python
from aitoolmaker import AIToolMaker

# Initialize
tool = AIToolMaker(
    api_key="YOUR_GEMINI_API_KEY",
    model="gemini-2.0-flash"
)

# Generate and run a chatbot
tool.create_tool(
    tool_type="chatbot",
    output="streamlit",
    run=True,
    name="My AI Assistant"
)
```

### Command Line

```bash
# Create a blog generator
aitoolmaker create --tool blog_generator --api-key YOUR_KEY --output streamlit

# Create and run immediately
aitoolmaker create --tool chatbot --api-key YOUR_KEY --run

# Generate a website
aitoolmaker create --tool sql_generator --api-key YOUR_KEY --output website
```

## Available Tools

| Tool                    | Description                                         |
| ----------------------- | --------------------------------------------------- |
| **chatbot**             | Professional AI assistant with conversation history |
| **blog_generator**      | AI-powered blog writer with keyword optimization    |
| **data_analyzer**       | Ask questions about CSV data using AI               |
| **sql_generator**       | Generate SQL queries from natural language          |
| **document_summarizer** | Summarize PDF and Word documents                    |
| **web_summarizer**      | Summarize website content                           |

## Usage Examples

### Generate Multiple Tools

```python
from aitoolmaker import AIToolMaker

api_key = "YOUR_API_KEY"
tools = ["chatbot", "blog_generator", "sql_generator"]

for tool_type in tools:
    maker = AIToolMaker(api_key=api_key, model="gemini-2.0-flash")
    result = maker.create_tool(
        tool_type=tool_type,
        output="streamlit",
        output_dir=f"./generated_{tool_type}"
    )
    print(f"{tool_type} created at {result['output_dir']}")
```

### Custom Branding

```python
from aitoolmaker import AIToolMaker

maker = AIToolMaker(api_key="YOUR_KEY", model="gemini-2.0-flash")

result = maker.create_tool(
    tool_type="data_analyzer",
    output="streamlit",
    name="DataMaster Pro",
    logo="./my_logo.png",
    output_dir="./my_data_tool"
)
```

### Generate Website

```python
from aitoolmaker import AIToolMaker

maker = AIToolMaker(api_key="YOUR_KEY", model="gemini-2.0-flash")

result = maker.create_tool(
    tool_type="sql_generator",
    output="website",
    name="SQL Wizard",
    output_dir="./sql_website"
)
```

## CLI Usage

### List Available Tools

```bash
aitoolmaker list
```

### Get Tool Information

```bash
aitoolmaker info chatbot
```

### Create Tool with Options

```bash
aitoolmaker create \
  --tool document_summarizer \
  --api-key YOUR_KEY \
  --model gemini-2.0-flash \
  --name "DocSummarizer Pro" \
  --logo ./logo.png \
  --output-dir ./my_summarizer
```

## Generated Output Structure

### Streamlit App

```
generated_chatbot/
├── app.py              # Main Streamlit application
├── api_key.py          # API key configuration
├── requirements.txt    # Python dependencies
├── README.md           # Usage instructions
└── utils.py            # Utility functions (if needed)
```

### Website

```
generated_chatbot_website/
├── index.html          # Main HTML file
├── css/
│   └── style.css       # Stylesheet
├── js/
│   └── app.js          # JavaScript logic
├── assets/
│   └── logo.png        # Logo image
└── README.md           # Deployment instructions
```

## Use Cases

- **Rapid Prototyping**: Quickly create AI tool prototypes
- **Client Demos**: Generate custom-branded demos
- **Internal Tools**: Build internal AI tools for teams
- **Learning**: Study production-ready AI code
- **Deployment**: Export portable, deployment-ready code

## Contributing

Contributions are welcome! To add a new tool:

1. Create a template file in `core/templates/your_tool.py`
2. Define the template constant
3. Register it in `core/templates/__init__.py`
4. Update `SUPPORTED_TOOLS` in `__init__.py`

## License

MIT License - See LICENSE file for details

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Google Gemini](https://deepmind.google/technologies/gemini/)

## Support

- **Issues**: [GitHub Issues](https://github.com/MoustafaMohamed01/aitoolmaker/issues)
- **Email**: moustafamohmd5@gmail.com

---

Made by the **Moustafa Mohamed**

- **Linkedin** [Moustafa Mohamed](https://www.linkedin.com/in/moustafamohamed01/)
- **Github** [MoustafaMohamed01](https://github.com/MoustafaMohamed01)
- **Kaggle** [moustafamohamed01](https://www.kaggle.com/moustafamohamed01)
