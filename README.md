# TemplateAI - Development System

نظام تطوير TemplateAI لإنشاء قوالب WordPress تلقائياً باستخدام AI

## Quick Start

### 1. متطلبات التثبيت
- Docker & Docker Compose
- Git (اختياري)

### 2. تجهيز البيئة

```bash
cd development-system
cp .env.example .env
```

### 3. تشغيل النظام

```bash
docker-compose up -d
```

### 4. التحقق من الخدمات

```bash
bash scripts/health-check.sh
```

## الخدمات

- **API Gateway** (8000): نقطة دخول API الرئيسية
- **LangGraph Orchestrator** (8001): تنسيق سير العمل
- **AutoGen Agents** (8002): وكلاء AI
- **Code Generation** (8003): توليد الأكواد
- **Testing Service** (8004): اختبار القوالب
- **Database Service** (8005): خدمات قاعدة البيانات

## الأوامر الأساسية

```bash
# عرض حالة الخدمات
docker-compose ps

# عرض السجلات
docker-compose logs -f

# إيقاف جميع الخدمات
docker-compose down

# حذف البيانات
docker-compose down -v
```

## الملفات المهمة

- `docker-compose.yml`: تكوين جميع الخدمات
- `.env`: متغيرات البيئة
- `services/`: كود كل خدمة
- `config/`: ملفات التكوين
- `scripts/`: سكريبتات مساعدة
