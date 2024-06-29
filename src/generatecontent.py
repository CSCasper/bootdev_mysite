import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    if markdown.startswith('# '):
        return markdown.split('\n')[0][2:]
    else:
        raise ValueError('No title found in markdown')
    
def generate_page(src_path, template_path, dst_path):
    print(f"Genereating page from {src_path} to {dst_path} using {template_path}")
    file_contents = open(src_path).read()
    template = open(template_path).read()
    content = markdown_to_html_node(file_contents).to_html()
    title = extract_title(file_contents)
    template = template.replace("{{ Content }}", content)
    template = template.replace("{{ Title }}", title)
    if not os.path.exists(os.path.dirname(dst_path)):
        os.makedirs(os.path.dirname(dst_path))
    open(dst_path, 'w').write(template)
    
def generate_pages_recursive(src_dir, template_path, dst_dir):
    for file in os.listdir(src_dir):
        src_file = os.path.join(src_dir, file)
        dst_file = os.path.join(dst_dir, file.replace('.md', '.html'))
        if os.path.isdir(src_file):
            generate_pages_recursive(src_file, template_path, dst_file)
        elif file.endswith('.md'):
            generate_page(src_file, template_path, dst_file)