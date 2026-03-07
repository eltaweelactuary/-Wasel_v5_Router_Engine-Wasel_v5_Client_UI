import os
import re

src = r"c:\Users\Ahmed\OneDrive - Konecta\Documents\mcp\Wasel_v5_Router_Engine\app.py"
dst = r"c:\Users\Ahmed\OneDrive - Konecta\Documents\mcp\Wasel_v5_Client_UI\index.html"
os.makedirs(os.path.dirname(dst), exist_ok=True)

with open(src, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract everything between PAGE = r""" and """
match = re.search(r'PAGE\s*=\s*r"""(.*?)"""', content, re.DOTALL)
if match:
    html = match.group(1).strip()
    # Replace relative fetch with absolute API placeholder
    html = html.replace("fetch('/t'", "fetch(API_URL + '/t'")
    html = html.replace("fetch('/chat'", "fetch(API_URL + '/chat'")
    
    # Inject API_URL at the top of script
    html = html.replace("<script>", "<script>\nconst API_URL = 'https://YOUR_GOOGLE_CLOUD_URL_HERE'; // TODO: Partner MUST update this\n")
    
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(html)
    print("UI extracted successfully!")
else:
    print("FAILED TO EXTRACT PAGE")
