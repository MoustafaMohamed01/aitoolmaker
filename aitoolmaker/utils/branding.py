import os
from pathlib import Path


class BrandingManager:
    """Manages branding for generated tools."""
    
    DEFAULT_NAMES = {
        "chatbot": "AI Assistant Pro",
        "blog_generator": "Blog AI Assistant",
        "data_analyzer": "AI CSV Data Analyzer",
        "sql_generator": "SQL Query Generator",
        "document_summarizer": "PDF & Word Document Summarizer",
        "web_summarizer": "Website Summarizer"
    }
    
    def __init__(self):
        """Initialize BrandingManager."""
        self.logo_dir = Path(__file__).parent.parent / "logo"
        self.logo_dir.mkdir(exist_ok=True)
        
    def apply_branding(self, tool_type: str, name: str = None, logo: str = None):
        """
        Apply branding to a tool.
        
        Args:
            tool_type (str): Type of tool
            name (str): Custom name (optional)
            logo (str): Path to custom logo (optional)
            
        Returns:
            tuple: (final_name, final_logo_path)
        """
        # Use provided name or default
        final_name = name if name else self.DEFAULT_NAMES.get(tool_type, "AI Tool")
        
        # Use provided logo or default
        if logo and os.path.exists(logo):
            final_logo_path = logo
        else:
            # Use default logo if it exists
            default_logo = self.logo_dir / "default_logo.png"
            final_logo_path = str(default_logo) if default_logo.exists() else None
        
        return final_name, final_logo_path
    
    def get_default_name(self, tool_type: str):
        """Get default name for a tool type."""
        return self.DEFAULT_NAMES.get(tool_type, "AI Tool")
    
    def create_default_logo(self):
        """
        Create a simple default logo.
        This is a placeholder - in production, you'd have actual logo files.
        """
        # Placeholder for logo creation logic
        # In a real implementation, you might use PIL to create a simple logo
        pass
