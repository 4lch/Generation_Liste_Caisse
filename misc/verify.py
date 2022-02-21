import codecs

lines_g = []
lines_d = []

with codecs.open('generated.csv', 'r', 'utf-8') as generated:
    l = generated.readlines()
    lines_g = l

with codecs.open('Docan_empty.csv', 'r', 'utf-8') as docan:
    l = docan.readlines()
    lines_d = l

for i in range(len(lines_d)):
    d_s = lines_d[i].strip().split(',')
    for i in range(len(d_s)):
        d_s[i] = d_s[i].strip()
    d_arr = ','.join(d_s)
    
    g_s = lines_g[i].strip().split(',')
    for i in range(len(g_s)):
        g_s[i] = g_s[i].strip()
    g_arr = ','.join(g_s)

    if d_s != g_s:
        print(f'{d_s=}')
        print(f'{g_s=}\n\n------\n')
