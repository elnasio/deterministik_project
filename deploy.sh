cat > ~/deploy.sh << 'EOF'
#!/usr/bin/env bash
set -euo pipefail

echo "=== 🚀 Deploying FastAPI Project ==="

# masuk ke folder project
cd /home/moriesdeo/projects/deterministik_project

# aktifkan virtual environment
source .venv/bin/activate

# tarik kode terbaru
git pull

# install/update dependency
pip install --upgrade pip
pip install -r requirements.txt

# restart service systemd
sudo systemctl restart fastapi
sudo systemctl status fastapi --no-pager --lines=3

echo "=== ✅ Deploy finished! ==="
EOF

chmod +x ~/deploy.sh