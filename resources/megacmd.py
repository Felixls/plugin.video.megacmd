import subprocess
import urllib


MEGA_CMD_PATH = "mega"

# A simple command to invoke mega-cmd-server if not already invoked
subprocess.call(MEGA_CMD_PATH + "-" + "ls")


def get_output(cmd):
    cmd = [MEGA_CMD_PATH + "-" + cmd[0]] + cmd[1:]
    output = subprocess.check_output(cmd)
    output_splits = output.decode("utf-8").split("\n")
    output_splits.remove("")
    return output_splits


def list_files(megapath="."):
    files_list = get_output(["ls", megapath])
    attrs_list = get_output(["ls", "-l", megapath])

    if files_list[0] == attrs_list[0]:
        files_list.pop(0)
        attrs_list.pop(0)

    attrs_list.pop(0)
    files_info = []

    for filename, attrs in zip(files_list, attrs_list):
        is_dir = attrs.startswith("d")
        path = "{}/{}".format(megapath, filename).replace("//", "/")
        file_info = {"name": filename,
                     "is_dir": is_dir,
                     "path": path,
                     "url": webdav_url(path)}

        # if is_dir:
        #     file_info["contents"] = list_files(filename),

        files_info.append(file_info)

    return files_info


def webdav_url(megapath="."):
    output = get_output(["ftp", megapath])
    raw_url = output[0]
    url = raw_url[raw_url.find('ftp://'):]
    return url
