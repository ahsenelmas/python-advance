class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        if self.file:
            self.file.close()

# Usage
with FileOpener("test.txt", "w") as f:
    f.write("Hello from Python custom context manager!")
