from app.services.github_service import (
    get_readme
)

from app.utils.readme_parser import (
    parse_readme
)

text = get_readme(
    "fastapi",
    "fastapi"
)

result = parse_readme(text)

print(result)