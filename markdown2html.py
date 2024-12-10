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

        with open(input_file, 'r') as read, open(output_file, 'w') as html:
            for line in read:
                # Handle headings
                stripped_line = line.lstrip('#')
                heading_level = len(line) - len(stripped_line)

                # Handle unordered lists
                stripped_unordered = line.lstrip('-')
                unordered_num = len(line) - len(stripped_unordered)

                # Handle ordered lists
                stripped_ordered = line.lstrip('*')
                ordered_num = len(line) - len(stripped_ordered)

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
                        stripped_line.strip(),
                        heading_level
                    ))
                elif unordered_num:
                    # Start unordered list if not already started
                    if not unordered_start:
                        html.write('<ul>\n')
                        unordered_start = True

                    # Write list item
                    html.write('<li>{}</li>\n'
                               .format(stripped_unordered.strip()))
                elif ordered_num:
                    # Start ordered list if not already started
                    if not ordered_start:
                        html.write('<ol>\n')
                        ordered_start = True

                    # Write list item
                    html.write('<li>{}</li>\n'
                               .format(stripped_ordered.strip()))
                elif line.strip():
                    # Close any open list before writing a paragraph
                    if unordered_start:
                        html.write('</ul>\n')
                        unordered_start = False
                    if ordered_start:
                        html.write('</ol>\n')
                        ordered_start = False

                    # Write paragraph
                    html.write('<p>{}</p>\n'.format(line.strip()))

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
