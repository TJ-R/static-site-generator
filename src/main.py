import os
import shutil


def main():
    copy_src_to_public()


def copy_src_to_public():
    src_path = "./static"
    dst_path = "./public"
    if os.path.exists(dst_path):
        print("Deleting public dir...")
        shutil.rmtree(dst_path)

    os.mkdir(dst_path)

    if os.path.exists(src_path):
        files_to_copy = os.listdir(src_path)

        if len(files_to_copy) > 0:
            for file in files_to_copy:
                print("Copying " + file + "...")
                shutil.copy(os.path.join(src_path, file), dst_path)

                if os.path.isfile(os.path.join(dst_path, file)) is not True:
                    raise OSError("Newly generated file not found")

    else:
        raise OSError("Source path does not exist")

    print("File copy from src to public completed.")


main()
