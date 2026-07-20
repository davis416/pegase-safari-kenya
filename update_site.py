import os
import glob

directory = r"c:\Users\DAVIS\OneDrive\Desktop\ericotour-safari"

html_files = glob.glob(os.path.join(directory, "*.html"))
md_files = glob.glob(os.path.join(directory, "*.md"))

for file_path in html_files + md_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    content = content.replace("Ericotour Safari", "Pégase Safari Kenya")
    # Replace single Ericotour safely, ignoring URLs
    content = content.replace(" Ericotour ", " Pégase Safari Kenya ")
    content = content.replace("Ericotour.", "Pégase Safari Kenya.")
    content = content.replace("Ericotour,", "Pégase Safari Kenya,")
    
    # Phone numbers
    content = content.replace("254112485855", "254741972551")
    content = content.replace("+254 112 485855", "+254 741 972551")
    
    # Emails
    content = content.replace("erickmwangalamganga9@gmail.com", "rahimbaraka23@gmail.com")

    # Dark mode fix
    content = content.replace("document.body.classList.toggle('dark')", "document.documentElement.classList.toggle('dark')")
    content = content.replace("document.body.classList.contains('dark')", "document.documentElement.classList.contains('dark')")
    
    tailwind_script = '<script src="https://cdn.tailwindcss.com"></script>'
    tailwind_config = '<script src="https://cdn.tailwindcss.com"></script>\n  <script>tailwind.config = { darkMode: \'class\' }</script>'
    if tailwind_config not in content:
        content = content.replace(tailwind_script, tailwind_config)

    # Mobile view fix for Header
    old_header = '<header class="flex justify-between items-center bg-white dark:bg-gray-800 py-4 px-8 shadow-md">'
    new_header = '<header class="flex flex-col md:flex-row justify-between items-center bg-white dark:bg-gray-800 py-4 px-4 md:px-8 shadow-md gap-4">'
    content = content.replace(old_header, new_header)

    # Mobile view fix for Nav
    old_nav = '<nav class="flex space-x-6">'
    new_nav = '<nav class="flex flex-wrap justify-center items-center gap-4">'
    content = content.replace(old_nav, new_nav)
    
    # Let's fix the mode toggle button ml-4 which might look weird if we use gap
    old_btn = 'class="text-2xl cursor-pointer ml-4 transition-transform hover:scale-110"'
    new_btn = 'class="text-2xl cursor-pointer transition-transform hover:scale-110"'
    content = content.replace(old_btn, new_btn)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updates completed successfully.")
