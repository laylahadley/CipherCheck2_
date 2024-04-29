import sys

def caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            # Convert to uppercase
            char = char.upper()
            # Shift the letter
            shifted_char = chr(((ord(char) - 65 + shift) % 26) + 65)
            encrypted_message += shifted_char
    return encrypted_message

# Check if the shift amount is provided
if len(sys.argv) != 2:
    print("Usage: python caesar_cipher.py <shift_amount>")
    sys.exit(1)

try:
    shift_amount = int(sys.argv[1])
    if shift_amount < 0 or shift_amount > 25:
        print("Shift amount must be between 0 and 25")
        sys.exit(1)
except ValueError:
    print("Invalid shift amount")
    sys.exit(1)

# Read message from stdin
for line in sys.stdin:
    message = line.strip()

# Convert message to uppercase
message = message.upper()

# Encrypt the message
encrypted_message = caesar_cipher(message, shift_amount)

# Print the encrypted message in blocks of five letters
block_size = 5
for i in range(0, len(encrypted_message), block_size):
    print(encrypted_message[i:i+block_size], end=" ")

    # Print a newline every ten blocks
    if (i+block_size) % (block_size * 10) == 0:
        print()

# Print a newline at the end
print()

