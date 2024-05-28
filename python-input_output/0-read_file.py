#!/user/bin/python3
# 0-read_file.py


def read_file(filename=""):
    """print text from other file"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
