from data import *
from incompatibilities import *

nbtot = 0
nbvalid = 0
with open('out.csv', 'w', encoding='utf-8') as out:
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
                                            # print(lineArray)
                                            # change back ambiguous strings to O, N and Aucune
                                            margeFinal = 'O' if (marge == MARGE_OUI) else 'N'
                                            renduFinal = 'O' if (rendu == RENDU_OUI) else 'N'
                                            scanFinal = 'O' if (scan == SCAN_OUI) else 'N'

                                            numerisationFinal = 'Aucune' if (numerisation == NUMERISATION_AUCUNE) else numerisation
                                            finitionFinal = 'Aucune' if (finition == FINITION_AUCUNE) else finition
                                            # Write output string to CSV
                                            out.write(f'{forma}, {typ}, {support}, {margeFinal}, {renduFinal}, {numerisationFinal}, {scanFinal}, {finitionFinal}, {traitement}\n')

print(f'{nbtot} total combinations')
percent =  "{:.2f}".format(100 * nbvalid / nbtot)
print(f'{nbvalid} valid combinations written ({percent}%)')
