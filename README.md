# Markdown to HTML - Holberton School

Welcome to the **Markdown to HTML** project repository! This project is part of the **Holberton School Full-Stack** curriculum, focused on converting Markdown files into HTML using Python.

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

---

## Description

This project involves creating a Python script that converts **Markdown** syntax into **HTML** tags, supporting basic Markdown elements like headings, lists, paragraphs, bold text, and advanced syntax like MD5 hashing and character removal. This tool is designed to facilitate the process of converting plain Markdown files (e.g., `README.md`) into well-formatted HTML documents.

The project starts with basic file handling tasks, such as checking arguments and managing error cases. As the project progresses, the script is extended to support the conversion of more Markdown elements.

This project provides hands-on experience in parsing text files, working with file I/O in Python, and implementing common text formatting features.

---

## Project Structure

The `markdown_to_html` directory includes the following files:

| File               | Description                                                                                                                                       |
| ------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| `markdown2html.py`  | Python script that converts a Markdown file into an HTML file by parsing various Markdown elements such as headings, lists, paragraphs, bold/italic text, and custom Markdown syntax. |
| `README.md`         | Markdown file providing project instructions and examples. This file contains documentation for both the project and the code itself.                        |

### Project steps

| Steps                | Description                                                                                                                                                                               |
| -------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0. Script Setup      | Create a Python script `markdown2html.py` that accepts two command-line arguments: input Markdown file and output HTML file. Implement error handling for missing arguments and invalid files. |
| 1. Headings          | Modify the script to handle Markdown headings (`#` to `######`) and convert them into corresponding HTML `<h1>` to `<h6>` tags using Python's string manipulation techniques.              |
| 2. Unordered Lists   | Enhance the script to convert Markdown unordered list syntax (`- item`) into HTML `<ul>` with `<li>` elements, handling multiple list items and nested lists.                             |
| 3. Ordered Lists     | Add support for converting ordered lists (`* item`) into HTML `<ol>` with `<li>` elements, ensuring correct list numbering and list item parsing.                                           |
| 4. Paragraphs        | Implement conversion for paragraphs, ensuring that blocks of text separated by blank lines are wrapped in HTML `<p>` tags. New lines within paragraphs should be converted to `<br />`. |
| 5. Bold and Emphasis | Add support for parsing bold (`**text**` or `__text__`) and emphasized (`*text*` or `_text_`) text, converting them into HTML `<b>` and `<em>` tags using regular expressions.                |
| 6. Advanced Features | Implement special Markdown syntax:  `[[text]]` should be converted to an MD5 hash. `((text))` should remove all occurrences of the letter "c" (case insensitive) using regex and string methods. |

---

## Learning Objectives

By the end of this project, the following concepts should be clearly understood and explainable without external assistance:

- The basics of **Markdown** syntax and its uses in documentation.
- How to convert **Markdown** elements (headings, lists, text) into corresponding **HTML** tags.
- How to handle file input/output in Python using the `open()` function.
- How to parse and process a text file, identifying different formatting rules with **regular expressions** and string manipulation techniques.
- The ability to use regular expressions (`re` module) and string manipulation techniques in Python for text parsing.
- How to handle user inputs and provide appropriate error messages when the input is invalid using exception handling.
- The structure of a basic Python script with argument parsing and error handling.

This project strengthens Python skills and provides a deep understanding of both Markdown and HTML syntax. It also helps develop tools that can parse and manipulate text content programmatically.

---
