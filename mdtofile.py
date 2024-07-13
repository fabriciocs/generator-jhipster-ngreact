import os
import logging
import re

def sanitize_filename(filename):
    # Replace invalid characters with underscores
    new_name =  re.sub(r'[<>:"/\\|?*]', '_', filename)
    new_name = re.sub(r'[`]', '', new_name)
    new_name = re.sub(r'^\d+\.', '', new_name)
    return new_name

def create_files_from_markdown(markdown_file_path, output_directory):
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Check if the Markdown file exists
    if not os.path.exists(markdown_file_path):
        logging.error(f"Markdown file not found: {markdown_file_path}")
        return

    # Read the content of the Markdown file
    with open(markdown_file_path, 'r', encoding='utf-8') as markdown_file:
        markdown_content = markdown_file.read()

    # Split the content by headers (assuming each file section starts with ###)
    sections = markdown_content.split("###")

    # Process each section
    for section in sections:
        lines = section.strip().split('\n')
        if len(lines) < 2:
            continue
        
        file_name = sanitize_filename(lines[0].strip())
        print(f"\t\t\t3: {lines[3]}\n\t\t\t-1:{lines[-1]}")
        file_content = "\n".join(lines[3:-1])
        file_content = f"\n{file_content}\n"
        # Define the output file path
        output_file_path = os.path.join(output_directory, file_name)

        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        # Write the content to the file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(file_content)
            logging.info(f"Created file: {output_file_path}")

# Example usage
markdown_file_path = "C:\\repos\\generator-jhipster-react-mui\\ctt3.md"
output_directory = "C:\\repos\\generator-jhipster-react-mui\\ai-gen\\entities"

create_files_from_markdown(markdown_file_path, output_directory)
