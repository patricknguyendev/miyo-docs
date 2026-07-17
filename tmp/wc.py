import re, sys
files = [
  "account/manage-your-data.mdx","account/secure-your-account.mdx",
  "accounts/add-a-manual-account.mdx","accounts/connect-a-bank.mdx",
  "accounts/connect-and-manage-accounts.mdx","accounts/manage-linked-institutions.mdx",
  "budgets/category-targets.mdx","budgets/choose-budget-mode.mdx",
  "budgets/create-and-manage-budget.mdx","budgets/overview.mdx",
  "changelog.mdx","debt/debt-workspace.mdx"
]
for f in files:
    text = open(f).read()
    text2 = re.sub(r'^---\n.*?\n---\n', '', text, count=1, flags=re.S)
    offset = len(text) - len(text2)
    prefix_lines = text[:offset].count("\n")
    lines = text2.split("\n")
    in_code = False
    for i, line in enumerate(lines, 1):
        lineno = i + prefix_lines
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code: continue
        stripped = line.lstrip()
        if stripped.startswith("#"): continue
        if stripped.startswith("|"): continue
        if stripped.startswith("<") or stripped.startswith(">"): continue
        s = line
        s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
        s = re.sub(r'`[^`]*`', 'CODE', s)
        s = re.sub(r'\*+', '', s)
        for sent in re.split(r'(?<=[.!?])\s+', s):
            sent = sent.strip(" -\t")
            # strip leading list markers/digits
            sent = re.sub(r'^[\-\*\d\.\)]+\s*', '', sent)
            words = sent.split()
            if len(words) > 30:
                print(f"{f}:{lineno} ({len(words)} words): {' '.join(words[:15])}...")
