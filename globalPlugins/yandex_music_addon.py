# -*- coding: UTF-8 -*-
import globalPluginHandler
import wx
import config
import gui
import ui
import addonHandler
from scriptHandler import script
import tones
import threading
import time
import core
import os
import sys
import re
import languageHandler
import webbrowser

lib_path = os.path.join(os.path.dirname(__file__), 'yandex_music_lib')
if lib_path not in sys.path:
	sys.path.insert(0, lib_path)

try:
	from yandex_music import Client
	YANDEX_AVAILABLE = True
except ImportError:
	YANDEX_AVAILABLE = False

addonHandler.initTranslation()

TRANSLATIONS = {
	"uz": {
		"Yandex Music Settings": "Yandex Musiqa Sozlamalari",
		"Yandex Token (Required):": "Yandex Token (Majburiy):",
		"Download Folder:": "Yuklab olish papkasi:",
		"Bitrate Quality:": "Qo'shiq sifati (Bitreyt):",
		"Get Token (Open Browser)": "Token Olish (Brauzerni ochish)",
		"Check Token Validity": "Tokenni Tekshirish",
		"Checking...": "Tekshirilmoqda...",
		"Info": "Ma'lumot",
		"Success": "Muvaffaqiyatli",
		"Error": "Xatolik",
		"Please enter a token first!": "Iltimos, avval tokenni kiriting!",
		"Browser will open. Log in to Yandex, then copy the long text after 'access_token=' from the URL.": "Brauzer ochiladi. Yandex ga kiring va silka (URL) dagi 'access_token=' dan keyingi uzun kodni nusxalab oling.",
		"Token is Valid! Account: ": "Token yaroqli! Hisob: ",
		"Token is Invalid!": "Token yaroqsiz yoki eskirgan!",
		"Open Yandex Downloader": "Yandex Yuklovchini ochish",
		"Search:": "Qidiruv (yoki Havola):",
		"Search": "Qidirish",
		"My Music": "Mening Musiqalarim",
		"Download Selected": "Yuklab Olish",
		"View/Open": "Ichiga Kirish / Ko'rish",
		"Close": "Yopish",
		"Searching...": "Qidirilmoqda...",
		"No results": "Hech narsa topilmadi",
		"Downloading...": "Yuklanmoqda...",
		"Downloading tracks...": "Qo'shiqlar yuklanmoqda...",
		"Downloaded:": "Yuklandi:",
		"Error:": "Xato:",
		"Done!": "Tayyor!",
		"Token missing! Please enter it in NVDA settings.": "Token kiritilmagan! Iltimos, NVDA sozlamalariga kiriting.",
		"Loading profile...": "Profil yuklanmoqda...",
		"Please open the artist first, then download albums.": "Iltimos, avval Artist ichiga kiring, so'ngra albomni yuklang.",
		"[My] Liked Tracks": "[Mening] Yoqtirgan Qo'shiqlarim",
		"[My Playlist]": "[Mening Pleylistim]",
		"[Liked Album]": "[Yoqtirgan Albomim]",
		"My Liked Tracks": "Mening Yoqtirgan Qo'shiqlarim",
		"Press Download to save this item.": "Tanlanganni saqlash uchun 'Yuklab Olish' tugmasini bosing.",
		"Can only view Artist profiles.": "Faqatgina Artist (San'atkor) profilining ichiga kirish mumkin.",
		"Cannot view this item.": "Bu elementni ko'rib bo'lmaydi.",
		"Token successfully received and entered!": "Token muvaffaqiyatli olindi va maydonga kiritildi!",
		"An error occurred:\n": "Xatolik yuz berdi:\n",
		"Browser will open for Yandex token...\n\nConfirmation code to enter: {code}\n\nThis code is automatically copied to clipboard! \nPaste and confirm it in the browser.": "Yandex token olish uchun brauzer ochiladi.\n\nKiritishingiz kerak bo'lgan tasdiqlash kodi: {code}\n\nBu kod avtomatik ravishda buferga nusxalandi! \nBrauzerda sahifa ochilgach, kodni joylab, tasdiqlang.",
		"UI error: ": "UI xatosi: ",
		"Error: yandex-music library missing!": "Xato: yandex-music kutubxonasi topilmadi!",
		"Yandex Music Downloader": "YaMusic Helper (Yandex Musiqa)",
		"Track": "Trek",
		"Album": "Albom",
		"Artist": "San'atkor",
		"Playlist": "Pleylist",
		"Copy Token": "Tokenni nusxalash",
		"Token copied to clipboard!": "Token xotiraga (buferga) nusxalandi!",
		"Disclaimer & Terms of Use": "Ogohlantirish va Foydalanish shartlari",
		"DISCLAIMER_TEXT": "OGOHLANTIRISH: Ushbu qo'shimcha faqat ta'lim va ko'zi ojiz foydalanuvchilarga qulaylik yaratish maqsadida ishlab chiqilgan bo'lib, Yandex LLC kompaniyasiga rasmiy aloqasi yo'q. Yuklab olingan barcha materiallar faqat shaxsiy maqsadlarda foydalanish uchun mo'ljallangan. Muallif ushbu dasturdan noto'g'ri foydalanilishi uchun javobgar emas.\n\nUshbu shartlarga rozimisiz?",
		"Preview / Listen": "Tinglash",
		"Save Lyrics": "Qo'shiq matnini saqlash",
		"Lyrics": "Qo'shiq matnlari",
		"No lyrics available for this track.": "Bu qo'shiq uchun matn topilmadi.",
		"Lyrics saved to: ": "Matn saqlandi: ",
		"This is not an album.": "Bu albom emas.",
		"This is not a track.": "Bu trek (qo'shiq) emas.",
		"This is not a playlist.": "Bu pleylist emas.",
		"Go Back (Backspace)": "Orqaga qaytish (Backspace)",
		"Already at main menu": "Siz asosiy ro'yxatdasiz",
		"Preview Player (e.g. default, aimp.exe):": "Eshitish Pleyeri (masalan: default, aimp.exe):",
		"Preview Player (e.g. default, aimp.exe, vlc.exe):": "Eshitish Pleyeri (masalan: default, aimp.exe):",
		"Browse...": "Tanlash...",
		"Select Player Executable": "Pleyer dasturini (.exe) tanlang",
		"You can only preview tracks.": "Faqatgina treklarni (qo'shiqlarni) eshitib ko'rish mumkin.",
		"Loading stream...": "Audio oqimi yuklanmoqda...",
		"My Playlists": "Mening pleylistlarim",
		"Add to Playlist": "Pleylistga qo'shish",
		"Create Playlist": "Pleylist yaratish",
		"Playlist name:": "Pleylist nomi:",
		"Track already exists in this playlist!": "Bu trek ushbu pleylistda bor!",
		"Track added successfully!": "Trek muvaffaqiyatli qo'shildi!",
		"Select Playlist": "Pleylistni tanlang",
		"Enter new playlist name:": "Yangi pleylist nomini kiriting:"
	},
	"ru": {
		"Yandex Music Settings": "Настройки Яндекс Музыки",
		"Yandex Token (Required):": "Токен Яндекс (Обязательно):",
		"Download Folder:": "Папка для загрузок:",
		"Bitrate Quality:": "Качество (Битрейт):",
		"Get Token (Open Browser)": "Получить Токен (Открыть браузер)",
		"Check Token Validity": "Проверить Токен",
		"Checking...": "Проверка...",
		"Info": "Информация",
		"Success": "Успешно",
		"Error": "Ошибка",
		"Please enter a token first!": "Пожалуйста, сначала введите токен!",
		"Browser will open. Log in to Yandex, then copy the long text after 'access_token=' from the URL.": "Откроется браузер. Войдите в Яндекс, затем скопируйте длинный текст после 'access_token=' из ссылки (URL).",
		"Token is Valid! Account: ": "Токен действителен! Аккаунт: ",
		"Token is Invalid!": "Токен недействителен или устарел!",
		"Open Yandex Downloader": "Открыть Загрузчик Яндекс",
		"Search:": "Поиск (или Ссылка):",
		"Search": "Искать",
		"My Music": "Моя Музыка",
		"Download Selected": "Скачать",
		"View/Open": "Войти / Просмотр",
		"Close": "Закрыть",
		"Searching...": "Поиск...",
		"No results": "Ничего не найдено",
		"Downloading...": "Загрузка...",
		"Downloading tracks...": "Загрузка треков...",
		"Downloaded:": "Загружено:",
		"Error:": "Ошибка:",
		"Done!": "Готово!",
		"Token missing! Please enter it in NVDA settings.": "Токен отсутствует! Введите его в настройках NVDA.",
		"Loading profile...": "Загрузка профиля...",
		"Please open the artist first, then download albums.": "Пожалуйста, сначала откройте профиль Артиста.",
		"[My] Liked Tracks": "[Мои] Понравившиеся треки",
		"[My Playlist]": "[Мой Плейлист]",
		"[Liked Album]": "[Понравившийся альбом]",
		"My Liked Tracks": "Мои Понравившиеся треки",
		"Press Download to save this item.": "Нажмите 'Скачать', чтобы сохранить этот элемент.",
		"Can only view Artist profiles.": "Входить можно только в профиль Артиста (Исполнителя).",
		"Cannot view this item.": "Невозможно просмотреть этот элемент.",
		"Token successfully received and entered!": "Токен успешно получен и введен!",
		"An error occurred:\n": "Произошла ошибка:\n",
		"Browser will open for Yandex token...\n\nConfirmation code to enter: {code}\n\nThis code is automatically copied to clipboard! \nPaste and confirm it in the browser.": "Откроется браузер для получения токена Яндекс...\n\nКод подтверждения для ввода: {code}\n\nЭтот код автоматически скопирован в буфер обмена! \nВставьте и подтвердите его в браузере.",
		"UI error: ": "Ошибка UI: ",
		"Error: yandex-music library missing!": "Ошибка: библиотека yandex-music отсутствует!",
		"Yandex Music Downloader": "YaMusic Helper (Яндекс Музыка)",
		"Track": "Трек",
		"Album": "Альбом",
		"Artist": "Артист",
		"Playlist": "Плейлист",
		"Copy Token": "Копировать токен",
		"Token copied to clipboard!": "Токен скопирован в буфер обмена!",
		"Disclaimer & Terms of Use": "Правовое уведомление и Условия",
		"DISCLAIMER_TEXT": "ВНИМАНИЕ: Данное дополнение разработано исключительно в образовательных целях и для удобства незрячих пользователей. Оно является неофициальным клиентом и не имеет официального отношения к компании Яндекс. Все скачанные материалы предназначены только для личного использования. Автор не несет ответственности за любое неправомерное использование.\n\nВы принимаете эти условия?",
		"Preview / Listen": "Слушать",
		"Save Lyrics": "Сохранить текст песни",
		"Lyrics": "Тексты песен",
		"No lyrics available for this track.": "Текст этой песни не найден.",
		"Lyrics saved to: ": "Текст сохранен в: ",
		"This is not an album.": "Это не альбом.",
		"This is not a track.": "Это не трек.",
		"This is not a playlist.": "Это не плейлист.",
		"Go Back (Backspace)": "Назад (Backspace)",
		"Already at main menu": "Вы уже в главном меню",
		"Preview Player (e.g. default, aimp.exe):": "Плеер (например: default, aimp.exe):",
		"Preview Player (e.g. default, aimp.exe, vlc.exe):": "Плеер (например: default, aimp.exe):",
		"Browse...": "Обзор...",
		"Select Player Executable": "Выберите файл плеера (.exe)",
		"You can only preview tracks.": "Прослушивать можно только треки.",
		"Loading stream...": "Загрузка потока...",
		"My Playlists": "Мои плейлисты",
		"Add to Playlist": "Добавить в плейлист",
		"Create Playlist": "Создать плейлист",
		"Playlist name:": "Имя плейлиста:",
		"Track already exists in this playlist!": "Этот трек уже есть в данном плейлисте!",
		"Track added successfully!": "Трек успешно добавлен!",
		"Select Playlist": "Выберите плейлист",
		"Enter new playlist name:": "Введите имя нового плейлиста:"
	}
}

def _(text):
	try:
		lang = languageHandler.getLanguage().lower()
	except Exception:
		lang = "en"
		
	if lang.startswith("uz"): 
		return TRANSLATIONS["uz"].get(text, text)
	elif lang.startswith("ru"): 
		return TRANSLATIONS["ru"].get(text, text)
	return text

confspec = {
	"token": "string(default='')",
	"download_folder": "string(default='')",
	"bitrate": "integer(default=320)",
	"accepted_disclaimer": "boolean(default=False)",
	"preview_player": "string(default='default')"
}
config.conf.spec["yandexMusic"] = confspec


def check_disclaimer():
	if config.conf["yandexMusic"].get("accepted_disclaimer", False):
		return True
	
	# Translators: UI message for DISCLAIMER_TEXT
	msg = _("DISCLAIMER_TEXT")
	if msg == "DISCLAIMER_TEXT":
		msg = "DISCLAIMER: This addon is developed solely for educational and accessibility purposes. It is an unofficial client and has no official affiliation with Yandex LLC. All downloaded materials are for personal use only. The author is not responsible for any misuse of this tool.\n\nDo you accept these terms?"
		
	# Translators: UI message for Disclaimer & Terms of Use
	res = wx.MessageBox(msg, _("Disclaimer & Terms of Use"), wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING)
	if res == wx.YES:
		config.conf["yandexMusic"]["accepted_disclaimer"] = True
		return True
	return False


class YandexMusicSettingsPanel(gui.settingsDialogs.SettingsPanel):
	# Translators: UI message for Yandex Music Settings
	title = _("Yandex Music Settings")

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		
		# Translators: UI message for Yandex Token (Required):
		self.tokenCtrl = sHelper.addLabeledControl(_("Yandex Token (Required):"), wx.TextCtrl, style=wx.TE_PASSWORD)
		self.tokenCtrl.SetValue(config.conf["yandexMusic"]["token"])
		
		# Token tugmalari
		btnSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: UI message for Get Token (Open Browser)
		self.btnGetToken = wx.Button(self, label=_("Get Token (Open Browser)"))
		# Translators: UI message for Copy Token
		self.btnCopyToken = wx.Button(self, label=_("Copy Token"))
		# Translators: UI message for Check Token Validity
		self.btnCheckToken = wx.Button(self, label=_("Check Token Validity"))
		btnSizer.Add(self.btnGetToken, flag=wx.RIGHT, border=5)
		btnSizer.Add(self.btnCopyToken, flag=wx.RIGHT, border=5)
		btnSizer.Add(self.btnCheckToken)
		sHelper.addItem(btnSizer)
		
		self.btnGetToken.Bind(wx.EVT_BUTTON, self.onGetToken)
		self.btnCopyToken.Bind(wx.EVT_BUTTON, self.onCopyToken)
		self.btnCheckToken.Bind(wx.EVT_BUTTON, self.onCheckToken)
		
		# Translators: UI message for Download Folder:
		self.outFolderCtrl = sHelper.addLabeledControl(_("Download Folder:"), wx.TextCtrl)
		default_folder = os.path.join(os.path.expanduser("~"), "Downloads", "YandexMusic")
		current_folder = config.conf["yandexMusic"]["download_folder"]
		self.outFolderCtrl.SetValue(current_folder if current_folder else default_folder)
		
		self.bitrateChoice = sHelper.addLabeledControl(
			# Translators: UI message for Bitrate Quality:
			_("Bitrate Quality:"), wx.Choice, choices=["192 kbps", "320 kbps"]
		)
		self.bitrateChoice.SetSelection(0 if config.conf["yandexMusic"]["bitrate"] == 192 else 1)
		
		# Player selection
		# Translators: UI message for Preview Player (e.g. default, aimp.exe):
		lbl_player = wx.StaticText(self, label=_("Preview Player (e.g. default, aimp.exe):"))
		sHelper.addItem(lbl_player)
		
		player_sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.previewPlayerCtrl = wx.TextCtrl(self)
		self.previewPlayerCtrl.SetValue(config.conf["yandexMusic"].get("preview_player", "default"))
		
		# Translators: UI message for Browse...
		self.btnBrowsePlayer = wx.Button(self, label=_("Browse..."))
		self.btnBrowsePlayer.Bind(wx.EVT_BUTTON, self.onBrowsePlayer)
		
		player_sizer.Add(self.previewPlayerCtrl, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=5)
		player_sizer.Add(self.btnBrowsePlayer, proportion=0)
		sHelper.addItem(player_sizer)

	def onBrowsePlayer(self, event):
		# Translators: UI message for Select Player Executable
		with wx.FileDialog(self, _("Select Player Executable"), wildcard="Executable files (*.exe)|*.exe",
						   style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return
			pathname = fileDialog.GetPath()
			self.previewPlayerCtrl.SetValue(pathname)

	def onGetToken(self, event):
		if not check_disclaimer(): return
		def thread_func():
			try:
				from yandex_music import Client
				import api
				client = Client()
				
				def on_code(code):
					# Translators: UI message for Browser will open for Yandex token...\n\nConfirmation code to enter: {code}\n\nThis code is automatically copied to clipboard! \nPaste and confirm it in the browser.
					msg = _("Browser will open for Yandex token...\n\nConfirmation code to enter: {code}\n\nThis code is automatically copied to clipboard! \nPaste and confirm it in the browser.").format(code=code.user_code)
					
					def ui_update():
						try:
							api.copyToClip(code.user_code)
							# Translators: UI message for Info
							wx.MessageBox(msg, _("Info"), wx.OK | wx.ICON_INFORMATION)
							webbrowser.open(code.verification_url)
						except Exception as inner_e:
							# Translators: UI message for UI error: 
							wx.MessageBox(_("UI error: ") + str(inner_e), _("Error"), wx.OK | wx.ICON_ERROR)
							
					wx.CallAfter(ui_update)
					
				token_obj = client.device_auth(on_code=on_code)
				access_token = token_obj.access_token if hasattr(token_obj, 'access_token') else str(token_obj)
				
				def on_success():
					self.tokenCtrl.SetValue(access_token)
					# Translators: UI message for Token successfully received and entered!
					wx.MessageBox(_("Token successfully received and entered!"), _("Success"), wx.OK | wx.ICON_INFORMATION)
				wx.CallAfter(on_success)
				
			except Exception as e:
				import traceback
				err_str = str(e) + "\n" + traceback.format_exc()
				# Translators: UI message for An error occurred:\n
				wx.CallAfter(lambda err=err_str: wx.MessageBox(_("An error occurred:\n") + err, _("Error"), wx.OK | wx.ICON_ERROR))

		threading.Thread(target=thread_func).start()

	def onCopyToken(self, event):
		token = self.tokenCtrl.GetValue().strip()
		if not token:
			# Translators: UI message for Please enter a token first!
			wx.MessageBox(_("Please enter a token first!"), _("Error"), wx.OK | wx.ICON_ERROR)
			return
		try:
			import api
			api.copyToClip(token)
			# Translators: UI message for Token copied to clipboard!
			wx.MessageBox(_("Token copied to clipboard!"), _("Success"), wx.OK | wx.ICON_INFORMATION)
		except Exception as e:
			# Translators: UI message for UI error: 
			wx.MessageBox(_("UI error: ") + str(e), _("Error"), wx.OK | wx.ICON_ERROR)

	def onCheckToken(self, event):
		token = self.tokenCtrl.GetValue().strip()
		if not token:
			# Translators: UI message for Please enter a token first!
			wx.MessageBox(_("Please enter a token first!"), _("Error"), wx.OK | wx.ICON_ERROR)
			return
			
		self.btnCheckToken.Disable()
		# Translators: UI message for Checking...
		self.btnCheckToken.SetLabel(_("Checking..."))
		
		def check():
			try:
				client = Client(token).init()
				account = client.me.account
				name = account.full_name or account.login or "User"
				# Translators: UI message for Token is Valid! Account: 
				msg = f"{_('Token is Valid! Account: ')} {name}"
				# Translators: UI message for Success
				wx.CallAfter(wx.MessageBox, msg, _("Success"), wx.OK | wx.ICON_INFORMATION)
			except Exception as e:
				# Translators: UI message for Token is Invalid!
				wx.CallAfter(wx.MessageBox, f"{_('Token is Invalid!')}\n\n{str(e)}", _("Error"), wx.OK | wx.ICON_ERROR)
			finally:
				def restore():
					self.btnCheckToken.Enable()
					# Translators: UI message for Check Token Validity
					self.btnCheckToken.SetLabel(_("Check Token Validity"))
				wx.CallAfter(restore)
				
		threading.Thread(target=check).start()

	def onSave(self):
		config.conf["yandexMusic"]["token"] = self.tokenCtrl.GetValue().strip()
		config.conf["yandexMusic"]["download_folder"] = self.outFolderCtrl.GetValue().strip()
		config.conf["yandexMusic"]["bitrate"] = 192 if self.bitrateChoice.GetSelection() == 0 else 320
		config.conf["yandexMusic"]["preview_player"] = self.previewPlayerCtrl.GetValue().strip()


class YandexMusicDialog(wx.Dialog):
	def __init__(self, parent):
		# Translators: UI message for Yandex Music Downloader
		super(YandexMusicDialog, self).__init__(parent, title=_("Yandex Music Downloader"), size=(500, 500))
		self.client = None
		self.search_results = []
		self.history = []
		self._init_ui()
		self.Bind(wx.EVT_CLOSE, self.on_close)
		self.Bind(wx.EVT_CHAR_HOOK, self.on_char_hook)

	def _init_ui(self):
		panel = wx.Panel(self)
		vbox = wx.BoxSizer(wx.VERTICAL)
		
		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: UI message for Search:
		lbl_search = wx.StaticText(panel, label=_("Search:"))
		self.tc_search = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
		# Translators: UI message for Search
		self.btn_search = wx.Button(panel, label=_("Search"))
		# Translators: UI message for My Playlists
		self.btn_my_music = wx.Button(panel, label=_("My Playlists"))
		
		hbox1.Add(lbl_search, flag=wx.RIGHT, border=8)
		hbox1.Add(self.tc_search, proportion=1)
		hbox1.Add(self.btn_search, flag=wx.LEFT, border=8)
		hbox1.Add(self.btn_my_music, flag=wx.LEFT, border=8)
		
		self.tc_search.Bind(wx.EVT_TEXT_ENTER, self.on_search)
		self.btn_search.Bind(wx.EVT_BUTTON, self.on_search)
		self.btn_my_music.Bind(wx.EVT_BUTTON, self.on_my_music)
		
		self.lb_results = wx.ListBox(panel, style=wx.LB_EXTENDED)
		
		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: UI message for Close
		self.btn_close = wx.Button(panel, label=_("Close"))
		hbox2.Add(self.btn_close, proportion=1)
		
		self.btn_close.Bind(wx.EVT_BUTTON, self.on_close)
		
		self.lb_results.Bind(wx.EVT_LISTBOX_DCLICK, self.on_view)
		self.lb_results.Bind(wx.EVT_CONTEXT_MENU, self.on_context_menu)
		self.lb_results.Bind(wx.EVT_KEY_DOWN, self.on_key_down)
		
		vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(self.lb_results, proportion=1, flag=wx.EXPAND|wx.ALL, border=10)
		vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=10)
		
		panel.SetSizer(vbox)
		self.tc_search.SetFocus()

	def on_char_hook(self, event):
		keycode = event.GetKeyCode()
		if event.AltDown() and keycode == wx.WXK_F4:
			self.on_close(None)
			return
		if keycode == wx.WXK_ESCAPE:
			self.on_close(None)
		elif keycode in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):
			if wx.Window.FindFocus() == self.lb_results:
				self.on_view(None)
				return
			event.Skip()
		elif keycode in (ord('A'), ord('a'), 1060, 1092, ord('D'), ord('d'), 1042, 1074, ord('P'), ord('p'), 1047, 1079, ord('T'), ord('t'), 1045, 1077):
			if wx.Window.FindFocus() == self.lb_results:
				sels = self.lb_results.GetSelections()
				if not sels:
					event.Skip()
					return
				item_type, display_text, obj = self.search_results[sels[0]]
				
				if keycode in (ord('A'), ord('a'), 1060, 1092):
					if item_type == "Album":
						self.on_download(None)
					else:
						# Translators: UI message for This is not an album.
						wx.CallAfter(ui.message, _("This is not an album."))
					return
				elif keycode in (ord('D'), ord('d'), 1042, 1074):
					if item_type == "Track" or item_type == "LikedTracks":
						self.on_download(None)
					else:
						# Translators: UI message for This is not a track.
						wx.CallAfter(ui.message, _("This is not a track."))
					return
				elif keycode in (ord('P'), ord('p'), 1047, 1079):
					if item_type == "Playlist":
						self.on_download(None)
					else:
						# Translators: UI message for This is not a playlist.
						wx.CallAfter(ui.message, _("This is not a playlist."))
					return
				elif keycode in (ord('T'), ord('t'), 1045, 1077):
					if item_type == "Track":
						self.on_save_lyrics(None)
					else:
						# Translators: UI message for This is not a track.
						wx.CallAfter(ui.message, _("This is not a track."))
					return
			event.Skip()
		elif keycode == wx.WXK_BACK:
			if wx.Window.FindFocus() == self.lb_results:
				self.go_back()
				return
			event.Skip()
		else:
			event.Skip()
	def on_context_menu(self, event):
		sels = self.lb_results.GetSelections()
		if not sels: return
		sel = sels[0]
		
		item_type, display_text, obj = self.search_results[sel]
		
		menu = wx.Menu()
		
		if self.history:
			# Translators: UI message for Go Back (Backspace)
			item_back = menu.Append(wx.ID_ANY, _("Go Back (Backspace)"))
			self.Bind(wx.EVT_MENU, lambda e: self.go_back(), item_back)
			
		if item_type != "Track":
			# Translators: UI message for View/Open
			item_view = menu.Append(wx.ID_ANY, _("View/Open"))
			self.Bind(wx.EVT_MENU, self.on_view, item_view)
			
		if item_type == "Track":
			# Translators: UI message for Preview / Listen
			item_preview = menu.Append(wx.ID_ANY, _("Preview / Listen"))
			self.Bind(wx.EVT_MENU, self.on_preview, item_preview)
			
			# Translators: UI message for Add to Playlist
			item_add_playlist = menu.Append(wx.ID_ANY, _("Add to Playlist"))
			self.Bind(wx.EVT_MENU, self.on_add_to_playlist, item_add_playlist)
			
			# Translators: UI message for Save Lyrics
			item_lyrics = menu.Append(wx.ID_ANY, _("Save Lyrics"))
			self.Bind(wx.EVT_MENU, self.on_save_lyrics, item_lyrics)
			
		# Translators: UI message for Download Selected
		item_download = menu.Append(wx.ID_ANY, _("Download Selected"))
		self.Bind(wx.EVT_MENU, self.on_download, item_download)
		
		self.PopupMenu(menu)
		menu.Destroy()

	def on_key_down(self, event):
		keycode = event.GetKeyCode()
		if event.ControlDown() and keycode == ord('P'):
			self.on_preview(None)
		elif keycode in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):
			self.on_view(None)
		elif keycode == wx.WXK_BACK:
			self.go_back()
		else:
			event.Skip()

	def on_save_lyrics(self, event):
		sels = self.lb_results.GetSelections()
		if not sels: return
		sel = sels[0]
		item_type, display_text, obj = self.search_results[sel]
		
		if item_type != "Track":
			return
			
		def do_save():
			try:
				client = self.get_client()
				if not client: return
				
				from logHandler import log
				log.info(f"YAMUSIC: Getting lyrics for {obj.id}")
				lyrics_text = None
				
				try:
					# Try supplement first
					supplement = obj.get_supplement()
					if supplement and getattr(supplement, 'lyrics', None) and getattr(supplement.lyrics, 'full_lyrics', None):
						lyrics_text = supplement.lyrics.full_lyrics
						log.info("YAMUSIC: Got lyrics from supplement")
				except Exception as e:
					log.error(f"YAMUSIC: Supplement error: {e}")
					
				if not lyrics_text:
					try:
						# Try tracks_lyrics fallback
						client = self.get_client()
						lyrics_obj = client.tracks_lyrics(obj.id) if client else None
						if lyrics_obj:
							lyrics_text = lyrics_obj.fetch_lyrics()
							log.info("YAMUSIC: Got lyrics from tracks_lyrics")
					except Exception as e:
						log.error(f"YAMUSIC: tracks_lyrics error: {e}")

				if not lyrics_text:
					# Translators: UI message for No lyrics available for this track.
					wx.CallAfter(ui.message, _("No lyrics available for this track."))
					return
					
				text = lyrics_text
					
				base_folder = config.conf["yandexMusic"].get("download_folder", "").strip()
				import os
				import re
				if not base_folder:
					base_folder = os.path.join(os.path.expanduser("~"), "Downloads", "YandexMusic")
				
				# Translators: UI message for Lyrics
				lyrics_folder = os.path.join(base_folder, _("Lyrics"))
				if not os.path.exists(lyrics_folder):
					os.makedirs(lyrics_folder)
					
				safe_title = re.sub(r'[\\/*?:"<>|]', "", display_text).strip()
				filepath = os.path.join(lyrics_folder, f"{safe_title}.txt")
				
				with open(filepath, "w", encoding="utf-8") as f:
					f.write(text)
					
				# Translators: UI message for Lyrics saved to: 
				wx.CallAfter(ui.message, _("Lyrics saved to: ") + filepath)
			except Exception as e:
				from logHandler import log
				log.error(f"YAMUSIC Save Error: {e}", exc_info=True)
				# Translators: UI message for Error:
				wx.CallAfter(ui.message, _("Error:") + " " + str(e))
				
		import threading
		threading.Thread(target=do_save).start()

	def on_add_to_playlist(self, event):
		sels = self.lb_results.GetSelections()
		if not sels: return
		sel = sels[0]
		item_type, display_text, obj = self.search_results[sel]
		
		if item_type != "Track":
			return
			
		# Translators: UI message for Loading profile...
		ui.message(_("Loading profile..."))
		
		def do_add():
			try:
				client = self.get_client()
				if not client: return
				my_playlists = client.users_playlists_list()
				if not my_playlists:
					wx.CallAfter(ui.message, _("No results"))
					return
				
				titles = [p.title for p in my_playlists]
				
				def show_dialog():
					# Translators: UI message for Select Playlist
					dlg = wx.SingleChoiceDialog(self, _("Select Playlist"), _("Add to Playlist"), titles)
					if dlg.ShowModal() == wx.ID_OK:
						sel_idx = dlg.GetSelection()
						p = my_playlists[sel_idx]
						
						def add_track():
							try:
								full_playlist = client.users_playlists(kind=p.kind, user_id=p.uid)
								exists = False
								for st in full_playlist.tracks:
									if st.track and str(st.track.id) == str(obj.id):
										exists = True
										break
								if exists:
									wx.CallAfter(ui.message, _("Track already exists in this playlist!"))
								else:
									rev = full_playlist.revision
									client.users_playlists_insert_track(kind=p.kind, track_id=obj.id, album_id=obj.albums[0].id if obj.albums else None, revision=rev)
									wx.CallAfter(ui.message, _("Track added successfully!"))
							except Exception as e:
								wx.CallAfter(ui.message, _("Error:") + " " + str(e))
						threading.Thread(target=add_track).start()
					dlg.Destroy()
				wx.CallAfter(show_dialog)
			except Exception as e:
				wx.CallAfter(ui.message, _("Error:") + " " + str(e))
				
		threading.Thread(target=do_add).start()

	def on_preview(self, event):
		sels = self.lb_results.GetSelections()
		if not sels: return
		
		sel = sels[0]
		item_type, display_text, obj = self.search_results[sel]
		
		if item_type != "Track":
			# Translators: UI message for You can only preview tracks.
			ui.message(_("You can only preview tracks."))
			return
			
		# Translators: UI message for Loading stream...
		ui.message(_("Loading stream..."))
		def load_stream():
			try:
				client = self.get_client()
				if not client: return
				infos = obj.get_download_info(get_direct_links=True)
				infos.sort(key=lambda x: x.bitrate_in_kbps, reverse=True)
				direct_url = infos[0].get_direct_link()
				
				player = config.conf["yandexMusic"].get("preview_player", "default").strip()
				if player.lower() == "default" or not player:
					import webbrowser
					webbrowser.open(direct_url)
				else:
					import subprocess
					if not os.path.isabs(player) and not "\\" in player:
						subprocess.Popen(f'start "" "{player}" "{direct_url}"', shell=True)
					else:
						subprocess.Popen([player, direct_url])
			except Exception as e:
				from logHandler import log
				log.error(f"YAMUSIC Save Error: {e}", exc_info=True)
				# Translators: UI message for Error:
				wx.CallAfter(ui.message, _("Error:") + " " + str(e))
				
		threading.Thread(target=load_stream).start()

	def go_back(self):
		if not self.history:
			# Translators: UI message for Already at main menu
			ui.message(_("Already at main menu"))
			return
		prev_results, prev_sel = self.history.pop()
		self.search_results = prev_results
		self.lb_results.Clear()
		for item_type, display_text, obj in prev_results:
			self.lb_results.Append(display_text)
		if prev_sel != wx.NOT_FOUND and prev_sel < self.lb_results.GetCount():
			self.lb_results.SetSelection(prev_sel)
			self.lb_results.SetFocus()
			ui.message(self.lb_results.GetString(prev_sel))

	def get_client(self):
		token = config.conf["yandexMusic"]["token"].strip()
		if not token:
			# Translators: UI message for Please enter a token first!
			ui.message(_("Please enter a token first!"))
			return None
		try:
			return Client(token).init()
		except Exception:
			# Translators: UI message for Token is Invalid!
			ui.message(_("Token is Invalid!"))
			return None

	def on_my_music(self, event):
		self.history = []
		# Translators: UI message for Loading profile...
		ui.message(_("Loading profile..."))
		
		def load_my():
			try:
				client = self.get_client()
				if not client: return
				results = []
				# Translators: UI message for Create Playlist
				results.append(("CreatePlaylist", _("Create Playlist"), None))
				# Translators: UI message for [My] Liked Tracks
				results.append(("LikedTracks", _("[My] Liked Tracks"), None))
				
				my_playlists = client.users_playlists_list()
				if my_playlists:
					for p in my_playlists:
						# Translators: UI message for [My Playlist]
						results.append(("Playlist", f"{_('[My Playlist]')} {p.title}", p))
						
				liked_albums = client.users_likes_albums()
				if liked_albums:
					for la in liked_albums[:15]:
						a = la.album
						artist = a.artists[0].name if a.artists else "Unknown"
						# Translators: UI message for [Liked Album]
						results.append(("Album", f"{_('[Liked Album]')} {artist} - {a.title}", a))
						
				wx.CallAfter(self._update_results, results, push_history=True)
				# Translators: UI message for Done!
				wx.CallAfter(ui.message, _("Done!"))
			except Exception as e:
				from logHandler import log
				log.error(f"YAMUSIC Save Error: {e}", exc_info=True)
				# Translators: UI message for Error:
				wx.CallAfter(ui.message, _("Error:") + " " + str(e))
				
		threading.Thread(target=load_my).start()

	def on_search(self, event):
		query = self.tc_search.GetValue().strip()
		if not query: return
		
		# Translators: UI message for Searching...
		ui.message(_("Searching..."))
		self.lb_results.Clear()
		self.search_results = []
		self.history = []
		
		def do_search():
			try:
				client = self.get_client()
				if not client: return
				
				results = []
				if "music.yandex" in query:
					if "/track/" in query:
						match = re.search(r'/track/(\d+)', query)
						if match:
							t = client.tracks([match.group(1)])[0]
							artist = t.artists[0].name if t.artists else "Unknown"
							# Translators: UI message for Track
							results.append(("Track", f"[{_('Track')}] {artist} - {t.title}", t))
					elif "/album/" in query:
						match = re.search(r'/album/(\d+)', query)
						if match:
							a = client.albums([match.group(1)])[0]
							artist = a.artists[0].name if a.artists else "Unknown"
							# Translators: UI message for Album
							results.append(("Album", f"[{_('Album')}] {artist} - {a.title}", a))
					elif "/artist/" in query:
						match = re.search(r'/artist/(\d+)', query)
						if match:
							art = client.artists([match.group(1)])[0]
							# Translators: UI message for Artist
							results.append(("Artist", f"[{_('Artist')}] {art.name}", art))
					elif "/playlists/" in query:
						match1 = re.search(r'/users/([^/]+)/playlists/([a-zA-Z0-9.\-]+)', query)
						match2 = re.search(r'/playlists/([a-zA-Z0-9.\-]+)', query)
						
						p = None
						if match1:
							p = client.users_playlists(kind=match1.group(2), user_id=match1.group(1))
						elif match2:
							kind = match2.group(1)
							try:
								import urllib.request
								req = urllib.request.Request(query, headers={'User-Agent': 'Mozilla/5.0'})
								html = urllib.request.urlopen(req).read().decode('utf-8')
								m = re.search(r'"uid"\s*:\s*(\d+)', html)
								if m:
									p = client.users_playlists(kind=kind, user_id=m.group(1))
							except Exception:
								pass
								
						if p:
							owner = p.owner.name if p.owner else "Unknown"
							# Translators: UI message for Playlist
							results.append(("Playlist", f"[{_('Playlist')}] {owner} - {p.title}", p))
				else:
					res = client.search(query)
					
					if res.artists:
						for art in res.artists.results[:5]:
							# Translators: UI message for Artist
							results.append(("Artist", f"[{_('Artist')}] {art.name}", art))
							
					if res.tracks:
						for t in res.tracks.results[:8]:
							artist = t.artists[0].name if t.artists else "Unknown"
							# Translators: UI message for Track
							results.append(("Track", f"[{_('Track')}] {artist} - {t.title}", t))
							
					if res.albums:
						for a in res.albums.results[:5]:
							artist = a.artists[0].name if a.artists else "Unknown"
							# Translators: UI message for Album
							results.append(("Album", f"[{_('Album')}] {artist} - {a.title}", a))
							
					if res.playlists:
						for p in res.playlists.results[:5]:
							owner = p.owner.name if p.owner else "Unknown"
							# Translators: UI message for Playlist
							results.append(("Playlist", f"[{_('Playlist')}] {owner} - {p.title}", p))
							
				wx.CallAfter(self._update_results, results, push_history=True)
			except Exception as e:
				from logHandler import log
				log.error(f"YAMUSIC Save Error: {e}", exc_info=True)
				# Translators: UI message for Error:
				wx.CallAfter(ui.message, _("Error:") + " " + str(e))
				
		threading.Thread(target=do_search).start()
		
	def on_view(self, event):
		sels = self.lb_results.GetSelections()
		if not sels: return
		sel = sels[0]
		
		item_type, display_text, obj = self.search_results[sel]
		
		if item_type == "CreatePlaylist":
			# Translators: UI message for Enter new playlist name:
			dlg = wx.TextEntryDialog(self, _("Enter new playlist name:"), _("Create Playlist"))
			if dlg.ShowModal() == wx.ID_OK:
				title = dlg.GetValue().strip()
				if title:
					def create_pl():
						try:
							client = self.get_client()
							if client:
								client.users_playlists_create(title=title)
								wx.CallAfter(self.on_my_music, None)
						except Exception as e:
							wx.CallAfter(ui.message, _("Error:") + " " + str(e))
					threading.Thread(target=create_pl).start()
			dlg.Destroy()
			return
			
		if item_type == "Artist":
			# Translators: UI message for Loading profile...
			ui.message(_("Loading profile..."))
			
			def load_artist():
				try:
					client = self.get_client()
					if not client: return
					results = []
					try:
						albums_res = client.artists_direct_albums(obj.id)
						albums = getattr(albums_res, 'albums', albums_res) or []
						for a in list(albums)[:15]:
							# Translators: UI message for Album
							results.append(("Album", f"[{_('Album')}] {a.title}", a))
					except Exception:
						pass
						
					try:
						tracks_res = client.artists_tracks(obj.id)
						tracks = getattr(tracks_res, 'tracks', tracks_res) or []
						for t in list(tracks)[:15]:
							# Translators: UI message for Track
							results.append(("Track", f"[{_('Track')}] {t.title}", t))
					except Exception:
						pass
						
					if not results:
						# Translators: UI message for No results
						wx.CallAfter(ui.message, _("No results"))
						return
						
					wx.CallAfter(self._update_results, results, push_history=True)
					# Translators: UI message for Done!
					wx.CallAfter(ui.message, _("Done!"))
				except Exception as e:
					from logHandler import log
				log.error(f"YAMUSIC Save Error: {e}", exc_info=True)
				# Translators: UI message for Error:
				wx.CallAfter(ui.message, _("Error:") + " " + str(e))
			
			threading.Thread(target=load_artist).start()
			
		elif item_type == "Album":
			# Translators: UI message for Loading profile...
			ui.message(_("Loading profile..."))
			
			def load_album():
				try:
					client = self.get_client()
					if not client: return
					results = []
					full_album = client.albums_with_tracks(obj.id)
					if isinstance(full_album, list):
						full_album = full_album[0]
					
					if getattr(full_album, 'volumes', None):
						for vol in full_album.volumes:
							for track in vol:
								artist = track.artists[0].name if track.artists else "Unknown"
								# Translators: UI message for Track
								results.append(("Track", f"[{_('Track')}] {artist} - {track.title}", track))
					else:
						# Translators: UI message for No tracks found in this album.
						wx.CallAfter(ui.message, _("No tracks found in this album."))
						return
						
					wx.CallAfter(self._update_results, results, push_history=True)
					# Translators: UI message for Done!
					wx.CallAfter(ui.message, _("Done!"))
				except Exception as e:
					from logHandler import log
				log.error(f"YAMUSIC Save Error: {e}", exc_info=True)
				# Translators: UI message for Error:
				wx.CallAfter(ui.message, _("Error:") + " " + str(e))
			threading.Thread(target=load_album).start()
			
		elif item_type == "Playlist":
			# Translators: UI message for Loading profile...
			ui.message(_("Loading profile..."))
			
			def load_playlist():
				try:
					client = self.get_client()
					if not client: return
					results = []
					full_playlist = client.users_playlists(kind=obj.kind, user_id=obj.uid)
					for short_track in full_playlist.tracks:
						track = short_track.track
						if track:
							artist = track.artists[0].name if track.artists else "Unknown"
							# Translators: UI message for Track
							results.append(("Track", f"[{_('Track')}] {artist} - {track.title}", track))
					wx.CallAfter(self._update_results, results, push_history=True)
					# Translators: UI message for Done!
					wx.CallAfter(ui.message, _("Done!"))
				except Exception as e:
					from logHandler import log
				log.error(f"YAMUSIC Save Error: {e}", exc_info=True)
				# Translators: UI message for Error:
				wx.CallAfter(ui.message, _("Error:") + " " + str(e))
			threading.Thread(target=load_playlist).start()
			
		elif item_type == "LikedTracks":
			# Translators: UI message for Loading profile...
			ui.message(_("Loading profile..."))
			
			def load_liked():
				try:
					client = self.get_client()
					if not client: return
					results = []
					tracks_info = client.users_likes_tracks().tracks
					for short_track in tracks_info[:50]:
						try:
							track = client.tracks([short_track.id])[0]
							artist = track.artists[0].name if track.artists else "Unknown"
							# Translators: UI message for Track
							results.append(("Track", f"[{_('Track')}] {artist} - {track.title}", track))
						except:
							pass
					wx.CallAfter(self._update_results, results, push_history=True)
					# Translators: UI message for Done!
					wx.CallAfter(ui.message, _("Done!"))
				except Exception as e:
					from logHandler import log
				log.error(f"YAMUSIC Save Error: {e}", exc_info=True)
				# Translators: UI message for Error:
				wx.CallAfter(ui.message, _("Error:") + " " + str(e))
			threading.Thread(target=load_liked).start()
			
		elif item_type == "Track":
			self.on_preview(None)
		else:
			# Translators: UI message for Cannot view this item.
			wx.CallAfter(ui.message, _("Cannot view this item."))

	def _update_results(self, results, push_history=False):
		if push_history and self.search_results:
			sels = self.lb_results.GetSelections()
			sel = sels[0] if sels else wx.NOT_FOUND
			self.history.append((self.search_results, sel))
		self.search_results = results
		self.lb_results.Clear()
		if not results:
			# Translators: UI message for No results
			ui.message(_("No results"))
			return
			
		for item_type, display_text, obj in results:
			self.lb_results.Append(display_text)
		
		self.lb_results.SetSelection(0)
		self.lb_results.SetFocus()
		ui.message(self.lb_results.GetString(0))

	def on_download(self, event):
		sels = self.lb_results.GetSelections()
		if not sels: return
		
		for sel in sels:
			if self.search_results[sel][0] == "Artist":
				# Translators: UI message for Please open the artist first, then download albums.
				ui.message(_("Please open the artist first, then download albums."))
				return
			
		download_dir = config.conf["yandexMusic"]["download_folder"]
		if not download_dir:
			download_dir = os.path.join(os.path.expanduser("~"), "Downloads", "YandexMusic")
		if not os.path.exists(download_dir):
			os.makedirs(download_dir)
			
		bitrate = config.conf["yandexMusic"]["bitrate"]
		# Translators: UI message for Downloading...
		ui.message(_("Downloading..."))
		
		def do_download():
			is_gathering = [True]
			
			def pulse():
				step = 0
				while is_gathering[0]:
					tones.beep(440 + (step % 4) * 20, 50)
					step += 1
					time.sleep(0.5)
			
			threading.Thread(target=pulse).start()
			
			try:
				tracks_to_download = []
				client = self.get_client()
				
				for sel in sels:
					item_type, display_text, obj = self.search_results[sel]
					
					if item_type == "Track":
						filename = f"{obj.artists[0].name if obj.artists else 'Unknown'} - {obj.title}.mp3"
						filename = "".join(c for c in filename if c not in r'\/:*?"<>|')
						path = os.path.join(download_dir, filename)
						tracks_to_download.append((obj, path))
						
					elif item_type == "Album":
						full_album = client.albums_with_tracks(obj.id)
						album_dir_name = f"Album - {obj.artists[0].name if obj.artists else 'Unknown'} - {obj.title}"
						album_dir_name = "".join(c for c in album_dir_name if c not in r'\/:*?"<>|')
						album_path = os.path.join(download_dir, album_dir_name)
						if not os.path.exists(album_path):
							os.makedirs(album_path)
							
						for vol in full_album.volumes:
							for track in vol:
								t_filename = f"{track.title}.mp3".replace("/", "_").replace(":", "_")
								t_path = os.path.join(album_path, t_filename)
								tracks_to_download.append((track, t_path))
								
					elif item_type == "Playlist":
						full_playlist = client.users_playlists(kind=obj.kind, user_id=obj.uid)
						playlist_dir_name = f"Playlist - {obj.title}"
						playlist_dir_name = "".join(c for c in playlist_dir_name if c not in r'\/:*?"<>|')
						playlist_path = os.path.join(download_dir, playlist_dir_name)
						if not os.path.exists(playlist_path):
							os.makedirs(playlist_path)
							
						for short_track in full_playlist.tracks:
							track = short_track.track
							if track:
								t_filename = f"{track.title}.mp3".replace("/", "_").replace(":", "_")
								t_path = os.path.join(playlist_path, t_filename)
								tracks_to_download.append((track, t_path))
								
					elif item_type == "LikedTracks":
						tracks_info = client.users_likes_tracks().tracks
						
						# Translators: UI message for My Liked Tracks
						liked_dir_name = _("My Liked Tracks")
						liked_path = os.path.join(download_dir, liked_dir_name)
						if not os.path.exists(liked_path):
							os.makedirs(liked_path)
							
						for short_track in tracks_info:
							try:
								track = client.tracks([short_track.id])[0]
								t_filename = f"{track.artists[0].name if track.artists else 'Unknown'} - {track.title}.mp3"
								t_filename = "".join(c for c in t_filename if c not in r'\/:*?"<>|')
								t_path = os.path.join(liked_path, t_filename)
								tracks_to_download.append((track, t_path))
							except Exception:
								pass 
								
				is_gathering[0] = False
				total = len(tracks_to_download)
				
				if total == 0:
					# Translators: UI message for No results
					wx.CallAfter(ui.message, _("No results"))
					return
					
				dlg = [None]
				def show_dlg():
					dlg[0] = wx.ProgressDialog(
						# Translators: UI message for Downloading...
						_("Downloading..."),
						# Translators: UI message for Downloading tracks...
						_("Downloading tracks..."),
						maximum=total,
						parent=gui.mainFrame,
						style=wx.PD_APP_MODAL | wx.PD_AUTO_HIDE
					)
				wx.CallAfter(show_dlg)
				
				while dlg[0] is None:
					time.sleep(0.1)
				
				total_downloaded = 0
				for track, path in tracks_to_download:
					try:
						infos = track.get_download_info()
						best_info = next((i for i in infos if i.bitrate_in_kbps == bitrate), None)
						if not best_info and infos:
							infos.sort(key=lambda x: x.bitrate_in_kbps, reverse=True)
							best_info = infos[0]
							
						if best_info:
							track.download(path, bitrate_in_kbps=best_info.bitrate_in_kbps)
						else:
							track.download(path)
							
						try:
							cover_bytes = track.download_cover_bytes()
							from mutagen.mp3 import MP3
							from mutagen.id3 import ID3, APIC, error
							audio = MP3(path, ID3=ID3)
							try:
								audio.add_tags()
							except error:
								pass
							audio.tags.add(
								APIC(
									encoding=3, 
									mime='image/jpeg', 
									type=3, 
									desc='Cover',
									data=cover_bytes
								)
							)
							audio.save()
						except Exception as cover_err:
							pass
							
					except Exception as e:
						wx.CallAfter(ui.message, f"Download error: {e}")
						time.sleep(1)
					total_downloaded += 1
					
					percent = int((total_downloaded / float(total)) * 100)
					pitch = int(110 * (2.0 ** (percent / 25.0)))
					tones.beep(pitch, 100)
					
					wx.CallAfter(ui.message, f"{percent}%")
					# Translators: UI message for Downloaded:
					wx.CallAfter(dlg[0].Update, total_downloaded, f"{_('Downloaded:')} {total_downloaded}/{total}")
				
				def finish_dlg():
					if dlg[0]:
						dlg[0].Hide()
						dlg[0].Destroy()
				wx.CallAfter(finish_dlg)
				tones.beep(1760, 200); tones.beep(2000, 200)
				# Translators: UI message for Done!
				wx.CallAfter(ui.message, f"{_('Done!')} {total_downloaded} {_('tracks')}")
				
			except Exception as e:
				is_gathering[0] = False
				from logHandler import log
				log.error(f"YAMUSIC Save Error: {e}", exc_info=True)
				# Translators: UI message for Error:
				wx.CallAfter(ui.message, _("Error:") + " " + str(e))
				
		threading.Thread(target=do_download).start()

	def on_close(self, event):
		self.Hide()
		wx.CallAfter(self.Destroy)


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Translators: UI message for YaMusic Helper
	scriptCategory = _("YaMusic Helper")

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(YandexMusicSettingsPanel)

	def terminate(self):
		try:
			gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(YandexMusicSettingsPanel)
		except ValueError:
			pass
		super(GlobalPlugin, self).terminate()

	# Translators: UI message for Open Yandex Downloader
	@script(description=_("Open Yandex Downloader"), gesture="kb:NVDA+shift+y")
	def script_openYandex(self, gesture):
		if not YANDEX_AVAILABLE:
			# Translators: UI message for Error: yandex-music library missing!
			ui.message(_("Error: yandex-music library missing!"))
			return
			
		def show():
			if not check_disclaimer(): return
			dlg = YandexMusicDialog(gui.mainFrame)
			dlg.Show()
		wx.CallAfter(show)
