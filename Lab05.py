def is_valid_part(part):
    """Checks if a string represents a valid part of an IP address."""
    if part.isdigit():
        num = int(part)
        if 0 <= num <= 255:
            if len(part) == 1 or part[0] != '0':
                return True
    return False

def is_valid_ip(ip):
    """Validates an entire IP address."""
    parts = ip.split('.')
    if len(parts) == 4:
        return all(is_valid_part(part) for part in parts)
    return False

def decimal_to_binary(n):
    """Converts a positive integer to binary representation recursively."""
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

def binary_to_decimal(b):
    """Converts a binary string to its decimal equivalent recursively."""
    if b == "":
        return 0
    else:
        return binary_to_decimal(b[:-1]) * 2 + int(b[-1])


print(is_valid_part("255"))
print(is_valid_part("256"))
print(is_valid_part("01"))
print(is_valid_part("0"))

print(is_valid_ip("192.168.1.1"))
print(is_valid_ip("192.168.256.1"))
print(is_valid_ip("192.168.1"))
print(is_valid_ip("192.168.01.1"))


print(decimal_to_binary(10))
print(decimal_to_binary(255))
print(decimal_to_binary(1))

print(binary_to_decimal("1010"))
print(binary_to_decimal("11111111"))
print(binary_to_decimal("1"))
