import os
import hashlib


def hashfile(path, hasher=0, blocksize = 65536):
    current_file = open(path, 'rb')
    hasher = hashlib.md5() if hasher == 0 else hasher
    buf = current_file.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = current_file.read(blocksize)
    current_file.close()
    return hasher.hexdigest()


def hasDuplicateFile(abs_path, size, size_dict):
    hash1 = hashfile(abs_path)
    if True in [hash1 == hashfile(i) for i in size_dict[size]]:
        hash2 = hashfile(abs_path, hashlib.sha1())
        if True in [hash2 == hashfile(i, hashlib.sha1()) for i in size_dict[size]]:
            return True

    return False


def listDuplicatingFiles(directory):
    if not os.path.isdir(directory):
        print "{0} is not a directory".format(directory)
        raise ValueError

    size_dict = {}
    filenames = []

    for root, dirs, files in os.walk(directory):
        for current_file in files:
            abs_path = os.path.abspath(os.path.join(root, current_file))
            size = os.path.getsize(abs_path)
            if size in size_dict:
                if not hasDuplicateFile(abs_path, size, size_dict):
                    filenames.append(abs_path)
                    size_dict[size].append(abs_path)
            else:
                size_dict[size] = [abs_path]
                filenames.append(abs_path)

    return filenames
