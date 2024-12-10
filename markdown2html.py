#!/usr/bin/python3
"""
Markdown to HTML converter.

This script validates input arguments for converting a Markdown file
to an HTML file. It processes Markdown headings (#, ##, etc.)
and converts them to corresponding HTML heading tags (<h1>, <h2>, etc.).

Usage: ./markdown2html.py README.md README.html
"""

import os  # For file and path-related operations
import sys  # For interacting with the command-line arguments and system


def process_markdown(input_file, output_file):
    """
    Reads a Markdown file, processes its content, and writes the HTML output.
    """
    try:
        unordered_start = False
        ordered_start = False
        previous_line_was_paragraph = False

        with open(input_file, 'r') as read, open(output_file, 'w') as html:
            for line in read:
                stripped_line = line.strip()  # Strip leading/trailing spaces
                stripped_unordered = line.lstrip('-')
                stripped_ordered = line.lstrip('*')
                stripped_heading = line.lstrip('#')

                heading_level = len(line) - len(stripped_heading)
                unordered_num = len(line) - len(stripped_unordered)
                ordered_num = len(line) - len(stripped_ordered)

                # Handle headings
                if 1 <= heading_level <= 6:
                    # Close any open list before writing a heading
                    if unordered_start:
                        html.write('</ul>\n')
                        unordered_start = False
                    if ordered_start:
                        html.write('</ol>\n')
                        ordered_start = False
                    # Write heading
                    html.write('<h{}>{}</h{}>\n'.format(
                        heading_level,
                        stripped_heading.strip(),
                        heading_level
                    ))
                    previous_line_was_paragraph = False

                # Handle unordered lists
                elif unordered_num:
                    # Start unordered list if not already started
                    if not unordered_start:
                        html.write('<ul>\n')
                        unordered_start = True
                    # Write list item
                    html.write('<li>{}</li>\n'
                               .format(stripped_unordered.strip()))
                    previous_line_was_paragraph = False

                # Handle ordered lists
                elif ordered_num:
                    # Start ordered list if not already started
                    if not ordered_start:
                        html.write('<ol>\n')
                        ordered_start = True
                    # Write list item
                    html.write('<li>{}</li>\n'
                               .format(stripped_ordered.strip()))
                    previous_line_was_paragraph = False

                elif stripped_line:
                    # Close any open list before writing a paragraph
                    if unordered_start:
                        html.write('</ul>\n')
                        unordered_start = False
                    if ordered_start:
                        html.write('</ol>\n')
                        ordered_start = False
                    if previous_line_was_paragraph:
                        # Add <br> if the previous line was also a paragraph
                        html.write('<br/>\n')
                    # Write paragraph
                    html.write('<p>{}</p>\n'.format(stripped_line))
                    previous_line_was_paragraph = True
                else:  # Handle empty lines
                    previous_line_was_paragraph = False

            # Close any remaining open lists
            if unordered_start:
                html.write('</ul>\n')
            if ordered_start:
                html.write('</ol>\n')

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """
    Main function to validate input arguments and file existence.
    """
    # Validate the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    # Extract input and output file names
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Validate the existence of the input file
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Processes the markdown
    process_markdown(input_file, output_file)

    # Success case exits with status 0
    sys.exit(0)


if __name__ == "__main__":
    main()
