"""Helper for safe text replacement in docx paragraphs, preserving formatting."""
from docx import Document

def replace_in_paragraph(para, old, new):
    """Replace old text with new text in a paragraph, preserving run formatting."""
    # Try single-run replacement first
    for run in para.runs:
        if old in run.text:
            run.text = run.text.replace(old, new, 1)
            return True
    # Cross-run replacement
    combined = ''.join(run.text for run in para.runs)
    if old not in combined:
        return False
    idx = combined.find(old)
    new_combined = combined[:idx] + new + combined[idx + len(old):]
    # Redistribute across runs
    pos = 0
    for run in para.runs:
        rlen = len(run.text)
        run.text = new_combined[pos:pos + rlen]
        pos += rlen
    if len(new_combined) > pos:
        para.runs[-1].text += new_combined[pos:]
    elif len(new_combined) < pos:
        excess = pos - len(new_combined)
        for run in reversed(para.runs):
            if excess <= 0:
                break
            if len(run.text) <= excess:
                excess -= len(run.text)
                run.text = ''
            else:
                run.text = run.text[:len(run.text) - excess]
                excess = 0
    return True


def find_section_paras(doc, heading_fragment):
    """Return list of (index, paragraph) for body paragraphs in a section."""
    in_section = False
    result = []
    for i, p in enumerate(doc.paragraphs):
        style = p.style.name if p.style else ''
        if 'Heading' in style and p.text.strip():
            if heading_fragment in p.text:
                in_section = True
                continue
            elif in_section:
                break
        elif in_section and p.text.strip():
            result.append((i, p))
    return result
