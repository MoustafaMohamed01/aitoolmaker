import os
import shutil
import zipfile
from pathlib import Path


class FileManager:
    """Manages files and directories for AIToolMaker."""
    
    @staticmethod
    def create_directory(path: str, clean: bool = False):
        """
        Create a directory.
        
        Args:
            path (str): Directory path
            clean (bool): Whether to clean existing directory
        """
        path = Path(path)
        
        if clean and path.exists():
            shutil.rmtree(path)
        
        path.mkdir(parents=True, exist_ok=True)
        return path
    
    @staticmethod
    def copy_file(source: str, destination: str):
        """
        Copy a file from source to destination.
        
        Args:
            source (str): Source file path
            destination (str): Destination file path
        """
        source = Path(source)
        destination = Path(destination)
        
        if not source.exists():
            raise FileNotFoundError(f"Source file not found: {source}")
        
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(source, destination)
        
        return destination
    
    @staticmethod
    def zip_directory(directory: str, output_file: str = None):
        """
        Create a zip file from a directory.
        
        Args:
            directory (str): Directory to zip
            output_file (str): Output zip file path (optional)
            
        Returns:
            str: Path to created zip file
        """
        directory = Path(directory)
        
        if not directory.exists():
            raise FileNotFoundError(f"Directory not found: {directory}")
        
        if output_file is None:
            output_file = f"{directory.name}.zip"
        
        output_path = Path(output_file)
        
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(directory.parent)
                    zipf.write(file_path, arcname)
        
        print(f"📦 Created zip file: {output_path.absolute()}")
        return str(output_path.absolute())
    
    @staticmethod
    def write_file(path: str, content: str, encoding: str = "utf-8"):
        """
        Write content to a file.
        
        Args:
            path (str): File path
            content (str): Content to write
            encoding (str): File encoding (default: utf-8)
        """
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding=encoding) as f:
            f.write(content)
        
        return path
    
    @staticmethod
    def read_file(path: str, encoding: str = "utf-8"):
        """
        Read content from a file.
        
        Args:
            path (str): File path
            encoding (str): File encoding (default: utf-8)
            
        Returns:
            str: File content
        """
        path = Path(path)
        
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        
        with open(path, 'r', encoding=encoding) as f:
            return f.read()
