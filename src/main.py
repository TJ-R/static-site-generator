import os
import shutil


def main():
    copy_src_to_dst("./static", "./public")


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


main()
