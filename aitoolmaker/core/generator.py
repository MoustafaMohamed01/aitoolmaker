import os
import shutil
from pathlib import Path
from jinja2 import Template
from .templates import get_template

class ToolGenerator:
    """Generates Streamlit apps and websites for AI tools."""
    
    def __init__(self, api_key: str, model: str, api_provider: str = "gemini"):
        """
        Initialize the ToolGenerator.
        
        Args:
            api_key (str): API key for the AI service
            model (str): Model name to use
            api_provider (str): API provider (gemini, openai, anthropic)
        """
        self.api_key = api_key
        self.model = model
        self.api_provider = api_provider
        
    def generate_streamlit_tool(
        self, 
        tool_type: str, 
        name: str, 
        logo_path: str, 
        output_dir: str = None
    ):
        """
        Generate a complete Streamlit application for the specified tool.
        
        Args:
            tool_type (str): Type of tool to generate
            name (str): Name of the tool
            logo_path (str): Path to logo file
            output_dir (str): Output directory for generated files
            
        Returns:
            dict: Information about generated files
        """
        # Set default output directory
        if output_dir is None:
            output_dir = f"./generated_{tool_type}"
        
        # Create output directory
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Get the appropriate template
        template_content = get_template(tool_type, "streamlit")
        
        # Prepare template variables
        template_vars = {
            "api_key": self.api_key,
            "model": self.model,
            "tool_name": name,
            "logo_path": logo_path
        }
        
        # Render the main app file
        template = Template(template_content)
        rendered_code = template.render(**template_vars)
        
        # Write app.py
        app_file = output_path / "app.py"
        with open(app_file, "w", encoding="utf-8") as f:
            f.write(rendered_code)
        
        # Create api_key.py
        api_key_file = output_path / "api_key.py"
        api_key_content = self._generate_api_key_file()
        with open(api_key_file, "w", encoding="utf-8") as f:
            f.write(api_key_content)
        
        # Copy utility files if needed
        if tool_type == "document_summarizer":
            utils_content = get_template(tool_type, "utils")
            utils_file = output_path / "utils.py"
            utils_template = Template(utils_content)
            utils_rendered = utils_template.render(**template_vars)
            with open(utils_file, "w", encoding="utf-8") as f:
                f.write(utils_rendered)
        
        # Create requirements.txt
        requirements_file = output_path / "requirements.txt"
        requirements = self._generate_requirements(tool_type)
        with open(requirements_file, "w", encoding="utf-8") as f:
            f.write(requirements)
        
        # Copy logo if provided
        if logo_path and os.path.exists(logo_path):
            logo_dest = output_path / "logo.png"
            shutil.copy(logo_path, logo_dest)
        
        # Create README
        readme_file = output_path / "README.md"
        readme_content = self._generate_readme(tool_type, name)
        with open(readme_file, "w", encoding="utf-8") as f:
            f.write(readme_content)
        
        print(f"✅ {name} generated successfully at: {output_path.absolute()}")
        
        return {
            "output_dir": str(output_path.absolute()),
            "app_path": str(app_file.absolute()),
            "files": [
                "app.py",
                "api_key.py", 
                "requirements.txt",
                "README.md"
            ]
        }
    
    def generate_website(
        self, 
        tool_type: str, 
        name: str, 
        logo_path: str, 
        output_dir: str = None
    ):
        """
        Generate a standalone HTML/CSS/JS website for the tool.
        
        Args:
            tool_type (str): Type of tool to generate
            name (str): Name of the tool
            logo_path (str): Path to logo file
            output_dir (str): Output directory for generated files
            
        Returns:
            dict: Information about generated files
        """
        # Set default output directory
        if output_dir is None:
            output_dir = f"./generated_{tool_type}_website"
        
        # Create output directory structure
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories
        (output_path / "css").mkdir(exist_ok=True)
        (output_path / "js").mkdir(exist_ok=True)
        (output_path / "assets").mkdir(exist_ok=True)
        
        # Get templates
        html_template = get_template(tool_type, "html")
        css_template = get_template(tool_type, "css")
        js_template = get_template(tool_type, "js")
        
        # Prepare template variables
        template_vars = {
            "api_key": self.api_key,
            "model": self.model,
            "tool_name": name,
            "logo_path": "assets/logo.png" if logo_path else ""
        }
        
        # Render and write HTML
        html_content = Template(html_template).render(**template_vars)
        with open(output_path / "index.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        
        # Render and write CSS
        css_content = Template(css_template).render(**template_vars)
        with open(output_path / "css" / "style.css", "w", encoding="utf-8") as f:
            f.write(css_content)
        
        # Render and write JavaScript
        js_content = Template(js_template).render(**template_vars)
        with open(output_path / "js" / "app.js", "w", encoding="utf-8") as f:
            f.write(js_content)
        
        # Copy logo if provided
        if logo_path and os.path.exists(logo_path):
            logo_dest = output_path / "assets" / "logo.png"
            shutil.copy(logo_path, logo_dest)
        
        # Create README
        readme_file = output_path / "README.md"
        readme_content = self._generate_website_readme(tool_type, name)
        with open(readme_file, "w", encoding="utf-8") as f:
            f.write(readme_content)
        
        print(f"✅ {name} website generated successfully at: {output_path.absolute()}")
        
        return {
            "output_dir": str(output_path.absolute()),
            "index_path": str((output_path / "index.html").absolute()),
            "files": [
                "index.html",
                "css/style.css",
                "js/app.js",
                "README.md"
            ]
        }
    
    def _generate_api_key_file(self):
        """Generate api_key.py content."""
        if self.api_provider == "gemini":
            return f"GEMINI_API_KEY = '{self.api_key}'\n"
        elif self.api_provider == "openai":
            return f"OPENAI_API_KEY = '{self.api_key}'\n"
        else:
            return f"API_KEY = '{self.api_key}'\n"
    
    def _generate_requirements(self, tool_type: str):
        """Generate requirements.txt based on tool type."""
        base_requirements = [
            "streamlit>=1.28.0",
            "google-generativeai>=0.3.0"
        ]
        
        tool_specific = {
            "data_analyzer": ["pandas>=2.0.0"],
            "document_summarizer": [
                "langchain>=0.1.0",
                "langchain-google-genai>=0.0.6",
                "langchain-community>=0.0.13",
                "pypdf>=3.17.0",
                "python-docx>=1.0.0",
                "faiss-cpu>=1.7.4"
            ],
            "web_summarizer": [
                "requests>=2.31.0",
                "beautifulsoup4>=4.12.0"
            ]
        }
        
        requirements = base_requirements.copy()
        if tool_type in tool_specific:
            requirements.extend(tool_specific[tool_type])
        
        return "\n".join(requirements) + "\n"
    
    def _generate_readme(self, tool_type: str, name: str):
        """Generate README.md for Streamlit app."""
        return f"""# {name}

## Description
This is an AI-powered {tool_type.replace('_', ' ')} generated by AIToolMaker.

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Update your API key in `api_key.py`

## Usage

Run the application:
```bash
streamlit run app.py
```

## Features
- Built with Streamlit
- Powered by {self.model}
- Easy to customize and extend

## Generated by AIToolMaker
This tool was automatically generated using the AIToolMaker library.
"""
    
    def _generate_website_readme(self, tool_type: str, name: str):
        """Generate README.md for website."""
        return f"""# {name} - Standalone Website

## Description
This is a standalone HTML/CSS/JS website for an AI-powered {tool_type.replace('_', ' ')}.

## Usage

Simply open `index.html` in a web browser or deploy to any web hosting service.

## Deployment Options
- **GitHub Pages**: Push to a GitHub repository and enable Pages
- **Netlify**: Drag and drop the folder to Netlify
- **Vercel**: Deploy via Vercel CLI or web interface
- **Any static hosting**: Upload files via FTP

## Files Structure
```
├── index.html          # Main HTML file
├── css/
│   └── style.css      # Stylesheet
├── js/
│   └── app.js         # JavaScript logic
├── assets/
│   └── logo.png       # Logo image
└── README.md          # This file
```

## Features
- No backend required
- Mobile responsive
- Modern UI/UX
- Powered by {self.model}

## Generated by AIToolMaker
This website was automatically generated using the AIToolMaker library.
"""
