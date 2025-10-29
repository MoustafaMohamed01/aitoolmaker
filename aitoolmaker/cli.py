import argparse
import sys
from . import AIToolMaker


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='AIToolMaker - Generate and run AI-powered tools',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate a chatbot (Streamlit)
  aitoolmaker create --tool chatbot --api-key YOUR_KEY --output streamlit
  
  # Generate and run a blog generator
  aitoolmaker create --tool blog_generator --api-key YOUR_KEY --run
  
  # Generate a website
  aitoolmaker create --tool sql_generator --api-key YOUR_KEY --output website
  
  # List available tools
  aitoolmaker list
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Create command
    create_parser = subparsers.add_parser('create', help='Create a new AI tool')
    create_parser.add_argument(
        '--tool',
        required=True,
        choices=['chatbot', 'blog_generator', 'data_analyzer', 'sql_generator', 
                 'document_summarizer', 'web_summarizer'],
        help='Type of tool to create'
    )
    create_parser.add_argument(
        '--api-key',
        required=True,
        help='API key for the AI service'
    )
    create_parser.add_argument(
        '--model',
        default='gemini-2.0-flash',
        help='Model name to use (default: gemini-2.0-flash)'
    )
    create_parser.add_argument(
        '--output',
        choices=['streamlit', 'website'],
        default='streamlit',
        help='Output format (default: streamlit)'
    )
    create_parser.add_argument(
        '--run',
        action='store_true',
        help='Run the tool immediately after generation'
    )
    create_parser.add_argument(
        '--name',
        help='Custom name for the tool'
    )
    create_parser.add_argument(
        '--logo',
        help='Path to custom logo image'
    )
    create_parser.add_argument(
        '--output-dir',
        help='Output directory for generated files'
    )
    create_parser.add_argument(
        '--api-provider',
        choices=['gemini', 'openai', 'anthropic'],
        default='gemini',
        help='API provider (default: gemini)'
    )
    
    # List command
    list_parser = subparsers.add_parser('list', help='List available tools')
    
    # Info command
    info_parser = subparsers.add_parser('info', help='Get information about a tool')
    info_parser.add_argument(
        'tool',
        choices=['chatbot', 'blog_generator', 'data_analyzer', 'sql_generator',
                 'document_summarizer', 'web_summarizer'],
        help='Tool type to get info about'
    )
    
    # Version command
    version_parser = subparsers.add_parser('version', help='Show version information')
    
    args = parser.parse_args()
    
    if args.command == 'create':
        handle_create(args)
    elif args.command == 'list':
        handle_list()
    elif args.command == 'info':
        handle_info(args)
    elif args.command == 'version':
        handle_version()
    else:
        parser.print_help()


def handle_create(args):
    """Handle the create command."""
    try:
        print(f"\n🤖 AIToolMaker - Creating {args.tool}...")
        print("="*60)
        
        tool_maker = AIToolMaker(
            api_key=args.api_key,
            model=args.model,
            api_provider=args.api_provider
        )
        
        result = tool_maker.create_tool(
            tool_type=args.tool,
            output=args.output,
            run=args.run,
            name=args.name,
            logo=args.logo,
            output_dir=args.output_dir
        )
        
        if not args.run:
            print(f"\n✅ Tool created successfully!")
            print(f"📁 Output directory: {result['output_dir']}")
            
            if args.output == 'streamlit':
                print(f"\n🚀 To run your tool:")
                print(f"   cd {result['output_dir']}")
                print(f"   streamlit run app.py")
            else:
                print(f"\n🌐 To use your website:")
                print(f"   Open {result['index_path']} in a browser")
        
        print("\n" + "="*60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


def handle_list():
    """Handle the list command."""
    print("\n📋 Available Tools:")
    print("="*60)
    
    tools = {
        "chatbot": "Professional AI chatbot with conversation history",
        "blog_generator": "Generate well-structured blog posts with AI",
        "data_analyzer": "Ask questions about your CSV data using AI",
        "sql_generator": "Generate SQL queries from natural language",
        "document_summarizer": "Summarize PDF and Word documents",
        "web_summarizer": "Summarize website content"
    }
    
    for tool, description in tools.items():
        print(f"\n  • {tool}")
        print(f"    {description}")
    
    print("\n" + "="*60)
    print("Use 'aitoolmaker info <tool>' for more details")
    print()


def handle_info(args):
    """Handle the info command."""
    tool_maker = AIToolMaker(api_key="dummy", model="gemini-2.0-flash")
    info = tool_maker.get_tool_info(args.tool)
    
    if info:
        print(f"\n📊 Tool Information: {info['name']}")
        print("="*60)
        print(f"\nDescription: {info['description']}")
        print("\nFeatures:")
        for feature in info['features']:
            print(f"  • {feature}")
        print("\n" + "="*60)
    else:
        print(f"No information available for: {args.tool}")


def handle_version():
    """Handle the version command."""
    from . import __version__, __author__
    print(f"\nAIToolMaker v{__version__}")
    print(f"Author: {__author__}")
    print()


if __name__ == '__main__':
    main()
