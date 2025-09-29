from utils.file_opener import FileOpener

if __name__ == "__main__":
    with FileOpener("example.txt", "w") as f:
        f.write("Hello from advanced FileOpener project!")
