# TeachBooks: Interactive Academic Publishing Template

The TeachBooks template provides a robust, accessible, and interactive framework for educators, university students, and practitioners to develop and publish educational materials online. This template requires no prior knowledge of Git, Jupyter Book, Python, or web server deployment.

## Problem Statement

Creating engaging, interactive, and formally structured educational resources often demands significant web development expertise. Educators need a streamlined solution to deploy problem-based learning materials without getting bogged down by technical overhead. 

**Solution:** The TeachBooks template automates the publishing pipeline, allowing you to focus purely on pedagogical content creation.

## Action-Oriented Setup Guide

Follow these steps to initialize and deploy your own TeachBook:

1. **Initialize from Template:** Click the "Use this template" button on the [TeachBooks template repository](https://github.com/TeachBooks/main/template) to generate a new repository.
2. **Configure Repository Details:** Assign a descriptive repository name. Ensure the repository visibility is set correctly (Public repositories allow open contribution; Private requires appropriate GitHub subscription tiers).
3. **Enable GitHub Pages:** To publish your material online, navigate to your repository settings: `Settings` -> `Pages` -> `Build and deployment`. Set the `Source` to `GitHub Actions`.
4. **Trigger Deployment:** Go to the `Actions` tab, select the `call-deploy-book` workflow, and trigger a run if the initial commit failed due to GitHub Pages not being enabled initially.
5. **Access Your TeachBook:** Upon successful deployment, your book will be accessible at `https://<username>.github.io/<repository_name>`.
6. **Start Creating:** Visit the introductory tutorials to begin creating content. See the `book/tutorials/basics.md` and `book/tutorials/interactive_widgets.md` for foundational concepts.

## Local Development

To develop and test your TeachBook locally:

1. Clone your repository: `git clone <your-repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Build the book: `teachbooks build book`
4. The generated HTML will be available in `book/_build/html/index.html`

## Features & Extensions

This template includes predefined configurations for the TeachBooks suite, such as live code execution, interactive syntax exercises, and dynamic widgets. For comprehensive documentation on all features, refer to the [TeachBooks Manual](https://teachbooks.io/manual).

## License & Reuse

Content generated using this template should be appropriately licensed. We recommend the [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/). Please provide adequate attribution when reusing this structure.