import os
import re

def test_readme_links():
    assert os.path.exists('README.md')
    with open('README.md', 'r') as f:
        content = f.read()
    
    # Check for basic tutorials
    assert 'book/tutorials/basics.md' in content or 'tutorials/basics.md' in content, "README should link to basics tutorial"
    assert 'book/tutorials/interactive_widgets.md' in content or 'tutorials/interactive_widgets.md' in content, "README should link to interactive widgets tutorial"

def test_tutorial_files_exist():
    assert os.path.exists('book/tutorials/basics.md')
    assert os.path.exists('book/tutorials/interactive_widgets.md')

def test_intro_links():
    assert os.path.exists('book/intro.md')
    with open('book/intro.md', 'r') as f:
        content = f.read()
    assert 'tutorials/basics.md' in content or 'basics.md' in content, "Intro should link to basics tutorial"

def test_references_file_exist():
    assert os.path.exists('book/references.md')


def test_toc_includes_tutorials():
    assert os.path.exists("book/_toc.yml")
    with open("book/_toc.yml", "r") as f:
        content = f.read()
    assert "tutorials/basics" in content or "tutorials/basics.md" in content, "TOC must include basics tutorial"
    assert "tutorials/interactive_widgets" in content or "tutorials/interactive_widgets.md" in content, "TOC must include interactive widgets tutorial"

