from pydantic import BaseModel
from datetime import datetime


class CompanySearchProfile(BaseModel):
    """
    This is the description of what the company is looking for.
    You can include any fields here that you think are important for matching.
    It could be as simple as just one query line as like in a search engine, or you can ask user to set-up more complex criteria.
    It's up to you what information you would want to get from the user and how. (single query, multiple keywords, etc.)
    """
    search_text: str = "school"
    """Text that can be used for semantic search to find relevant tender notices."""

    min_submission_deadline: datetime = None
    """Earliest allowed submission deadline for the tender proposals."""

    max_submission_deadline: datetime = None
    """Latest allowed submission deadline for the tender proposals."""

    min_publication_deadline: datetime = None
    """Earliest allowed publication date for the tender notice."""

    max_publication_deadline: datetime = None
    """Latest allowed publication date for the tender notice."""

    min_volume: int = None
    """Minimum estimated contract value in EUR for the tender."""

    max_volume: int = None
    """Maximum estimated contract value in EUR for the tender."""

    cpv_codes: list = None
    """List of Common Procurement Vocabulary (CPV) codes identifying the type of services or goods in the tender.
    """

    location: str = None
    """Geographic location where the tender is being issued or services will be provided (country/city)."""

