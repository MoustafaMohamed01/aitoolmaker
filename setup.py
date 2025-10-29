from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='aitoolmaker',
    version='0.1.0',
    author='Moustafa Mohamed',
    author_email='moustafamohmd5@gmail.com',
    description='A framework for automatically generating and running Streamlit-based AI tools and chatbots',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MoustafaMohamed01/aitoolmaker',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.8',
    install_requires=[
        'streamlit>=1.28.0',
        'google-generativeai>=0.3.0',
        'jinja2>=3.0.0',
        'pandas>=2.0.0',
        'langchain>=0.1.0',
        'langchain-google-genai>=0.0.6',
        'langchain-community>=0.0.13',
        'pypdf>=3.17.0',
        'python-docx>=1.0.0',
        'faiss-cpu>=1.7.4',
        'requests>=2.31.0',
        'beautifulsoup4>=4.12.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'black>=23.0.0',
            'flake8>=6.0.0',
            'mypy>=1.0.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'aitoolmaker=aitoolmaker.cli:main',
        ],
    },
    include_package_data=True,
    package_data={
        'aitoolmaker': [
            'logo/*',
            'core/templates/*',
        ],
    },
    keywords='ai, chatbot, streamlit, tool-generator, gemini, openai, automation',
    project_urls={
        'Bug Reports': 'https://github.com/MoustafaMohamed01/aitoolmaker/issues',
        'Documentation': 'https://github.com/MoustafaMohamed01/aitoolmaker/blob/main/README.md',
        'Source': 'https://github.com/MoustafaMohamed01/aitoolmaker',
    },
)
