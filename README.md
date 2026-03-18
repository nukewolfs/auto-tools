# AutoTools 🛠️

办公自动化工具箱 - 批量处理文件、Excel的神器

## 功能

- 📁 **批量重命名** - 按序号/日期批量重命名文件
- 📂 **自动分类** - 按文件类型自动分类
- 📊 **Excel合并** - 批量合并Excel文件

## 安装

```bash
pip install autotools-nukewolfs
```

## 使用

```python
from autotools import FileTool, ExcelTool

# 批量重命名
FileTool.batch_rename('./folder', prefix='file_')

# 按类型分类
FileTool.classify_by_type('./folder')

# 合并Excel
ExcelTool.merge_files('./excel_folder', 'output.xlsx')
```

## 命令行

```bash
autotools rename ./folder --prefix "report_"
autotools classify ./folder
autotools merge ./excel_folder
```

## 作者

- GitHub: [@nukewolfs](https://github.com/nukewolfs)

## License

MIT
