import ast


class CodeScanner:

    def scan_file(self, filepath):

        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()

        tree = ast.parse(source)

        issues = []

        issues.extend(self.find_print_statements(tree))

        issues.extend(self.find_eval_usage(tree))

        issues.extend(self.find_exec_usage(tree))

        issues.extend(self.find_long_functions(tree))

        issues.extend(self.find_pass_statements(tree))

        return issues

    def find_print_statements(self, tree):

        issues = []

        for node in ast.walk(tree):

            if isinstance(node, ast.Call):

                if isinstance(node.func, ast.Name):

                    if node.func.id == "print":

                        issues.append({
                            "type": "Print Statement",
                            "severity": "Low",
                            "line": node.lineno,
                            "message": "Remove print() before production."
                        })

        return issues

    def find_eval_usage(self, tree):

        issues = []

        for node in ast.walk(tree):

            if isinstance(node, ast.Call):

                if isinstance(node.func, ast.Name):

                    if node.func.id == "eval":

                        issues.append({
                            "type": "Security",
                            "severity": "High",
                            "line": node.lineno,
                            "message": "Avoid eval()."
                        })

        return issues

    def find_exec_usage(self, tree):

        issues = []

        for node in ast.walk(tree):

            if isinstance(node, ast.Call):

                if isinstance(node.func, ast.Name):

                    if node.func.id == "exec":

                        issues.append({
                            "type": "Security",
                            "severity": "High",
                            "line": node.lineno,
                            "message": "Avoid exec()."
                        })

        return issues

    def find_pass_statements(self, tree):

        issues = []

        for node in ast.walk(tree):

            if isinstance(node, ast.Pass):

                issues.append({
                    "type": "Incomplete Code",
                    "severity": "Medium",
                    "line": node.lineno,
                    "message": "pass statement found."
                })

        return issues

    def find_long_functions(self, tree):

        issues = []

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                if len(node.body) > 30:

                    issues.append({
                        "type": "Maintainability",
                        "severity": "Medium",
                        "line": node.lineno,
                        "message": f"Function '{node.name}' is too long."
                    })

        return issues