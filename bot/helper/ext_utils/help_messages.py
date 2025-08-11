#!/usr/bin/env python3
from bot.helper.telegram_helper.bot_commands import BotCommands

YT_HELP_MESSAGE = ["""<i>Envoyez des liens/fichiers avec la commande ou en réponse à la commande pour mirror ou leech les sites supportés par ytdl sur Telegram, GDrive ou DDL avec différents moteurs comme RClone ou yt-dlp</i>

➲ <b><u>Arguments disponibles</u></b> :

1.  <b>-n ou -name :</b> Renommer le fichier.
2.  <b>-z ou -zip :</b> Zipper les fichiers ou liens
3.  <b>-up ou -upload :</b> Uploader vers votre Drive, RClone ou DDL
4.  <b>-b ou -bulk :</b> Télécharger plusieurs liens en masse.
5.  <b>-i :</b> Télécharger plusieurs liens par réponse
6.  <b>-m ou -sd ou -samedir :</b> Télécharger plusieurs liens dans le même répertoire d'upload.
7.  <b>-opt ou -options :</b> Ajouter des options personnalisées yt-dlp au lien
8.  <b>-s ou -select :</b> Sélectionner des fichiers depuis les liens yt-dlp même si la qualité est spécifiée
9.  <b>-rcf :</b> Flags supplémentaires RClone
10. <b>-id :</b> ID ou lien du dossier GDrive
11. <b>-index:</b> URL d'index pour gdrive_arg
12. <b>-c ou -category :</b> Catégorie GDrive pour l'upload, nom spécifique (insensible à la casse)
13. <b>-ud ou -dump :</b> Catégorie de dump pour l'upload, nom spécifique (insensible à la casse) ou chat_id ou nom d'utilisateur
14. <b>-ss ou -screenshots :</b> Générer des captures d'écran pour les fichiers leechés
15. <b>-t ou -thumb :</b> Miniature personnalisée pour un leech spécifique
""", """
➲ <b><i>Envoyer un lien avec la ligne de commande</i></b> :
<code>/cmd</code> lien -s -n nouveau nom -opt x:y|x1:y1

➲ <b><i>En répondant à un lien</i></b> :
<code>/cmd</code> -n nouveau nom -z mot de passe -opt x:y|x1:y1

➲ <b><i>Nouveau nom</i></b> : -n ou -name
<code>/cmd</code> lien -n nouveau nom
<b>Note :</b> Ne pas ajouter l'extension du fichier

➲ <b><i>Génération de captures d'écran</b> : -ss ou -screenshots
<code>/cmd</code> lien -ss nombre ,Captures d'écran pour chaque fichier vidéo

➲ <b><i>Miniature personnalisée</b> : -t ou -thumb
<code>/cmd</code> lien -t lien_tg|lien_dl
<b>Lien direct :</b> lien_dl spécifie le lien de téléchargement, qui doit être une URL d'image
<b>Lien Telegram :</b> Donnez un lien public/privé/super pour télécharger l'image depuis Telegram

➲ <b><i>Boutons de qualité</i></b> : -s ou -select
Si la qualité par défaut est ajoutée via les options yt-dlp et que vous devez sélectionner la qualité pour un lien spécifique ou des liens avec la fonction multi-liens.
<code>/cmd</code> lien -s

➲ <b<i>Zipper des fichiers (avec/sans mot de passe)</i></b> : -z ou -zip motdepasse
<code>/cmd</code> lien -z (zip)
<code>/cmd</code> lien -z motdepasse (zip protégé par mot de passe)

➲ <b><i>Options</i></b> : -opt ou -options
<code>/cmd</code> lien -opt playliststart:^10|fragment_retries:^inf|matchtitle:S13|writesubtitles:true|live_from_start:true|postprocessor_args:{"ffmpeg": ["-threads", "4"]}|wait_for_video:(5, 100)
<b>Note :</b> Ajoutez `^` avant un entier ou un float, certaines valeurs doivent être numériques et d'autres en string.
Comme playlist_items:10 fonctionne avec string, pas besoin d'ajouter `^` avant le nombre mais playlistend ne fonctionne qu'avec un entier donc vous devez ajouter `^` comme dans l'exemple ci-dessus.
Vous pouvez ajouter des tuples et des dict aussi. Utilisez des guillemets doubles dans les dict.

➲ <b><i>Multi-liens uniquement en répondant au premier lien</i></b> : -i
<code>/cmd</code> -i 10(nombre de liens)

➲ <b><i>Multi-liens dans le même répertoire d'upload uniquement en répondant au premier lien</i></b> : -m ou -sd ou -samedir
<code>/cmd</code> -i 10(nombre de liens) -m nom du dossier

➲ <b><i>Upload vers un Drive personnalisé :</i></b> -id & -index(Optionnel)
<code>/{cmd}</code> -id <code>lien_dossier_drive</code> ou <code>id_drive</code> -index <code>https://example.com/0:</code>
Ici, drive_id doit être un ID de dossier ou un lien de dossier et index doit être une URL sinon ce ne sera pas accepté.

➲ <b><i>Sélection de catégorie personnalisée :</i></b> -c ou -category
<code>/{cmd}</code> -c <code>nom_catégorie</code>
Ceci fonctionne pour les catégories du bot ainsi que les UserTDs (si activés)
Vous pouvez aussi sélectionner l'upload Drive depuis les boutons si vous en avez plus d'un et que cet argument n'est pas spécifié

➲ <b><i>Sélection de dump personnalisé :</i></b> -ud ou -dump
<code>/{cmd}</code> -ud <code>nom_dump</code> ou <code>@username</code> ou <code>-100xxxxxx chat_id</code> ou all
Vous pouvez aussi sélectionner le chat de dump depuis les boutons si vous en avez plus d'un et que cet argument n'est pas spécifié
Utilisez -ud all pour uploader dans tous vos chats de dump
Assurez-vous que le bot est déjà admin sinon ce ne sera pas accepté.

➲ <b><i>Upload</i></b> : -up ou -upload
<code>/cmd</code> lien -up <code>rcl</code> (Pour sélectionner la config rclone, remote et path)
<code>/cmd</code> lien -up <code>ddl</code>
Vous pouvez directement ajouter le chemin d'upload : -up remote:dir/subdir

Si DEFAULT_UPLOAD est `rc` alors vous pouvez passer up: `gd` pour uploader en utilisant les outils gdrive vers GDRIVE_ID.
Si DEFAULT_UPLOAD est `gd` alors vous pouvez passer up: `rc` pour uploader vers RCLONE_PATH.
Si DEFAULT_UPLOAD est `ddl` alors vous pouvez passer up: `rc` ou `gd` pour uploader vers RCLONE_PATH ou GDRIVE_ID
Si vous voulez ajouter un chemin manuellement depuis votre config (uploadé depuis usetting) ajoutez <code>mrcc:</code> avant le chemin sans espace
<code>/cmd</code> lien -up <code>mrcc:</code>main:dump

➲ <b><i>Flags RClone</i></b> : -rcf
<code>/cmd</code> lien -up path|rcl -rcf --buffer-size:8M|--drive-starred-only|key|key:value
Ceci remplacera tous les autres flags sauf --exclude
Voir tous les <a href='https://rclone.org/flags/'>RcloneFlags</a>.

➲ <b><i>Téléchargement en masse</i></b> : -b ou -bulk
Bulk peut être utilisé par message texte ou en répondant à un fichier texte contenant des liens séparés par des nouvelles lignes.
Vous ne pouvez l'utiliser qu'en répondant à un message(texte/fichier).
Toutes les options doivent être avec le lien !
<b>Exemple :</b>
lien1 -n nouveau nom -up remote1:path1 -rcf |key:value|key:value
lien2 -z -n nouveau nom -up remote2:path2
lien3 -z -n nouveau nom -opt ytdlpoptions

<b>Note :</b> Vous ne pouvez pas ajouter l'arg -m pour certains liens seulement, faites-le pour tous les liens ou utilisez multi sans bulk !
lien pswd: pass(zip) opt: ytdlpoptions up: remote2:path2
Répondez à cet exemple avec cette cmd <code>/cmd</code> b(bulk)
Vous pouvez définir le début et la fin des liens dans le bulk avec -b début:fin ou seulement la fin avec -b :fin ou seulement le début avec -b début. Par défaut, le début est à zéro(premier lien) jusqu'à inf.

➲ <b>NOTES :</b>
Voir toutes les options API yt-dlp depuis ce <a href='https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184'>FICHIER</a>
"""]

MIRROR_HELP_MESSAGE = ["""<i>Envoyez des liens/fichiers avec la commande ou en réponse à la commande pour mirror ou leech sur Telegram, GDrive ou DDL avec différents moteurs comme RClone, Aria2 ou qBit</i>

➲ <b><u>Arguments disponibles</u></b> :

1.  <b>-n ou -name :</b> Renommer le fichier.
2.  <b>-z ou -zip :</b> Zipper les fichiers ou liens
3.  <b>-e ou -extract ou -uz ou -unzip :</b> Extraire/Dézipper des fichiers depuis une archive
4.  <b>-up ou -upload :</b> Uploader vers votre Drive, RClone ou DDL
6.  <b>-b ou -bulk :</b> Télécharger plusieurs liens en masse.
7.  <b>-i :</b> Télécharger plusieurs liens par réponse
9.  <b>-m ou -sd ou -samedir :</b> Télécharger plusieurs liens dans le même répertoire d'upload.
10. <b>-d ou -seed :</b> Seed un torrent Bittorrent.
11. <b>-s ou -select :</b> Sélectionner des fichiers depuis un torrent via Bittorrent
12. <b>-u ou -user :</b> Entrer un nom d'utilisateur pour l'authentification
13. <b>-p ou -pass :</b> Entrer un mot de passe pour l'authentification
14. <b>-j ou -join :</b> Joindre plusieurs fichiers.
15. <b>-rcf :</b> Flags supplémentaires RClone
16. <b>-id :</b> ID ou lien du dossier GDrive
17. <b>-index:</b> URL d'index pour gdrive_arg
18. <b>-c ou -category :</b> Catégorie GDrive pour l'upload, nom spécifique (insensible à la casse)
19. <b>-ud ou -dump :</b> Catégorie de dump pour l'upload, nom spécifique (insensible à la casse) ou chat_id ou nom d'utilisateur
20. <b>-ss ou -screenshots :</b> Générer des captures d'écran pour les fichiers leechés
21. <b>-t ou -thumb :</b> Miniature personnalisée pour un leech spécifique
""", """
➲ <b><i>Avec la commande</i></b> :
<code>/cmd</code> lien -n nouveau nom

➲ <b><i>En répondant à un lien/fichier</i></b> :
<code>/cmd</code> -n nouveau nom -z -e -up destination_upload

➲ <b><i>Nouveau nom personnalisé</i></b> : -n ou -name
<code>/cmd</code> lien -n nouveau nom
<b>NOTES</b> : Ne fonctionne pas avec les torrents.

➲ <b><i>Authentification lien direct</i></b> : -u -p ou -user -pass
<code>/cmd</code> lien -u nom_utilisateur -p mot_de_passe

➲ <b><i>En-têtes personnalisés lien direct</i></b> : -h ou -headers
<code>/cmd</code> lien -h clé: valeur clé1: valeur1

➲ <b><i>Génération de captures d'écran</b> : -ss ou -screenshots
<code>/cmd</code> lien -ss nombre ,Captures d'écran pour chaque fichier vidéo

➲ <b><i>Miniature personnalisée</b> : -t ou -thumb
<code>/cmd</code> lien -t lien_tg|lien_dl
<b>Lien direct :</b> lien_dl spécifie le lien de téléchargement, qui doit être une URL d'image
<b>Lien Telegram :</b> Donnez un lien public/privé/super pour télécharger l'image depuis Telegram

➲ <b><i>Extraire / Zipper</i></b> : -uz -z ou -zip -unzip ou -e -extract
<code>/cmd</code> lien -e motdepasse (extraire protégé par mot de passe)
<code>/cmd</code> lien -z motdepasse (zipper protégé par mot de passe)
<code>/cmd</code> lien -z motdepasse -e (extraire et zipper protégé par mot de passe)
<code>/cmd</code> lien -e motdepasse -z motdepasse (extraire protégé par mot de passe et zipper protégé par mot de passe)
<b>NOTES :</b> Quand extract et zip sont ajoutés avec la cmd, cela extraira d'abord puis zippera, donc toujours extraire en premier

➲ <b><i>Sélection qBittorrent</i></b> : -s ou -select
<code>/cmd</code> lien -s ou en répondant à un fichier/lien

➲ <b><i>Seed qBittorrent / Aria2</i></b> : -d ou -seed
<code>/cmd</code> lien -d ratio:temps_seed ou en répondant à un fichier/lien
Pour spécifier ratio et temps de seed, ajoutez -d ratio:temps. Ex : -d 0.7:10 (ratio et temps) ou -d 0.7 (seulement ratio) ou -d :10 (seulement temps) où le temps est en minutes.

➲ <b><i>Multi-liens uniquement en répondant au premier lien/fichier</i></b> : -i
<code>/cmd</code> -i 10(nombre de liens/fichiers)

➲ <b><i>Multi-liens dans le même répertoire d'upload uniquement en répondant au premier lien/fichier</i></b> : -m ou -sd ou -samedir
<code>/cmd</code> -i 10(nombre de liens/fichiers) -m nom du dossier (multi message)
<code>/cmd</code> -b -m nom du dossier (message/fichier en masse)

➲ <b><i>Upload vers un Drive personnalisé :</i></b> -id & -index(Optionnel)
<code>/{cmd}</code> -id <code>lien_dossier_drive</code> ou <code>id_drive</code> -index <code>https://example.com/0:</code>
Ici, drive_id doit être un ID de dossier ou un lien de dossier et index doit être une URL sinon ce ne sera pas accepté.

➲ <b><i>Sélection de catégorie personnalisée :</i></b> -c ou -category
<code>/{cmd}</code> -c <code>nom_catégorie</code>
Ceci fonctionne pour les catégories du bot ainsi que les UserTDs (si activés)
Vous pouvez aussi sélectionner l'upload Drive depuis les boutons si vous en avez plus d'un et que cet argument n'est pas spécifié

➲ <b><i>Sélection de dump personnalisé :</i></b> -ud ou -dump
<code>/{cmd}</code> -ud <code>nom_dump</code> ou <code>@username</code> ou <code>-100xxxxxx chat_id</code> ou all
Vous pouvez aussi sélectionner le chat de dump depuis les boutons si vous en avez plus d'un et que cet argument n'est pas spécifié
Utilisez -ud all pour uploader dans tous vos chats de dump
Assurez-vous que le bot est déjà admin sinon ce ne sera pas accepté.

➲ <b><i>Upload personnalisé</i></b> : -up ou -upload
<code>/cmd</code> lien -up <code>rcl</code> (Pour sélectionner la config rclone, remote et path)
<code>/cmd</code> lien -up <code>ddl</code>
Vous pouvez directement ajouter le chemin d'upload : -up remote:dir/subdir

Si DEFAULT_UPLOAD est `rc` alors vous pouvez passer up: `gd` pour uploader en utilisant les outils gdrive vers GDRIVE_ID.
Si DEFAULT_UPLOAD est `gd` alors vous pouvez passer up: `rc` pour uploader vers RCLONE_PATH.
Si DEFAULT_UPLOAD est `ddl` alors vous pouvez passer up: `rc` ou `gd` pour uploader vers RCLONE_PATH ou GDRIVE_ID
Si vous voulez ajouter un chemin manuellement depuis votre config (uploadé depuis usetting) ajoutez <code>mrcc:</code> avant le chemin sans espace
<code>/cmd</code> lien -up <code>mrcc:</code>main:dump

➲ <b><i>Flags RClone</i></b> : -rcf
<code>/cmd</code> lien|path|rcl -up path|rcl -rcf --buffer-size:8M|--drive-starred-only|key|key:value
Ceci remplacera tous les autres flags sauf --exclude
Voir tous les <a href='https://rclone.org/flags/'>RcloneFlags</a>.

➲ <b><i>Téléchargement en masse</i></b> : -b ou -bulk
Bulk peut être utilisé par message texte ou en répondant à un fichier texte contenant des liens séparés par des nouvelles lignes.
Vous ne pouvez l'utiliser qu'en répondant à un message(texte/fichier).
Toutes les options doivent être avec le lien !
<b>Quelques exemples :</b>
lien1 -n nouveau nom -up remote1:path1 -rcf |key:value|key:value
lien2 -z -n nouveau nom -up remote2:path2
lien3 -uz -n nouveau nom -up remote2:path2
<b>NOTES :</b> Vous ne pouvez pas ajouter l'arg -m pour certains liens seulement, faites-le pour tous les liens ou utilisez multi sans bulk !
Répondez à cet exemple avec cette cmd <code>/cmd</code> -b(bulk)
Vous pouvez définir le début et la fin des liens dans le bulk comme seed, avec -b début:fin ou seulement la fin avec -b :fin ou seulement le début avec -b début. Par défaut, le début est à zéro(premier lien) jusqu'à inf.

➲ <b><i>Joindre des fichiers divisés</i></b> : -j ou -join
Cette option ne fonctionnera qu'avant extract et zip, donc sera principalement utilisée avec l'argument -m (samedir)
Cette option n'est pas pour fusionner deux liens/fichiers.
<b>Par réponse :</b>
<code>/cmd</code> -i 3 -j -m nom du dossier
<code>/cmd</code> -b -j -m nom du dossier
Si vous avez un lien avec des fichiers divisés :
<code>/cmd</code> lien -j

➲ <b><i>Téléchargement RClone</i></b> :
Traiter les chemins rclone exactement comme des liens
<code>/cmd</code> main:dump/ubuntu.iso ou <code>rcl</code>(Pour sélectionner config, remote et path)
Les utilisateurs peuvent ajouter leur propre rclone depuis les paramètres utilisateur

Si vous voulez ajouter un chemin manuellement depuis votre config, ajoutez <code>mrcc:</code> avant le chemin sans espace
<code>/cmd</code> <code>mrcc:</code>main:dump/ubuntu.iso

➲ <b><i>Liens Telegram</i></b> :
Traiter les liens tg comme n'importe quel lien direct
Certains liens nécessitent un accès utilisateur donc assurez-vous d'ajouter USER_SESSION_STRING pour cela.
<b><u>Types de liens :</u></b>
• <b>Public :</b> <code>https://t.me/channel_name/message_id</code>
• <b>Privé :</b> <code>tg://openmessage?user_id=xxxxxx&message_id=xxxxx</code>
• <b>Super :</b> <code>https://t.me/c/channel_id/message_id</code>

➲ <b>NOTES :</b>
1. Les commandes qui commencent par <b>qb</b> sont UNIQUEMENT pour les torrents.
"""]

RSS_HELP_MESSAGE = """
➲ <b>Format pour ajouter une URL de flux :</b>
Titre1 lien (requis)
Titre2 lien -c cmd -inf xx -exf xx
Titre3 lien -c cmd -d ratio:time -z motdepasse

➲ <b><i>Détails des arguments :</i></b>
-c commande + n'importe quel arg
-inf Pour le filtre des mots inclus.
-exf Pour le filtre des mots exclus.

<b>Exemple :</b> Titre https://www.rss-url.com inf: 1080 ou 720 ou 144p|mkv ou mp4|hevc exf: flv ou web|xxx opt: up: mrcc:remote:path/subdir rcf: --buffer-size:8M|key|key:value
Ce filtre analysera les liens dont les titres contiennent `(1080 ou 720 ou 144p) et (mkv ou mp4) et hevc` et ne contiennent pas (flv ou web) et xxx`. Vous pouvez ajouter ce que vous voulez.

Autre exemple : inf:  1080  ou 720p|.web. ou .webrip.|hvec ou x264. Ceci analysera les titres qui contiennent ( 1080  ou 720p) et (.web. ou .webrip.) et (hvec ou x264). J'ai ajouté un espace avant et après 1080 pour éviter les mauvais matchs. Si ce nombre `10805695` est dans le titre, il matchera 1080 si ajouté sans espaces après.

➲ <b><i>Notes sur les filtres :</i></b>
1. | signifie et.
2. Ajoutez `or` entre des clés similaires, vous pouvez l'ajouter entre des qualités ou entre des extensions, donc n'ajoutez pas de filtre comme ça f: 1080|mp4 ou 720|web car ceci analysera 1080 et (mp4 ou 720) et web ... pas (1080 et mp4) ou (720 et web)."
3. Vous pouvez ajouter `or` et `|` autant que vous voulez."
4. Regardez le titre s'il a un caractère spécial statique après ou avant les qualités ou extensions ou autre et utilisez-les dans le filtre pour éviter les mauvais matchs.

<b>Timeout :</b> 60 sec.
"""

CLONE_HELP_MESSAGE = ["""<i>Envoyez un lien Gdrive | Gdtot | Filepress | Filebee | Appdrive | Gdflix ou un chemin RClone avec ou en répondant au lien/rc_path par commande avec args.</i>

➲ <b><u>Arguments disponibles</u></b> :

1. <b>-up ou -upload :</b> Uploader vers votre Drive, RClone ou DDL
2. <b>-i :</b> Télécharger plusieurs liens par réponse
3. <b>-rcf :</b> Flags supplémentaires RClone
4. <b>-id :</b> ID ou lien du dossier GDrive
5. <b>-index:</b> URL d'index pour gdrive_arg
6. <b>-c ou -category :</b> Catégorie GDrive pour l'upload, nom spécifique (insensible à la casse)""",
"""➲ <b><i>Liens :</i></b>
Gdrive | Gdtot | Filepress | Filebee | Appdrive | Gdflix link ou chemin rclone

➲ <b><i>Multi-liens (uniquement en répondant au premier gdlink ou rclone_path) :</i></b>
<code>/cmd</code> -i 10(nombre de liens/chemins)

➲ <b><i>Lien Gdrive :</i></b>
<code>/cmd</code> lien_gdrive

➲ <b><i>Chemin RClone avec Flags RC :</i></b> -rcf
<code>/cmd</code> (rcl ou rclone_path) -up (rcl ou rclone_path) -rcf flagkey:flagvalue|flagkey|flagkey:flagvalue

➲ <b><i>Upload vers un Drive personnalisé :</i></b> -id & -index(Optionnel)
<code>/{cmd}</code> -id <code>lien_dossier_drive</code> ou <code>id_drive</code> -index <code>https://example.com/0:</code>

➲ <b><i>Sélection de catégorie personnalisée :</i></b> -c ou -category
<code>/{cmd}</code> -c <code>nom_catégorie</code>

<b>NOTES :</b>
1. Si -up ou -upload n'est pas spécifié alors la destination rclone sera RCLONE_PATH depuis <code>config.env</code>.
2. Si UserTD est activé, alors il uploadera uniquement vers UserTD soit par argument direct soit par boutons de catégorie.
3. Pour les multi-uploads personnalisés, utilisez toujours l'argument dans les messages respectifs puis répondez avec /cmd -i 10(nombre)
"""]

CATEGORY_HELP_MESSAGE = """Répondez à un /{cmd} actif qui a été utilisé pour démarrer le téléchargement ou ajoutez gid avec {cmd}
Cette commande sert principalement à changer de catégorie si vous décidez de changer de catégorie depuis un téléchargement déjà ajouté.
Mais vous pouvez toujours utiliser -c ou -category avec pour sélectionner une catégorie avant le début du téléchargement.

➲ <b><i>Upload vers un Drive personnalisé</i></b>
<code>/{cmd}</code> -id <code>lien_dossier_drive</code> ou <code>id_drive</code> -index <code>https://example.com/0:</code> gid ou en répondant à un téléchargement actif

<b>NOTE :</b> drive_id doit être un ID de dossier ou un lien de dossier et index doit être une URL sinon ce ne sera pas accepté.
"""

help_string = [f'''⌬ <b><i>Commandes de base !</i></b>

<b>Utilisez les commandes Mirror pour télécharger votre lien/fichier/rcl</b>
┠ /{BotCommands.MirrorCommand[0]} ou /{BotCommands.MirrorCommand[1]}: Télécharger via fichier/url/media pour uploader vers le Cloud Drive.
┖ /{BotCommands.CategorySelect}: Sélectionner une catégorie personnalisée pour uploader vers le Cloud Drive depuis UserTds ou les catégories du bot.

<b>Utilisez les commandes qBit uniquement pour les torrents :</b>
┠ /{BotCommands.QbMirrorCommand[0]} ou /{BotCommands.QbMirrorCommand[1]}: Télécharger en utilisant qBittorrent et uploader vers le Cloud Drive.
┖ /{BotCommands.BtSelectCommand}: Sélectionner des fichiers depuis les torrents par btsel_gid ou réponse.

<b>Utilisez les commandes yt-dlp pour YouTube ou tout site supporté :</b>
┖ /{BotCommands.YtdlCommand[0]} ou /{BotCommands.YtdlCommand[1]}: Mirror un lien supporté par yt-dlp.

<b>Utilisez les commandes Leech pour uploader vers Telegram :</b>
┠ /{BotCommands.LeechCommand[0]} ou /{BotCommands.LeechCommand[1]}: Uploader vers Telegram.
┠ /{BotCommands.QbLeechCommand[0]} ou /{BotCommands.QbLeechCommand[1]}: Télécharger en utilisant qBittorrent et uploader vers Telegram(Uniquement pour les torrents).
┖ /{BotCommands.YtdlLeechCommand[0]} ou /{BotCommands.YtdlLeechCommand[1]}: Télécharger en utilisant Yt-Dlp(lien supporté) et uploader vers telegram.

<b>Commandes G-Drive :</b>
┠ /{BotCommands.CloneCommand[0]}: Copier un fichier/dossier vers le Cloud Drive.
┠ /{BotCommands.CountCommand} [drive_url]: Compter les fichiers/dossiers de Google Drive.
┖ /{BotCommands.DeleteCommand} [drive_url]: Supprimer un fichier/dossier de Google Drive (Uniquement Owner & Sudo).

<b>Annuler les tâches :</b>
┖ /{BotCommands.CancelMirror}: Annuler une tâche par cancel_gid ou réponse.''',

f'''⌬ <b><i>Commandes utilisateurs !</i></b>

<b>Paramètres du bot :</b>
┖ /{BotCommands.UserSetCommand[0]} ou /{BotCommands.UserSetCommand[1]} [requête]: Ouvrir les paramètres utilisateur (MP aussi)

<b>Authentification :</b>
┖ /login: Se connecter au bot pour accéder au bot sans système de mot de passe temporaire (Privé)

<b>Statistiques du bot :</b>
┠ /{BotCommands.StatusCommand[0]} ou /{BotCommands.StatusCommand[1]}: Affiche une page de statut de toutes les tâches actives.
┠ /{BotCommands.StatsCommand[0]} ou /{BotCommands.StatsCommand[1]}: Affiche les statistiques détaillées du serveur.
┖ /{BotCommands.PingCommand[0]} ou /{BotCommands.PingCommand[1]}: Vérifier le temps que prend le ping du bot.

<b>Flux RSS :</b>
┖ /{BotCommands.RssCommand}: Ouvrir le menu RSS (Sub/Unsub/Start/Pause)''',

f'''⌬ <b><i>Commandes Owner ou Sudos !</i></b>

<b>Paramètres du bot :</b>
┠ /{BotCommands.BotSetCommand[0]} ou /{BotCommands.BotSetCommand[1]} [requête]: Ouvrir les paramètres du bot (Uniquement Owner & Sudo).
┖ /{BotCommands.UsersCommand}: Afficher les infos statistiques des utilisateurs (Uniquement Owner & Sudo).

<b>Authentification :</b>
┠ /{BotCommands.AuthorizeCommand[0]} ou /{BotCommands.AuthorizeCommand[1]}: Autoriser un chat ou un utilisateur à utiliser le bot (Uniquement Owner & Sudo).
┠ /{BotCommands.UnAuthorizeCommand[0]} ou /{BotCommands.UnAuthorizeCommand[1]}: Désautoriser un chat ou un utilisateur à utiliser le bot (Uniquement Owner & Sudo).
┠ /{BotCommands.AddSudoCommand}: Ajouter un utilisateur sudo (Uniquement Owner).
┠ /{BotCommands.RmSudoCommand}: Supprimer des utilisateurs sudo (Uniquement Owner).
┠ /{BotCommands.AddBlackListCommand[0]} ou /{BotCommands.AddBlackListCommand[1]}: Ajouter un utilisateur en liste noire, pour qu'il ne puisse plus utiliser le bot.
┖ /{BotCommands.RmBlackListCommand[0]} ou /{BotCommands.RmBlackListCommand[1]}: Supprimer un utilisateur de la liste noire, pour qu'il puisse à nouveau utiliser le bot.

<b>Statistiques du bot :</b>
┖ /{BotCommands.BroadcastCommand[0]} ou /{BotCommands.BroadcastCommand[1]} [réponse_msg]: Diffuser aux utilisateurs en MP qui ont démarré le bot à tout moment.

<b>Commandes G-Drive :</b>
┖ /{BotCommands.GDCleanCommand[0]} ou /{BotCommands.GDCleanCommand[1]} [drive_id]: Supprimer tous les fichiers d'un dossier spécifique dans Google Drive.

<b>Annuler les tâches :</b>
┖ /{BotCommands.CancelAllCommand[0]}: Annuler toutes les tâches & /{BotCommands.CancelAllCommand[1]} pour plusieurs bots.

<b>Maintenance :</b>
┠ /{BotCommands.RestartCommand[0]} ou /{BotCommands.RestartCommand[1]}: Redémarrer et mettre à jour le bot (Uniquement Owner & Sudo).
┠ /{BotCommands.RestartCommand[2]}: Redémarrer et mettre à jour tous les bots (Uniquement Owner & Sudo).
┖ /{BotCommands.LogCommand}: Obtenir un fichier log du bot. Pratique pour les rapports de crash (Uniquement Owner & Sudo).

<b>Exécuteurs :</b>
┠ /{BotCommands.ShellCommand}: Exécuter des commandes shell (Uniquement Owner).
┠ /{BotCommands.EvalCommand}: Exécuter du code Python Ligne | Lignes (Uniquement Owner).
┠ /{BotCommands.ExecCommand}: Exécuter des commandes dans Exec (Uniquement Owner).
┠ /{BotCommands.ClearLocalsCommand}: Effacer les locals de {BotCommands.EvalCommand} ou {BotCommands.ExecCommand} (Uniquement Owner).
┖ /exportsession: Générer un StringSession utilisateur de la même version Pyro (Uniquement Owner).

<b>Flux RSS :</b>
┖ /{BotCommands.RssCommand}: Ouvrir le menu RSS (Sub/Unsub/Start/Pause)

<b>Extras :</b>
┠ /{BotCommands.AddImageCommand} [url/photo]: Ajouter des images dans le bot
┖ /{BotCommands.ImagesCommand}: Générer une grille d'images stockées.''',

f'''⌬ <b><i>Commandes diverses !</i></b>

<b>Extras :</b>
┠ /{BotCommands.SpeedCommand[0]} ou /{BotCommands.SpeedCommand[1]}: Vérifier la vitesse du VPS/Serveur.
┖ /{BotCommands.MediaInfoCommand[0]} ou /{BotCommands.MediaInfoCommand[1]} [url/media]: Générer des MediaInfo de Media ou URLs DL

<b>Recherche Torrent/Drive :</b>
┠ /{BotCommands.ListCommand} [requête]: Rechercher dans Google Drive(s).
┖ /{BotCommands.SearchCommand} [requête]: Rechercher des torrents avec API.

<b>Recherche Films/Séries/Dramas :</b>
┠ /{BotCommands.IMDBCommand}: Rechercher dans IMDB.
┠ /{BotCommands.AniListCommand}: Rechercher des anime dans AniList.
┠ /{BotCommands.AnimeHelpCommand}: Guide d'aide pour les anime.
┖ /{BotCommands.MyDramaListCommand}: Rechercher dans MyDramaList.
''']


PASSWORD_ERROR_MESSAGE = """
<b>Ce lien nécessite un mot de passe !</b>
- Insérez le signe <b>::</b> après le lien et écrivez le mot de passe après le signe.
<b>Exemple :</b> {}::love you
Note : Pas d'espaces entre les signes <b>::</b>
Pour le mot de passe, vous pouvez utiliser un espace !
"""

default_desp = {'AS_DOCUMENT': 'Type par défaut des uploads de fichiers Telegram. Par défaut False signifie comme média.',
                'ANIME_TEMPLATE': 'Définir un template pour le Template AniList. Balises HTML supportées',
                'AUTHORIZED_CHATS': 'Remplir user_id et chat_id des groupes/utilisateurs que vous voulez autoriser. Séparez-les par un espace.',
                'AUTO_DELETE_MESSAGE_DURATION': "Intervalle de temps (en secondes) après lequel le bot supprime son message et le message de commande qui est censé être vu instantanément.\n\n <b>NOTE :</b> Mettre à -1 pour désactiver la suppression automatique des messages.",
                'BASE_URL': 'URL BASE valide où le bot est déployé pour utiliser la sélection de fichiers web torrent. Le format de l\'URL devrait être http://myip, où myip est l\'IP/Domaine(public) de votre bot ou si vous avez choisi un port autre que 80 écrivez-le dans ce format http://myip:port (http et non https). Str',
                'BASE_URL_PORT': 'Quel est le port BASE_URL. Par défaut 80. Int',
                'BLACKLIST_USERS': 'Restreindre un utilisateur d\'utiliser le bot. Cela affichera un message BlackListé. USER_ID séparés par un espace. Str',
                'BOT_MAX_TASKS': 'Nombre maximum de tâches que le bot exécutera en parallèle. (Tâches en file d\'attente incluses). Int',
                'STORAGE_THRESHOLD': 'Pour laisser un espace de stockage spécifique libre et tout téléchargement qui conduirait à avoir moins d\'espace libre que cette valeur sera annulé, l\'unité par défaut est GB. Int',
                'LEECH_LIMIT':  'Pour limiter la taille des leech Torrent/Direct/ytdlp, l\'unité par défaut est GB. Int',
                'CLONE_LIMIT': 'Pour limiter la taille des dossiers/fichiers Google Drive que vous pouvez cloner, l\'unité par défaut est GB. Int',
                'MEGA_LIMIT': 'Pour limiter la taille des téléchargements Mega, l\'unité par défaut est GB. Int',
                'TORRENT_LIMIT': 'Pour limiter la taille des téléchargements torrent, l\'unité par défaut est GB. Int',
                'DIRECT_LIMIT': 'Pour limiter la taille des téléchargements de liens directs, l\'unité par défaut est GB. Int',
                'YTDLP_LIMIT': 'Pour limiter la taille des téléchargements ytdlp, l\'unité par défaut est GB. Int',
                'PLAYLIST_LIMIT': 'Pour limiter le nombre maximum de playlists. Int',
                'IMAGES': 'Ajouter plusieurs liens d\'images telegraph(graph.org) séparés par des espaces.',
                'IMG_SEARCH': 'Mettre un mot-clé pour télécharger des images. Séparez chaque nom par , comme anime, iron man, god of war',
                'IMG_PAGE': 'Définir la valeur de page pour télécharger une image. Chaque page a environ 70 images. Par défaut 1. Int',
                'IMDB_TEMPLATE': 'Définir le template IMBD par défaut du bot. Balises HTML, Emojis supportés. str',
                'AUTHOR_NAME': 'Nom d\'auteur pour les pages Telegraph, affiché dans la page Telegraph comme par AUTHOR_NAME',
                'AUTHOR_URL': 'URL d\'auteur pour la page Telegraph, mettez l\'URL de la chaîne pour afficher Rejoindre la chaîne. Str',
                'COVER_IMAGE': 'Image de couverture pour la page Telegraph. Mettez le lien d\'une photo Telegraph',
                'TITLE_NAME': 'Nom du titre pour les pages Telegraph (en utilisant la commande /list)',
                'GD_INFO': 'Description des fichiers uploadés vers gdrive en utilisant le bot',
                'DELETE_LINKS': 'Supprimer les liens TgLink/Magnet/Fichier au démarrage de la tâche pour nettoyer automatiquement le groupe. Par défaut False',
                'EXCEP_CHATS': 'Exceptions de chats qui n\'utiliseront pas les logs, chat_id séparés par un espace. Str',
                'SAFE_MODE': 'Masquer le nom de la tâche, le lien source et l\'indexation des liens Leech pour des précautions de sécurité. Par défaut False',
                'SOURCE_LINK': 'Ajouter un bouton supplémentaire de lien source qu\'il s\'agisse d\'un lien Magnet, Fichier ou DL. Par défaut False',
                'SHOW_EXTRA_CMDS': 'Ajouter des commandes supplémentaires à côté du format Arg pour -z ou -e. \n\n<b>COMMANDES : </b> /unzipxxx ou /zipxxx ou /uzx ou /zx',
                'BOT_THEME': 'Thème du bot à changer. Pour l\'instant le thème par défaut disponible est minimal. Vous pouvez créer votre propre thème et l\'ajouter dans BSet. \n\n<b>Format d\'exemple</b>: https://t.ly/9rVXq',
                'USER_MAX_TASKS': 'Limiter le nombre maximum de tâches pour les utilisateurs du groupe à la fois. utiliser Int',
                'DAILY_TASK_LIMIT': 'Nombre maximum de tâches qu\'un utilisateur peut faire en un jour. utiliser Int',
                'DISABLE_DRIVE_LINK': 'Désactiver le bouton de lien drive. Par défaut False. Bool',
                'DAILY_MIRROR_LIMIT': 'Taille totale jusqu\'à laquelle un utilisateur peut Mirror en un jour. l\'unité par défaut est GB. Int',
                'GDRIVE_LIMIT': 'Pour limiter la taille des liens de dossiers/fichiers Google Drive pour leech, Zip, Unzip. l\'unité par défaut est GB. Int',
                'DAILY_LEECH_LIMIT': 'Taille totale jusqu\'à laquelle un utilisateur peut Leech en un jour. l\'unité par défaut est GB. Int',
                'USER_TASKS_LIMIT': 'La limite maximum pour chaque utilisateur pour toutes les tâches. Int',
                'FSUB_IDS': 'Remplir chat_id(-100xxxxxx) des groupes/chaînes que vous voulez forcer à s\'abonner. Séparez-les par un espace. Int\n\nNote : Le bot doit être ajouté dans le chat_id rempli en tant qu\'admin',
                'BOT_PM': 'Envoyer les fichiers/liens aussi en MP du BOT. Par défaut False',
                'BOT_TOKEN': 'Le token du bot Telegram que vous avez obtenu depuis @BotFather',
                'CMD_SUFFIX': 'Numéro d\'index des commandes du bot Telegram ou texte personnalisé. Ceci sera ajouté à la fin de toutes les commandes sauf les commandes globales. Str',
                'DATABASE_URL': "Votre URL de base de données Mongo (chaîne de connexion). Suivez ce Generate Database pour générer une base de données. Les données seront sauvegardées dans la base de données : auth et sudo users, paramètres utilisateurs incluant les thumbnails pour chaque utilisateur, données rss et tâches incomplètes.\n\n <b>NOTE :</b> Vous pouvez toujours éditer tous les paramètres sauvegardés dans la base de données depuis le site officiel -> (Browse collections)",
                'DEFAULT_UPLOAD': 'Si rc pour uploader vers RCLONE_PATH ou gd pour uploader vers GDRIVE_ID ou ddl pour uploader vers DDLserver. Par défaut gd.',
                'DOWNLOAD_DIR': 'Le chemin vers le dossier local où les téléchargements devraient être téléchargés. ',
                'MDL_TEMPLATE': 'Définir le template personnalisé par défaut MyDramaList du bot. Balises HTML, Emojis supportés',
                'CLEAN_LOG_MSG': 'Nettoyer les logs Leech & les messages de début de tâche en MP du bot. Par défaut False',
                'LEECH_LOG_ID': "ID du chat où les fichiers leechés seront uploadés. Int. NOTE : Uniquement disponible pour les superGroup/chaîne. Ajoutez -100 avant l'id de la chaîne/superGroup. En bref n'ajoutez pas l'id du bot ou votre id !",
                'MIRROR_LOG_ID': "ID du chat où les fichiers Mirror seront envoyés. Int. NOTE : Uniquement disponible pour les superGroup/chaîne. Ajoutez -100 avant l'id de la chaîne/superGroup. En bref n'ajoutez pas l'id du bot ou votre id !. Pour plusieurs id, séparez-les par un espace.",
                'EQUAL_SPLITS': 'Diviser les fichiers plus grands que LEECH_SPLIT_SIZE en parties égales (Ne fonctionne pas avec la cmd zip). Par défaut False.',
                'EXTENSION_FILTER': "Extensions de fichiers qui ne seront pas uploadées/clonées. Séparez-les par un espace.",
                'GDRIVE_ID': 'Ceci est l\'ID de dossier/TeamDrive du Google Drive OR root vers lequel vous voulez uploader tous les mirrors en utilisant google-api-python-client.',
                'INCOMPLETE_TASK_NOTIFIER': 'Recevoir des messages de tâches incomplètes après redémarrage. Requiert une base de données et un superGroup. Par défaut False',
                'INDEX_URL': 'Voir https://gitlab.com/ParveenBhadooOfficial/Google-Drive-Index.',
                'IS_TEAM_DRIVE': 'Mettre True si upload vers TeamDrive en utilisant google-api-python-client. Par défaut False',
                'SHOW_MEDIAINFO': 'Ajouter un bouton pour afficher MediaInfo dans les fichiers leechés. Bool',
                'SCREENSHOTS_MODE': 'Activer ou désactiver la génération de captures d\'écran via -ss arg. Par défaut False. Bool',
                'CAP_FONT': 'Ajouter une police de caption personnalisée aux fichiers leechés, Valeurs disponibles : b, i, u, s, code, spoiler. Réinitialiser Var pour utiliser Regular (Pas de formatage)',
                'LEECH_FILENAME_PREFIX': 'Ajouter un préfixe personnalisé au nom des fichiers leechés. Str',
                'LEECH_FILENAME_SUFFIX': 'Ajouter un suffixe personnalisé au nom des fichiers leechés. Str',
                'LEECH_FILENAME_CAPTION': 'Ajouter une légende personnalisée aux fichiers/vidéos leechés. Str',
                'LEECH_FILENAME_REMNAME': 'Supprimer un mot personnalisé du nom des fichiers leechés. Str',
                'LOGIN_PASS': 'Mot de passe permanent pour que l\'utilisateur saute le système de token',
                'TOKEN_TIMEOUT': 'Timeout du token pour chaque membre de groupe en sec. Int',
                'DEBRID_LINK_API': 'Définir l\'API debrid-link.com pour le support de leeching des 172 hébergeurs supportés. Str',
                'REAL_DEBRID_API': 'Définir l\'API real-debrid.com pour le cache des torrents et quelques hébergeurs supportés (VPN Peut-être). Str',
                'LEECH_SPLIT_SIZE': 'Taille des parties divisées en bytes. Par défaut 2GB. Par défaut 4GB si votre compte est premium.',
                'MEDIA_GROUP': 'Voir les parties de fichiers divisés uploadés dans un groupe média. Par défaut False.',
                'MEGA_EMAIL': 'E-Mail utilisé pour se connecter sur mega.nz pour utiliser un compte premium. Str',
                'MEGA_PASSWORD': 'Mot de passe pour le compte mega.nz. Str',
                'OWNER_ID': 'L\'ID Telegram User (pas le nom d\'utilisateur) du propriétaire du bot.',
                'QUEUE_ALL': 'Nombre de tâches parallèles de téléchargements et uploads. Par exemple si 20 tâches sont ajoutées et QUEUE_ALL est 8, alors la somme des tâches d\'upload et de téléchargement est 8 et le reste en file d\'attente. Int. NOTE : si vous voulez remplir QUEUE_DOWNLOAD ou QUEUE_UPLOAD, alors la valeur QUEUE_ALL doit être supérieure ou égale à la plus grande et inférieure ou égale à la somme de QUEUE_UPLOAD et QUEUE_DOWNLOAD',
                'QUEUE_DOWNLOAD': 'Nombre de toutes les tâches de téléchargement parallèles. Int',
                'QUEUE_UPLOAD': 'Nombre de toutes les tâches d\'upload parallèles. Int',
                'RCLONE_FLAGS': 'key:value|key|key|key:value . Voir tous les RcloneFlags.',
                'RCLONE_PATH': "Chemin rclone par défaut vers lequel vous voulez uploader tous les mirrors en utilisant rclone.",
                'RCLONE_SERVE_URL': 'URL valide où le bot est déployé pour utiliser rclone serve. Le format de l\'URL devrait être http://myip, où myip est l\'IP/Domaine(public) de votre bot ou si vous avez choisi un port autre que 80 écrivez-le dans ce format http://myip:port (http et non https)',
                'RCLONE_SERVE_USER': 'Nom d\'utilisateur pour l\'authentification rclone serve.',
                'RCLONE_SERVE_PASS': 'Mot de passe pour l\'authentification rclone serve.',
                'RCLONE_SERVE_PORT': 'Quel est le port RCLONE_SERVE_URL. Par défaut 8080.',
                'RSS_CHAT_ID': 'ID du chat où les liens rss seront envoyés. Si vous voulez que le message soit envoyé à la chaîne alors ajoutez l\'id de la chaîne. Ajoutez -100 avant l\'id de la chaîne. Int',
                'RSS_DELAY': 'Temps en secondes pour l\'intervalle de rafraîchissement rss. Recommandé au moins 900 secondes. Par défaut 900 en sec. Int',
                'SEARCH_API_LINK': 'Lien de l\'app api de recherche. Obtenez votre api en déployant ce dépôt. Sites supportés : 1337x, Piratebay, Nyaasi, Torlock, Torrent Galaxy, Zooqle, Kickass, Bitsearch, MagnetDL, Libgen, YTS, Limetorrent, TorrentFunk, Glodls, TorrentProject et YourBittorrent',
                'SEARCH_LIMIT': 'Limite de recherche pour l\'api de recherche, limite pour chaque site et pas la limite globale des résultats. Par défaut zéro (Limite api par défaut pour chaque site).',
                'SEARCH_PLUGINS': 'Liste des plugins de recherche qBittorrent (liens github raw). J\'ai ajouté quelques plugins, vous pouvez supprimer/ajouter des plugins comme vous voulez.',
                'STATUS_LIMIT': 'Limiter le nombre de tâches affichées dans le message de statut avec boutons. Par défaut 10. NOTE : La limite recommandée est 4 tâches.',
                'STATUS_UPDATE_INTERVAL': 'Temps en secondes après lequel le message de progression/statut sera mis à jour. Recommandé au moins 10 secondes.',
                'STOP_DUPLICATE': "Le bot vérifiera le nom du fichier/dossier dans Drive dans le cas d'un upload vers GDRIVE_ID. S'il est présent dans Drive alors le téléchargement ou clonage sera stoppé. (NOTE : L'élément sera vérifié en utilisant le nom et pas le hash, donc cette fonctionnalité n'est pas encore parfaite). Par défaut False",
                'SUDO_USERS': 'Remplir user_id des utilisateurs que vous voulez donner la permission sudo. Séparez-les par un espace. Int',
                'TELEGRAM_API': 'Ceci est pour authentifier votre compte Telegram pour télécharger les fichiers Telegram. Vous pouvez l\'obtenir depuis https://my.telegram.org.',
                'TELEGRAM_HASH': 'Ceci est pour authentifier votre compte Telegram pour télécharger les fichiers Telegram. Vous pouvez l\'obtenir depuis https://my.telegram.org.',
                'TIMEZONE': 'Définir votre fuseau horaire préféré pour le message de redémarrage. Obtenez le vôtre à <a href="http://www.timezoneconverter.com/cgi-bin/findzone.tzc">Here</a> Str',
                'TORRENT_TIMEOUT': 'Timeout des torrents morts en téléchargement avec qBittorrent et Aria2c en secondes. Int',
                'UPSTREAM_REPO': "Lien de votre dépôt github, si votre dépôt est privé ajoutez https://username:{githubtoken}@github.com/{username}/{reponame} format. Obtenez le token depuis les paramètres Github. Ainsi vous pouvez mettre à jour votre bot depuis le dépôt rempli à chaque redémarrage.",
                'UPSTREAM_BRANCH': 'Branche upstream pour la mise à jour. Par défaut master.',
                'UPGRADE_PACKAGES': 'Installer le nouveau fichier de requirements sans penser au crash. Bool',
                'SAVE_MSG': 'Ajouter un bouton de sauvegarde de message. Bool',
                'SET_COMMANDS': 'Définir automatiquement les commandes du bot. Bool',
                'JIODRIVE_TOKEN': 'Définir le token pour jiodrive.xyz pour télécharger les fichiers. str',
                'USER_TD_MODE': 'Activer le User GDrive TD à utiliser. Par défaut False',
                'USER_TD_SA': 'Ajouter un mail SA global pour l\'utilisateur pour donner les permissions au bot pour l\'upload UserTD. Comme wzmlx@googlegroups.com. Str',
                'USER_SESSION_STRING': "Pour télécharger/uploader depuis votre compte telegram et pour envoyer rss. Pour générer une session string utilisez cette commande <code>python3 generate_string_session.py</code> après avoir monté le dossier du dépôt pour être sûr.\n\n<b>NOTE :</b> Vous ne pouvez pas utiliser le bot avec un message privé. Utilisez-le avec un superGroup.",
                'USE_SERVICE_ACCOUNTS': 'Si oui ou non utiliser les Service Accounts, avec google-api-python-client. Pour que cela fonctionne voir la section Using Service Accounts ci-dessous. Par défaut False",
                'WEB_PINCODE': ' Si oui ou non demander un pincode avant de sélectionner les fichiers depuis un torrent dans le web ou pas. Par défaut False. Bool.',
                'YT_DLP_OPTIONS': 'Options par défaut yt-dlp. Voir toutes les options possibles ICI ou utilisez ce script pour convertir les arguments cli en options api. Format: key:value|key:value|key:value. Ajoutez ^ avant un entier ou un float, certains nombres doivent être numériques et d\'autres string. \nExemple: "format:bv*+mergeall[vcodec=none]|nocheckcertificate:True"'
                }