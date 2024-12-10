# Markdown to HTML - Holberton School

Welcome to the **Markdown to HTML** project repository! This project is part of the **Holberton School Web Development** curriculum, focused on converting Markdown files into HTML using Python.

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Learning Objectives](#learning-objectives)

---

## Description

This project involves converting **Markdown** syntax into **HTML** tags. Markdown is a lightweight markup language that enables easy-to-read and easy-to-write plain text formatting, commonly used in files like `README.md`. The goal is to create a Python script that converts Markdown syntax into the corresponding HTML.

The project starts with basic file handling tasks, such as checking arguments and managing error cases. As the project progresses, the script is extended to support the conversion of Markdown elements like headings, lists, paragraphs, and more advanced formatting such as bold and italic text.

This project provides hands-on experience in parsing text files, working with file I/O in Python, and implementing common text formatting features.

---

## Project Structure

The `markdown_to_html` directory includes the following files:

| File               | Description                                                                                                                                       |
| ------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| `markdown2html.py` | Python script that converts a Markdown file into an HTML file by parsing various Markdown elements such as headings, lists, paragraphs, and more. |
| `README.md`        | Markdown file providing project instructions and examples.                                                                                        |

### Project steps

| Steps                | Description                                                  |
| -------------------- | :----------------------------------------------------------- |
| 0. Script Setup      | Create a Python script `markdown2html.py` that accepts two command-line arguments: input Markdown file and output HTML file. Implement error handling for missing arguments and invalid files. |
| 1. Headings          | Modify the script to handle Markdown headings (`#` to `######`) and convert them into corresponding HTML `<h1>` to `<h6>` tags. |
| 2. Unordered Lists   | Enhance the script to convert Markdown unordered list syntax (`- item`) into HTML `<ul>` with `<li>` elements. |
| 3. Ordered Lists     | Add support for converting ordered lists (`* item`) into HTML `<ol>` with `<li>` elements. |
| 4. Paragraphs        | Implement conversion for paragraphs, ensuring that blocks of text separated by blank lines are wrapped in HTML `<p>` tags. New lines within paragraphs should be converted to `<br />`. |
| 5. Bold and Emphasis | Add support for parsing bold (`**text**` or `__text__`) and italic (`*text*` or `_text_`) text, converting them into HTML `<b>` and `<em>` tags, respectively. |
| 6. Advanced Features | Implement special Markdown syntax:  `[[text]]` should be converted to an MD5 hash. `((text))` should remove all occurrences of the letter "c" (case insensitive). |

---

## Learning Objectives

By the end of this project, the following concepts should be clearly understood and explainable without external assistance:

- The basics of **Markdown** syntax and its uses in documentation.
- How to convert **Markdown** elements (headings, lists, text) into corresponding **HTML** tags.
- How to handle file input/output in Python.
- How to parse and process a text file, identifying different formatting rules.
- The ability to use regular expressions and string manipulation techniques in Python for text parsing.
- How to handle user inputs and provide appropriate error messages when the input is invalid.
- The structure of a basic Python script with argument parsing and error handling.

This project strengthens Python skills and provides a deep understanding of both Markdown and HTML syntax. It also helps develop tools that can parse and manipulate text content programmatically.

---
