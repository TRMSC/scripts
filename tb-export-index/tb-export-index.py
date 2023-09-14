#!/usr/bin/env python3

import os
import re

# Get content of index.html file
def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Search for index.html files and merge
def merge_html_files(base_directory, output_file):
    merged_html = ""

    first_html_found = False

    for root, _, files in os.walk(base_directory):
        for file in files:
            if file == 'index.html':
                html_content = read_html_file(os.path.join(root, file))

                if not first_html_found:
                    # Add html and head only if it hasn't been added before
                    merged_html += html_content.split('<body>', 1)[0]
                    first_html_found = True

                # Add body
                body_content = re.search(r'<body>(.*?)</body>', html_content, re.DOTALL)
                if body_content:
                    # Adjust links
                    body_content = re.sub(r'href="([^"]*)"', r'href="{}\/\1"'.format(root), body_content.group(1))
                    body_content = re.sub(r'src="([^"]*)"', r'src="{}\/\1"'.format(root), body_content)
                    merged_html += body_content

    with open(output_file, 'w', encoding='utf-8') as merged_file:
        merged_file.write(merged_html)

if __name__ == "__main__":
    base_directory = "."  
    output_file = "merged.html"

    merge_html_files(base_directory, output_file)
    print(f"Index files were merged into {output_file}.")
