from .chatbot import CHATBOT_TEMPLATE
from .blog_generator import BLOG_GENERATOR_TEMPLATE
from .data_analyzer import DATA_ANALYZER_TEMPLATE
from .sql_generator import SQL_GENERATOR_TEMPLATE
from .document_summarizer import DOCUMENT_SUMMARIZER_TEMPLATE, DOCUMENT_UTILS_TEMPLATE
from .web_summarizer import WEB_SUMMARIZER_TEMPLATE
from .web_templates import get_html_template, get_css_template, get_js_template


def get_template(tool_type: str, format_type: str = "streamlit"):
    """
    Get the appropriate template for a tool.
    
    Args:
        tool_type (str): Type of tool (chatbot, blog_generator, etc.)
        format_type (str): Format type (streamlit, html, css, js, utils)
        
    Returns:
        str: Template content
    """
    if format_type == "streamlit":
        templates = {
            "chatbot": CHATBOT_TEMPLATE,
            "blog_generator": BLOG_GENERATOR_TEMPLATE,
            "data_analyzer": DATA_ANALYZER_TEMPLATE,
            "sql_generator": SQL_GENERATOR_TEMPLATE,
            "document_summarizer": DOCUMENT_SUMMARIZER_TEMPLATE,
            "web_summarizer": WEB_SUMMARIZER_TEMPLATE
        }
        return templates.get(tool_type, "")
    
    elif format_type == "utils":
        if tool_type == "document_summarizer":
            return DOCUMENT_UTILS_TEMPLATE
        return ""
    
    elif format_type == "html":
        return get_html_template(tool_type)
    
    elif format_type == "css":
        return get_css_template(tool_type)
    
    elif format_type == "js":
        return get_js_template(tool_type)
    
    return ""


__all__ = ['get_template']
