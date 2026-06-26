import re


def parse_readme(readme_text: str):

    if not readme_text:
        return {
            "headings": [],
            "technologies": [],
            "has_installation": False,
            "has_examples": False
        }

    headings = re.findall(r"^#+\s+(.*)", readme_text, re.MULTILINE)

    technologies = []

    keywords = [
        "FastAPI",
        "Starlette",
        "Pydantic",
        "Uvicorn",
        "Docker",
        "Kubernetes",
        "TensorFlow",
        "PyTorch",
        "React",
        "Next.js",
        "Vue",
        "Angular",
        "PostgreSQL",
        "MongoDB",
        "Redis"
    ]

    for keyword in keywords:
        if keyword.lower() in readme_text.lower():
            technologies.append(keyword)

    has_installation = (
        "installation" in readme_text.lower()
        or "install" in readme_text.lower()
    )

    has_examples = (
        "example" in readme_text.lower()
        or "quickstart" in readme_text.lower()
    )

    return {

        "headings": headings,

        "technologies": sorted(list(set(technologies))),

        "has_installation": has_installation,

        "has_examples": has_examples

    }