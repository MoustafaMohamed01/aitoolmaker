import subprocess
import sys
import os
from pathlib import Path


class StreamlitRunner:
    """Handles running Streamlit applications."""
    
    def __init__(self):
        """Initialize the StreamlitRunner."""
        pass
    
    def run_tool(self, app_path: str, port: int = 8501):
        """
        Run a Streamlit application.
        
        Args:
            app_path (str): Path to the app.py file
            port (int): Port to run the app on (default: 8501)
        """
        app_path = Path(app_path)
        
        if not app_path.exists():
            raise FileNotFoundError(f"App file not found: {app_path}")
        
        # Change to the app directory
        app_dir = app_path.parent
        original_dir = os.getcwd()
        
        try:
            os.chdir(app_dir)
            
            print(f"🚀 Starting Streamlit app: {app_path.name}")
            print(f"📍 Directory: {app_dir}")
            print(f"🌐 URL: http://localhost:{port}")
            print("\n" + "="*50)
            print("Press Ctrl+C to stop the server")
            print("="*50 + "\n")
            
            # Run streamlit
            subprocess.run([
                sys.executable, 
                "-m", 
                "streamlit", 
                "run", 
                app_path.name,
                "--server.port", 
                str(port)
            ])
            
        except KeyboardInterrupt:
            print("\n\n🛑 Stopping Streamlit app...")
        
        finally:
            os.chdir(original_dir)
    
    def run_tool_subprocess(self, app_path: str, port: int = 8501):
        """
        Run a Streamlit application in a subprocess (non-blocking).
        
        Args:
            app_path (str): Path to the app.py file
            port (int): Port to run the app on (default: 8501)
            
        Returns:
            subprocess.Popen: The subprocess object
        """
        app_path = Path(app_path)
        
        if not app_path.exists():
            raise FileNotFoundError(f"App file not found: {app_path}")
        
        app_dir = app_path.parent
        
        print(f"🚀 Starting Streamlit app in background: {app_path.name}")
        print(f"🌐 URL: http://localhost:{port}")
        
        process = subprocess.Popen([
            sys.executable,
            "-m",
            "streamlit",
            "run",
            str(app_path.absolute()),
            "--server.port",
            str(port)
        ], cwd=str(app_dir))
        
        return process
