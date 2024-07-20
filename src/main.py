import os
import shutil


def main():
    copy_src_to_public()


def copy_src_to_public():
    path = "./public"
    if os.path.exists(path):
        print("Deleting public dir...")
        shutil.rmtree(path)
    else:
        os.mkdir(path)
        files_to_copy = os.listdir()

        if len(files_to_copy) > 0:
            for file in files_to_copy:
                print("Copying " + file + "...")
                shutil.copy(file, path)

                if os.isfile(os.path.join(path, file)) is not True:
                    raise OSError("Newly generated file not found")

    print("File copy from src to public completed.")


main()
