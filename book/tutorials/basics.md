# Basics of TeachBooks

## The Publishing Challenge
Educators frequently need to seamlessly blend narrative text with executable code. Traditional static PDFs separate the theory from the practical, creating a disjointed learning experience for the student.

## The Solution: Markdown and Jupyter Notebooks
TeachBooks elegantly solves this by integrating Markdown for high-quality, readable prose with Jupyter Notebooks for executable code. This unified format ensures students can read the theory and immediately practice the application.

## Step-by-Step Guide: Your First Page
1. **Create a Markdown File:** Start by creating a file with a `.md` extension (e.g., `my_lesson.md`).
2. **Write Narrative:** Use standard Markdown syntax for headings, lists, and emphasis to explain the core concepts.
3. **Embed Code Blocks:** To show examples, use fenced code blocks.
4. **Link to TOC:** Ensure your new file is listed under the `chapters` section of `book/_toc.yml`.

### Example
To include a Python code snippet:
```python
def greet_student(name):
    print(f"Welcome to TeachBooks, {name}!")
```

By structuring your content this way, you adopt an Action-Oriented approach, enabling learners to directly engage with the material.