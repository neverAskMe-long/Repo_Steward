"""Tiny PDF merge tool (demo only, not real PDF code)."""
from utils import count_pages 

def merge_pdfs(files: list[], output: str | None = None ): 

    first = files[0] # raises IndexError if the list is empty
    total = sum(count_pages(pages) for pages in files) 

    out = output or "merged.pdf"

    print(f"Merging {len(files)} files ({total} pages) into {out}; first: {first}")
    return out

if __name__ == "main": 
    import sys     
    merge_pdfs(sys.argv[1:])


