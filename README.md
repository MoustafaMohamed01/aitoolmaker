# AIToolMaker

**Build AI-powered tools, chatbots, and full websites instantly — no manual coding needed.**

AIToolMaker is a Python library that lets you **generate, customize, and run Streamlit AI apps or full HTML/CSS/JS websites** just by describing the tool you want and providing your LLM API key (e.g., Gemini, OpenAI, Anthropic).

Whether you want a chatbot, summarizer, SQL generator, or blog writer — AIToolMaker builds it automatically and can run it right away.

---

## Features

 - **Auto Code Generation** — Instantly create ready-to-run Streamlit code for AI tools.  
 - **Run Instantly** — Skip the code and just run your tool directly.  
 - **Website Export** — Generate full HTML/CSS/JS websites for your AI tools.  
 - **Plug in Any Model** — Works with Gemini, OpenAI, Anthropic, etc.  
 - **Smart Branding** — Add your own logo and name, or let AIToolMaker auto-brand your app.  
 - **Extensible** — Add your own custom tools and templates easily.

---

## How It Works

You describe the tool you want → AIToolMaker generates code or website files → you can run or publish instantly.

```python
from aitoolmaker import AIToolMaker

# Initialize the library with your API key and model
tool = AIToolMaker(
    api_key="YOUR_GEMINI_API_KEY",
    model="gemini-2.0-flash"
)

# Example 1: Generate a Streamlit chatbot code file
tool.create_tool(
    tool_type="chatbot",
    output="streamlit",
    run=False,
    name="MyChatBot",
    logo="logo.png"
)

# Example 2: Instantly run a blog generator app
tool.create_tool(
    tool_type="blog_generator",
    output="streamlit",
    run=True
)

# Example 3: Generate a full website version
tool.create_tool(
    tool_type="summarizer",
    output="website",
    run=False,
    name="SummaryPro"
)
````

You can also use it via CLI:

```bash
aitoolmaker create --tool chatbot --output streamlit --run --model gemini-2.0-flash
```

---

## Supported Tool Types (Initial Version)

* Chatbot
* Blog Generator
* CSV / Data Analyzer
* Document Summarizer
* Website Summarizer
* SQL Query Generator
* Code Explainer

*(You can add your own custom tool templates — the system is modular!)*

---

## Project Structure

```
aitoolmaker/
 ├── __init__.py
 ├── core/
 │   ├── generator.py
 │   ├── runners.py
 │   ├── templates/
 │   │   ├── streamlit/
 │   │   └── website/
 ├── tools/
 │   ├── chatbot.py
 │   ├── summarizer.py
 │   ├── blog_generator.py
 │   └── ...
 ├── utils/
 │   ├── branding.py
 │   ├── config_loader.py
 │   └── file_manager.py
 ├── logo/
 │   └── default_logo.png
 ├── setup.py
 └── README.md
```

---

## Installation

```bash
pip install aitoolmaker
```

Or install from source:

```bash
git clone https://github.com/MoustafaMohamed01/AIToolMaker.git
cd AIToolMaker
pip install -e .
```

---

## Configuration

You’ll need a valid **LLM API key**, for example:

```bash
export GEMINI_API_KEY="your_gemini_api_key"
```

Or directly in Python:

```python
tool = AIToolMaker(api_key="your_gemini_api_key", model="gemini-2.0-flash")
```

---

## Examples

### Generate and Run a Chatbot

```python
tool.create_tool("chatbot", output="streamlit", run=True)
```

### Generate a Summarizer Website

```python
tool.create_tool("summarizer", output="website", run=False, name="TextSummary")
```

### CLI Usage

```bash
aitoolmaker create --tool sql_generator --output website --model gemini-2.0-flash
```

---

## Use Cases

* Build internal AI dashboards with Streamlit instantly
* Create branded AI SaaS prototypes in minutes
* Auto-generate websites for AI tools (HTML/CSS/JS)
* Integrate with Gemini or OpenAI APIs for custom AI apps
* Teach AI development quickly in classrooms or tutorials

---

## Extending the Library

Add your own tools inside the `/tools/` directory.
Each tool must follow this structure:

```python
def build_tool(api_key, model, name, logo):
    # your tool logic here
    # should return Streamlit or HTML/JS code
```

Then register it in `/core/generator.py`.

---

## PyPI Metadata

**Package name:** `aitoolmaker`
**Author:** Moustafa Mohamed
**License:** MIT
**Python:** 3.10+
**Frameworks:** Streamlit, Jinja2, requests
**Version:** 0.1.0

---

## Contributing

Contributions are welcome!
To contribute:

1. Fork this repo
2. Create a new branch (`feature/your-feature`)
3. Commit your changes
4. Submit a pull request

---

## License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## Links

* **GitHub:** [https://github.com/MoustafaMohamed01/AIToolMaker](https://github.com/MoustafaMohamed01/AIToolMaker)
* **PyPI:** [https://pypi.org/project/aitoolmaker/](https://pypi.org/project/aitoolmaker/)
* **Author:** [Moustafa Mohamed](https://www.linkedin.com/in/moustafamohamed01/)

