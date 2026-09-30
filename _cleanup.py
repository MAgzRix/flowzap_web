import re

p = '/workspace/main.html'
s = open(p, encoding='utf-8').read()

def cut(start_marker, end_marker):
    global s
    n = 0
    while start_marker in s:
        i = s.index(start_marker)
        j = s.index(end_marker, i)
        assert j > i, (start_marker, end_marker)
        s = s[:i] + s[j:]
        n += 1
        if n > 5:
            break
    print('cut', repr(start_marker[:45]), 'x', n)

# FAQ tab block
cut('    <!-- ============ TAB: FAQ ============ -->',
    '    <!-- ============ TAB: TRIGGERS ============ -->')

# WhatsApp Flows tab block
cut('    <!-- ============ TAB: WHATSAPP FLOWS ============ -->',
    '    <!-- ============ TAB: EVENT LOG ============ -->')

# FAQ modal block
cut('<!-- ============ FAQ MODAL ============ -->',
    '<!-- ============ TRIGGER MODAL ============ -->')

# FAQ JS section
cut('// ============ FAQ ============', '// ============ TRIGGERS ============')

# init call
s = s.replace('renderWarehouse();\nrenderFaqs();\nrenderTriggers();',
              'renderWarehouse();\nrenderTriggers();')

# switchTab render line
s = s.replace("  if (tab === 'faq') renderFaqs();\n", "")

# titles entries
s, n1 = re.subn(r"\n *faq: \['FAQ[^\n]*", "", s)
s, n2 = re.subn(r"\n *'whatsapp-flows': \[[^\n]*", "", s)
print('titles removed:', n1, n2)

# tour step for whatsapp-flows
s, n3 = re.subn(r"\n *\{ target: '\[data-tab=\"whatsapp-flows\"\][^\n]*", "", s)
print('tour steps removed:', n3)

open(p, 'w', encoding='utf-8').write(s)
print('done')
