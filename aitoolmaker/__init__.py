"""
AIToolMaker - A Framework for Generating AI-Powered Tools
=========================================================

AIToolMaker automatically generates and runs Streamlit-based AI tools and chatbots.

Usage:
    from aitoolmaker import AIToolMaker
    
    tool = AIToolMaker(
        api_key="YOUR_GEMINI_API_KEY",
        model="gemini-2.0-flash"
    )
    
    tool.create_tool(
        tool_type="chatbot",
        output="streamlit",
        run=True,
        name="My AI Assistant"
    )
"""

__version__ = "1.0.0"
__author__ = "AIToolMaker Team"
__license__ = "MIT"

from .core.generator import ToolGenerator
from .core.runners import StreamlitRunner
from .utils.branding import BrandingManager

class AIToolMaker:
    """
    Main class for AIToolMaker library.
    
    This class provides a simple interface to generate and run AI-powered tools.
    """
    
    SUPPORTED_TOOLS = [
        "chatbot",
        "blog_generator", 
        "data_analyzer",
        "sql_generator",
        "document_summarizer",
        "web_summarizer"
    ]
    
    SUPPORTED_OUTPUTS = ["streamlit", "website"]
    
    def __init__(self, api_key: str, model: str = "gemini-2.0-flash", api_provider: str = "gemini"):
        """
        Initialize AIToolMaker.
        
        Args:
            api_key (str): API key for the AI model (Gemini, OpenAI, etc.)
            model (str): Model name to use (default: gemini-2.0-flash)
            api_provider (str): API provider - 'gemini', 'openai', or 'anthropic' (default: gemini)
        """
        if not api_key:
            raise ValueError("API key is required")
        
        self.api_key = api_key
        self.model = model
        self.api_provider = api_provider.lower()
        
        self.generator = ToolGenerator(api_key, model, api_provider)
        self.runner = StreamlitRunner()
        self.branding = BrandingManager()
        
    def create_tool(
        self,
        tool_type: str,
        output: str = "streamlit",
        run: bool = False,
        name: str = None,
        logo: str = None,
        output_dir: str = None
    ):
        """
        Create an AI tool.
        
        Args:
            tool_type (str): Type of tool to create (chatbot, blog_generator, etc.)
            output (str): Output format - 'streamlit' or 'website' (default: streamlit)
            run (bool): Whether to run the tool immediately (default: False)
            name (str): Custom name for the tool (optional)
            logo (str): Path to custom logo (optional)
            output_dir (str): Directory to save generated files (optional)
            
        Returns:
            str: Path to generated files or status message
        """
        # Validate inputs
        if tool_type not in self.SUPPORTED_TOOLS:
            raise ValueError(
                f"Unsupported tool type: {tool_type}. "
                f"Supported types: {', '.join(self.SUPPORTED_TOOLS)}"
            )
        
        if output not in self.SUPPORTED_OUTPUTS:
            raise ValueError(
                f"Unsupported output format: {output}. "
                f"Supported formats: {', '.join(self.SUPPORTED_OUTPUTS)}"
            )
        
        # Apply branding
        name, logo_path = self.branding.apply_branding(tool_type, name, logo)
        
        # Generate the tool
        if output == "streamlit":
            result = self.generator.generate_streamlit_tool(
                tool_type, name, logo_path, output_dir
            )
            
            if run:
                print(f"Running {name}...")
                self.runner.run_tool(result["app_path"])
                return f"Tool running at {result['app_path']}"
            else:
                return result
        
        elif output == "website":
            result = self.generator.generate_website(
                tool_type, name, logo_path, output_dir
            )
            return result
    
    def list_tools(self):
        """List all available tool types."""
        return self.SUPPORTED_TOOLS
    
    def get_tool_info(self, tool_type: str):
        """
        Get information about a specific tool type.
        
        Args:
            tool_type (str): The tool type to get info about
            
        Returns:
            dict: Tool information including description and requirements
        """
        tool_descriptions = {
            "chatbot": {
                "name": "AI Chatbot Assistant",
                "description": "Professional AI chatbot with conversation history",
                "features": ["Streaming responses", "Download conversations", "Professional persona"]
            },
            "blog_generator": {
                "name": "AI Blog Writer",
                "description": "Generate well-structured blog posts with AI",
                "features": ["Keyword optimization", "Word count control", "Markdown export"]
            },
            "data_analyzer": {
                "name": "CSV Data Analyzer", 
                "description": "Ask questions about your CSV data using AI",
                "features": ["CSV upload", "Natural language queries", "Data insights"]
            },
            "sql_generator": {
                "name": "SQL Query Generator",
                "description": "Generate SQL queries from natural language",
                "features": ["Multiple SQL dialects", "Query explanations", "Expected output preview"]
            },
            "document_summarizer": {
                "name": "Document Summarizer",
                "description": "Summarize PDF and Word documents using AI",
                "features": ["PDF support", "DOCX support", "Intelligent summarization"]
            },
            "web_summarizer": {
                "name": "Website Summarizer",
                "description": "Summarize website content using AI",
                "features": ["URL scraping", "Markdown output", "Download summaries"]
            }
        }
        
        if tool_type in tool_descriptions:
            return tool_descriptions[tool_type]
        else:
            return None


__all__ = ['AIToolMaker']
