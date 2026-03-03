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


def test_interactive_widgets_content():
    assert os.path.exists("book/tutorials/interactive_widgets.md")
    with open("book/tutorials/interactive_widgets.md", "r") as f:
        content = f.read()
    assert "Syntax Exercises" in content, "Must include documentation for syntax exercises"
    assert "Problem:" in content or "Challenge:" in content, "Must use Problem-Based Learning approach"


def test_f1_5_interactive_widget():
    assert os.path.exists('book/f1.5-map-projections.md')
    with open('book/f1.5-map-projections.md', 'r') as f:
        content = f.read()
    assert 'ipywidgets' in content or 'interact' in content or '{code-cell} ipython3' in content, "F1.5 must contain an interactive widget demonstration"

def test_f1_5_glossary_present():
    assert os.path.exists('book/f1.5-map-projections.md')
    with open('book/f1.5-map-projections.md', 'r') as f:
        content = f.read()
    assert 'Glossary' in content, "F1.5 must contain a Glossary section"
    assert 'WGS84' in content, "F1.5 must explain WGS84"

def test_f1_5_pbl_activities():
    assert os.path.exists('book/f1.5-map-projections.md')
    with open('book/f1.5-map-projections.md', 'r') as f:
        content = f.read()
    assert 'Programming Task' in content, "F1.5 must contain a programming task"
    assert 'Case Study' in content, "F1.5 must contain a real-world case study"
    assert 'Quiz' in content, "F1.5 must contain a theoretical quiz"
