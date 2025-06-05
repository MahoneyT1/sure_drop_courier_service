# test_receipt.py
from weasyprint import HTML

HTML(string="""
    <h1>Test Receipt</h1>
    <p>This PDF was generated inside a virtualenv.</p>
""").write_pdf("receipt.pdf")
