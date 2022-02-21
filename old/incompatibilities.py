from data import *

incomps = [
    # --- Film format and type options ---
    # No incomps for 120
    # No incomps for 135
    # Incomps for 110 film
    set([FORMAT_110, TYPE_C41_MANUEL]),
    set([FORMAT_110, TYPE_NB_MANUEL]),
    set([FORMAT_110, TYPE_NB_SCALA]),
    # Incomps for 126 film
    set([FORMAT_126, TYPE_C41_MANUEL]),
    set([FORMAT_126, TYPE_NB_MANUEL]),
    set([FORMAT_126, TYPE_NB_SCALA]),
    # Incomps for 127 film
    set([FORMAT_127, TYPE_C41_MANUEL]),
    set([FORMAT_127, TYPE_NB_MANUEL]),
    set([FORMAT_127, TYPE_NB_SCALA]),
    # Incomps for 4x5" film
    set([FORMAT_4x5, TYPE_C41_MACHINE]),
    set([FORMAT_4x5, TYPE_NB_MACHINE]),
    # Incomps for 8x10" film
    set([FORMAT_8x10, TYPE_C41_MACHINE]),
    set([FORMAT_8x10, TYPE_NB_MACHINE]),


    # --- Format et support ---
    # 120
    set([FORMAT_120, SUPPORT_SPROCKET]),
    set([FORMAT_120, SUPPORT_LOMOKINO]),
    set([FORMAT_120, SUPPORT_PLANCHE_CONTACT_MANUEL]),
    # 135
    set([FORMAT_135, SUPPORT_PLANCHE_CONTACT_MANUEL]),
    # 110
    set([FORMAT_110, SUPPORT_10x15]),
    set([FORMAT_110, SUPPORT_13x19]),
    set([FORMAT_110, SUPPORT_15x23]),
    set([FORMAT_110, SUPPORT_LOMOKINO]),
    set([FORMAT_110, SUPPORT_PLANCHE_CONTACT]),
    set([FORMAT_110, SUPPORT_PLANCHE_CONTACT_MANUEL]),
    set([FORMAT_110, SUPPORT_SPINNER]),
    set([FORMAT_110, SUPPORT_TIRAGE_LECTURE]),
    # 126
    set([FORMAT_126, SUPPORT_10x15]),
    set([FORMAT_126, SUPPORT_13x19]),
    set([FORMAT_126, SUPPORT_15x23]),
    set([FORMAT_126, SUPPORT_LOMOKINO]),
    set([FORMAT_126, SUPPORT_PLANCHE_CONTACT]),
    set([FORMAT_126, SUPPORT_PLANCHE_CONTACT_MANUEL]),
    set([FORMAT_126, SUPPORT_SPINNER]),
    set([FORMAT_126, SUPPORT_TIRAGE_LECTURE]),
    # 127
    set([FORMAT_127, SUPPORT_10x15]),
    set([FORMAT_127, SUPPORT_13x19]),
    set([FORMAT_127, SUPPORT_15x23]),
    set([FORMAT_127, SUPPORT_LOMOKINO]),
    set([FORMAT_127, SUPPORT_PLANCHE_CONTACT]),
    set([FORMAT_127, SUPPORT_PLANCHE_CONTACT_MANUEL]),
    set([FORMAT_127, SUPPORT_SPINNER]),
    set([FORMAT_127, SUPPORT_TIRAGE_LECTURE]),
    # 4x5"
    set([FORMAT_4x5, SUPPORT_10x15]),
    set([FORMAT_4x5, SUPPORT_13x19]),
    set([FORMAT_4x5, SUPPORT_15x23]),
    set([FORMAT_4x5, SUPPORT_LOMOKINO]),
    set([FORMAT_4x5, SUPPORT_PLANCHE_CONTACT]),
    set([FORMAT_4x5, SUPPORT_PLANCHE_CONTACT_MANUEL]),
    set([FORMAT_4x5, SUPPORT_SPINNER]),
    set([FORMAT_4x5, SUPPORT_SPROCKET]),
    set([FORMAT_4x5, SUPPORT_TIRAGE_LECTURE]),
    # 8x10"
    set([FORMAT_8x10, SUPPORT_10x15]),
    set([FORMAT_8x10, SUPPORT_13x19]),
    set([FORMAT_8x10, SUPPORT_15x23]),
    set([FORMAT_8x10, SUPPORT_LOMOKINO]),
    set([FORMAT_8x10, SUPPORT_PLANCHE_CONTACT]),
    set([FORMAT_8x10, SUPPORT_PLANCHE_CONTACT_MANUEL]),
    set([FORMAT_8x10, SUPPORT_SPINNER]),
    set([FORMAT_8x10, SUPPORT_SPROCKET]),
    set([FORMAT_8x10, SUPPORT_TIRAGE_LECTURE]),


    # --- Format et numérisation ---
    # Incomps for 110 film
    set([FORMAT_110, NUMERISATION_HR500_SHD]),
    set([FORMAT_110, NUMERISATION_HR500_UHD]),
    set([FORMAT_110, NUMERISATION_HS1800_L,]),
    set([FORMAT_110, NUMERISATION_HS1800_XL]),
    set([FORMAT_110, NUMERISATION_SD,]),
    # Incomps for 126 film
    set([FORMAT_126, NUMERISATION_HR500_SHD]),
    set([FORMAT_126, NUMERISATION_HR500_UHD]),
    set([FORMAT_126, NUMERISATION_HS1800_L,]),
    set([FORMAT_126, NUMERISATION_HS1800_XL]),
    set([FORMAT_126, NUMERISATION_SD,]),
    # Incomps for 127 film
    set([FORMAT_127, NUMERISATION_HR500_SHD]),
    set([FORMAT_127, NUMERISATION_HR500_UHD]),
    set([FORMAT_127, NUMERISATION_HS1800_L,]),
    set([FORMAT_127, NUMERISATION_HS1800_XL]),
    set([FORMAT_127, NUMERISATION_SD,]),
    # Incomps for 4x5" film
    set([FORMAT_4x5, NUMERISATION_HR500_SHD]),
    set([FORMAT_4x5, NUMERISATION_HR500_UHD]),
    set([FORMAT_4x5, NUMERISATION_HS1800_L,]),
    set([FORMAT_4x5, NUMERISATION_HS1800_XL]),
    set([FORMAT_4x5, NUMERISATION_SD,]),
    # Incomps for 8x10" film
    set([FORMAT_8x10, NUMERISATION_HR500_HD]),
    set([FORMAT_8x10, NUMERISATION_HR500_SHD]),
    set([FORMAT_8x10, NUMERISATION_HR500_UHD]),
    set([FORMAT_8x10, NUMERISATION_HS1800_L,]),
    set([FORMAT_8x10, NUMERISATION_HS1800_XL]),
    set([FORMAT_8x10, NUMERISATION_SD,]),


    # --- Format et finition ---
    # 135
    set([FORMAT_135, FINITION_AUCUNE]),
    # 120
    set([FORMAT_120, FINITION_AUCUNE]),
    set([FORMAT_120, FINITION_MISE_SOUS_CACHE]),
    # 110 
    set([FORMAT_110, FINITION_DECOUPE_4]),
    set([FORMAT_110, FINITION_DECOUPE_6]),
    set([FORMAT_110, FINITION_DETRUIRE]),
    set([FORMAT_110, FINITION_BANDE]),
    set([FORMAT_110, FINITION_MISE_SOUS_CACHE]),
    # 126
    set([FORMAT_126, FINITION_DECOUPE_4]),
    set([FORMAT_126, FINITION_DECOUPE_6]),
    set([FORMAT_126, FINITION_DETRUIRE]),
    set([FORMAT_126, FINITION_BANDE]),
    set([FORMAT_126, FINITION_MISE_SOUS_CACHE]),
    # 127 
    set([FORMAT_127, FINITION_DECOUPE_4]),
    set([FORMAT_127, FINITION_DECOUPE_6]),
    set([FORMAT_127, FINITION_DETRUIRE]),
    set([FORMAT_127, FINITION_BANDE]),
    set([FORMAT_127, FINITION_MISE_SOUS_CACHE]),
    # 4x5"
    set([FORMAT_4x5, FINITION_DECOUPE_4]),
    set([FORMAT_4x5, FINITION_DECOUPE_6]),
    set([FORMAT_4x5, FINITION_DETRUIRE]),
    set([FORMAT_4x5, FINITION_BANDE]),
    set([FORMAT_4x5, FINITION_MISE_SOUS_CACHE]),
    # 8x10"
    set([FORMAT_8x10, FINITION_DECOUPE_4]),
    set([FORMAT_8x10, FINITION_DECOUPE_6]),
    set([FORMAT_8x10, FINITION_DETRUIRE]),
    set([FORMAT_8x10, FINITION_BANDE]),
    set([FORMAT_8x10, FINITION_MISE_SOUS_CACHE]),


    # --- Type et Finition (MSC seulement avec E6)
    set([FINITION_MISE_SOUS_CACHE, TYPE_C41_MACHINE]),
    set([FINITION_MISE_SOUS_CACHE, TYPE_C41_MANUEL]),
    set([FINITION_MISE_SOUS_CACHE, TYPE_NB_MACHINE]),
    set([FINITION_MISE_SOUS_CACHE, TYPE_NB_MANUEL]),
    set([FINITION_MISE_SOUS_CACHE, TYPE_NB_SCALA]),


    # --- Support et marges ---
    set([SUPPORT_AUCUN, MARGE_OUI]),
    set([SUPPORT_TIRAGE_LECTURE, MARGE_OUI]),
    set([SUPPORT_PLANCHE_CONTACT, MARGE_OUI]),
    set([SUPPORT_PLANCHE_CONTACT_MANUEL, MARGE_OUI]),
    set([SUPPORT_LOMOKINO, MARGE_OUI]),
    set([SUPPORT_SPINNER, MARGE_OUI]),
    set([SUPPORT_SPROCKET, MARGE_OUI]),
    set([SUPPORT_10x15, MARGE_NON]),
    set([SUPPORT_13x19, MARGE_NON]),
    set([SUPPORT_15x23, MARGE_NON]),


    # --- Support et rendu ---
    set([SUPPORT_AUCUN, RENDU_OUI]),
    set([SUPPORT_PLANCHE_CONTACT, RENDU_OUI]),
    set([SUPPORT_PLANCHE_CONTACT_MANUEL, RENDU_OUI]),
    set([SUPPORT_LOMOKINO, RENDU_OUI]),
    set([SUPPORT_10x15, RENDU_NON]),
    set([SUPPORT_13x19, RENDU_NON]),
    set([SUPPORT_15x23, RENDU_NON]),
    set([SUPPORT_SPINNER, RENDU_NON]),
    set([SUPPORT_SPROCKET, RENDU_NON]),
    set([SUPPORT_TIRAGE_LECTURE, RENDU_NON]),




    # --- Support et Numérisation ---
    # Lomokino
    set([SUPPORT_LOMOKINO, NUMERISATION_AUCUNE]),
    set([SUPPORT_LOMOKINO, NUMERISATION_HR500_SHD]),
    set([SUPPORT_LOMOKINO, NUMERISATION_HR500_UHD]),
    set([SUPPORT_LOMOKINO, NUMERISATION_HS1800_L]),
    set([SUPPORT_LOMOKINO, NUMERISATION_HS1800_XL]),
    set([SUPPORT_LOMOKINO, NUMERISATION_SD]),
    # Spinner
    set([SUPPORT_SPINNER, NUMERISATION_AUCUNE]),
    set([SUPPORT_SPINNER, NUMERISATION_HR500_SHD]),
    set([SUPPORT_SPINNER, NUMERISATION_HR500_UHD]),
    set([SUPPORT_SPINNER, NUMERISATION_HS1800_L]),
    set([SUPPORT_SPINNER, NUMERISATION_HS1800_XL]),
    set([SUPPORT_SPINNER, NUMERISATION_SD]),
    # Sprocket
    set([SUPPORT_SPROCKET, NUMERISATION_AUCUNE]),
    set([SUPPORT_SPROCKET, NUMERISATION_HR500_SHD]),
    set([SUPPORT_SPROCKET, NUMERISATION_HR500_UHD]),
    set([SUPPORT_SPROCKET, NUMERISATION_HS1800_L]),
    set([SUPPORT_SPROCKET, NUMERISATION_HS1800_XL]),
    set([SUPPORT_SPROCKET, NUMERISATION_SD]),


    # --- Scan (brut dispo) et numérisation
    set([SCAN_OUI, NUMERISATION_AUCUNE]),
    set([SCAN_OUI, NUMERISATION_SD]),


    # --- Express et qq chose ? ---
]