#!/bin/bash
# VAAM Client Data Deployment Script
# Usage: bash deploy_client_data.sh

SERVER_IP="46.101.102.220"
SERVER_USER="vaam"  # və ya root
APP_PATH="/home/vaam/app"

echo "======================================"
echo "  VAAM Client Data Deployment"
echo "======================================"
echo ""

# 1. Upload seed script to server
echo "📤 Uploading seed_client_data.py to server..."
scp seed_client_data.py ${SERVER_USER}@${SERVER_IP}:${APP_PATH}/

if [ $? -eq 0 ]; then
    echo "✅ File uploaded successfully"
else
    echo "❌ Failed to upload file"
    exit 1
fi

echo ""
echo "🚀 Connecting to server and running seed script..."
echo ""

# 2. Connect to server and run the script
ssh ${SERVER_USER}@${SERVER_IP} << 'ENDSSH'
    cd /home/vaam/app
    source venv/bin/activate
    
    echo "Running seed script..."
    python seed_client_data.py
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Client data successfully added to production database!"
    else
        echo ""
        echo "❌ Error occurred while seeding data"
        exit 1
    fi
ENDSSH

echo ""
echo "======================================"
echo "  ✅ Deployment Completed!"
echo "======================================"
echo ""
echo "Check the website: https://your-domain.com"
echo "Check admin panel: https://your-domain.com/admin"
