from typing import List
from tendara_ai_challenge.matching.models import Notice
from tendara_ai_challenge.matching.search_profile import CompanySearchProfile


def find_relevant_notices(search_profile: CompanySearchProfile, available_notices: List[Notice]) -> List[Notice]:
    """Given the company's search profile and all notices, returns only the relevant notices for the company."""
    # TODO: Implement this

    return available_notices
