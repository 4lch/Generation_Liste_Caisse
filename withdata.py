import json
import numpy as np
import pandas as pd
import tkinter as tk
from dictVartoName import *
from productCodes import *
import time
import codecs
from progress.bar import ChargingBar

avals = []
bvals = []
selecteda = ''
selectedb = ''


def main():
    match = load_match_grid()

    window = tk.Tk()
    window.title('Génération Caisse - Nation Photo')
    window.geometry("900x600")

    tk.Grid.rowconfigure(window, 0, weight=1)
    tk.Grid.columnconfigure(window, 0, weight=1)

    #Create & Configure frame 
    frame=tk.Frame(window)

    frame.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W) 

    menubar = tk.Menu(window)
    window.config(menu=menubar)

    menu_format = tk.Menu(menubar, tearoff=0)
    menu_type = tk.Menu(menubar, tearoff=0)
    menu_support = tk.Menu(menubar, tearoff=0)
    menu_marge = tk.Menu(menubar, tearoff=0)
    menu_rendu = tk.Menu(menubar, tearoff=0)
    menu_numerisation = tk.Menu(menubar, tearoff=0)
    menu_scan = tk.Menu(menubar, tearoff=0)
    menu_finition = tk.Menu(menubar, tearoff=0)
    menu_generer = tk.Menu(menubar, tearoff=0)

    menubar.add_cascade(label='Format', menu=menu_format)
    menubar.add_cascade(label='Type', menu=menu_type)
    menubar.add_cascade(label='Support', menu=menu_support)
    menubar.add_cascade(label='Marge', menu=menu_marge)
    menubar.add_cascade(label='Rendu', menu=menu_rendu)
    menubar.add_cascade(label='Numerisation', menu=menu_numerisation)
    menubar.add_cascade(label='Scan', menu=menu_scan)
    menubar.add_cascade(label='Finition', menu=menu_finition)
    menubar.add_cascade(label='Générer le document final', menu=menu_generer)

    menu_format.add_command(label='Format - type', command=lambda:handle_command('FORMAT-TYPE', match, frame, window))
    menu_format.add_command(label='Format - support', command=lambda:handle_command('FORMAT-SUPPORT', match, frame, window))
    menu_format.add_command(label='Format - marge', command=lambda:handle_command('FORMAT-MARGE', match, frame, window))
    menu_format.add_command(label='Format - rendu', command=lambda:handle_command('FORMAT-RENDU', match, frame, window))
    menu_format.add_command(label='Format - numerisation', command=lambda:handle_command('FORMAT-NUMERISATION', match, frame, window))
    menu_format.add_command(label='Format - scan', command=lambda:handle_command('FORMAT-SCAN', match, frame, window))
    menu_format.add_command(label='Format - finition', command=lambda:handle_command('FORMAT-FINITION', match, frame, window))
    menu_format.add_command(label='Format - traitement', command=lambda:handle_command('FORMAT-TRAITEMENT', match, frame, window))

    menu_type.add_command(label='Type - support', command=lambda:handle_command('TYPE-SUPPORT', match, frame, window))
    menu_type.add_command(label='Type - marge', command=lambda:handle_command('TYPE-MARGE', match, frame, window))
    menu_type.add_command(label='Type - rendu', command=lambda:handle_command('TYPE-RENDU', match, frame, window))
    menu_type.add_command(label='Type - numerisation', command=lambda:handle_command('TYPE-NUMERISATION', match, frame, window))
    menu_type.add_command(label='Type - scan', command=lambda:handle_command('TYPE-SCAN', match, frame, window))
    menu_type.add_command(label='Type - finition', command=lambda:handle_command('TYPE-FINITION', match, frame, window))
    menu_type.add_command(label='Type - traitement', command=lambda:handle_command('TYPE-TRAITEMENT', match, frame, window))

    menu_support.add_command(label='Support - marge', command=lambda:handle_command('SUPPORT-MARGE', match, frame, window))
    menu_support.add_command(label='Support - rendu', command=lambda:handle_command('SUPPORT-RENDU', match, frame, window))
    menu_support.add_command(label='Support - numerisation', command=lambda:handle_command('SUPPORT-NUMERISATION', match, frame, window))
    menu_support.add_command(label='Support - scan', command=lambda:handle_command('SUPPORT-SCAN', match, frame, window))
    menu_support.add_command(label='Support - finition', command=lambda:handle_command('SUPPORT-FINITION', match, frame, window))
    menu_support.add_command(label='Support - traitement', command=lambda:handle_command('SUPPORT-TRAITEMENT', match, frame, window))

    menu_marge.add_command(label='Marge - rendu', command=lambda:handle_command('MARGE-RENDU', match, frame, window))
    menu_marge.add_command(label='Marge - numerisation', command=lambda:handle_command('MARGE-NUMERISATION', match, frame, window))
    menu_marge.add_command(label='Marge - scan', command=lambda:handle_command('MARGE-SCAN', match, frame, window))
    menu_marge.add_command(label='Marge - finition', command=lambda:handle_command('MARGE-FINITION', match, frame, window))
    menu_marge.add_command(label='Marge - traitement', command=lambda:handle_command('MARGE-TRAITEMENT', match, frame, window))

    menu_rendu.add_command(label='Rendu - numerisation', command=lambda:handle_command('RENDU-NUMERISATION', match, frame, window))
    menu_rendu.add_command(label='Rendu - scan', command=lambda:handle_command('RENDU-SCAN', match, frame, window))
    menu_rendu.add_command(label='Rendu - finition', command=lambda:handle_command('RENDU-FINITION', match, frame, window))
    menu_rendu.add_command(label='Rendu - traitement', command=lambda:handle_command('RENDU-TRAITEMENT', match, frame, window))

    menu_numerisation.add_command(label='Numerisation - scan', command=lambda:handle_command('NUMERISATION-SCAN', match, frame, window))
    menu_numerisation.add_command(label='Numerisation - finition', command=lambda:handle_command('NUMERISATION-FINITION', match, frame, window))
    menu_numerisation.add_command(label='Numerisation - traitement', command=lambda:handle_command('NUMERISATION-TRAITEMENT', match, frame, window))

    menu_scan.add_command(label='Scan - finition', command=lambda:handle_command('SCAN-FINITION', match, frame, window))
    menu_scan.add_command(label='Scan - traitement', command=lambda:handle_command('SCAN-TRAITEMENT', match, frame, window))

    menu_finition.add_command(label='Finition - traitement', command=lambda:handle_command('FINITION-TRAITEMENT', match, frame, window))

    menu_generer.add_command(label='Générer le document final', command=lambda:generate_final_doc(match))
    menu_generer.add_command(label='Remplir le document Docan', command=lambda:fill_docan_doc())

    window.mainloop()

def handle_command(arg, match, frame, window):
    a, b = arg.split('-')

    names = match.columns.values.tolist()
    global avals
    avals = [s for s in names if a in s]
    global bvals
    bvals = [s for s in names if b in s]

    global selecteda
    selecteda = avals[0]
    global selectedb
    selectedb = bvals[0]

    print('A values: ', avals, '\nB values: ', bvals)

    frame=tk.Frame(window)

    frame.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

    # Create grid
    for row_index in range(max(len(avals), len(bvals))):
        tk.Grid.rowconfigure(frame, row_index, weight=1)
        for col_index in range(3):
            tk.Grid.columnconfigure(frame, col_index, weight=1)
    
    # Create left column
    for i, av in enumerate(avals):
        btn = tk.Button(frame, text=av, bg='#eee', command=lambda i=i, av=av: handle_btn_choice_a(i, 0, av, frame, match)) #create a button inside frame 
        btn.grid(row=i, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        if av == selecteda:
            btn['bg'] = '#30c5f2'

    # Create middle column
    for i in range(max(len(avals), len(bvals))):
        btn = tk.Button(frame) #create a button inside frame 
        btn.grid(row=i, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
        btn['text'] = ''
        btn['state'] = 'disabled'
        btn['bg'] = '#555'

    # Create right column
    for i, bv in enumerate(bvals):
        btn = tk.Button(frame, text=bv, bg='#eee', command=lambda i=i, bv=bv: handle_btn_choice_b(i, 2, bv, frame, match)) #create a button inside frame 
        btn.grid(row=i, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
        val = match[bv][selecteda]

        if val == '?':
            btn['bg'] = '#eee'
        elif val == 'O':
            btn['bg'] = '#67f58d'
        elif val == 'N':
            btn['bg'] = '#f26a63'
        else:
            btn['bg'] = '#d163f2'


    # for av in avals:
    #     for bv in bvals:
    #         match[av][bv] = 'Z'

    match.to_csv('match.csv')
    return True

def handle_btn_choice_a(row, col, name, frame, match):
    global selecteda
    selecteda = name

    # Reset all buttons to gray
    for i in range(len(avals)):
        b = frame.grid_slaves(row=i, column=col)[0]
        b['bg'] = '#eee'

    # Select button and paint it blue
    btn = frame.grid_slaves(row=row, column=col)[0]
    btn['bg'] = '#30c5f2'

    # print('Selected A: ', btn['text'])

    # Put correct color for B buttons
    for i, val in enumerate(bvals):
        b = frame.grid_slaves(row=i, column=2)[0]
        status = match[bvals[i]][selecteda]
        if status == '?':
            b['bg'] = '#eee'
        elif status == 'O':
            b['bg'] = '#67f58d'
        elif status == 'N':
            b['bg'] = '#f26a63'
        else:
            b['bg'] = '#d163f2'

def handle_btn_choice_b(row, col, name, frame, match):
    global selectedb
    selectedb = name

    b = frame.grid_slaves(row=row, column=col)[0]
    val = match[selectedb][selecteda]
    newVal = ''

    if val == '?':
        newVal = 'O'
    elif val == 'O':
        newVal = 'N'
    else:
        newVal = 'O'

    match[selectedb][selecteda] = newVal

    if newVal == '?':
        b['bg'] = '#eee'
    elif newVal == 'O':
        b['bg'] = '#67f58d'
    elif newVal == 'N':
        b['bg'] = '#f26a63'
    else:
        b['bg'] = '#d163f2'

    # print('name: ', name, ', row: ', row, '\ncol: ', col)
    # print('Selected B: ', b['text'])

    match.to_csv('match.csv')

def generate_empty_match_grid(): 
    with open('properties.json') as jsonfile:
        data = json.load(jsonfile)

        formats = data['formats']
        types = data['types']
        supports = data['supports']
        marges = data['marges']
        rendus = data['rendus']
        numerisations = data['numerisations']
        scans = data['scans']
        finitions = data['finitions']
        traitements = data['traitements']

        alldata = formats + types + supports + marges + rendus + numerisations + scans + finitions + traitements

        topstring = 'PARAMS,'+','.join(alldata)

        timestamp = str(round(time.time() * 1000))

        with open(f'match-{timestamp}.csv', 'w') as match:
            match.write(topstring + '\n')
            for i, val in enumerate(alldata):
                match.write(val + i*',?' + ',X' + (len(alldata) - i - 1)*',?' + '\n')

def load_match_grid():
    return pd.read_csv('match.csv', index_col='PARAMS')

def build_product_code(forma, typ, support, numerisation, finition, traitement):
    traitement_multipliers = {'TRAITEMENT_NORMAL': 1, 'TRAITEMENT_EXPRESS_X2': 2, 'TRAITEMENT_EXPRESS_X3': 3}

    traitement_mult = traitement_multipliers[traitement]

    infoset = set([forma, typ, support, numerisation, finition])
    codes_arr = []
    dev_option = ''

    # --- DEV RELATED CODES ---
    if 'FORMAT_8x10' in infoset:
        dev_option = codes['DEV_PF_8X10']
    elif set(['FORMAT_4x5', 'TYPE_NB_MANUEL']).issubset(infoset):
        dev_option = codes['DEV_PLAN_FILM_NB']
    elif set(['FORMAT_4x5', 'TYPE_C41_MANUEL']).issubset(infoset):
        dev_option = codes['DEV_PLAN_FILM_C41']
    elif set(['FORMAT_4x5', 'TYPE_E6_MANUEL']).issubset(infoset):
        dev_option = codes['DEV_PLAN_FILM_E6']
    elif 'TYPE_NB_MANUEL' in infoset:
        dev_option = codes['DEV_NB_MANUEL']
    elif 'TYPE_C41_MANUEL' in infoset:
        dev_option = codes['DEV_C41_MANUEL']
    elif 'TYPE_E6_MANUEL' in infoset:
        dev_option = codes['DEV_E6_MANUEL']
    # TODO add Washi support
    elif 'TYPE_NB_MACHINE' in infoset:
        dev_option = codes['DEV_NB']
    elif 'TYPE_C41_MACHINE' in infoset:
        dev_option = codes['DEV_C41']
    elif 'TYPE_E6' in infoset:
        dev_option = codes['DEV_E6']
    elif 'TYPE_NB_SCALA' in infoset:
        dev_option = codes['DEV_SCALA']
    elif 'TYPE_ECN2' in infoset:
        dev_option = codes['DEV_ECN2']
    
    # Multiply dev code according to multiplier
    # if (dev_option != ''):
    #     for i in range(traitement_mult):
    #         codes_arr.append(dev_option)

    if (dev_option !=  ''):
        if traitement_mult == 2:
            dev_option += '*2'
        elif traitement_mult == 3:
            dev_option += '*3'
    
    codes_arr.append(dev_option)

    if 'SUPPORT_LOMOKINO' in infoset:
        codes_arr.append(codes['FORFAIT_LOMOKINO_NO_PACK_NO_DEV'])
    elif 'SUPPORT_SPINNER' in infoset:
        codes_arr.append(codes['FORFAIT_SPINNER'])
    elif 'SUPPORT_SPROCKET' in infoset:
        codes_arr.append(codes['FORFAIT_SPROCKET_110_126_127'])
    # --- END OF DEV CODES ---

    # ---------------------------------------------------------------------

    # --- NUMERISATION CODES ---
    # Exception : code différent pour scan 4x5, sélectionné avec la num HD HR500 par manque d'autre option
    if (('SUPPORT_LOMOKINO' not in infoset) and ('SUPPORT_SPINNER' not in infoset) and ('SUPPORT_SPROCKET' not in infoset)):
        if set(['FORMAT_4x5', 'NUMERISATION_HR500_HD']).issubset(infoset):
            codes_arr.append(codes['NUMERISATION_4X5_FORFAIT'])
        elif 'NUMERISATION_SD' in infoset:
            codes_arr.append(codes['NUMERISATION_STANDARD'])
        elif 'NUMERISATION_HS1800_L' in infoset:
            codes_arr.append(codes['NUMERISATION_HS1800_L'])
        elif 'NUMERISATION_HR500_SHD' in infoset:
            codes_arr.append(codes['NUMERISATION_HR500_SHD'])
        elif 'NUMERISATION_HR500_UHD' in infoset:
            codes_arr.append(codes['NUMERISATION_HR500_UHD'])
        elif 'NUMERISATION_HS1800_XL' in infoset:
            codes_arr.append(codes['NUMERISATION_HS1800_XL'])
        elif 'NUMERISATION_HR500_HD' in infoset:
            codes_arr.append(codes['NUMERISATION_HR500_HD'])
        # TODO Support for Washi scanning
    # --- END OF NUMERISATION CODES ---
    
    # ---------------------------------------------------------------------

    # --- FORFAIT CODES ---
    # Lomokino, sprocket, spinner handled above, excluded anyway
    if 'SUPPORT_TIRAGE_LECTURE' in infoset:
        codes_arr.append(codes['FORFAIT_TIRAGE_LECTURE'])
    elif 'SUPPORT_10x15' in infoset:
        codes_arr.append(codes['FORFAIT_TIRAGE_10X15_10x10'])
    elif 'SUPPORT_13x19' in infoset:
        codes_arr.append(codes['FORFAIT_TIRAGE_13X19_13x13'])
    elif 'SUPPORT_15x23' in infoset:
        codes_arr.append(codes['FORFAIT_TIRAGE_15X15_15X23'])

    # Mise sous cache sous forfaits mais indépendante des supports
    if 'FINITION_MISE_SOUS_CACHE' in infoset:
        codes_arr.append(codes['FORFAIT_MISE_SOUS_CACHE'])
    # --- END OF FORFAIT CODES ---

    return codes_arr

def generate_final_doc(match):
    incomps = []
    rownames = match.columns.values.tolist()
    colnames = match.columns.values.tolist()

    # Generate incompatibilities list
    for row in rownames:
        for col in colnames:
            if match[row][col] == 'N':
                incomps.append(set([row, col]))
    # print(incomps)

    # Extract properties based on name (eg, every format is named FORMAT_xxx)
    formats = [n for n in rownames if 'FORMAT' in n]
    types = [n for n in rownames if 'TYPE' in n]
    supports = [n for n in rownames if 'SUPPORT' in n]
    marges = [n for n in rownames if 'MARGE' in n]
    rendus = [n for n in rownames if 'RENDU' in n]
    numerisations = [n for n in rownames if 'NUMERISATION' in n]
    scans = [n for n in rownames if 'SCAN' in n]
    finitions = [n for n in rownames if 'FINITION' in n]
    traitements = [n for n in rownames if 'TRAITEMENT' in n]

    print('Formats : ', formats)
    print('Types : ', types)
    print('Supports : ', supports)
    print('Marges : ', marges)
    print('Rendus : ', rendus)
    print('Numerisations : ', numerisations)
    print('Scans : ', scans)
    print('Finitions : ', finitions)
    print('Traitements : ', traitements)

    nbtot = 0
    nbvalid = 0

    # bar = ChargingBar('Processing', max=len(formats) * len(types) * len(supports) * len(marges) * len(rendus) * len(numerisations) * len(scans) * len(finitions) * len(traitements))

    with open('generated.csv', 'w', encoding='utf-8') as out:
        out.write('Code, Format, Type, Support, Marge, Rendu, Numérisation, Scan, Finition, Traitement, CodeProduit1, CodeProduit2, CodeProduit3, CodeProduit4, CodeProduit5, CodeProduit6\n')

        
        for forma in formats:
            for typ in types:
                for support in supports:
                    for marge in marges:
                        for rendu in rendus:
                            for numerisation in numerisations:
                                for scan in scans:
                                    for finition in finitions:
                                        for traitement in traitements:

                                            nbtot += 1
                                            lineArray = [forma, typ, support, marge, rendu, numerisation, scan, finition, traitement]
                                            lineSet = set(lineArray)

                                            isValid = True
                                            for incomp in incomps:
                                                if incomp.issubset(lineSet):
                                                    isValid = False
                                                    break
                                            
                                            if isValid:
                                                nbvalid += 1

                                                product_codes = build_product_code(forma, typ, support, numerisation, finition, traitement)      
                                                product_code_str = ', ' + ', '.join(product_codes) if len(product_codes) else ''

                                                # Write output string to CSV
                                                out.write(f'{translatedictforexportonly[forma]}, {translatedictforexportonly[typ]}, {translatedictforexportonly[support]}, {translatedictforexportonly[marge]}, {translatedictforexportonly[rendu]}, {translatedictforexportonly[numerisation]}, {translatedictforexportonly[scan]}, {translatedictforexportonly[finition]}, {translatedictforexportonly[traitement]}' + product_code_str + '\n')
                                            
                                            # If there are no valid article with this combination, still print it to a new line without an article code
                                            # else:
                                            #     out.write(f'{translatedictforexportonly[forma]}, {translatedictforexportonly[typ]}, {translatedictforexportonly[support]}, {translatedictforexportonly[marge]}, {translatedictforexportonly[rendu]}, {translatedictforexportonly[numerisation]}, {translatedictforexportonly[scan]}, {translatedictforexportonly[finition]}, {translatedictforexportonly[traitement]}' + '\n')
                                            # bar.next()
    # bar.finish()

    print(f'{nbtot} total combinations')
    percent =  "{:.2f}".format(100 * nbvalid / nbtot)
    print(f'{nbvalid} valid combinations written ({percent}%)')

def fill_docan_doc():
    generated = []
    empty = []
    with codecs.open('generated.csv', 'r', 'utf-8') as generated_csv:
        lines = generated_csv.readlines()
        for l in lines:
            s = l.strip().split(',')
            for i, e in enumerate(s):
                s[i] = s[i].strip()
            
            generated.append(s)
            # print(s)

    with codecs.open('docan_empty.csv', 'r', 'utf-8') as empty_csv:
        lines = empty_csv.readlines()
        for l in lines:
            s = l.strip().split(',')[:10]
            for i, e in enumerate(s):
                s[i] = s[i].strip()

            empty.append(s)
            # print(s)

    print(len(empty))
    bar = ChargingBar('Processing', max=len(empty))

    no_written = 0
    no_to_write = len(generated)
    generated_left_after_writing = []
    with codecs.open('final.csv', 'w', 'utf-8') as output:
        for e in empty:
            docan_code = e[0]

            e_format = e[1]
            e_type = e[2]
            e_support = e[3]
            e_numerisation = e[6]
            e_finition = e[8]
            e_traitement = e[9]

            empty_s_with_docan_code = ','.join(e)

            found = False
            for i, g in enumerate(generated):

                g_format = g[0]
                g_type = g[1]
                g_support = g[2]
                g_marge = g[3]
                g_rendu = g[4]
                g_numerisation = g[5]
                g_scan = g[6]
                g_finition = g[7]
                g_traitement = g[8]

                # print(f'{e_format=} {g_format=}')
                # print(f'{e_type=} {g_type=}')
                # print(f'{e_support=} {g_support=}')
                # print(f'{e_numerisation=} {g_numerisation=}')
                # print(f'{e_finition=} {g_finition=}')
                # print(f'{e_traitement=} {g_traitement=}')

                if e_format == g_format and e_type == g_type and e_support == g_support and e_numerisation == g_numerisation and e_finition == g_finition and e_traitement == e_traitement:
                    out_str = docan_code + ',' + ','.join(g) + '\n'
                    generated_s_code = ','.join(g[9:])
                    # out_s = empty_s_with_docan_code + ',' + generated_s_code + '\n'
                    found = True
                    output.writelines(out_str)
                    generated.pop(i)
                    no_written += 1
                    break
            
            if not found:
                output.writelines(empty_s_with_docan_code + '\n')

            bar.next()
        
        generated_left_after_writing = generated
    bar.finish()

    print(f'Done. Wrote {no_written}/{no_to_write} possible combinations.')
    # print('Possible combinations that were not written : ')
    # print(generated_left_after_writing)

    with codecs.open('possibilities_not_written.csv', 'w', 'utf-8') as not_written:
        for l in generated_left_after_writing:
            not_written.writelines(', '.join(l) + '\n')

if __name__ == '__main__':
    # generate_empty_match_grid()
    main()
