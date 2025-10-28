import os

SRC_MD = "Innovation_Brief.md"
OUT_PDF = "Innovation_Brief.pdf"


def write_pdf_with_reportlab(lines, out_path=OUT_PDF):
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas
    except ImportError:
        raise

    c = canvas.Canvas(out_path, pagesize=A4)
    width, height = A4
    margin = 40
    y = height - margin
    c.setFont("Helvetica", 12)
    for line in lines:
        text = line.strip()
        if not text:
            y -= 10
            continue
        # Simple rendering, wrap long lines
        if len(text) > 100:
            # naive wrap
            parts = [text[i:i+100] for i in range(0, len(text), 100)]
        else:
            parts = [text]
        for part in parts:
            c.drawString(margin, y, part)
            y -= 14
            if y < margin:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = height - margin
    c.save()


def write_pdf_plaintext(lines, out_path=OUT_PDF):
    # fallback: write a plain text file so user can still view content
    with open(out_path, "w", encoding="utf-8") as f:
        f.writelines(lines)


if __name__ == "__main__":
    if not os.path.exists(SRC_MD):
        print("Missing Innovation_Brief.md")
        exit(1)
    with open(SRC_MD, "r", encoding="utf-8") as f:
        lines = f.readlines()

    try:
        write_pdf_with_reportlab(lines, OUT_PDF)
        print(f"Wrote {OUT_PDF} (ReportLab)")
    except ImportError:
        print("reportlab not installed — falling back to plain text output. To install: pip install reportlab")
        alt = OUT_PDF.replace('.pdf', '.txt')
        write_pdf_plaintext(lines, alt)
        print(f"Wrote {alt}")
