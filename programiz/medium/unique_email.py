def count_unique_emails(emails):
    s=set(emails)
    return len(s)
print(count_unique_emails(['abc@gmail','fvv@yahoo','abc@gmail']))