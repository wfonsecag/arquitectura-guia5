import sys
from pypdf import PdfReader

if len(sys.argv) < 2:
    print("Uso: python extract_pdf_text.py <ruta_pdf> [salida.txt]")
    sys.exit(1)

pdf_path = sys.argv[1]
out_path = sys.argv[2] if len(sys.argv) >= 3 else None

reader = PdfReader(pdf_path)
text_parts = []
for page in reader.pages:
    t = page.extract_text()
    if t:
        text_parts.append(t)

full_text = "\n\n".join(text_parts)

if out_path:
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_text)
else:
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    print(full_text)
