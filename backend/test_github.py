from app.services.github_service import get_repository_info

result = get_repository_info(
    "fastapi",
    "fastapi"
)

print(result)