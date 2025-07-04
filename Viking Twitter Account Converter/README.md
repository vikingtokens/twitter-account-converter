````markdown
# Viking Twitter Account Converter

Turn your raw Twitter account lines into whatever format you need—fast and easy.

## 🚀 Quickstart

1. **Clone or download** this repo  
2. **Install requirements**  
   ```bash
   pip install colorama
````

3. **Put your lines** into `input.txt` (one per line) using one of these formats:
   • `user:pass:mail:mailpwd:ct0:auth_token:2fa_backup_code`
   • `user:pass:mail:mailpwd:ct0:auth_token`
   • `user:pass:mail:ct0:auth_token`
4. **Run the converter**

   ```bash
   python converter.py
   ```
5. **Choose an option** (1–4) and watch your files appear in the `output/` folder

## 📂 Supported Options

1. Extract **auth\_token** only
2. Build `user:pass:mail:mailpwd:ct0:auth_token`
3. Build `user:pass:mail:ct0:auth_token`
4. Build `auth_token:account_password`

## ✅ What you get

• Clear console menu
• Warnings for any malformed lines
• Clean output files in `output/`
• Option to clear old outputs before each run

## 💬 Need help?

Message **@vikingtokens** on Telegram anytime.

---

*Viking Twitter Account Converter* keeps your workflow smooth so you can focus on sales, not scripts.