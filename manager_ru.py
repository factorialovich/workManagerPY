#!/usr/bin/env python3

"""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║                     🔮 UNIVERSAL BOT & SITE MANAGER                 ║
║                                                                      ║
║   Многофункциональная консольная панель для управления              ║
║   Telegram-ботами (Python/NodeJS) и сайтами (Nginx/Apache2).         ║
║                                                                      ║
║   ✔ Автоматический поиск ботов (включая глубокие подпапки)          ║
║   ✔ Поддержка Python venv                                           ║
║   ✔ Работа с Node.js ботами                                         ║
║   ✔ Управление сайтами через Nginx/Apache2                       ║
║   ✔ Реальные статусы процессов (psutil)                             ║
║   ✔ Авто-логирование и ротация логов                                ║
║   ✔ Перезапуск всех ботов одной командой                            ║
║   ✔ Опциональная мягкая 24-bit цветовая схема                       ║
║   ✔ Адаптация под Termius / iTerm2 / Kitty / XTerm                  ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                          📌  ИСПОЛЬЗОВАНИЕ                           ║
╟──────────────────────────────────────────────────────────────────────╢
║  ▸ Запуск                                                             ║
║        $ python3 manager.py                                          ║
║                                                                      ║
║  ▸ При первом запуске скрипт автоматически предложит создать алиас,  ║
║    чтобы панель запускалась командой, например:                      ║
║                                                                      ║
║        $ panel                                                       ║
║                                                                      ║
║  ▸ Меню позволяет:                                                   ║
║       – запускать ботов                                              ║
║       – останавливать                                                 ║
║       – перезапускать                                                 ║
║       – смотреть статусы                                              ║
║       – управлять сайтами в Nginx/Apache2                        ║
║       – мягко перезапускать Nginx/Apache2                         ║
║                                                                      ║
║  ▸ Логи:                                                              ║
║       Логи каждого бота пишутся в:                                   ║
║            bot_folder/logs/botname.log                               ║
║       При перезапуске лог автоматически архивируется.                ║
║                                                                      ║
║  ▸ Статусы процессов:                                                 ║
║       Определяются через psutil по рабочей директории процесса.      ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                      🔍  КАК СКРИПТ ИЩЕТ БОТОВ                       ║
╟──────────────────────────────────────────────────────────────────────╢
║  ▸ Python-бот определяется по наличию файла:                         ║
║       index.py, main.py, bot.py, app.py                              ║
║                                                                      ║
║  ▸ NodeJS-бот:                                                       ║
║       package.json + один из файлов:                                 ║
║       index.js, bot.js, main.js, app.js                              ║
║                                                                      ║
║  ▸ Рекурсивный поиск:                                                 ║
║       Скрипт проходит *все папки*, начиная с директории, где он      ║
║       расположен, и находит ботов даже в глубоких вложениях.         ║
║                                                                      ║
║  ▸ Автоматическое определение venv:                                   ║
║       Ищется папка: venv / .venv / env                               ║
║       Используется python из неё.                                    ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                           🌐  САЙТЫ (NGINX/APACHE2)               ║
╟──────────────────────────────────────────────────────────────────────╢
║  ▸ Скрипт читает конфиги:                                            ║
║       /etc/nginx/sites-available/                                    ║
║       /etc/apache2/sites-available/                                    ║
║                                                                      ║
║  ▸ Показывает статус:                                                 ║
║       🟢 включён                                                      ║
║       🔴 отключён                                                     ║
║                                                                      ║
║  ▸ Включение / отключение сайта:                                      ║
║       создаёт или удаляет symlink в sites-enabled                    ║
║                                                                      ║
║  ▸ Автоматический reload после изменений.                            ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                       🎨  ОФОРМЛЕНИЕ И ЦВЕТА                         ║
╟──────────────────────────────────────────────────────────────────────╢
║  Скрипт использует мягкую 24-битную палитру (soft purple / beige /   ║
║  pastel tones). Если терминал не поддерживает true-color, цвета      ║
║  опадают до безопасных 256-color.                                    ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                   🧰  ЗАВИСИМОСТИ (УСТАНОВИТЬ)                       ║
╟──────────────────────────────────────────────────────────────────────╢
║  ▸ Python 3.8+                                                        ║
║  ▸ psutil                                                             ║
║                                                                      ║
║        $ pip install psutil                                           ║
║                                                                      ║
║  ▸ Node.js (если используешь js-ботов)                               ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                        🔗  ПОЛЕЗНЫЕ ССЫЛКИ                           ║
╟──────────────────────────────────────────────────────────────────────╢
║  ◉ GitHub                                                           ║
║      https://github.com/factorialovich/workManagerPY              ║
║                                                                      ║
║  ◉ psutil docs:                                                      ║
║      https://psutil.readthedocs.io/                                  ║
║                                                                      ║
║  ◉ Nginx docs:                                                       ║
║      https://nginx.org/en/docs/                                      ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                          ⚠️  ПРЕДУПРЕЖДЕНИЕ                          ║
╟──────────────────────────────────────────────────────────────────────╢
║  Автор скрипта и сопровождающие лица не несут ответственности за     ║
║  повреждение серверов, потерю данных или неверную конфигурацию.      ║
║                                                                      ║
║  Всегда тестируйте изменения в безопасном окружении.                 ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                         ✨  СОЗДАТЕЛЬ СКРИПТА                         ║
╟──────────────────────────────────────────────────────────────────────╢
║      Автор: factorialovich                                              ║
║      Telegram: https://t.me/factorcode                                ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import shutil
import subprocess
import json
import re
from datetime import datetime, timezone, timedelta

try:
    import psutil
except ImportError:
    print("❌ Ошибка: библиотека 'psutil' не установлена.", file=sys.stderr)
    print("Установите ее командой: pip install psutil", file=sys.stderr)
    sys.exit(1)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь, откуда начинается поиск ботов (папка, где лежит этот скрипт)


# <- ---- Основные настройки ---- -> #

PYTHON_SCRIPTS = ['index.py', 'main.py', 'bot.py', 'app.py'] # если твоего бота скрипт не видит, то добавь название главного файла.
NODEJS_SCRIPTS = ['index.js', 'app.js', 'bot.js', 'main.js'] # аналогично

# <- ---- @factorcode ---- -> #

STATE_FILE = os.path.expanduser('~/.manager_state.json')
MSK_TIMEZONE = timezone(timedelta(hours=3))

class C:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    # ------
    _SOFT_PURPLE = '\033[38;2;190;160;255m'
    _SOFT_BEIGE = '\033[38;2;235;225;210m'
    _SOFT_RED = '\033[38;2;255;150;150m'
    _SOFT_GREEN = '\033[38;2;170;230;185m'
    _SOFT_YELLOW = '\033[38;2;245;215;140m'
    _SOFT_BLUE = '\033[38;2;165;205;255m'
    _SOFT_CYAN = '\033[38;2;170;235;235m'
    _MUTED = '\033[38;2;170;170;170m'
    # ------
    RED = _SOFT_RED
    GREEN = _SOFT_GREEN
    YELLOW = _SOFT_YELLOW
    BLUE = _SOFT_PURPLE
    CYAN = _SOFT_CYAN
    WHITE = _SOFT_BEIGE

def _supports_truecolor():
    """проверка поддержки 24-битного цвета."""
    if not sys.stdout.isatty():
        return False

    colorterm = os.environ.get('COLORTERM', '').lower()
    term = os.environ.get('TERM', '').lower()
    if 'truecolor' in colorterm or '24bit' in colorterm:
        return True
    if any(x in term for x in ['xterm-kitty', 'tmux-truecolor']):
        return True
    return False

_TRUECOLOR = _supports_truecolor()

def gradient_text(text, start_rgb, end_rgb):
    """возвращает строку с градиентом от start_rgb до end_rgb."""
    if not _TRUECOLOR or not text:
        return text

    r1, g1, b1 = start_rgb
    r2, g2, b2 = end_rgb
    length = len(text)
    if length == 1:
        return f"\033[38;2;{r1};{g1};{b1}m{text}{C.RESET}"

    parts = []
    for i, ch in enumerate(text):
        t = i / (length - 1)
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        parts.append(f"\033[38;2;{r};{g};{b}m{ch}")
    parts.append(C.RESET)
    return ''.join(parts)

def soft_separator(width=40):
    """мягкий градиентный разделитель."""
    line = "─" * width
    return gradient_text(line, (190, 160, 255), (245, 215, 160))

def load_state():
    """загружает состояние временных меток из файла."""
    if not os.path.exists(STATE_FILE):
        return {}
    try:
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_state(state):
    """сохраняет состояние временных меток в файл."""
    try:
        with open(STATE_FILE, 'w') as f:
            json.dump(state, f, indent=4)
    except IOError as e:
        print(f"{C.RED}❌ Не удалось сохранить состояние: {e}{C.RESET}")

def clear_screen():
    """очищает экран консоли."""
    os.system('cls' if os.name == 'nt' else 'clear')

def run_sudo_command(command, error_message):
    """выполняет команду с sudo и обрабатывает ошибки."""
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result
    except FileNotFoundError:
        print(f"{C.RED}❌ Команда 'sudo' или 'systemctl' не найдена.{C.RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{C.RED}❌ {error_message}. Возможно, требуются права суперпользователя.{C.RESET}")
        print(f"{C.YELLOW}   Попробуйте запустить скрипт через 'sudo python3 manager.py'{C.RESET}")
        print(f"   {C.WHITE}Детали ошибки: {e.stderr.strip()}{C.RESET}")
    return None

def discover_sites_from_nginx():
    """читает конфиги Nginx для обнаружения сайтов, их доменов и корневых папок."""
    sites = []
    available_path = '/etc/nginx/sites-available/'
    
    if not os.path.isdir(available_path):
        return []

    for config_file in sorted(os.listdir(available_path)):
        config_path = os.path.join(available_path, config_file)
        if not os.path.isfile(config_path):
            continue

        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                content = f.read()

            root_match = re.search(r'^\s*root\s+([^\s;]+);', content, re.MULTILINE)
            server_name_match = re.search(r'^\s*server_name\s+([^;]+);', content, re.MULTILINE)

            if root_match and server_name_match:
                root_path = root_match.group(1).strip('\'"')
                if not os.path.isdir(root_path):
                    continue

                server_names = server_name_match.group(1).split()
                
                valid_domain = None
                for name in server_names:
                    if '.' in name and name != '_' and name.lower() != 'localhost' and not name.replace('.', '').isdigit():
                        valid_domain = name
                        break
                
                if valid_domain:
                    site_type = "PHP" if os.path.isfile(os.path.join(root_path, 'index.php')) else "HTML"
                    sites.append({
                        'name': valid_domain,
                        'config': config_file,
                        'dir': root_path,
                        'type': site_type,
                        'server': 'nginx'
                    })

        except Exception as e:
            print(f"{C.YELLOW}⚠️ Не удалось прочитать или обработать конфиг {config_file}: {e}{C.RESET}")
            
    return sites
    
def discover_sites_from_apache():
    """читает конфиги Apache для обнаружения сайтов, их доменов и корневых папок."""
    sites = []
    available_path = '/etc/apache2/sites-available/'
    
    if not os.path.isdir(available_path):
        return []

    for config_file in sorted(os.listdir(available_path)):
        config_path = os.path.join(available_path, config_file)
        if not os.path.isfile(config_path):
            continue
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                content = f.read()

            docroot_match = re.search(r'^\s*DocumentRoot\s+([^\s#]+)', content, re.MULTILINE)
            server_name_match = re.search(r'^\s*ServerName\s+([^\s#]+)', content, re.MULTILINE)
            server_aliases = re.findall(r'^\s*ServerAlias\s+(.+)$', content, re.MULTILINE)

            if not docroot_match:
                continue
            root_path = docroot_match.group(1).strip('\'"')
            if not os.path.isdir(root_path):
                continue
            valid_domain = None
            if server_name_match:
                candidate = server_name_match.group(1).strip()
                if candidate and candidate != 'localhost':
                    valid_domain = candidate
            if not valid_domain and server_aliases:
                alias_line = server_aliases[0]
                for name in alias_line.split():
                    if '.' in name and name != '_' and name.lower() != 'localhost':
                        valid_domain = name
                        break
            if not valid_domain:
                valid_domain = config_file

            site_type = "PHP" if os.path.isfile(os.path.join(root_path, 'index.php')) else "HTML"
            sites.append({
                'name': valid_domain,
                'config': config_file,
                'dir': root_path,
                'type': site_type,
                'server': 'apache2'
            })

        except Exception as e:
            print(f"{C.YELLOW}⚠️ Не удалось прочитать или обработать конфиг Apache {config_file}: {e}{C.RESET}")            
    return sites

def discover_bots_recursive(start_dir):
    """рекурсивно ищет папки ботов, начиная с start_dir."""
    all_bots = []

    if not os.path.isdir(start_dir):
        print(f"{C.YELLOW}⚠️  Предупреждение: Директория для ботов {start_dir} не найдена.{C.RESET}")
        return all_bots
    for dirpath, dirnames, filenames in os.walk(start_dir):
        bot_type = None
        script_name = None

        # ищем Python-бота
        for script in PYTHON_SCRIPTS:
            if script in filenames:
                bot_type = 'python'
                script_name = script
                break

        # если не Python, то ищем NodeJS бота
        if not bot_type and 'package.json' in filenames:
            for script in NODEJS_SCRIPTS:
                if script in filenames:
                    bot_type = 'nodejs'
                    script_name = script
                    break
                    
        if bot_type and script_name:
            python_executable = None
            if bot_type == 'python':
                # проверяем наличие venv в этой же папке
                venv_names = ['venv', '.venv', 'env']
                for venv_name in venv_names:
                    venv_python_path = os.path.join(dirpath, venv_name, 'bin', 'python')
                    if os.path.isfile(venv_python_path):
                        python_executable = venv_python_path
                        break

            all_bots.append({
                'name': os.path.basename(dirpath),
                'dir': dirpath,
                'type': bot_type,
                'script': script_name,
                'python_executable': python_executable
            })
            dirnames[:] = []
    return all_bots    

def discover_all_bots_and_sites(web_server):
    """находит всех ботов рекурсивно от BASE_DIR и сайты в зависимости от активного веб-сервера."""
    all_bots = discover_bots_recursive(BASE_DIR)
    all_sites = []
    if web_server and web_server.get('service') == 'nginx':
        all_sites = discover_sites_from_nginx()
    elif web_server and web_server.get('service') == 'apache2':
        all_sites = discover_sites_from_apache()
    return all_bots, all_sites

def update_bots_status(all_bots, state):
    """обновляет статус и время ботов."""
    running_procs = {proc.info['cwd']: proc for proc in psutil.process_iter(['pid', 'cmdline', 'cwd', 'create_time']) if proc.info['cwd']}

    for bot in all_bots:
        bot_dir = bot['dir']
        if bot_dir in running_procs:
            proc = running_procs[bot_dir]
            bot['pid'] = proc.info['pid']
            start_time = datetime.fromtimestamp(proc.info['create_time'], tz=MSK_TIMEZONE).strftime('%Y-%m-%d %H:%M:%S')
            bot['status'] = f"🟢 Активен (PID: {bot['pid']})"
            bot['time_info'] = f" | Запущен: {start_time}"
        else:
            bot['pid'] = None
            bot['status'] = '🔴 Остановлен'
            if bot_dir in state and 'last_stopped' in state[bot_dir]:
                stop_time = datetime.fromtimestamp(state[bot_dir]['last_stopped'], tz=MSK_TIMEZONE).strftime('%Y-%m-%d %H:%M:%S')
                bot['time_info'] = f" | Остановлен: {stop_time}"
            else:
                bot['time_info'] = ""
    return all_bots

def update_sites_status(all_sites, web_server):
    """обновляет статус сайтов (включен/отключен в Nginx/Apache)."""
    if not web_server or web_server['service'] not in ('nginx', 'apache2'):
        for site in all_sites:
            site['status'] = '⚪️ Неизвестно (веб-сервер не поддерживается)'
        return all_sites
    
    enabled_path = f'/etc/{web_server["service"]}/sites-enabled/'
    if not os.path.isdir(enabled_path):
        return all_sites

    for site in all_sites:
        config_file = site.get('config')
        if not config_file:
            site['status'] = '⚠️ Ошибка конфига'
            continue
        
        site['status'] = '🟢 Включен' if os.path.lexists(os.path.join(enabled_path, config_file)) else '🔴 Отключен'
    return all_sites

def kill_bot(pid, name, bot_dir):
    """завершает процесс бота и записывает время остановки."""
    if not pid:
        print(f"{C.YELLOW}⚠️  Для '{name}' нет активного процесса.{C.RESET}")
        return False
    try:
        process = psutil.Process(pid)
        process.terminate()
        process.wait(timeout=3)
    except psutil.TimeoutExpired:
        process.kill()
    except psutil.NoSuchProcess:
        pass
    except Exception as e:
        print(f"{C.RED}❌ Не удалось завершить процесс {pid} для '{name}': {e}{C.RESET}")
        return False
    
    state = load_state()
    state[bot_dir] = {'last_stopped': time.time()}
    save_state(state)
    print(f"{C.GREEN}✅ Сессия для '{name}' (PID: {pid}) успешно завершена.{C.RESET}")
    return True

def start_bot(bot, logging_enabled=True):
    """запускает бота и удаляет запись о времени остановки."""
    name, bot_dir = bot['name'], bot['dir']
    print(f"{C.CYAN}🚀 Запускаю '{name}' ({bot['type']})...{C.RESET}")
    command = None
    if bot['type'] == 'python':
        # используем python из venv если он есть, иначе системный python3
        python_path = bot.get('python_executable') or 'python3'
        command = ['nohup', python_path, bot['script']]
        if bot.get('python_executable'):
            print(f"{C.BLUE}   Используется виртуальное окружение (venv).{C.RESET}")
    elif bot['type'] == 'nodejs':
        command = ['nohup', 'node', bot['script']]
    if not command:
        print(f"{C.RED}❌ Неизвестный тип бота: {bot['type']}{C.RESET}")
        return
    try:
        if logging_enabled:
            logs_dir = os.path.join(bot_dir, 'logs')
            os.makedirs(logs_dir, exist_ok=True)
            log_file_path = os.path.join(logs_dir, f"{name}.log")

            if os.path.exists(log_file_path):
                ts = datetime.now(MSK_TIMEZONE).strftime('%Y-%m-%d_%H-%M-%S')
                rotated_path = os.path.join(logs_dir, f"{name}_{ts}.log")
                try:
                    os.rename(log_file_path, rotated_path)
                    print(f"{C.YELLOW}ℹ️ Старый лог переименован в: {rotated_path}{C.RESET}")
                except OSError as e:
                    print(f"{C.RED}⚠️ Не удалось переименовать старый лог-файл: {e}{C.RESET}")
            with open(log_file_path, 'a') as log_file:
                subprocess.Popen(
                    command,
                    cwd=bot_dir,
                    stdout=log_file,
                    stderr=log_file,
                    start_new_session=True
                )
            print(f"{C.GREEN}✅ '{name}' запущен. Логи пишутся в: {log_file_path}{C.RESET}")
        else:
            subprocess.Popen(
                command,
                cwd=bot_dir,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True
            )
            print(f"{C.GREEN}✅ '{name}' запущен в фоновом режиме (без логирования).{C.RESET}")
            
        state = load_state()
        if bot_dir in state:
            state.pop(bot_dir)
            save_state(state)
    except Exception as e:
        print(f"{C.RED}❌ Не удалось запустить '{name}': {e}{C.RESET}")

def get_web_server_status():
    """проверяет статус Nginx и Apache2."""
    servers = {'nginx': 'Nginx', 'apache2': 'Apache2'}
    for service, name in servers.items():
        if shutil.which(service) and subprocess.run(['systemctl', 'is-active', '--quiet', service]).returncode == 0:
            return {'name': name, 'service': service, 'status': '🟢 Активен'}
    return {'name': 'Nginx/Apache', 'service': None, 'status': '🔴 Не найден'}

def reload_web_server(server):
    """мягко перезапускает веб-сервер."""
    if not server or not server['service']:
        print(f"{C.YELLOW}⚠️ Активный веб-сервер не обнаружен.{C.RESET}"); return False
        
    print(f"{C.CYAN}🔄 Применяю конфигурацию для {server['name']}...{C.RESET}")
    command = ['sudo', 'systemctl', 'reload', server['service']]
    if run_sudo_command(command, f"Ошибка при перезагрузке {server['name']}"):
        print(f"{C.GREEN}✅ {server['name']} успешно перезагружен.{C.RESET}")
        return True
    return False

def toggle_site_status(site, server, enable):
    """включает или отключает сайт."""
    service, site_name, config_file = server['service'], site['name'], site.get('config')
    available_path = f"/etc/{service}/sites-available/"
    enabled_path = f"/etc/{service}/sites-enabled/"
    
    if not config_file or not os.path.exists(os.path.join(available_path, config_file)):
        print(f"{C.RED}❌ Не найден файл конфигурации '{config_file}' для '{site_name}' в {available_path}{C.RESET}")
        return

    source, link = os.path.join(available_path, config_file), os.path.join(enabled_path, config_file)
    action_text = "Включаю" if enable else "Отключаю"
    command = ['sudo', 'ln', '-s', source, link] if enable else ['sudo', 'rm', link]
    error_msg = f"Ошибка при {'включении' if enable else 'отключении'} сайта"
    
    print(f"{C.CYAN}{action_text} сайт '{site_name}'...{C.RESET}")
    if run_sudo_command(command, error_msg):
        print(f"{C.GREEN}✅ Сайт '{site_name}' успешно {'включен' if enable else 'отключен'}.{C.RESET}")
        reload_web_server(server)

def display_menu(bots, sites, web_server):
    """отображает главное меню."""
    clear_screen()
    term_width = shutil.get_terminal_size().columns

    title = "⚙️ ПАНЕЛЬ УПРАВЛЕНИЯ ⚙️".center(term_width)
    title_colored = gradient_text(title, (190, 160, 255), (245, 215, 190))
    print(C.BOLD + title_colored + C.RESET)
    
    if not bots and not sites:
        print(f"\nНе найдено ни ботов в {C.CYAN}{BASE_DIR}{C.RESET}, ни сайтов для обнаруженного веб-сервера.")
        return None

    print(f"\n{C.BOLD}{C.CYAN}💎 Список ботов для управления:{C.RESET}")
    if bots:
        for i, bot in enumerate(bots):
            status_color = C.GREEN if '🟢' in bot['status'] else C.RED
            time_color = C.WHITE if '🟢' in bot['status'] else C.YELLOW
            # добавляем пометку (venv) если бот использует виртуальное окружение
            venv_tag = f" {C.BLUE}(venv){C.RESET}" if bot.get('python_executable') else ""
            print(f"  {C.YELLOW}[{i+1}]{C.RESET} {bot['name']:<20}{venv_tag} - {status_color}{bot['status']}{C.RESET}{time_color}{bot['time_info']}{C.RESET}")
    else: print("  Боты не найдены.")
    
    server_label = 'Nginx/Apache'
    if web_server and web_server.get('service') == 'nginx':
        server_label = 'Nginx'
    elif web_server and web_server.get('service') == 'apache2':
        server_label = 'Apache2'

    print(f"\n{C.BOLD}{C.CYAN}🌐 Список сайтов ({server_label}):{C.RESET}")
    if sites:
        for i, site in enumerate(sites):
            status_color = C.GREEN if '🟢' in site.get('status', '') else C.RED
            site_num = len(bots) + i + 1
            print(f"  {C.YELLOW}[{site_num}]{C.RESET} {site['name']:<20} - {status_color}{site.get('status', 'Статус неизвестен')}{C.RESET}")
    else:
        if web_server and web_server.get('service') == 'nginx':
            print("  Сайты в '/etc/nginx/sites-available/' не найдены.")
        elif web_server and web_server.get('service') == 'apache2':
            print("  Сайты в '/etc/apache2/sites-available/' не найдены.")
        else:
            print("  Веб-сервер не обнаружен или не поддерживается.")

    if web_server and web_server['service']:
       status_color = C.GREEN if '🟢' in web_server['status'] else C.RED
       print(f"\n{C.BOLD}{C.CYAN}🖥️  Веб-сервер:{C.RESET}")
       print(f"  {web_server['name']:<22} - {status_color}{web_server['status']}{C.RESET}")

    print("\n" + C.BLUE + "─" * 40 + C.RESET)
    print(f"{C.BOLD}--- Действия ---{C.RESET}")
    print(f"  {C.YELLOW}[r]{C.RESET} Перезагрузить {C.BOLD}ВСЕХ{C.RESET} активных ботов {C.RED}(без логирования){C.RESET}")
    if web_server and web_server['service']:
        print(f"  {C.YELLOW}[s]{C.RESET} 'Мягко' перезагрузить веб-сервер ({web_server['name']})")
    print(f"  {C.YELLOW}[q]{C.RESET} Выход")
    print(soft_separator(40))
    
    return input(f"{C.BOLD}Выберите номер для управления или введите команду: {C.RESET}").lower().strip()

def handle_single_bot_menu(bot):
    """меню управления для одного конкретного бота."""
    status_color = C.GREEN if '🟢' in bot['status'] else C.RED
    clear_screen()
    print(C.BOLD + C.YELLOW + f"--- Управление ботом: '{bot['name']}' ---" + C.RESET)
    print(f"  Статус: {status_color}{bot['status']}{C.RESET}{C.WHITE}{bot['time_info']}{C.RESET}")    
    print("\n" + soft_separator(35))
    
    if bot['pid']:
        print(f"  {C.YELLOW}[1]{C.RESET} 🔴 Остановить")
        print(f"  {C.YELLOW}[2]{C.RESET} 🔄 Перезагрузить")
    else:
        print(f"  {C.YELLOW}[1]{C.RESET} 🟢 Запустить")
    print(f"  {C.YELLOW}[любая другая клавиша]{C.RESET} ← Назад")
    print(soft_separator(35))
    action = input(f"{C.BOLD}Выберите действие: {C.RESET}").strip()

    ask_logging = lambda: input("Включить логирование в файл? [Y/n]: ").lower().strip() != 'n'

    if bot['pid']:
        if action == '1': kill_bot(bot['pid'], bot['name'], bot['dir'])
        elif action == '2':
            if kill_bot(bot['pid'], bot['name'], bot['dir']):
                time.sleep(1); start_bot(bot, logging_enabled=ask_logging())
    else:
        if action == '1': start_bot(bot, logging_enabled=ask_logging())

def handle_single_site_menu(site, web_server):
    """меню управления для одного конкретного сайта."""
    if web_server['service'] not in ('nginx', 'apache2'):
        print(f"{C.YELLOW}Управление сайтами доступно только для Nginx/Apache.{C.RESET}")
        time.sleep(2)
        return

    status_color = C.GREEN if '🟢' in site['status'] else C.RED
    clear_screen()
    print(C.BOLD + C.YELLOW + f"--- Управление сайтом: '{site['name']}' ---" + C.RESET)
    print(f"  Статус: {status_color}{site['status']}{C.RESET}")

    print("\n" + soft_separator(35))
    if '🟢' in site['status']:
        print(f"  {C.YELLOW}[1]{C.RESET} 🔴 Отключить сайт")
    else:
        print(f"  {C.YELLOW}[1]{C.RESET} 🟢 Включить сайт")
    print(f"  {C.YELLOW}[любая другая клавиша]{C.RESET} ← Назад")
    print(soft_separator(35))
    action = input(f"{C.BOLD}Выберите действие: {C.RESET}").strip()

    if action == '1':
        enable = '🔴' in site['status']
        toggle_site_status(site, web_server, enable=enable)

def initial_setup():
    """проверяет, был ли скрипт настроен, и если нет, создает алиас и перезапускается."""
    setup_flag_file = os.path.expanduser("~/.manager_setup_complete")
    if os.path.exists(setup_flag_file):
        return

    clear_screen()
    setup_title = "--- Первоначальная настройка ---"
    print(C.BOLD + gradient_text(setup_title, (190, 160, 255), (245, 215, 190)) + C.RESET)
    print("Похоже, вы запускаете этот скрипт впервые.")
    print("Давайте создадим команду для быстрого запуска.\n")

    alias_name = ""
    while not alias_name.isalnum():
        alias_name = input(f"Введите одно слово для вызова скрипта (например, 'panel'): {C.CYAN}").strip().lower()
        if not alias_name.isalnum():
            print(f"{C.RED}Имя может содержать только буквы и цифры.{C.RESET}")
    
    script_path = os.path.abspath(__file__)
    bashrc_path = os.path.expanduser("~/.bashrc")
    if not os.path.exists(bashrc_path): open(bashrc_path, 'a').close()
    alias_command = f"\nalias {alias_name}='python3 {script_path}' # Added by script. Creator @factorcode.\n"

    try:
        with open(bashrc_path, "a") as bashrc_file:
            bashrc_file.write(alias_command)
        
        open(setup_flag_file, 'a').close()
        print(f"\n{C.GREEN}✅ Алиас '{alias_name}' успешно добавлен в {bashrc_path}.{C.RESET}")
        print(f"{C.CYAN}Перезапускаю скрипт, чтобы применить изменения...{C.RESET}")
        time.sleep(2)

        os.execv('/bin/bash', ['/bin/bash', '-c', f"source {bashrc_path} && exec python3 '{script_path}'"])
    except Exception as e:
        print(f"{C.RED}❌ Не удалось записать в файл {bashrc_path}: {e}{C.RESET}")
        print("Вы можете добавить эту строку вручную:")
        print(f"{C.CYAN}{alias_command.strip()}{C.RESET}")
        input(f"{C.BOLD}Нажмите Enter, чтобы продолжить...{C.RESET}")

def main():
    """главная функция-цикл программы."""
    initial_setup()
    
    while True:
        try:
            state_data = load_state()
            web_server_info = get_web_server_status()
            all_bots, all_sites = discover_all_bots_and_sites(web_server_info)
            bots_with_status = update_bots_status(all_bots, state_data)
            sites_with_status = update_sites_status(all_sites, web_server_info)
            choice = display_menu(bots_with_status, sites_with_status, web_server_info)
            if choice is None: break

            if choice == 'q':
                clear_screen(); print(f"{C.CYAN}Выход из программы...{C.RESET}"); sys.exit(0)            
            elif choice == 'r':
                print(f"\n{C.YELLOW}🔄 Перезагрузка всех активных ботов...{C.RESET}\n")
                restarted_any = any(kill_bot(b['pid'], b['name'], b['dir']) and (time.sleep(1) or True) and start_bot(b, logging_enabled=False) is None for b in bots_with_status if b['pid'])
                if not restarted_any: print("Не было активных ботов для перезагрузки.")                
            elif choice == 's' and web_server_info and web_server_info['service']:
                reload_web_server(web_server_info)
            elif choice.isdigit():
                choice_num = int(choice)
                total_bots = len(bots_with_status)
                total_sites = len(sites_with_status)
                
                if 1 <= choice_num <= total_bots:
                    handle_single_bot_menu(bots_with_status[choice_num - 1])
                elif total_bots < choice_num <= total_bots + total_sites:
                    handle_single_site_menu(sites_with_status[choice_num - total_bots - 1], web_server_info)
                else:
                    print(f"{C.RED}❌ Неверный номер.{C.RESET}")
            else:
                print(f"{C.RED}❌ Неверный ввод.{C.RESET}")
            time.sleep(2)
        except KeyboardInterrupt:
            clear_screen(); print(f"\n{C.CYAN}Выход из программы...{C.RESET}"); sys.exit(0)
        except Exception as e:
            clear_screen(); print(f"{C.RED}❌ Произошла критическая ошибка: {e}{C.RESET}"); sys.exit(1)

if __name__ == "__main__":
    main() # @factorcode