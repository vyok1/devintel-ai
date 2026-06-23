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