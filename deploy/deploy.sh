#!/bin/bash
set -e

# =============================================
# Vaam Project - Server Deploy Script
# Run on the server after code is pulled
# =============================================

APP_DIR="/home/vaam/app"
VENV_DIR="$APP_DIR/venv"

echo "=========================================="
echo "  Deploying Vaam Project..."
echo "=========================================="

cd "$APP_DIR"

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Install/update dependencies
echo "[1/6] Installing dependencies..."
pip install -q -r requirements.txt

# Run database migrations
echo "[2/6] Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "[3/6] Collecting static files..."
python manage.py collectstatic --noinput

# Compile translation messages
echo "[4/6] Compiling translations..."
python manage.py compilemessages || true

# Restart Gunicorn
echo "[5/6] Restarting Gunicorn..."
sudo systemctl restart vaam

# Verify service status
echo "[6/6] Checking service status..."
sudo systemctl is-active --quiet vaam && echo "✓ Vaam service is running!" || echo "✗ Service failed to start!"

echo "=========================================="
echo "  Deployment complete!"
echo "=========================================="
