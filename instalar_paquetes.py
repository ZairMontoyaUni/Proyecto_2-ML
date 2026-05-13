#!/usr/bin/env python
"""
Script para instalar dependencias de forma robusta.
Ejecuta: python instalar_paquetes.py
"""

import subprocess
import sys

PACKAGES = [
    "numpy>=1.21.0",
    "pandas>=1.3.0",
    "matplotlib>=3.4.0",
    "seaborn>=0.11.0",
    "scikit-learn>=1.0.0",
    "tqdm>=4.62.0",
    "tensorflow==2.15.0",  # Más estable para Python 3.9
    "torch==2.0.1",  # CPU version
    "transformers==4.34.0",
    "datasets==2.14.5",
    "sentencepiece>=0.1.97",
]

print("=" * 70)
print("📦 INSTALADOR DE DEPENDENCIAS")
print("=" * 70)
print(f"Python: {sys.version.split()[0]}")
print(f"Path: {sys.executable}\n")

failed = []
success = []

for pkg in PACKAGES:
    pkg_name = pkg.split(">=")[0].split("==")[0]
    print(f"⏳ {pkg_name:<25}", end="", flush=True)

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-q", pkg],
            timeout=300,
            capture_output=True,
        )
        if result.returncode == 0:
            print("✔")
            success.append(pkg_name)
        else:
            print("✘")
            failed.append(pkg_name)
    except Exception as e:
        print(f"✘ ({str(e)[:20]})")
        failed.append(pkg_name)

print("\n" + "=" * 70)
print(f"✅ Exitoso: {len(success)}")
print(f"❌ Fallido: {len(failed)}")

if failed:
    print(f"\n⚠️  Paquetes fallidos: {', '.join(failed)}")
    print("\nIntenta instalarlos manualmente:")
    for pkg in failed:
        print(f"  pip install {pkg}")

print("=" * 70)
