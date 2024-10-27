from openai import BaseModel

class CompanySearchProfile(BaseModel):
    """
    This is the description of what the company is looking for.
    You can include any fields here that you think are important for matching.
    It could be as simple as just one query line as like in a search engine, or you can ask user to set-up more complex criteria.
    It's up to you what information you would want to get from the user and how. (single query, multiple keywords, etc.)
    """
    # TODO: Implement this
