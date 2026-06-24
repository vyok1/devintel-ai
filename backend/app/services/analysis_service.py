from app.models.analysis_report import AnalysisReport

def create_analysis(db, analysis_data):
    report = AnalysisReport(
        repository_id=analysis_data.repository_id,
        summary=analysis_data.summary,
        technologies=analysis_data.technologies,
        complexity=analysis_data.complexity
    )

    db.add(report)
    db.commit()
    db.refresh(report)

    return report
def generate_analysis(repo_info):
    language = repo_info.get("language", "Unknown")
    stars = repo_info.get("stars", 0)

    if stars > 10000:
        complexity = "High"
    elif stars > 1000:
        complexity = "Medium"
    else:
        complexity = "Low"

    return {
        "summary": f"{repo_info['name']} repository analysis",
        "technologies": language,
        "complexity": complexity
    }
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