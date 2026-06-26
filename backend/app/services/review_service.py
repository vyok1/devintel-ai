import os

from app.utils.code_scanner import CodeScanner


scanner = CodeScanner()


def review_project(project_path):

    report = []

    files_scanned = 0

    for root, dirs, files in os.walk(project_path):

        for file in files:

            if file.endswith(".py"):

                files_scanned += 1

                filepath = os.path.join(root, file)

                try:

                    issues = scanner.scan_file(filepath)

                    for issue in issues:

                        issue["file"] = filepath

                    report.extend(issues)

                except Exception as e:

                    report.append({

                        "file": filepath,

                        "type": "Scanner Error",

                        "severity": "High",

                        "line": 0,

                        "message": str(e)

                    })

    return {

        "files_scanned": files_scanned,

        "issues_found": len(report),

        "issues": report

    }