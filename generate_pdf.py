#!/usr/bin/env python3
"""
生成 AI Coding 工程实践档案 PDF
依赖: pip install markdown weasyprint
"""

import markdown
from pathlib import Path
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

def generate_pdf():
    # 读取所有 markdown 文件
    data_dir = Path(__file__).parent / 'data'

    # 按顺序合并文档
    files = [
        'projects-metrics.md',
        'case-01-circuit-breaker.md',
        'case-02-heap-fragmentation.md',
        'case-03-upload-atomicity.md',
        'multi-agent-workflow.md',
        'external-audit-log.md',
    ]

    # 生成 HTML 内容
    html_parts = ['''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>AI Coding 工程实践档案 - 证据链</title>
    <style>
        @page {
            size: A4;
            margin: 2cm;
        }
        body {
            font-family: "Microsoft YaHei", "SimSun", sans-serif;
            line-height: 1.6;
            color: #333;
        }
        h1 {
            color: #667eea;
            page-break-before: always;
            margin-top: 0;
        }
        h1:first-of-type {
            page-break-before: avoid;
        }
        h2 {
            color: #764ba2;
            margin-top: 1.5em;
        }
        h3 {
            color: #555;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1em 0;
            font-size: 0.9em;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f5f5f5;
            font-weight: bold;
        }
        code {
            background: #f4f4f4;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: "Courier New", monospace;
            font-size: 0.9em;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        pre code {
            background: none;
            padding: 0;
        }
        .page-break {
            page-break-after: always;
        }
    </style>
</head>
<body>
    <h1 style="text-align: center; color: #667eea; font-size: 2em;">AI Coding 工程实践档案</h1>
    <p style="text-align: center; color: #666; margin-bottom: 3em;">证据链补充文档 · 脱敏版</p>
''']

    # 转换每个文档
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'nl2br'])

    for filename in files:
        filepath = data_dir / filename
        if filepath.exists():
            content = filepath.read_text(encoding='utf-8')
            html_content = md.convert(content)
            html_parts.append(html_content)
            md.reset()

    html_parts.append('</body></html>')

    # 生成 PDF
    output_dir = Path(__file__).parent / 'downloads'
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / 'ai-coding-evidence.pdf'

    font_config = FontConfiguration()
    html_string = '\n'.join(html_parts)

    HTML(string=html_string).write_pdf(
        output_file,
        font_config=font_config
    )

    print(f"✅ PDF 已生成: {output_file}")
    print(f"📄 文件大小: {output_file.stat().st_size / 1024 / 1024:.2f} MB")

if __name__ == '__main__':
    try:
        generate_pdf()
    except ImportError as e:
        print(f"❌ 缺少依赖: {e}")
        print("请安装: pip install markdown weasyprint")
    except Exception as e:
        print(f"❌ 生成失败: {e}")
