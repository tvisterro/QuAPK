import os,sys,subprocess,glob,locale,time,re
from pathlib import Path
class C:
 R='\033[91m';G='\033[92m';Y='\033[93m';B='\033[94m';M='\033[95m';C='\033[96m';W='\033[97m';E='\033[0m'
T={'en':{'title':'QuAPK v0.1 (α) - Meta Quest APK/OBB Installer','lang_detected':'Language detected: English','warn_dev':'[ ! ] WARNING: Developer mode must be enabled on your Meta Quest device','warn_resp':'[ ! ] WARNING: The developer is not responsible for any damage to your device','warn_backup':'[ ! ] WARNING: Make sure to backup your important data before proceeding','warn_unofficial':'[ ! ] WARNING: Installing unofficial APKs may void your warranty','warn_security':'[ ! ] WARNING: Only install APKs from trusted sources','check_adb':'[ * ] Checking ADB installation...','adb_not_found':'[ ! ] ERROR: ADB not found. Please install Android SDK Platform Tools','download_adb':'[ ! ] Download from: https://developer.android.com/studio/releases/platform-tools','check_device':'[ * ] Checking connected devices...','no_device':'[ ! ] ERROR: No Meta Quest device found. Make sure USB debugging is enabled','device_found':'[ ✓ ] Device found: {}','select_mode':'\nSelect installation mode:\n1. APK only\n2. APK + OBB\nChoice: ','invalid_choice':'[ ! ] Invalid choice. Please enter 1 or 2','search_apk':'[ * ] Searching for APK files...','no_apk':'[ ! ] ERROR: No APK files found in current directory','select_apk':'\nSelect APK to install:','apk_choice':'Enter number: ','search_obb':'[ * ] Searching for OBB files...','no_obb':'[ ! ] ERROR: No OBB files found for this APK','detect_pkg':'[ * ] Detecting package name from APK...','pkg_found':'[ ✓ ] Package name: {}','backup_check':'[ * ] Checking if app already installed...','backup_create':'[ * ] Creating backup of existing app...','backup_done':'[ ✓ ] Backup created: {}','final_warn':'\n[ ! ] FINAL WARNING: You are about to install:\n    APK: {}\n    Package: {}','obb_info':'    OBB: {}','confirm':'\nAre you sure you want to continue? (yes/no): ','cancelled':'[ ! ] Installation cancelled by user','install_apk':'[ * ] Installing APK...','install_success':'[ ✓ ] APK installed successfully','install_fail':'[ ! ] ERROR: APK installation failed','create_obb_dir':'[ * ] Creating OBB directory...','push_obb':'[ * ] Pushing OBB file...','obb_success':'[ ✓ ] OBB file pushed successfully','obb_fail':'[ ! ] ERROR: Failed to push OBB file','complete':'\n[ ✓ ] Installation completed successfully!','rollback_prompt':'\n[ ! ] Installation failed. Rollback to previous version? (yes/no): ','rollback_start':'[ * ] Starting rollback...','rollback_success':'[ ✓ ] Rollback completed successfully','rollback_fail':'[ ! ] ERROR: Rollback failed','exit':'\nPress Enter to exit...'},'es':{'title':'QuAPK v0.1 (α) - Instalador APK/OBB para Meta Quest','lang_detected':'Idioma detectado: Español','warn_dev':'[ ! ] ADVERTENCIA: El modo desarrollador debe estar habilitado en tu Meta Quest','warn_resp':'[ ! ] ADVERTENCIA: El desarrollador no se responsabiliza por daños al dispositivo','warn_backup':'[ ! ] ADVERTENCIA: Asegúrate de respaldar tus datos importantes antes de continuar','warn_unofficial':'[ ! ] ADVERTENCIA: Instalar APKs no oficiales puede anular tu garantía','warn_security':'[ ! ] ADVERTENCIA: Solo instala APKs de fuentes confiables','check_adb':'[ * ] Verificando instalación de ADB...','adb_not_found':'[ ! ] ERROR: ADB no encontrado. Instala Android SDK Platform Tools','download_adb':'[ ! ] Descarga desde: https://developer.android.com/studio/releases/platform-tools','check_device':'[ * ] Verificando dispositivos conectados...','no_device':'[ ! ] ERROR: No se encontró Meta Quest. Asegúrate que la depuración USB esté habilitada','device_found':'[ ✓ ] Dispositivo encontrado: {}','select_mode':'\nSelecciona modo de instalación:\n1. Solo APK\n2. APK + OBB\nOpción: ','invalid_choice':'[ ! ] Opción inválida. Ingresa 1 o 2','search_apk':'[ * ] Buscando archivos APK...','no_apk':'[ ! ] ERROR: No se encontraron archivos APK en el directorio actual','select_apk':'\nSelecciona APK para instalar:','apk_choice':'Ingresa número: ','search_obb':'[ * ] Buscando archivos OBB...','no_obb':'[ ! ] ERROR: No se encontraron archivos OBB para este APK','detect_pkg':'[ * ] Detectando nombre del paquete desde APK...','pkg_found':'[ ✓ ] Nombre del paquete: {}','backup_check':'[ * ] Verificando si la app ya está instalada...','backup_create':'[ * ] Creando respaldo de la app existente...','backup_done':'[ ✓ ] Respaldo creado: {}','final_warn':'\n[ ! ] ADVERTENCIA FINAL: Estás por instalar:\n    APK: {}\n    Paquete: {}','obb_info':'    OBB: {}','confirm':'\n¿Estás seguro de continuar? (si/no): ','cancelled':'[ ! ] Instalación cancelada por el usuario','install_apk':'[ * ] Instalando APK...','install_success':'[ ✓ ] APK instalado exitosamente','install_fail':'[ ! ] ERROR: Falló la instalación del APK','create_obb_dir':'[ * ] Creando directorio OBB...','push_obb':'[ * ] Transfiriendo archivo OBB...','obb_success':'[ ✓ ] Archivo OBB transferido exitosamente','obb_fail':'[ ! ] ERROR: Falló la transferencia del archivo OBB','complete':'\n[ ✓ ] ¡Instalación completada exitosamente!','rollback_prompt':'\n[ ! ] Instalación fallida. ¿Restaurar versión anterior? (si/no): ','rollback_start':'[ * ] Iniciando restauración...','rollback_success':'[ ✓ ] Restauración completada exitosamente','rollback_fail':'[ ! ] ERROR: Falló la restauración','exit':'\nPresiona Enter para salir...'},'fr':{'title':'QuAPK v0.1 (α) - Installateur APK/OBB pour Meta Quest','lang_detected':'Langue détectée: Français','warn_dev':'[ ! ] AVERTISSEMENT: Le mode développeur doit être activé sur votre Meta Quest','warn_resp':'[ ! ] AVERTISSEMENT: Le développeur n\'est pas responsable des dommages à votre appareil','warn_backup':'[ ! ] AVERTISSEMENT: Sauvegardez vos données importantes avant de continuer','warn_unofficial':'[ ! ] AVERTISSEMENT: Installer des APK non officiels peut annuler votre garantie','warn_security':'[ ! ] AVERTISSEMENT: N\'installez que des APK de sources fiables','check_adb':'[ * ] Vérification de l\'installation d\'ADB...','adb_not_found':'[ ! ] ERREUR: ADB introuvable. Installez Android SDK Platform Tools','download_adb':'[ ! ] Téléchargez depuis: https://developer.android.com/studio/releases/platform-tools','check_device':'[ * ] Vérification des appareils connectés...','no_device':'[ ! ] ERREUR: Aucun Meta Quest trouvé. Assurez-vous que le débogage USB est activé','device_found':'[ ✓ ] Appareil trouvé: {}','select_mode':'\nSélectionnez le mode d\'installation:\n1. APK seulement\n2. APK + OBB\nChoix: ','invalid_choice':'[ ! ] Choix invalide. Entrez 1 ou 2','search_apk':'[ * ] Recherche de fichiers APK...','no_apk':'[ ! ] ERREUR: Aucun fichier APK trouvé dans le répertoire actuel','select_apk':'\nSélectionnez l\'APK à installer:','apk_choice':'Entrez le numéro: ','search_obb':'[ * ] Recherche de fichiers OBB...','no_obb':'[ ! ] ERREUR: Aucun fichier OBB trouvé pour cet APK','detect_pkg':'[ * ] Détection du nom du package depuis l\'APK...','pkg_found':'[ ✓ ] Nom du package: {}','backup_check':'[ * ] Vérification si l\'app est déjà installée...','backup_create':'[ * ] Création d\'une sauvegarde de l\'app existante...','backup_done':'[ ✓ ] Sauvegarde créée: {}','final_warn':'\n[ ! ] AVERTISSEMENT FINAL: Vous allez installer:\n    APK: {}\n    Package: {}','obb_info':'    OBB: {}','confirm':'\nÊtes-vous sûr de vouloir continuer? (oui/non): ','cancelled':'[ ! ] Installation annulée par l\'utilisateur','install_apk':'[ * ] Installation de l\'APK...','install_success':'[ ✓ ] APK installé avec succès','install_fail':'[ ! ] ERREUR: L\'installation de l\'APK a échoué','create_obb_dir':'[ * ] Création du répertoire OBB...','push_obb':'[ * ] Transfert du fichier OBB...','obb_success':'[ ✓ ] Fichier OBB transféré avec succès','obb_fail':'[ ! ] ERREUR: Échec du transfert du fichier OBB','complete':'\n[ ✓ ] Installation terminée avec succès!','rollback_prompt':'\n[ ! ] Installation échouée. Restaurer la version précédente? (oui/non): ','rollback_start':'[ * ] Démarrage de la restauration...','rollback_success':'[ ✓ ] Restauration terminée avec succès','rollback_fail':'[ ! ] ERREUR: La restauration a échoué','exit':'\nAppuyez sur Entrée pour quitter...'},'de':{'title':'QuAPK v0.1 (α) - Meta Quest APK/OBB Installer','lang_detected':'Sprache erkannt: Deutsch','warn_dev':'[ ! ] WARNUNG: Entwicklermodus muss auf Ihrer Meta Quest aktiviert sein','warn_resp':'[ ! ] WARNUNG: Der Entwickler übernimmt keine Verantwortung für Schäden am Gerät','warn_backup':'[ ! ] WARNUNG: Sichern Sie wichtige Daten bevor Sie fortfahren','warn_unofficial':'[ ! ] WARNUNG: Installation inoffizieller APKs kann Ihre Garantie ungültig machen','warn_security':'[ ! ] WARNUNG: Installieren Sie nur APKs aus vertrauenswürdigen Quellen','check_adb':'[ * ] Prüfe ADB-Installation...','adb_not_found':'[ ! ] FEHLER: ADB nicht gefunden. Bitte Android SDK Platform Tools installieren','download_adb':'[ ! ] Download von: https://developer.android.com/studio/releases/platform-tools','check_device':'[ * ] Prüfe verbundene Geräte...','no_device':'[ ! ] FEHLER: Kein Meta Quest gefunden. USB-Debugging muss aktiviert sein','device_found':'[ ✓ ] Gerät gefunden: {}','select_mode':'\nInstallationsmodus wählen:\n1. Nur APK\n2. APK + OBB\nAuswahl: ','invalid_choice':'[ ! ] Ungültige Auswahl. Bitte 1 oder 2 eingeben','search_apk':'[ * ] Suche APK-Dateien...','no_apk':'[ ! ] FEHLER: Keine APK-Dateien im aktuellen Verzeichnis gefunden','select_apk':'\nAPK zur Installation auswählen:','apk_choice':'Nummer eingeben: ','search_obb':'[ * ] Suche OBB-Dateien...','no_obb':'[ ! ] FEHLER: Keine OBB-Dateien für diese APK gefunden','detect_pkg':'[ * ] Erkenne Paketnamen aus APK...','pkg_found':'[ ✓ ] Paketname: {}','backup_check':'[ * ] Prüfe ob App bereits installiert ist...','backup_create':'[ * ] Erstelle Backup der vorhandenen App...','backup_done':'[ ✓ ] Backup erstellt: {}','final_warn':'\n[ ! ] LETZTE WARNUNG: Sie installieren:\n    APK: {}\n    Paket: {}','obb_info':'    OBB: {}','confirm':'\nSind Sie sicher, dass Sie fortfahren möchten? (ja/nein): ','cancelled':'[ ! ] Installation vom Benutzer abgebrochen','install_apk':'[ * ] Installiere APK...','install_success':'[ ✓ ] APK erfolgreich installiert','install_fail':'[ ! ] FEHLER: APK-Installation fehlgeschlagen','create_obb_dir':'[ * ] Erstelle OBB-Verzeichnis...','push_obb':'[ * ] Übertrage OBB-Datei...','obb_success':'[ ✓ ] OBB-Datei erfolgreich übertragen','obb_fail':'[ ! ] FEHLER: OBB-Übertragung fehlgeschlagen','complete':'\n[ ✓ ] Installation erfolgreich abgeschlossen!','rollback_prompt':'\n[ ! ] Installation fehlgeschlagen. Vorherige Version wiederherstellen? (ja/nein): ','rollback_start':'[ * ] Starte Wiederherstellung...','rollback_success':'[ ✓ ] Wiederherstellung erfolgreich abgeschlossen','rollback_fail':'[ ! ] FEHLER: Wiederherstellung fehlgeschlagen','exit':'\nEnter drücken zum Beenden...'},'ru':{'title':'QuAPK v0.1 (α) - Установщик APK/OBB для Meta Quest','lang_detected':'Определён язык: Русский','warn_dev':'[ ! ] ВНИМАНИЕ: На Meta Quest должен быть включён режим разработчика','warn_resp':'[ ! ] ВНИМАНИЕ: Разработчик не несёт ответственности за повреждение устройства','warn_backup':'[ ! ] ВНИМАНИЕ: Сделайте резервную копию важных данных перед продолжением','warn_unofficial':'[ ! ] ВНИМАНИЕ: Установка неофициальных APK может аннулировать гарантию','warn_security':'[ ! ] ВНИМАНИЕ: Устанавливайте APK только из доверенных источников','check_adb':'[ * ] Проверка установки ADB...','adb_not_found':'[ ! ] ОШИБКА: ADB не найден. Установите Android SDK Platform Tools','download_adb':'[ ! ] Скачать: https://developer.android.com/studio/releases/platform-tools','check_device':'[ * ] Проверка подключённых устройств...','no_device':'[ ! ] ОШИБКА: Meta Quest не найден. Убедитесь что включена отладка по USB','device_found':'[ ✓ ] Найдено устройство: {}','select_mode':'\nВыберите режим установки:\n1. Только APK\n2. APK + OBB\nВыбор: ','invalid_choice':'[ ! ] Неверный выбор. Введите 1 или 2','search_apk':'[ * ] Поиск APK файлов...','no_apk':'[ ! ] ОШИБКА: APK файлы не найдены в текущей папке','select_apk':'\nВыберите APK для установки:','apk_choice':'Введите номер: ','search_obb':'[ * ] Поиск OBB файлов...','no_obb':'[ ! ] ОШИБКА: OBB файлы для этого APK не найдены','detect_pkg':'[ * ] Определение имени пакета из APK...','pkg_found':'[ ✓ ] Имя пакета: {}','backup_check':'[ * ] Проверка установлено ли приложение...','backup_create':'[ * ] Создание резервной копии существующего приложения...','backup_done':'[ ✓ ] Резервная копия создана: {}','final_warn':'\n[ ! ] ПОСЛЕДНЕЕ ПРЕДУПРЕЖДЕНИЕ: Вы устанавливаете:\n    APK: {}\n    Пакет: {}','obb_info':'    OBB: {}','confirm':'\nВы уверены что хотите продолжить? (да/нет): ','cancelled':'[ ! ] Установка отменена пользователем','install_apk':'[ * ] Установка APK...','install_success':'[ ✓ ] APK успешно установлен','install_fail':'[ ! ] ОШИБКА: Установка APK не удалась','create_obb_dir':'[ * ] Создание папки OBB...','push_obb':'[ * ] Передача OBB файла...','obb_success':'[ ✓ ] OBB файл успешно передан','obb_fail':'[ ! ] ОШИБКА: Не удалось передать OBB файл','complete':'\n[ ✓ ] Установка успешно завершена!','rollback_prompt':'\n[ ! ] Установка не удалась. Восстановить предыдущую версию? (да/нет): ','rollback_start':'[ * ] Начало восстановления...','rollback_success':'[ ✓ ] Восстановление успешно завершено','rollback_fail':'[ ! ] ОШИБКА: Восстановление не удалось','exit':'\nНажмите Enter для выхода...'},'zh':{'title':'QuAPK v0.1 (α) - Meta Quest APK/OBB 安装器','lang_detected':'检测到语言：中文','warn_dev':'[ ! ] 警告：必须在Meta Quest上启用开发者模式','warn_resp':'[ ! ] 警告：开发者不对设备损坏负责','warn_backup':'[ ! ] 警告：继续前请备份重要数据','warn_unofficial':'[ ! ] 警告：安装非官方APK可能使保修失效','warn_security':'[ ! ] 警告：仅从可信来源安装APK','check_adb':'[ * ] 检查ADB安装...','adb_not_found':'[ ! ] 错误：未找到ADB。请安装Android SDK Platform Tools','download_adb':'[ ! ] 下载地址：https://developer.android.com/studio/releases/platform-tools','check_device':'[ * ] 检查已连接设备...','no_device':'[ ! ] 错误：未找到Meta Quest。确保已启用USB调试','device_found':'[ ✓ ] 找到设备：{}','select_mode':'\n选择安装模式：\n1. 仅APK\n2. APK + OBB\n选择：','invalid_choice':'[ ! ] 无效选择。请输入1或2','search_apk':'[ * ] 搜索APK文件...','no_apk':'[ ! ] 错误：当前目录未找到APK文件','select_apk':'\n选择要安装的APK：','apk_choice':'输入编号：','search_obb':'[ * ] 搜索OBB文件...','no_obb':'[ ! ] 错误：未找到此APK的OBB文件','detect_pkg':'[ * ] 从APK检测包名...','pkg_found':'[ ✓ ] 包名：{}','backup_check':'[ * ] 检查应用是否已安装...','backup_create':'[ * ] 创建现有应用备份...','backup_done':'[ ✓ ] 备份已创建：{}','final_warn':'\n[ ! ] 最后警告：您将安装：\n    APK：{}\n    包名：{}','obb_info':'    OBB：{}','confirm':'\n确定要继续吗？(是/否)：','cancelled':'[ ! ] 用户取消安装','install_apk':'[ * ] 安装APK...','install_success':'[ ✓ ] APK安装成功','install_fail':'[ ! ] 错误：APK安装失败','create_obb_dir':'[ * ] 创建OBB目录...','push_obb':'[ * ] 传输OBB文件...','obb_success':'[ ✓ ] OBB文件传输成功','obb_fail':'[ ! ] 错误：OBB文件传输失败','complete':'\n[ ✓ ] 安装成功完成！','rollback_prompt':'\n[ ! ] 安装失败。恢复到之前版本？(是/否)：','rollback_start':'[ * ] 开始恢复...','rollback_success':'[ ✓ ] 恢复成功完成','rollback_fail':'[ ! ] 错误：恢复失败','exit':'\n按Enter键退出...'},'ja':{'title':'QuAPK v0.1 (α) - Meta Quest APK/OBB インストーラー','lang_detected':'検出された言語：日本語','warn_dev':'[ ! ] 警告：Meta Questで開発者モードを有効にする必要があります','warn_resp':'[ ! ] 警告：開発者はデバイスの損傷について責任を負いません','warn_backup':'[ ! ] 警告：続行する前に重要なデータをバックアップしてください','warn_unofficial':'[ ! ] 警告：非公式APKのインストールは保証を無効にする可能性があります','warn_security':'[ ! ] 警告：信頼できるソースからのみAPKをインストールしてください','check_adb':'[ * ] ADBインストールを確認中...','adb_not_found':'[ ! ] エラー：ADBが見つかりません。Android SDK Platform Toolsをインストールしてください','download_adb':'[ ! ] ダウンロード：https://developer.android.com/studio/releases/platform-tools','check_device':'[ * ] 接続されたデバイスを確認中...','no_device':'[ ! ] エラー：Meta Questが見つかりません。USBデバッグが有効になっていることを確認してください','device_found':'[ ✓ ] デバイスが見つかりました：{}','select_mode':'\nインストールモードを選択：\n1. APKのみ\n2. APK + OBB\n選択：','invalid_choice':'[ ! ] 無効な選択。1または2を入力してください','search_apk':'[ * ] APKファイルを検索中...','no_apk':'[ ! ] エラー：現在のディレクトリにAPKファイルが見つかりません','select_apk':'\nインストールするAPKを選択：','apk_choice':'番号を入力：','search_obb':'[ * ] OBBファイルを検索中...','no_obb':'[ ! ] エラー：このAPKのOBBファイルが見つかりません','detect_pkg':'[ * ] APKからパッケージ名を検出中...','pkg_found':'[ ✓ ] パッケージ名：{}','backup_check':'[ * ] アプリがすでにインストールされているか確認中...','backup_create':'[ * ] 既存のアプリのバックアップを作成中...','backup_done':'[ ✓ ] バックアップが作成されました：{}','final_warn':'\n[ ! ] 最終警告：インストールするもの：\n    APK：{}\n    パッケージ：{}','obb_info':'    OBB：{}','confirm':'\n続行してもよろしいですか？(はい/いいえ)：','cancelled':'[ ! ] ユーザーによってインストールがキャンセルされました','install_apk':'[ * ] APKをインストール中...','install_success':'[ ✓ ] APKが正常にインストールされました','install_fail':'[ ! ] エラー：APKのインストールに失敗しました','create_obb_dir':'[ * ] OBBディレクトリを作成中...','push_obb':'[ * ] OBBファイルを転送中...','obb_success':'[ ✓ ] OBBファイルが正常に転送されました','obb_fail':'[ ! ] エラー：OBBファイルの転送に失敗しました','complete':'\n[ ✓ ] インストールが正常に完了しました！','rollback_prompt':'\n[ ! ] インストールに失敗しました。以前のバージョンに戻しますか？(はい/いいえ)：','rollback_start':'[ * ] ロールバックを開始中...','rollback_success':'[ ✓ ] ロールバックが正常に完了しました','rollback_fail':'[ ! ] エラー：ロールバックに失敗しました','exit':'\nEnterキーを押して終了...'}}
def gl():
 try:
  l=locale.getdefaultlocale()[0]
  if l:return l.split('_')[0]if l.split('_')[0]in T else'en'
 except:pass
 return'en'
L=gl();t=T.get(L,T['en'])
def p(k,c=''):
 m=t[k]
 if'[ ! ]'in m:print(f"{C.R}{m}{C.E}")
 elif'[ ✓ ]'in m:print(f"{C.G}{m}{C.E}")
 elif'[ * ]'in m:print(f"{C.B}{m}{C.E}")
 else:print(m)
def r(c):
 try:
  if os.name=='nt':
   s=subprocess.STARTUPINFO();s.dwFlags|=subprocess.STARTF_USESHOWWINDOW;x=subprocess.run(c,shell=True,capture_output=True,text=True,startupinfo=s)
  else:x=subprocess.run(c,shell=True,capture_output=True,text=True)
  return x.returncode==0,x.stdout.strip(),x.stderr.strip()
 except:return False,'',''
def ca():
 p('check_adb');o,_,_=r('adb version')
 if not o:p('adb_not_found');p('download_adb');return False
 return True
def gd():
 p('check_device');o,u,_=r('adb devices')
 if o and u:
  l=u.split('\n')[1:]
  for x in l:
   if'\tdevice'in x:d=x.split('\t')[0];print(f"{C.G}{t['device_found'].format(d)}{C.E}");return d
 p('no_device');return None
def ga():
 p('search_apk');a=[]
 for f in Path('.').iterdir():
  if f.suffix.lower()=='.apk'and f.is_file():a.append(str(f))
 if not a:p('no_apk');return None
 return sorted(a)
def gp(a):
 p('detect_pkg');c='aapt'if os.name!='nt'else'aapt.exe';o,u,_=r(f'{c} dump badging "{a}"')
 if o and u:
  m=re.search(r"package: name='([^']+)'",u)
  if m:k=m.group(1);print(f"{C.G}{t['pkg_found'].format(k)}{C.E}");return k
 o,u,_=r(f'adb shell aapt dump badging /data/local/tmp/temp.apk')
 if o and u:
  m=re.search(r"package: name='([^']+)'",u)
  if m:k=m.group(1);print(f"{C.G}{t['pkg_found'].format(k)}{C.E}");return k
 b=Path(a).stem
 if'.'in b:k=b;print(f"{C.G}{t['pkg_found'].format(k)}{C.E}");return k
 return None
def ba(k):
 p('backup_check');o,u,_=r(f'adb shell pm list packages')
 if o and k in u:
  p('backup_create');b=f'backup_{k}_{int(time.time())}.ab';o,_,_=r(f'adb backup -f {b} -apk {k}')
  if o:print(f"{C.G}{t['backup_done'].format(b)}{C.E}");return b
 return None
def ia(a):
 p('install_apk');o,_,e=r(f'adb install -r "{a}"')
 if o or'Success'in e:p('install_success');return True
 p('install_fail');return False
def go(k):return f'/storage/emulated/0/Android/obb/{k}/'
def po(o,k):
 p('create_obb_dir');d=go(k);r(f'adb shell mkdir -p {d}');p('push_obb');x,_,_=r(f'adb push "{o}" {d}')
 if x:p('obb_success');return True
 p('obb_fail');return False
def rb(b):
 a=input(f"{C.Y}{t['rollback_prompt']}{C.E}").lower()
 if a in['yes','да','si','oui','ja','是','はい','y']:
  p('rollback_start')
  if b and os.path.exists(b):
   o,_,_=r(f'adb restore {b}')
   if o:p('rollback_success');return
  p('rollback_fail')
def main():
 os.system('cls'if os.name=='nt'else'clear')
 print(f"{C.C}{'='*60}{C.E}\n{C.M}{t['title']}{C.E}\n{C.G}{t['lang_detected']}{C.E}\n{C.C}{'='*60}{C.E}")
 p('warn_dev');p('warn_resp');p('warn_backup');p('warn_unofficial');p('warn_security');print(f"{C.C}{'='*60}{C.E}")
 if not ca():input(t['exit']);sys.exit(1)
 d=gd()
 if not d:input(t['exit']);sys.exit(1)
 m=input(f"{C.Y}{t['select_mode']}{C.E}")
 if m not in['1','2']:p('invalid_choice');input(t['exit']);sys.exit(1)
 a=ga()
 if not a:input(t['exit']);sys.exit(1)
 print(f"{C.Y}{t['select_apk']}{C.E}")
 for i,x in enumerate(a):print(f"{C.W}{i+1}. {x}{C.E}")
 try:
  c=int(input(f"{C.Y}{t['apk_choice']}{C.E}"))-1
  if c<0 or c>=len(a):raise ValueError
 except:p('invalid_choice');input(t['exit']);sys.exit(1)
 x=a[c];k=gp(x)
 if not k:k=Path(x).stem.replace(' ','.');print(f"{C.G}{t['pkg_found'].format(k)}{C.E}")
 o=None
 if m=='2':
  p('search_obb');b=[]
  for f in Path('.').iterdir():
   if f.suffix.lower()=='.obb'and f.is_file():b.append(str(f))
  if not b:p('no_obb');input(t['exit']);sys.exit(1)
  o=b[0]
 print(f"{C.R}{t['final_warn'].format(x,k)}{C.E}")
 if o:print(f"{C.R}{t['obb_info'].format(o)}{C.E}")
 n=input(f"{C.Y}{t['confirm']}{C.E}").lower()
 if n not in['yes','да','si','oui','ja','是','はい','y']:p('cancelled');input(t['exit']);sys.exit(0)
 b=ba(k)
 if not ia(x):rb(b);input(t['exit']);sys.exit(1)
 if m=='2'and o:
  if not po(o,k):rb(b);input(t['exit']);sys.exit(1)
 print(f"{C.G}{t['complete']}{C.E}");input(t['exit'])
if __name__=='__main__':
 try:main()
 except KeyboardInterrupt:print(f"\n{C.R}{t.get('cancelled','Cancelled')}{C.E}");sys.exit(0)
 except Exception as e:print(f"\n{C.R}[ ! ] ERROR: {e}{C.E}");input(t.get('exit','Press Enter to exit...'));sys.exit(1)