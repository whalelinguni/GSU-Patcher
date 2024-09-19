import os

def patch_dll(dll_path, old_byte, new_byte, offset):
    # Convert old_byte and new_byte to bytes
    old_byte = bytes([old_byte])
    new_byte = bytes([new_byte])

    print("### DLL Patching Script ###\n")
    print(f"Target DLL: {dll_path}")
    print(f"Expected Byte: 0x{old_byte.hex().upper()}")
    print(f"New Byte:      0x{new_byte.hex().upper()}")
    print(f"Offset:        0x{offset:X}\n")

    # Ensure the file exists
    if not os.path.isfile(dll_path):
        print(f"[ERROR] File '{dll_path}' does not exist.")
        return

    file_size = os.path.getsize(dll_path)
    print(f"[INFO] File Size: {file_size} bytes")

    if offset >= file_size:
        print(f"[ERROR] Offset 0x{offset:X} is out of the file's range.")
        return

    with open(dll_path, "r+b") as f:
        # Move directly to the offset
        f.seek(offset)

        # Read the byte at the given offset
        current_byte = f.read(1)

        print(f"[INFO] Current Byte at 0x{offset:X}: 0x{current_byte.hex().upper()}")

        # Check if the current byte matches the old byte
        if current_byte == old_byte:
            # Patch the byte
            f.seek(offset)
            f.write(new_byte)
            print(f"[SUCCESS] Byte at offset 0x{offset:X} patched from 0x{old_byte.hex().upper()} to 0x{new_byte.hex().upper()}.\n")
        else:
            print(f"[WARNING] Byte at offset 0x{offset:X} does not match the expected value 0x{old_byte.hex().upper()}.")
            print(f"          Current value is 0x{current_byte.hex().upper()}.\n")

    print("### Patching Completed ###\n")

# Replace with your DLL path and correct offset
dll_path = 'GSCommon.dll'
old_byte = 0x74  # The byte currently at the location
new_byte = 0x75  # The byte you want to replace it with
offset = 0x2DA11  # The exact offset where the byte needs to be changed

# Run the patch
patch_dll(dll_path, old_byte, new_byte, offset)
