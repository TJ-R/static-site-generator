import os
import shutil
from block_markdown import extract_title, markdown_to_html


def main():
    copy_src_to_dst("./static", "./public")
    generate_page("content/index.md", "template.html", "public/index.html")


def copy_src_to_dst(src_path, dst_path):
    if os.path.exists(dst_path):
        print("Deleting public dir...")
        shutil.rmtree(dst_path)

    os.mkdir(dst_path)

    if os.path.exists(src_path):
        print(src_path)
        files_to_copy = os.listdir(src_path)

        if len(files_to_copy) > 0:
            for file in files_to_copy:
                if os.path.isfile(os.path.join(src_path, file)):
                    shutil.copy(os.path.join(src_path, file), dst_path)
                else:
                    new_src_path = os.path.join(src_path, file)
                    new_dst_path = os.path.join(dst_path, file)
                    copy_src_to_dst(new_src_path, new_dst_path)

    else:
        raise OSError("Source path does not exist")

    print(f"File copy from {src_path} to {dst_path} completed.")


def generate_page(src_path, template_path, dst_path):
    print(f"Generating page from {src_path} to {dst_path} using {template_path}")
    src_md = ""
    template_md = ""
    with open(src_path, 'r') as f:
        src_md = f.read()
        f.close()

    with open(template_path, 'r') as f:
        template_html = f.read()
        f.close()

    title = extract_title(src_md)
    src_html = markdown_to_html(src_md).to_html()

    final_html = template_html.replace("{{ Title }}", title)
    final_html = template_html.replace("{{ Content }}", src_html)

    directory = os.path.dirname(dst_path)
    os.makedirs(directory, exist_ok=True)

    with open(dst_path, 'w') as f:
        f.write(final_html)
        f.close()


main()
