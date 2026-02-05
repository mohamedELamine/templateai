# نسخ المشروع إلى VPS

## الطريقة 1: استخدام SCP (الأسهل والأسرع)

### على جهازك المحلي:

```bash
# الانتقال إلى مجلد المشروع الأب
cd /Users/mohammed

# نسخ المشروع إلى VPS
scp -r development-system root@YOUR_VPS_IP:/opt/templateai

# أو إذا كنت تستخدم SSH key
scp -i /path/to/key -r development-system root@YOUR_VPS_IP:/opt/templateai
```

## الطريقة 2: استخدام Git

### على جهازك المحلي:

```bash
# تهيئة مستودع Git (إذا لم تفعل بعد)
cd /Users/mohammed/development-system
git init
git add .
git commit -m "Initial commit"

# إضافة remote (إذا كان لديك GitHub/GitLab)
git remote add origin https://github.com/yourname/templateai.git
git push -u origin main
```

### على VPS:

```bash
ssh root@YOUR_VPS_IP
mkdir -p /opt/templateai
cd /opt/templateai
git clone https://github.com/yourname/templateai.git .
```

## الطريقة 3: نسخ يدوي عبر SFTP

```bash
# اتصل عبر SFTP
sftp root@YOUR_VPS_IP

# قم بإنشاء المجلدات
mkdir -p /opt/templateai
cd /opt/templateai

# انسخ الملفات باستخدام واجهة SFTP
```

---

## خطوات ما بعد النسخ على VPS

```bash
# 1. اتصل بـ VPS
ssh root@YOUR_VPS_IP

# 2. تحقق من الملفات
cd /opt/templateai
ls -la

# 3. قم بتحديث .env بكلماتك المرورية الخاصة
nano .env

# 4. قم بتشغيل Docker Compose
docker-compose up -d

# 5. تحقق من الخدمات
docker-compose ps

# 6. اختبر الصحة
bash scripts/health-check.sh

# 7. اختبر API
curl http://localhost:8000/health
```

---

## استبدال المتغيرات

في ملف `.env`، استبدل:
- `YOUR_VPS_IP`: عنوان IP خادمك
- كلماتك المرورية بكلمات قوية
- مفاتيح API الخاصة بك (Gemini, Claude, GLM)

