#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '📺 Canal Anime'
    ST_BN1_URL = 'https://t.me/Godanimes'
    ST_BN2_NAME = '🔄 Mise à jour'
    ST_BN2_URL = 'https://t.me/ZeeXDev'
    ST_MSG = '''<i>🤖 Ce bot peut sauvegarder tous vos liens/fichiers/torrents vers Google Drive ou tout cloud rclone, vers Telegram ou vers des serveurs DDL.</i>
<b>💡 Tapez {help_command} pour obtenir la liste des commandes disponibles</b>'''
    ST_BOTPM = '''<i>📩 Maintenant, ce bot enverra tous vos fichiers et liens ici. Commencez à l'utiliser...</i>'''
    ST_UNAUTH = '''<i>🔒 Vous n'êtes pas un utilisateur autorisé ! Déployez votre propre bot WZML-X Mirror-Leech</i>'''
    OWN_TOKEN_GENERATE = '''<b>⚠️ Le token temporaire ne vous appartient pas !</b>\n\n<i>🔑 Veuillez générer le vôtre.</i>'''
    USED_TOKEN = '''<b>⏳ Token temporaire déjà utilisé !</b>\n\n<i>🔄 Veuillez en générer un nouveau.</i>'''
    LOGGED_PASSWORD = '''<b>🔐 Bot déjà connecté via mot de passe</b>\n\n<i>❌ Inutile d'accepter des tokens temporaires.</i>'''
    ACTIVATE_BUTTON = '🔓 Activer le Token Temporaire'
    TOKEN_MSG = '''<b><u>🔑 Token de connexion temporaire généré !</u></b>
<b>🔢 Token temporaire :</b> <code>{token}</code>
<b>⏱ Validité :</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Activé ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>🔓 Le bot est déjà connecté !</b>'
    INVALID_PASS = '<b>❌ Mot de passe invalide !</b>\n\n🔑 Veuillez entrer le bon mot de passe.'
    PASS_LOGGED = '<b>🎉 Connexion permanente du bot réussie !</b>'
    LOGIN_USED = '<b>📝 Utilisation de la connexion :</b>\n\n<code>/cmd [motdepasse]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Afficher les logs'
    WEB_PASTE_BT = '📨 Coller en ligne (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = '📌 Basique'
    USER_BT = '👤 Utilisateurs'
    MICS_BT = '🔧 Divers'
    O_S_BT = '👑 Propriétaire & Sudos'
    CLOSE_BT = '❌ Fermer'
    HELP_HEADER = "㊂ <b><i>📚 Menu d'aide !</i></b>\n\n<b>💡 NOTE : <i>Cliquez sur n'importe quelle CMD pour plus de détails.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''⌬ <b><i>📊 STATISTIQUES DU BOT :</i></b>
┖ <b>⏱ Temps de fonctionnement :</b> {bot_uptime}

┎ <b><i>🧠 RAM (MÉMOIRE) :</i></b>
┃ {ram_bar} {ram}%
┖ <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

┎ <b><i>💾 MÉMOIRE SWAP :</i></b>
┃ {swap_bar} {swap}%
┖ <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

┎ <b><i>💽 DISQUE :</i></b>
┃ {disk_bar} {disk}%
┃ <b>📥 Lecture totale :</b> {disk_read}
┃ <b>📤 Écriture totale :</b> {disk_write}
┖ <b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}'''
    
    SYS_STATS = '''⌬ <b><i>🖥 SYSTÈME D'EXPLOITATION :</i></b>
├ <b>⏱ Temps de fonctionnement :</b> {os_uptime}
├ <b>🔄 Version OS :</b> {os_version}
┖ <b>🏗 Architecture OS :</b> {os_arch}

⌬ <b><i>🌐 STATISTIQUES RÉSEAU :</i></b>
├ <b>📤 Upload :</b> {up_data}
├ <b>📥 Download :</b> {dl_data}
├ <b>📨 Paquets envoyés :</b> {pkt_sent}k
├ <b>📩 Paquets reçus :</b> {pkt_recv}k
┖ <b>🔁 Données totales I/O :</b> {tl_data}

┎ <b>⚙️ CPU :</b>
┃ {cpu_bar} {cpu}%
├ <b>🌀 Fréquence CPU :</b> {cpu_freq}
├ <b>⚖️ Charge moyenne système :</b> {sys_load}
├ <b>🖥 Core(s) physiques :</b> {p_core} | <b>💻 Core(s) virtuels :</b> {v_core}
├ <b>🔢 Total Core(s) :</b> {total_core}
┖ <b>🚀 CPU(s) utilisables :</b> {cpu_use}'''
    
    REPO_STATS = '''⌬ <b><i>📦 STATISTIQUES DU DÉPÔT :</i></b>
├ <b>🔄 Bot mis à jour :</b> {last_commit}
├ <b>🏷 Version actuelle :</b> {bot_version}
├ <b>🆕 Dernière version :</b> {lat_version}
┖ <b>📝 Dernier changement :</b> {commit_details}

⌬ <b>📌 REMARQUES :</b> <code>{remarks}</code>'''
    
    BOT_LIMITS = '''⌬ <b><i>⚠️ LIMITES DU BOT :</i></b>
├ <b>📥 Limite directe :</b> {DL} GB
├ <b>🧲 Limite torrent :</b> {TL} GB
├ <b>☁️ Limite GDrive :</b> {GL} GB
├ <b>🎬 Limite YT-DLP :</b> {YL} GB
├ <b>🎵 Limite playlist :</b> {PL}
├ <b>🔐 Limite Mega :</b> {ML} GB
├ <b>♻️ Limite clone :</b> {CL} GB
┖ <b>📤 Limite leech :</b> {LL} GB

┎ <b>🔑 Validité du token :</b> {TV}
├ <b>⏱ Limite de temps utilisateur :</b> {UTI} / tâche
├ <b>🧵 Tâches parallèles utilisateur :</b> {UT}
┖ <b>🤖 Tâches parallèles du bot :</b> {BT}'''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>🔄 Redémarrage...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''⌬ <b><i>✅ Redémarré avec succès !</i></b>
├ <b>📅 Date :</b> {date}
├ <b>⏰ Heure :</b> {time}
├ <b>🌍 Fuseau horaire :</b> {timz}
┖ <b>🔄 Version :</b> {version}'''
    RESTARTED = '''⌬ <b><i>🤖 Bot redémarré !</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>🏓 Début du ping...</i>'
    PING_VALUE = '<b>🏓 Pong</b>\n<code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b><i>🚀 Tâche démarrée</i></b>
├ <b>🔧 Mode :</b> {Mode}
┖ <b>👤 Par :</b> {Tag}\n\n"""
    LINKS_SOURCE = """➪ <b>🔗 Source :</b>
┖ <b>⏰ Ajouté le :</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "➪ <b><u>🚀 Tâche démarrée :</u></b>\n┃\n┖ <b>🔗 Lien :</b> <a href='{msg_link}'>Cliquez ici</a>"
    L_LOG_START =           "➪ <b><u>📤 Leech démarré :</u></b>\n┃\n├ <b>👤 Utilisateur :</b> {mention} ( #ID{uid} )\n┖ <b>🔗 Source :</b> <a href='{msg_link}'>Cliquez ici</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b><i>📁 {Name}</i></b>\n┃\n'
    SIZE =                  '├ <b>📏 Taille : </b>{Size}\n'
    ELAPSE =                '├ <b>⏱ Temps écoulé : </b>{Time}\n'
    MODE =                  '├ <b>🔧 Mode : </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '├ <b>📦 Total fichiers : </b>{Files}\n'
    L_CORRUPTED_FILES =     '├ <b>⚠️ Fichiers corrompus : </b>{Corrupt}\n'
    L_CC =                  '┖ <b>👤 Par : </b>{Tag}\n\n'
    PM_BOT_MSG =            '➪ <b><i>📩 Fichier(s) envoyé(s) ci-dessus</i></b>'
    L_BOT_MSG =             '➪ <b><i>🔒 Fichier(s) envoyé(s) en MP du bot (Privé)</i></b>'
    L_LL_MSG =              '➪ <b><i>🔗 Fichier(s) envoyé(s). Accès via Liens...</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '├ <b>📝 Type : </b>{Mimetype}\n'
    M_SUBFOLD =             '├ <b>📂 Sous-dossiers : </b>{Folder}\n'
    TOTAL_FILES =           '├ <b>📦 Fichiers : </b>{Files}\n'
    RCPATH =                '├ <b>🗂 Chemin : </b><code>{RCpath}</code>\n'
    M_CC =                  '┖ <b>👤 Par : </b>{Tag}\n\n'
    M_BOT_MSG =             '➪ <b><i>🔗 Lien(s) envoyé(s) en MP du bot (Privé)</i></b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Lien Cloud'
    SAVE_MSG =        '💾 Sauvegarder'
    RCLONE_LINK =     '♻️ Lien RClone'
    DDL_LINK =        '📎 Lien {Serv}'
    SOURCE_URL =      '🔐 Lien Source'
    INDEX_LINK_F =    '🗂 Lien Index'
    INDEX_LINK_D =    '⚡ Lien Index'
    VIEW_LINK =       '👀 Voir Lien'
    CHECK_PM =        '📥 Voir en MP'
    CHECK_LL =        '📋 Voir dans logs'
    MEDIAINFO_LINK =  '📃 MediaInfo'
    SCREENSHOTS =     '🖼 Captures'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<code>📌 {Name}</code>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n┃ {Bar}'
    PROCESSED =         '\n├ <b>📊 Traité :</b> {Processed}'
    STATUS =            '\n├ <b>🔄 Statut :</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b>⏱ ETA :</b> {Eta}'
    SPEED =             '\n├ <b>🚀 Vitesse :</b> {Speed}'
    ELAPSED =                                     ' | <b>⏳ Temps écoulé :</b> {Elapsed}'
    ENGINE =            '\n├ <b>⚙️ Moteur :</b> {Engine}'
    STA_MODE =          '\n├ <b>🔧 Mode :</b> {Mode}'
    SEEDERS =           '\n├ <b>🌱 Seeders :</b> {Seeders} | '
    LEECHERS =                                           '<b>🔄 Leechers :</b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n├ <b>📏 Taille : </b>{Size}'
    SEED_SPEED =     '\n├ <b>🚀 Vitesse : </b> {Speed} | '
    UPLOADED =                                     '<b>📤 Uploadé : </b> {Upload}'
    RATIO =          '\n├ <b>📊 Ratio : </b> {Ratio} | '
    TIME =                                         '<b>⏱ Temps : </b> {Time}'
    SEED_ENGINE =    '\n├ <b>⚙️ Moteur :</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n├ <b>📏 Taille : </b>{Size}'
    NON_ENGINE =     '\n├ <b>⚙️ Moteur :</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n├ <b>👤 Utilisateur :</b> <code>{User}</code> | '
    ID =                                                        '<b>🆔 ID :</b> <code>{Id}</code>'
    BTSEL =          '\n├ <b>🔘 Sélection :</b> {Btsel}'
    CANCEL =         '\n┖ {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '⌬ <b><i>📊 Statistiques du bot</i></b>\n'
    TASKS =  '├ <b>📝 Tâches :</b> {Tasks}\n'
    BOT_TASKS = '├ <b>🧵 Tâches :</b> {Tasks}/{Ttask} | <b>🆓 DISP :</b> {Free}\n'
    Cpu = '├ <b>⚙️ CPU :</b> {cpu}% | '
    FREE =                      '<b>🆓 F :</b> {free} [{free_p}%]'
    Ram = '\n├ <b>🧠 RAM :</b> {ram}% | '
    uptime =                     '<b>⏱ UPTIME :</b> {uptime}'
    DL = '\n┖ <b>📥 DL :</b> {DL}/s | '
    UL =                        '<b>📤 UL :</b> {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = '⟸'
    REFRESH = '🔄 ᴘᴀɢᴇs\n{Page}'
    NEXT = '⟹'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = '⚠️ Le fichier/dossier est déjà disponible sur Drive.\n🔍 Voici les résultats {content} :'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>🧮 Comptage :</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>📌 {COUNT_NAME}</i></b>\n┃\n'
    COUNT_SIZE = '├ <b>📏 Taille : </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '├ <b>📝 Type : </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '├ <b>📂 Sous-dossiers : </b>{COUNT_SUB}\n'
    COUNT_FILE = '├ <b>📦 Fichiers : </b>{COUNT_FILE}\n'
    COUNT_CC =   '┖ <b>👤 Par : </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>🔍 Recherche de <i>{NAME}</i></b>'
    LIST_FOUND = '<b>✅ {NO} résultat trouvé pour <i>{NAME}</i></b>'
    LIST_NOT_FOUND = '❌ Aucun résultat trouvé pour <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>💤 Aucun téléchargement actif !</i>
    
⌬ <b><i>📊 Statistiques du bot</i></b>
├ <b>⚙️ CPU :</b> {cpu}% | <b>🆓 F :</b> {free} [{free_p}%]
┖ <b>🧠 RAM :</b> {ram} | <b>⏱ UPTIME :</b> {uptime}'''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''㊂ <b><u>⚙️ Paramètres utilisateur :</u></b>
        
┎<b> 📛 Nom :</b> {NAME} ( <code>{ID}</code> )
├<b> 👤 Nom d'utilisateur :</b> {USERNAME}
├<b> 🌐 DC Telegram :</b> {DC}
┖<b> 🈯 Langue :</b> {LANG}

➪ <u><b>📝 Arguments disponibles :</b></u>
• <b>-s</b> ou <b>-set</b> : Définir directement via argument'''

    UNIVERSAL = '''㊂ <b><u>🌍 Paramètres universels : {NAME}</u></b>

┎<b> 🎬 Options YT-DLP :</b> <code>{YT}</code>
├<b> 📅 Tâches quotidiennes :</b> <code>{DT}</code> par jour
├<b> ⏱ Dernière utilisation :</b> <code>{LAST_USED}</code>
├<b> 🔑 Session utilisateur :</b> <code>{USESS}</code>
├<b> ℹ️ Mode MediaInfo :</b> <code>{MEDIAINFO}</code>
├<b> 💾 Mode sauvegarde :</b> <code>{SAVE_MODE}</code>
┖<b> 🤖 MP du bot :</b> <code>{BOT_PM}</code>'''

    MIRROR = '''㊂ <b><u>🔄 Paramètres Mirror/Clone : {NAME}</u></b>

┎<b> ⚙️ Config RClone :</b> <i>{RCLONE}</i>
├<b> 🔤 Préfixe Mirror :</b> <code>{MPREFIX}</code>
├<b> 🔤 Suffixe Mirror :</b> <code>{MSUFFIX}</code>
├<b> ✏️ Renommage Mirror :</b> <code>{MREMNAME}</code>
├<b> 🌐 Serveur(s) DDL :</b> <i>{DDL_SERVER}</i>
├<b> 📂 Mode TD utilisateur :</b> <i>{TMODE}</i>
├<b> 🔢 Total TD(s) utilisateur :</b> <i>{USERTD}</i>
┖<b> 📅 Mirror quotidien :</b> <code>{DM}</code> par jour'''

    LEECH = '''㊂ <b><u>📤 Paramètres Leech pour {NAME}</u></b>

┎<b> 📅 Leech quotidien : </b><code>{DL}</code> par jour
├<b> 📝 Type Leech :</b> <i>{LTYPE}</i>
├<b> 🖼 Miniature personnalisée :</b> <i>{THUMB}</i>
├<b> ✂️ Taille de division Leech :</b> <code>{SPLIT_SIZE}</code>
├<b> ⚖️ Divisions égales :</b> <i>{EQUAL_SPLIT}</i>
├<b> 🖼 Groupe média :</b> <i>{MEDIA_GROUP}</i>
├<b> 📝 Légende Leech :</b> <code>{LCAPTION}</code>
├<b> 🔤 Préfixe Leech :</b> <code>{LPREFIX}</code>
├<b> 🔤 Suffixe Leech :</b> <code>{LSUFFIX}</code>
├<b> 🗑 Dumps Leech :</b> <code>{LDUMP}</code>
┖<b> ✏️ Renommage Leech :</b> <code>{LREMNAME}</code>'''