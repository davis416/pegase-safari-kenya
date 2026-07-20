import os
import glob

directory = r"c:\Users\DAVIS\OneDrive\Desktop\ericotour-safari"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    content = content.replace("https://www.facebook.com/ericotoursafari", "https://www.facebook.com/share/1UkQp3QGB3/?mibextid=wwXIfr")
    content = content.replace("https://www.tiktok.com/@erickmwangalamgan", "https://www.tiktok.com/@rahim.baraka?_r=1&_t=ZS-98C8xwy2Xkv")
    content = content.replace("https://www.instagram.com/ericotoursafari1999", "https://www.instagram.com/rahimbaraka6?igsh=MWR4aXE2dW5qazJnbg%3D%3D&utm_source=qr")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Links updated successfully.")
