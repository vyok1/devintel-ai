from app.models.analysis_report import AnalysisReport


# -------------------------------------------------
# Repository Type Detection
# -------------------------------------------------

def detect_repository_type(repo_info):
    description = (repo_info.get("description") or "").lower()
    topics = [topic.lower() for topic in repo_info.get("topics", [])]

    if "fastapi" in description or "api" in description:
        return "Backend API Framework"

    if "django" in description:
        return "Backend Web Framework"

    if "machine learning" in description or "ml" in topics:
        return "Machine Learning Project"

    if "react" in topics:
        return "Frontend Web Application"

    if "nextjs" in topics or "next.js" in topics:
        return "Full Stack Web Application"

    if "cli" in topics:
        return "Command Line Tool"

    return "General Software Project"


# -------------------------------------------------
# Technology Stack Detection
# -------------------------------------------------

def detect_technology_stack(repo_info):

    language = repo_info.get("language", "")
    topics = [topic.lower() for topic in repo_info.get("topics", [])]

    stack = []

    if language:
        stack.append(language)

    topic_map = {
        "fastapi": "FastAPI",
        "django": "Django",
        "flask": "Flask",
        "react": "React",
        "nextjs": "Next.js",
        "next.js": "Next.js",
        "vue": "Vue.js",
        "angular": "Angular",
        "tensorflow": "TensorFlow",
        "pytorch": "PyTorch",
        "docker": "Docker",
        "kubernetes": "Kubernetes"
    }

    for topic in topics:
        if topic in topic_map:
            stack.append(topic_map[topic])

    return sorted(list(set(stack)))


# -------------------------------------------------
# Repository Complexity
# -------------------------------------------------

def calculate_complexity(repo_info):

    stars = repo_info.get("stars", 0)
    forks = repo_info.get("forks", 0)

    score = stars + (forks * 2)

    if score >= 100000:
        return "Very High"

    if score >= 20000:
        return "High"

    if score >= 5000:
        return "Medium"

    return "Low"


# -------------------------------------------------
# Repository Health
# -------------------------------------------------

def calculate_repository_health(repo_info):

    issues = repo_info.get("open_issues", 0)

    if issues < 50:
        return "Excellent"

    if issues < 500:
        return "Good"

    return "Needs Attention"


# -------------------------------------------------
# Recommended Skills
# -------------------------------------------------

def recommend_skills(repo_info):

    language = repo_info.get("language", "")
    topics = [topic.lower() for topic in repo_info.get("topics", [])]

    skills = []

    language_skills = {
        "Python": [
            "Python",
            "Object-Oriented Programming",
            "REST API",
            "Git"
        ],
        "JavaScript": [
            "JavaScript",
            "HTML",
            "CSS",
            "Git"
        ],
        "TypeScript": [
            "TypeScript",
            "JavaScript",
            "Git"
        ]
    }

    if language in language_skills:
        skills.extend(language_skills[language])

    topic_skills = {
        "fastapi": "FastAPI",
        "django": "Django",
        "flask": "Flask",
        "react": "React",
        "docker": "Docker",
        "kubernetes": "Kubernetes",
        "tensorflow": "TensorFlow",
        "pytorch": "PyTorch"
    }

    for topic in topics:
        if topic in topic_skills:
            skills.append(topic_skills[topic])

    return sorted(list(set(skills)))


# -------------------------------------------------
# Summary Generator
# -------------------------------------------------

def generate_summary(repo_info):

    return (
        f"{repo_info['name']} is a "
        f"{repo_info['language']} repository with "
        f"{repo_info['stars']} GitHub stars."
    )


# -------------------------------------------------
# Main Analysis Engine
# -------------------------------------------------

def generate_analysis(repo_info):

    technology_stack = detect_technology_stack(repo_info)

    return {

        "repository_type": detect_repository_type(repo_info),

        "complexity": calculate_complexity(repo_info),

        "repository_health": calculate_repository_health(repo_info),

        "technology_stack": technology_stack,

        "recommended_skills": recommend_skills(repo_info),

        "summary": generate_summary(repo_info),

        "technologies": ", ".join(technology_stack)
    }


# -------------------------------------------------
# Database Save
# -------------------------------------------------

def save_analysis(db, repository_id, analysis):

    report = AnalysisReport(

        repository_id=repository_id,

        summary=analysis["summary"],

        technologies=analysis["technologies"],

        complexity=analysis["complexity"]

    )

    db.add(report)
    db.commit()
    db.refresh(report)

    return report