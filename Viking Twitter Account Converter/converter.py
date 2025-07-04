import os
from colorama import init, Fore, Style

init(autoreset=True)
# set Windows console title (escape '|' so it appears literally)
os.system('title Viking Twitter Account Converter ^| Telegram: @vikingtokens')

input_file = "input.txt"
output_dir = "output"

# ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def parse_line(line, line_num):
    line = line.strip()
    if ";" in line or "," in line:
        raise ValueError("Use ':' as your separator, not ';' or ','")
    parts = line.split(":")
    if len(parts) < 2:
        raise ValueError("Too few ':' delimiters")
    last = parts[-1]
    # strip trailing 2FA/backup if it's all digits or <=20 chars
    if last.isdigit() or len(last) <= 20:
        auth_token = parts[-2].strip()
        base = parts[:-1]
    else:
        auth_token = last.strip()
        base = parts
    return base, auth_token

def option1(lines):
    tokens = []
    for idx, line in enumerate(lines, 1):
        try:
            _, auth = parse_line(line, idx)
            tokens.append(auth)
        except Exception as e:
            print(Fore.YELLOW + f"[Warning] Skipped line {idx}: {e}")

    if not tokens:
        print(Fore.RED + "❌ No valid tokens extracted.")
        return
    out_path = os.path.join(output_dir, "auth_tokens.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(tokens))
    print(Fore.GREEN + f"✅ Wrote {len(tokens)} tokens to {out_path}")

def option2(lines):
    results = []
    for idx, line in enumerate(lines, 1):
        try:
            base, auth = parse_line(line, idx)
            if len(base) != 6:
                raise ValueError("Expected 6 fields: user,pass,mail,mailpwd,ct0,token")
            user, pwd, mail, mailpwd, ct0 = (base[0].strip(), base[1].strip(), base[2].strip(), base[3].strip(), base[4].strip())
            results.append(f"{user}:{pwd}:{mail}:{mailpwd}:{ct0}:{auth}")
        except Exception as e:
            print(Fore.YELLOW + f"[Warning] Skipped line {idx}: {e}")

    if not results:
        print(Fore.RED + "❌ No valid lines for option 2.")
        return
    out_path = os.path.join(output_dir, "user_pass_mail_mailpwd_ct0_auth.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(results))
    print(Fore.GREEN + f"✅ Wrote {len(results)} lines to {out_path}")

def option3(lines):
    results = []
    for idx, line in enumerate(lines, 1):
        try:
            base, auth = parse_line(line, idx)
            if len(base) != 5:
                raise ValueError("Expected 5 fields: user,pass,mail,ct0,token")
            user, pwd, mail, ct0 = (base[0].strip(), base[1].strip(), base[2].strip(), base[3].strip())
            results.append(f"{user}:{pwd}:{mail}:{ct0}:{auth}")
        except Exception as e:
            print(Fore.YELLOW + f"[Warning] Skipped line {idx}: {e}")

    if not results:
        print(Fore.RED + "❌ No valid lines for option 3.")
        return
    out_path = os.path.join(output_dir, "user_pass_mail_ct0_auth.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(results))
    print(Fore.GREEN + f"✅ Wrote {len(results)} lines to {out_path}")

def option4(lines):
    results = []
    for idx, line in enumerate(lines, 1):
        try:
            base, auth = parse_line(line, idx)
            if len(base) < 4:
                raise ValueError("Expected at least 4 fields for auth:pass format")
            acct_pass = base[3].strip()
            results.append(f"{auth}:{acct_pass}")
        except Exception as e:
            print(Fore.YELLOW + f"[Warning] Skipped line {idx}: {e}")

    if not results:
        print(Fore.RED + "❌ No valid lines for option 4.")
        return
    out_path = os.path.join(output_dir, "auth_pass.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(results))
    print(Fore.GREEN + f"✅ Wrote {len(results)} lines to {out_path}")

def main():
    # load and validate input
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            lines = [l for l in f if l.strip()]
    except FileNotFoundError:
        print(Fore.RED + "❌ 'input.txt' not found. Add your lines there and re-run.")
        return
    if not lines:
        print(Fore.RED + "❌ 'input.txt' is empty. Add some lines and try again.")
        return

    # clear console
    os.system("cls" if os.name == "nt" else "clear")

    # clear previous outputs
    clear = input(Fore.LIGHTBLUE_EX + "Clear previous outputs? (y/n): ").strip().lower()
    if clear == "y":
        for fn in os.listdir(output_dir):
            if fn.endswith(".txt"):
                os.remove(os.path.join(output_dir, fn))
        print(Fore.GREEN + "✅ Output folder cleared\n")

    # title banner
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "   Viking Twitter Account Converter   ")
    print(Fore.CYAN + "   Telegram: @vikingtokens   ")
    print(Fore.CYAN + "=" * 50)
    print()

    # accepted formats
    print(Fore.CYAN + "Place your account lines in 'input.txt' with one of these formats:")
    print(Fore.LIGHTBLUE_EX + "  • user:pass:mail:mailpwd:ct0:auth_token:2fa_backup_code")
    print(Fore.LIGHTBLUE_EX + "  • user:pass:mail:mailpwd:ct0:auth_token")
    print(Fore.LIGHTBLUE_EX + "  • user:pass:mail:ct0:auth_token")
    print()

    # menu loop until valid choice
    choice = None
    while True:
        print(Fore.CYAN + "Choose an option:")
        print(Fore.LIGHTBLUE_EX + "1) Convert to auth_token only format")
        print(Fore.LIGHTBLUE_EX + "2) Convert to user:pass:mail:mailpwd:ct0:auth_token format")
        print(Fore.LIGHTBLUE_EX + "3) Convert to user:pass:mail:ct0:auth_token format")
        print(Fore.LIGHTBLUE_EX + "4) Convert to auth_token:account_password format")
        choice = input(Fore.LIGHTBLUE_EX + "Enter 1, 2, 3 or 4: ").strip()
        if choice in {"1", "2", "3", "4"}:
            break
        else:
            print(Fore.RED + f"❌ Invalid choice '{choice}'. please try again.\n")

    # execute selected option
    if choice == "1":
        option1(lines)
    elif choice == "2":
        option2(lines)
    elif choice == "3":
        option3(lines)
    elif choice == "4":
        option4(lines)

if __name__ == "__main__":
    main()
