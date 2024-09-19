
# GeekSquad MRI System Update - GSCommon.dll - Date Patch Script


## Overview

MRI 5.11.0.6 Release
Patch for 'GSCommon.dll' to disable date check / expiration.
Put script in 'MRI' dir with 'GSCommon.dll' and run to patch.

### What the Script Does

- **Target File:** `GSCommon.dll`
- **Original Byte:** `0x74`
- **Patched Byte:** `0x75`
- **Offset:** `0x2DA11`

## Usage

### Prerequisites

- **Python 3.x** installed on your system.

### Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/gscommon-date-patch.git
   cd gscommon-date-patch
   ```

2. **Place the DLL file:**

   Ensure that the `GSCommon.dll` file you want to patch is in the same directory as the script.

3. **Run the patch script:**

   ```bash
   python gsu-patch.py
   ```

4. **Verify the output:**

   The script will output messages indicating the success or failure of the patch operation. If the byte was successfully patched, the program should now run correctly.


## License

This project is license. See the [LICENSE](LICENSE) file for details.

---

**Disclaimer:** This script is provided as-is, without any warranty. Use it at your own risk. Make sure to back up your original DLL file before applying the patch.
