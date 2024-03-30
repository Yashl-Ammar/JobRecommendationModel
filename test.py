from app import content_recommendation_v2


# Define test case with descriptive name
def test_content_recommendation_v2_returns_expected_job_description():

    # Define input parameters
    title = 'Data entry'

    # Define expected job description
    job_description = (
        "Project Title: Data Entry - Data Analysis in Excel  "
        "I am looking for a freelancer who can assist"
        " me with data analysis using Excel. "
        "The project involves analyzing a "
        "dataset with less than 1000 entries.  "
        "Skills and Experience: - Proficiency in Excel and data "
        "analysis techniques - Strong understanding of statistical "
        "analysis and data visualization - Ability "
        "to clean and organize data for "
        "analysis purposes - Experience in interpreting and presenting "
        "data findings - Attention to detail and accuracy in data entry - "
        "Familiarity with basic formulas and functions in Excel  Software"
        " Requirements: - Proficiency in using Excel for data analysis - "
        "Familiarity with Excel functions and formulas for data manipulation"
        " and analysis  If you have the necessary skills and experience "
        "in data analysis using Excel, I would love to hear from you. "
        "Please provide examples of previous data analysis projects you have "
        "completed, and your availability to start the project. "
    )

    # Call the function
    recommendations = content_recommendation_v2(title)

    # Check if the length of recommendations is greater than 0
    assert len(recommendations) > 0

    assert recommendations.iloc[0]['job_description'] == job_description
