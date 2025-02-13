import os
import subprocess
import openpyxl
import re

def decompile_apk(jadx_path, apk_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    subprocess.run([jadx_path, '-d', output_dir, apk_path])

def search_in_files(keywords, regex_patterns, directory):
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.java') or file.endswith('.xml'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        for keyword in keywords:
                            if keyword in line:
                                results.append((file_path, line.strip()))
                        for pattern in regex_patterns:
                            if re.search(pattern, line):
                                results.append((file_path, line.strip()))
    return results

def write_results_to_excel(results, output_excel_path):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["File Path", "Line"])
    for result in results:
        sheet.append(result)
    workbook.save(output_excel_path)

def main():
    jadx_path = r"D:\\Downloads\\jadx-gui-1.5.1-with-jre-win\\jadx-gui-1.5.1.exe"
    apk_path = r"D:\\Desktop\\hash_rename_APKs\\hash_rename\\sweet_money.apk"
    output_dir = r"D:\\Desktop\\hash_rename_APKs\\hash_rename\\decompiled"
    keywords = ["package", "uses-permission", "http://", "wss://", "firebaseio.com"]
    regex_patterns = [r"\+91[-\s]?\d{10}"]
    output_excel_path = r"D:\\Desktop\\hash_rename_APKs\\hash_rename\\jadx_search_results.xlsx"

    decompile_apk(jadx_path, apk_path, output_dir)
    results = search_in_files(keywords, regex_patterns, output_dir)
    write_results_to_excel(results, output_excel_path)
    print(f"Results saved to {output_excel_path}")

if __name__ == "__main__":
    main()