#!/usr/bin/env python3
"""
AutoTools - 办公自动化工具箱
作者: nukewolfs
版本: 1.0.0
"""
import os
import sys
import json
import shutil
import zipfile
import subprocess
from pathlib import Path
from datetime import datetime

__version__ = "1.0.0"

class FileTool:
    """文件处理工具"""
    
    @staticmethod
    def batch_rename(folder, prefix='', suffix=''):
        """批量重命名"""
        folder = Path(folder)
        files = sorted([f for f in folder.iterdir() if f.is_file()])
        
        for i, f in enumerate(files, 1):
            new_name = f"{prefix}{i:03d}{suffix}{f.suffix}"
            f.rename(folder / new_name)
            print(f"✓ {f.name} → {new_name}")
        return len(files)
    
    @staticmethod
    def classify_by_type(folder):
        """按类型分类"""
        folder = Path(folder)
        type_map = {
            'images': ['.jpg', '.png', '.gif', '.bmp', '.webp'],
            'documents': ['.pdf', '.doc', '.txt', '.xlsx'],
            'videos': ['.mp4', '.avi', '.mov'],
            'audio': ['.mp3', '.wav'],
            'code': ['.py', '.js', '.html'],
        }
        
        for file in folder.iterdir():
            if not file.is_file():
                continue
            ext = file.suffix.lower()
            for cat, exts in type_map.items():
                if ext in exts:
                    target = folder / cat
                    target.mkdir(exist_ok=True)
                    shutil.move(str(file), str(target / file.name))
                    print(f"✓ {file.name} → {cat}/")
                    break

class ExcelTool:
    """Excel处理工具"""
    
    @staticmethod
    def merge_files(input_dir, output='merged.xlsx'):
        """合并Excel"""
        try:
            import pandas as pd
        except ImportError:
            print("需要安装: pip install pandas openpyxl")
            return False
            
        import glob
        files = glob.glob(f"{input_dir}/*.xlsx")
        if not files:
            print("没有找到Excel文件")
            return False
            
        df = pd.concat([pd.read_excel(f) for f in files], ignore_index=True)
        df.to_excel(output, index=False)
        print(f"✓ 合并完成: {output} ({len(df)} 行)")
        return True

def main():
    print("AutoTools v1.0.0")
    print("=" * 30)
    print("用法:")
    print("  python autotools.py rename <文件夹>")
    print("  python autotools.py classify <文件夹>")
    print("  python autotools.py merge <文件夹>")
    print("=" * 30)

if __name__ == "__main__":
    main()
