import json
import html
from datetime import datetime
import argparse


def convert_chrome_time(chrome_timestamp):
    """将Chrome/Edge时间戳转换为Unix时间戳"""
    if not chrome_timestamp:
        return '0'
    try:
        # Chrome时间戳是从1601-01-01开始的微秒数
        epoch_start = datetime(1601, 1, 1)
        unix_epoch = datetime(1970, 1, 1)
        delta = unix_epoch - epoch_start
        seconds_since_1601 = chrome_timestamp / 1_000_000
        return str(int(delta.total_seconds() + seconds_since_1601))
    except:
        return '0'


def process_node(node, output):
    """递归处理书签节点"""
    if node.get('type') == 'folder':
        folder_name = html.escape(node.get('name', 'Unnamed Folder'))
        output.append(f'<DT><H3 ADD_DATE="{convert_chrome_time(node.get("date_added"))}">{folder_name}</H3>')
        output.append('<DL><p>')
        for child in node.get('children', []):
            process_node(child, output)
        output.append('</DL><p>')
    elif node.get('type') == 'url':
        url = html.escape(node.get('url', ''))
        name = html.escape(node.get('name', 'Unnamed Link'))
        add_date = convert_chrome_time(node.get('date_added'))
        output.append(f'<DT><A HREF="{url}" ADD_DATE="{add_date}">{name}</A>')


def convert_edge_bookmarks(input_json, output_html):
    """主转换函数"""
    output = [
        '<!DOCTYPE NETSCAPE-Bookmark-file-1>',
        '<!-- This is an automatically generated file -->',
        '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">',
        '<TITLE>Bookmarks</TITLE>',
        '<H1>Bookmarks</H1>',
        '<DL><p>'
    ]

    # 处理所有根节点（书签栏、其他书签等）
    for root_key in input_json.get('roots', {}):
        root_node = input_json['roots'][root_key]
        if isinstance(root_node, dict) and 'children' in root_node:
            output.append(f'<!-- {root_key.capitalize()} Bookmarks -->')
            process_node(root_node, output)

    output.append('</DL><p>')

    with open(output_html, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='将Edge浏览器书签JSON转换为HTML格式')
    parser.add_argument('input', help='输入的JSON文件路径')
    parser.add_argument('output', help='输出的HTML文件路径')
    args = parser.parse_args()

    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            bookmarks_data = json.load(f)

        convert_edge_bookmarks(bookmarks_data, args.output)
        print(f'转换成功！输出文件：{args.output}')

    except Exception as e:
        print(f'转换失败：{str(e)}')