# رفع المشروع على GitHub

## خطوة 1: إنشاء مستودع على GitHub

1. اذهب إلى https://github.com/new
2. املأ البيانات:
   - **Repository name**: `templateai` (أو أي اسم تريده)
   - **Description**: "TemplateAI - Automated WordPress Template Generator"
   - **Visibility**: Public (للمستخدمين الآخرين) أو Private
   - اترك الخيارات الأخرى فارغة
3. اضغط "Create repository"

---

## خطوة 2: ربط مستودعك المحلي بـ GitHub

### الطريقة A: باستخدام HTTPS (الأسهل)

```bash
cd /Users/mohammed/development-system

# أضف remote (استبدل USERNAME باسم مستخدمك)
git remote add origin https://github.com/USERNAME/templateai.git

# غير اسم الفرع إلى main (اختياري)
git branch -M main

# ارفع الملفات
git push -u origin main
```

**عند الضغط على الأمر الأخير، ستُطلب منك كلمة مرورك أو personal access token**

### الطريقة B: باستخدام SSH (أكثر أماناً)

```bash
cd /Users/mohammed/development-system

# تحقق من وجود مفتاح SSH
ls ~/.ssh/id_rsa

# إذا لم يكن موجوداً، أنشئ واحداً:
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ""

# أضف المفتاح العام إلى GitHub:
# 1. انسخ محتوى ~/.ssh/id_rsa.pub
cat ~/.ssh/id_rsa.pub

# 2. اذهب إلى https://github.com/settings/keys
# 3. اضغط "New SSH key"
# 4. الصق المفتاح

# الآن استخدم SSH:
git remote add origin git@github.com:USERNAME/templateai.git
git branch -M main
git push -u origin main
```

---

## الحل السريع:

إذا حصلت على خطأ "remote already exists":

```bash
cd /Users/mohammed/development-system
git remote remove origin
git remote add origin https://github.com/USERNAME/templateai.git
git push -u origin main
```

---

## بعد الرفع بنجاح:

ستكون قادراً على النسخ من VPS بسهولة:

```bash
ssh root@YOUR_VPS_IP
cd /opt
git clone https://github.com/USERNAME/templateai.git
cd templateai
docker-compose up -d
```

---

## معلومات مهمة:

- استبدل `USERNAME` باسم مستخدمك على GitHub
- استبدل `templateai` باسم المستودع الذي اخترته
- إذا اخترت Private، ستحتاج إلى SSH keys أو personal access token

---

## مشاكل شائعة وحلولها:

### 1. "fatal: remote origin already exists"
```bash
git remote -v  # اعرض remotes الحالية
git remote remove origin  # احذف الموجود
git remote add origin ...  # أضف الجديد
```

### 2. "Authentication failed"
- استخدم personal access token بدلاً من كلمة المرور
- أو استخدم SSH keys

### 3. "error: src refspec main does not match any"
```bash
git branch -M main  # غير اسم الفرع إلى main
```

