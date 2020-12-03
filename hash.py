import hashlib

def SHA256hash(): 
    filename = input("Please enter the path to the file to generate the SHA256 Hash: ")
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        print("SHA256 Hash: " + sha256_hash.hexdigest())

def MD5hash():
    md5_hash = hashlib.md5()

    filename = input("Please enter the path to the file to generate the MD5 Hash: ")

    a_file = open(filename, "rb")
    content = a_file.read()
    md5_hash.update(content)

    digest = md5_hash.hexdigest()
    print("MD5 Hash: " + digest)

SHA256hash()
MD5hash()