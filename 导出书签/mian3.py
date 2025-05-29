import json


def convert_edge_bookmarks_to_html(bookmarks_json_path, output_html_path):
    with open(bookmarks_json_path, "r", encoding="utf-8") as file:
        bookmarks_data = json.load(file)

    # 获取书签栏和其他目录的书签
    bookmarks = []

    def extract_bookmarks(data):
        if isinstance(data, dict):
            if "children" in data:
                for child in data["children"]:
                    extract_bookmarks(child)
            elif "url" in data and "name" in data:
                bookmarks.append((data["name"], data["url"]))

    roots = bookmarks_data.get("roots", {})
    for key in roots:
        extract_bookmarks(roots[key])

    # 生成HTML书签文件
    html_content = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
    <TITLE>Bookmarks</TITLE>
    <H1>Bookmarks</H1>
    <DL><p>
    """

    for name, url in bookmarks:
        html_content += f'    <DT><A HREF="{url}">{name}</A>\n'

    html_content += "</DL><p>"

    with open(output_html_path, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"书签已成功转换并保存为 {output_html_path}")


# 示例用法
convert_edge_bookmarks_to_html("Bookmarks", "bookmarks1.html")
