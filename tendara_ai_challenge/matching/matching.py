from typing import List
from tendara_ai_challenge.matching.models import Notice
from tendara_ai_challenge.matching.search_profile import CompanySearchProfile
from tendara_ai_challenge.Chroma.Chroma import ChromaSingleton

client = ChromaSingleton()


def find_relevant_notices(search_profile: CompanySearchProfile) -> List[Notice]:
    """Given the company's search profile and all notices,
     returns only the relevant notices for the company."""
    available_notices = client.search(search_profile=search_profile)
    return [Notice.parse_raw(notice) for notice in available_notices]
