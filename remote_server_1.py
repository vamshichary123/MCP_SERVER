
from fastmcp import FastMCP

mcp = FastMCP('CareerConnect AI')


@mcp.tool
def search_jobs():
    '''Returns available job opportunities'''
    jobs = [
        'Data Scientist',
        'Data Analyst',
        'Machine Learning Engineer',
        'Python Developer',
        'AI Engineer',
        'Generative AI Engineer'
    ]
    return jobs


@mcp.tool
def get_job_requirements():
    '''Provides skills required for different job roles'''
    requirements = {
        'Data Scientist': [
            'Python', 'Machine Learning', 'Statistics',
            'SQL', 'Data Visualization'
        ],
        'Data Analyst': [
            'SQL', 'Excel', 'Python', 'Power BI',
            'Statistics'
        ],
        'Machine Learning Engineer': [
            'Python', 'Scikit-learn', 'TensorFlow',
            'Deep Learning', 'MLOps'
        ],
        'Python Developer': [
            'Python', 'OOP', 'Django', 'Flask',
            'SQL'
        ],
        'AI Engineer': [
            'Python', 'Machine Learning', 'Deep Learning',
            'LLMs', 'NLP'
        ],
        'Generative AI Engineer': [
            'Python', 'LangChain', 'RAG',
            'LLMs', 'Vector Databases'
        ]
    }
    return requirements


@mcp.tool
def check_eligibility():
    '''Checks candidate eligibility for job applications'''
    eligibility = {
        'Minimum Qualification': 'Bachelor Degree',
        'Experience': 'Freshers and Experienced',
        'Required Skills': 'Based on selected job role',
        'Status': 'Eligible to apply based on basic criteria'
    }
    return eligibility


@mcp.tool
def get_interview_questions():
    '''Provides interview preparation questions'''
    questions = {
        'Python': [
            'What are Python decorators?',
            'Explain OOP concepts in Python.',
            'What is the difference between list and tuple?'
        ],
        'SQL': [
            'What are SQL joins?',
            'Explain window functions.',
            'What is the difference between WHERE and HAVING?'
        ],
        'Machine Learning': [
            'What is overfitting?',
            'Explain Random Forest.',
            'What is the difference between classification and regression?'
        ],
        'Generative AI': [
            'What is an LLM?',
            'Explain Retrieval Augmented Generation.',
            'What is a vector database?'
        ]
    }
    return questions


@mcp.tool
def track_application():
    '''Checks the candidate's job application status'''
    application = {
        'Candidate': 'Demo Candidate',
        'Job Role': 'Data Scientist',
        'Application ID': 'APP1001',
        'Status': 'Under Review'
    }
    return application


if __name__ == '__main__':
    mcp.run(
        transport='streamable-http',
        port=5001,
        host='0.0.0.0'
    )
