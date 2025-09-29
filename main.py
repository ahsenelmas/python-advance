from utils.file_opener import FileOpener
from utils.email_layout import EmailLayout
from utils.email_layout_cl import email_context

if __name__ == "__main__":
    with FileOpener("example.txt", "w") as f:
      f.write("Hello from advanced FileOpener project!")

    with EmailLayout("Selma", "Ahsen") as email:
        print("I want to see you :)")

    with email_context("Selma", "Ahsen"):
        print("I want to see you :)")
