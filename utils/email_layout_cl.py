from contextlib import contextmanager

# @contextmanager
# def my_context():
#     print("Entering...")
#     yield "Resource"
#     print("Exiting...")

# with my_context() as r:
#     print(f"Using {r}")

@contextmanager
def email_context(recipient_name, sender_name):
    print(f"Hello {recipient_name}\n")
    yield
    print("\nBest Regards,")
    print(sender_name)
