import json

# 读取Edge浏览器的书签备份文件（通常为JSON格式）
def read_bookmarks(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# 将书签转换为HTML格式
def convert_to_html(bookmarks_data):
    html_content = '<!DOCTYPE NETSCAPE-Bookmark-file-1>\n'
    html_content += '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n'
    html_content += '<TITLE>Bookmarks</TITLE>\n'
    html_content += '<H1>Bookmarks</H1>\n'
    html_content += '<DL><p>\n'

    def process_folder(folder):
        # 递归处理文件夹内的书签
        nonlocal html_content
        if 'children' in folder:
            for item in folder['children']:
                if item['type'] == 'folder':
                    html_content += f'<DT><H3>{item["name"]}</H3>\n'
                    html_content += '<DL><p>\n'
                    process_folder(item)
                    html_content += '</DL><p>\n'
                elif item['type'] == 'url':
                    url = item['url']
                    name = item['name']
                    html_content += f'<DT><A HREF="{url}">{name}</A>\n'

    process_folder(bookmarks_data)
    html_content += '</DL><p>\n'

    return html_content

# 保存HTML格式的书签
def save_to_html(html_content, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

if __name__ == '__main__':
    input_file_path = 'Bookmarks.json'  # 替换为你的Edge书签备份文件路径
    output_file_path = 'bookmarks.html'       # 输出的HTML文件路径

    # 读取Edge书签备份文件
    bookmarks_data = read_bookmarks(input_file_path)
    print(bookmarks_data)

    # 将书签转换为HTML格式
    html_content = convert_to_html(bookmarks_data)

    # 保存为HTML文件
    save_to_html(html_content, output_file_path)

    print(f'书签已成功转换为HTML文件，并保存在 {output_file_path}')
