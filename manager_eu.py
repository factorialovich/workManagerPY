#!/usr/bin/env python3

"""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║                     🔮 UNIVERSAL BOT & SITE MANAGER                 ║
║                                                                      ║
║   Multifunctional console panel for managing                         ║
║   Telegram bots (Python/NodeJS) and sites (Nginx/Apache2).           ║
║                                                                      ║
║   ✔ Automatic bot discovery (including deep subdirectories)          ║
║   ✔ Python venv support                                              ║
║   ✔ Node.js bot support                                              ║
║   ✔ Site management via Nginx/Apache2                                ║
║   ✔ Real process statuses (psutil)                                   ║
║   ✔ Auto logging and log rotation                                    ║
║   ✔ Restart all bots with a single command                           ║
║   ✔ Optional soft 24-bit color theme                                 ║
║   ✔ Tuned for Termius / iTerm2 / Kitty / XTerm                       ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                          📌  USAGE                                   ║
╟──────────────────────────────────────────────────────────────────────╢
║  ▸ Run                                                               ║
║        $ python3 manager.py                                          ║
║                                                                      ║
║  ▸ On first run, the script will automatically offer to create an    ║
║    alias so that you can launch the panel with a short command, e.g.:║
║                                                                      ║
║        $ panel                                                       ║
║                                                                      ║
║  ▸ The menu allows you to:                                           ║
║       – start bots                                                   ║
║       – stop bots                                                    ║
║       – restart bots                                                 ║
║       – view statuses                                                ║
║       – manage sites in Nginx/Apache2                                ║
║       – gracefully reload Nginx/Apache2                              ║
║                                                                      ║
║  ▸ Logs:                                                             ║
║       Each bot's logs are written to:                                ║
║            bot_folder/logs/botname.log                               ║
║       On restart, the old log is automatically rotated.              ║
║                                                                      ║
║  ▸ Process statuses:                                                 ║
║       Determined via psutil by the process working directory.        ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                      🔍  HOW BOTS ARE DISCOVERED                     ║
╟──────────────────────────────────────────────────────────────────────╢
║  ▸ A Python bot is detected by presence of a file:                   ║
║       index.py, main.py, bot.py, app.py                              ║
║                                                                      ║
║  ▸ A NodeJS bot is detected by:                                      ║
║       package.json + one of the files:                               ║
║       index.js, bot.js, main.js, app.js                              ║
║                                                                      ║
║  ▸ Recursive search:                                                 ║
║       The script walks *all folders* starting from the directory     ║
║       where it is located and finds bots even in deep subfolders.    ║
║                                                                      ║
║  ▸ Automatic venv detection:                                         ║
║       Looks for folders: venv / .venv / env                          ║
║       Uses python from that venv if found.                           ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                     🌐  SITES (NGINX/APACHE2)                        ║
╟──────────────────────────────────────────────────────────────────────╢
║  ▸ The script reads configs from:                                    ║
║       /etc/nginx/sites-available/                                    ║
║       /etc/apache2/sites-available/                                  ║
║                                                                      ║
║  ▸ Shows site status:                                                ║
║       🟢 enabled                                                      ║
║       🔴 disabled                                                     ║
║                                                                      ║
║  ▸ Enable / disable site:                                            ║
║       Creates or removes symlink in sites-enabled                    ║
║                                                                      ║
║  ▸ Automatically reloads web server after changes.                   ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                       🎨  LOOK & FEEL / COLORS                       ║
╟──────────────────────────────────────────────────────────────────────╢
║  The script uses a soft 24-bit color palette (soft purple / beige /  ║
║  pastel tones). If the terminal does not support true color, colors  ║
║  gracefully fall back to safe 256-color equivalents.                 ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                   🧰  DEPENDENCIES (INSTALL)                         ║
╟──────────────────────────────────────────────────────────────────────╢
║  ▸ Python 3.8+                                                       ║
║  ▸ psutil                                                            ║
║                                                                      ║
║        $ pip install psutil                                          ║
║                                                                      ║
║  ▸ Node.js (if you use JS bots)                                      ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                        🔗  USEFUL LINKS                              ║
╟──────────────────────────────────────────────────────────────────────╢
║  ◉ GitHub                                                            ║
║      https://github.com/factorialovich/workManagerPY                 ║
║                                                                      ║
║  ◉ psutil docs:                                                      ║
║      https://psutil.readthedocs.io/                                  ║
║                                                                      ║
║  ◉ Nginx docs:                                                       ║
║      https://nginx.org/en/docs/                                      ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                          ⚠️  DISCLAIMER                              ║
╟──────────────────────────────────────────────────────────────────────╢
║  The author of the script and contributors are not responsible for   ║
║  any server damage, data loss or misconfiguration.                   ║
║                                                                      ║
║  Always test changes in a safe environment first.                    ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                         ✨  SCRIPT AUTHOR                            ║
╟──────────────────────────────────────────────────────────────────────╢
║      Author: factorialovich                                          ║
║      Telegram: https://t.me/factorcode                               ║
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
    print("❌ Error: Python library 'psutil' is not installed.", file=sys.stderr)
    print("Install it with: pip install psutil", file=sys.stderr)
    sys.exit(1)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# directory from which bot discovery starts (the folder where this script lives)


# <- ---- Core settings ---- -> #

# if your bot is not detected, add its main script filename here
PYTHON_SCRIPTS = ['index.py', 'main.py', 'bot.py', 'app.py']
# same idea for NodeJS bots
NODEJS_SCRIPTS = ['index.js', 'app.js', 'bot.js', 'main.js']

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
    """Check if terminal supports 24-bit color."""
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
    """Return string with gradient color from start_rgb to end_rgb."""
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
    """Soft gradient line separator."""
    line = "─" * width
    return gradient_text(line, (190, 160, 255), (245, 215, 160))

def load_state():
    """Load timestamp state from file."""
    if not os.path.exists(STATE_FILE):
        return {}
    try:
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_state(state):
    """Save timestamp state to file."""
    try:
        with open(STATE_FILE, 'w') as f:
            json.dump(state, f, indent=4)
    except IOError as e:
        print(f"{C.RED}❌ Failed to save state: {e}{C.RESET}")

def clear_screen():
    """Clear console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def run_sudo_command(command, error_message):
    """Run command with sudo and handle errors."""
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result
    except FileNotFoundError:
        print(f"{C.RED}❌ Command 'sudo' or 'systemctl' not found.{C.RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{C.RED}❌ {error_message}. Superuser privileges may be required.{C.RESET}")
        print(f"{C.YELLOW}   Try running script as: 'sudo python3 manager.py'{C.RESET}")
        print(f"   {C.WHITE}Error details: {e.stderr.strip()}{C.RESET}")
    return None

def discover_sites_from_nginx():
    """Read Nginx configs to discover sites, domains and root directories."""
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
            print(f"{C.YELLOW}⚠️ Failed to read or parse config {config_file}: {e}{C.RESET}")
            
    return sites
    
def discover_sites_from_apache():
    """Read Apache configs to discover sites, their domains and root directories."""
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
            print(f"{C.YELLOW}⚠️ Failed to read or parse Apache config {config_file}: {e}{C.RESET}")            
    return sites

def discover_bots_recursive(start_dir):
    """Recursively search for bot folders starting from start_dir."""
    all_bots = []

    if not os.path.isdir(start_dir):
        print(f"{C.YELLOW}⚠️  Warning: bots directory {start_dir} not found.{C.RESET}")
        return all_bots
    for dirpath, dirnames, filenames in os.walk(start_dir):
        bot_type = None
        script_name = None

        # search for Python bot
        for script in PYTHON_SCRIPTS:
            if script in filenames:
                bot_type = 'python'
                script_name = script
                break

        # if not Python, search for NodeJS bot
        if not bot_type and 'package.json' in filenames:
            for script in NODEJS_SCRIPTS:
                if script in filenames:
                    bot_type = 'nodejs'
                    script_name = script
                    break
                    
        if bot_type and script_name:
            python_executable = None
            if bot_type == 'python':
                # check for venv in the same folder
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
            # do not descend into this folder further (avoid nested bots)
            dirnames[:] = []
    return all_bots    

def discover_all_bots_and_sites(web_server):
    """Discover all bots (recursively from BASE_DIR) and sites depending on active web server."""
    all_bots = discover_bots_recursive(BASE_DIR)
    all_sites = []
    if web_server and web_server.get('service') == 'nginx':
        all_sites = discover_sites_from_nginx()
    elif web_server and web_server.get('service') == 'apache2':
        all_sites = discover_sites_from_apache()
    return all_bots, all_sites

def update_bots_status(all_bots, state):
    """Update bots statuses and timestamps."""
    running_procs = {
        proc.info['cwd']: proc
        for proc in psutil.process_iter(['pid', 'cmdline', 'cwd', 'create_time'])
        if proc.info['cwd']
    }

    for bot in all_bots:
        bot_dir = bot['dir']
        if bot_dir in running_procs:
            proc = running_procs[bot_dir]
            bot['pid'] = proc.info['pid']
            start_time = datetime.fromtimestamp(proc.info['create_time'], tz=MSK_TIMEZONE).strftime('%Y-%m-%d %H:%M:%S')
            bot['status'] = f"🟢 Running (PID: {bot['pid']})"
            bot['time_info'] = f" | Started: {start_time}"
        else:
            bot['pid'] = None
            bot['status'] = '🔴 Stopped'
            if bot_dir in state and 'last_stopped' in state[bot_dir]:
                stop_time = datetime.fromtimestamp(state[bot_dir]['last_stopped'], tz=MSK_TIMEZONE).strftime('%Y-%m-%d %H:%M:%S')
                bot['time_info'] = f" | Stopped: {stop_time}"
            else:
                bot['time_info'] = ""
    return all_bots

def update_sites_status(all_sites, web_server):
    """Update site statuses (enabled/disabled in Nginx/Apache)."""
    if not web_server or web_server['service'] not in ('nginx', 'apache2'):
        for site in all_sites:
            site['status'] = '⚪️ Unknown (web server not supported)'
        return all_sites
    
    enabled_path = f'/etc/{web_server["service"]}/sites-enabled/'
    if not os.path.isdir(enabled_path):
        return all_sites

    for site in all_sites:
        config_file = site.get('config')
        if not config_file:
            site['status'] = '⚠️ Config error'
            continue
        
        site['status'] = '🟢 Enabled' if os.path.lexists(os.path.join(enabled_path, config_file)) else '🔴 Disabled'
    return all_sites

def kill_bot(pid, name, bot_dir):
    """Terminate bot process and record stop time."""
    if not pid:
        print(f"{C.YELLOW}⚠️  Bot '{name}' has no active process.{C.RESET}")
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
        print(f"{C.RED}❌ Failed to terminate process {pid} for '{name}': {e}{C.RESET}")
        return False
    
    state = load_state()
    state[bot_dir] = {'last_stopped': time.time()}
    save_state(state)
    print(f"{C.GREEN}✅ Session for '{name}' (PID: {pid}) successfully terminated.{C.RESET}")
    return True

def start_bot(bot, logging_enabled=True):
    """Start bot and clear stop timestamp."""
    name, bot_dir = bot['name'], bot['dir']
    print(f"{C.CYAN}🚀 Starting '{name}' ({bot['type']})...{C.RESET}")
    command = None
    if bot['type'] == 'python':
        # use python from venv if available, otherwise system python3
        python_path = bot.get('python_executable') or 'python3'
        command = ['nohup', python_path, bot['script']]
        if bot.get('python_executable'):
            print(f"{C.BLUE}   Using virtual environment (venv).{C.RESET}")
    elif bot['type'] == 'nodejs':
        command = ['nohup', 'node', bot['script']]
    if not command:
        print(f"{C.RED}❌ Unknown bot type: {bot['type']}{C.RESET}")
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
                    print(f"{C.YELLOW}ℹ️ Old log renamed to: {rotated_path}{C.RESET}")
                except OSError as e:
                    print(f"{C.RED}⚠️ Failed to rename old log file: {e}{C.RESET}")
            with open(log_file_path, 'a') as log_file:
                subprocess.Popen(
                    command,
                    cwd=bot_dir,
                    stdout=log_file,
                    stderr=log_file,
                    start_new_session=True
                )
            print(f"{C.GREEN}✅ '{name}' started. Logs are written to: {log_file_path}{C.RESET}")
        else:
            subprocess.Popen(
                command,
                cwd=bot_dir,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True
            )
            print(f"{C.GREEN}✅ '{name}' started in background (no logging).{C.RESET}")
            
        state = load_state()
        if bot_dir in state:
            state.pop(bot_dir)
            save_state(state)
    except Exception as e:
        print(f"{C.RED}❌ Failed to start '{name}': {e}{C.RESET}")

def get_web_server_status():
    """Check status of Nginx and Apache2."""
    servers = {'nginx': 'Nginx', 'apache2': 'Apache2'}
    for service, name in servers.items():
        if shutil.which(service) and subprocess.run(['systemctl', 'is-active', '--quiet', service]).returncode == 0:
            return {'name': name, 'service': service, 'status': '🟢 Active'}
    return {'name': 'Nginx/Apache', 'service': None, 'status': '🔴 Not found'}

def reload_web_server(server):
    """Soft reload of web server."""
    if not server or not server['service']:
        print(f"{C.YELLOW}⚠️ No active web server detected.{C.RESET}")
        return False
        
    print(f"{C.CYAN}🔄 Applying configuration for {server['name']}...{C.RESET}")
    command = ['sudo', 'systemctl', 'reload', server['service']]
    if run_sudo_command(command, f"Error reloading {server['name']}"):
        print(f"{C.GREEN}✅ {server['name']} reloaded successfully.{C.RESET}")
        return True
    return False

def toggle_site_status(site, server, enable):
    """Enable or disable a site."""
    service, site_name, config_file = server['service'], site['name'], site.get('config')
    available_path = f"/etc/{service}/sites-available/"
    enabled_path = f"/etc/{service}/sites-enabled/"
    
    if not config_file or not os.path.exists(os.path.join(available_path, config_file)):
        print(f"{C.RED}❌ Config file '{config_file}' for '{site_name}' not found in {available_path}{C.RESET}")
        return

    source, link = os.path.join(available_path, config_file), os.path.join(enabled_path, config_file)
    action_text = "Enabling" if enable else "Disabling"
    command = ['sudo', 'ln', '-s', source, link] if enable else ['sudo', 'rm', link]
    error_msg = f"Error while {'enabling' if enable else 'disabling'} site"
    
    print(f"{C.CYAN}{action_text} site '{site_name}'...{C.RESET}")
    if run_sudo_command(command, error_msg):
        print(f"{C.GREEN}✅ Site '{site_name}' successfully {'enabled' if enable else 'disabled'}.{C.RESET}")
        reload_web_server(server)

def display_menu(bots, sites, web_server):
    """Render main menu."""
    clear_screen()
    term_width = shutil.get_terminal_size().columns

    title = "⚙️ CONTROL PANEL ⚙️".center(term_width)
    title_colored = gradient_text(title, (190, 160, 255), (245, 215, 190))
    print(C.BOLD + title_colored + C.RESET)
    
    if not bots and not sites:
        print(f"\nNo bots found in {C.CYAN}{BASE_DIR}{C.RESET} and no sites for the detected web server.")
        return None

    print(f"\n{C.BOLD}{C.CYAN}💎 Bot list:{C.RESET}")
    if bots:
        for i, bot in enumerate(bots):
            status_color = C.GREEN if '🟢' in bot['status'] else C.RED
            time_color = C.WHITE if '🟢' in bot['status'] else C.YELLOW
            # append (venv) label if bot uses virtual environment
            venv_tag = f" {C.BLUE}(venv){C.RESET}" if bot.get('python_executable') else ""
            print(
                f"  {C.YELLOW}[{i+1}]{C.RESET} {bot['name']:<20}{venv_tag} - "
                f"{status_color}{bot['status']}{C.RESET}"
                f"{time_color}{bot['time_info']}{C.RESET}"
            )
    else:
        print("  No bots found.")
    
    server_label = 'Nginx/Apache'
    if web_server and web_server.get('service') == 'nginx':
        server_label = 'Nginx'
    elif web_server and web_server.get('service') == 'apache2':
        server_label = 'Apache2'

    print(f"\n{C.BOLD}{C.CYAN}🌐 Site list ({server_label}):{C.RESET}")
    if sites:
        for i, site in enumerate(sites):
            status_color = C.GREEN if '🟢' in site.get('status', '') else C.RED
            site_num = len(bots) + i + 1
            print(
                f"  {C.YELLOW}[{site_num}]{C.RESET} {site['name']:<20} - "
                f"{status_color}{site.get('status', 'Status unknown')}{C.RESET}"
            )
    else:
        if web_server and web_server.get('service') == 'nginx':
            print("  No sites found in '/etc/nginx/sites-available/'.")
        elif web_server and web_server.get('service') == 'apache2':
            print("  No sites found in '/etc/apache2/sites-available/'.")
        else:
            print("  Web server not detected or not supported.")

    if web_server and web_server['service']:
        status_color = C.GREEN if '🟢' in web_server['status'] else C.RED
        print(f"\n{C.BOLD}{C.CYAN}🖥️  Web server:{C.RESET}")
        print(f"  {web_server['name']:<22} - {status_color}{web_server['status']}{C.RESET}")

    print("\n" + C.BLUE + "─" * 40 + C.RESET)
    print(f"{C.BOLD}--- Actions ---{C.RESET}")
    print(f"  {C.YELLOW}[r]{C.RESET} Restart {C.BOLD}ALL{C.RESET} active bots {C.RED}(without logging){C.RESET}")
    if web_server and web_server['service']:
        print(f"  {C.YELLOW}[s]{C.RESET} Soft reload web server ({web_server['name']})")
    print(f"  {C.YELLOW}[q]{C.RESET} Quit")
    print(soft_separator(40))
    
    return input(f"{C.BOLD}Select item number or enter a command: {C.RESET}").lower().strip()

def handle_single_bot_menu(bot):
    """Menu for managing a single bot."""
    status_color = C.GREEN if '🟢' in bot['status'] else C.RED
    clear_screen()
    print(C.BOLD + C.YELLOW + f"--- Bot management: '{bot['name']}' ---" + C.RESET)
    print(f"  Status: {status_color}{bot['status']}{C.RESET}{C.WHITE}{bot['time_info']}{C.RESET}")    
    print("\n" + soft_separator(35))
    
    if bot['pid']:
        print(f"  {C.YELLOW}[1]{C.RESET} 🔴 Stop")
        print(f"  {C.YELLOW}[2]{C.RESET} 🔄 Restart")
    else:
        print(f"  {C.YELLOW}[1]{C.RESET} 🟢 Start")
    print(f"  {C.YELLOW}[any other key]{C.RESET} ← Back")
    print(soft_separator(35))
    action = input(f"{C.BOLD}Choose action: {C.RESET}").strip()

    ask_logging = lambda: input("Enable logging to file? [Y/n]: ").lower().strip() != 'n'

    if bot['pid']:
        if action == '1':
            kill_bot(bot['pid'], bot['name'], bot['dir'])
        elif action == '2':
            if kill_bot(bot['pid'], bot['name'], bot['dir']):
                time.sleep(1)
                start_bot(bot, logging_enabled=ask_logging())
    else:
        if action == '1':
            start_bot(bot, logging_enabled=ask_logging())

def handle_single_site_menu(site, web_server):
    """Menu for managing a single site."""
    if web_server['service'] not in ('nginx', 'apache2'):
        print(f"{C.YELLOW}Site management is available only for Nginx/Apache.{C.RESET}")
        time.sleep(2)
        return

    status_color = C.GREEN if '🟢' in site['status'] else C.RED
    clear_screen()
    print(C.BOLD + C.YELLOW + f"--- Site management: '{site['name']}' ---" + C.RESET)
    print(f"  Status: {status_color}{site['status']}{C.RESET}")

    print("\n" + soft_separator(35))
    if '🟢' in site['status']:
        print(f"  {C.YELLOW}[1]{C.RESET} 🔴 Disable site")
    else:
        print(f"  {C.YELLOW}[1]{C.RESET} 🟢 Enable site")
    print(f"  {C.YELLOW}[any other key]{C.RESET} ← Back")
    print(soft_separator(35))
    action = input(f"{C.BOLD}Choose action: {C.RESET}").strip()

    if action == '1':
        enable = '🔴' in site['status']
        toggle_site_status(site, web_server, enable=enable)

def initial_setup():
    """Check if script was configured; if not, create alias and restart."""
    setup_flag_file = os.path.expanduser("~/.manager_setup_complete")
    if os.path.exists(setup_flag_file):
        return

    clear_screen()
    setup_title = "--- Initial setup ---"
    print(C.BOLD + gradient_text(setup_title, (190, 160, 255), (245, 215, 190)) + C.RESET)
    print("Looks like you are running this script for the first time.")
    print("Let's create a handy alias for quick launch.\n")

    alias_name = ""
    while not alias_name.isalnum():
        alias_name = input(f"Enter a single word to call the script (e.g. 'panel'): {C.CYAN}").strip().lower()
        if not alias_name.isalnum():
            print(f"{C.RED}Name can only contain letters and digits.{C.RESET}")
    
    script_path = os.path.abspath(__file__)
    bashrc_path = os.path.expanduser("~/.bashrc")
    if not os.path.exists(bashrc_path):
        open(bashrc_path, 'a').close()
    alias_command = f"\nalias {alias_name}='python3 {script_path}' # Added by script. Creator @factorcode.\n"

    try:
        with open(bashrc_path, "a") as bashrc_file:
            bashrc_file.write(alias_command)
        
        open(setup_flag_file, 'a').close()
        print(f"\n{C.GREEN}✅ Alias '{alias_name}' has been successfully added to {bashrc_path}.{C.RESET}")
        print(f"{C.CYAN}Restarting script to apply changes...{C.RESET}")
        time.sleep(2)

        os.execv('/bin/bash', ['/bin/bash', '-c', f"source {bashrc_path} && exec python3 '{script_path}'"])
    except Exception as e:
        print(f"{C.RED}❌ Failed to write to file {bashrc_path}: {e}{C.RESET}")
        print("You can add this line manually:")
        print(f"{C.CYAN}{alias_command.strip()}{C.RESET}")
        input(f"{C.BOLD}Press Enter to continue...{C.RESET}")

def main():
    """Main program loop."""
    initial_setup()
    
    while True:
        try:
            state_data = load_state()
            web_server_info = get_web_server_status()
            all_bots, all_sites = discover_all_bots_and_sites(web_server_info)
            bots_with_status = update_bots_status(all_bots, state_data)
            sites_with_status = update_sites_status(all_sites, web_server_info)
            choice = display_menu(bots_with_status, sites_with_status, web_server_info)
            if choice is None:
                break

            if choice == 'q':
                clear_screen()
                print(f"{C.CYAN}Exiting...{C.RESET}")
                sys.exit(0)
            elif choice == 'r':
                print(f"\n{C.YELLOW}🔄 Restarting all active bots...{C.RESET}\n")
                restarted_any = any(
                    kill_bot(b['pid'], b['name'], b['dir'])
                    and (time.sleep(1) or True)
                    and start_bot(b, logging_enabled=False) is None
                    for b in bots_with_status if b['pid']
                )
                if not restarted_any:
                    print("There were no active bots to restart.")
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
                    print(f"{C.RED}❌ Invalid number.{C.RESET}")
            else:
                print(f"{C.RED}❌ Invalid input.{C.RESET}")
            time.sleep(2)
        except KeyboardInterrupt:
            clear_screen()
            print(f"\n{C.CYAN}Exiting...{C.RESET}")
            sys.exit(0)
        except Exception as e:
            clear_screen()
            print(f"{C.RED}❌ Critical error occurred: {e}{C.RESET}")
            sys.exit(1)

if __name__ == "__main__":
    main()  # @factorcode