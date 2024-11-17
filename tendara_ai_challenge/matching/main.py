from tendara_ai_challenge.matching.matching import find_relevant_notices
from tendara_ai_challenge.matching.search_profile import CompanySearchProfile
from tendara_ai_challenge.matching.utils import pretty_print_notices


def main():
    search_profile = CompanySearchProfile()
    relevant_notices = find_relevant_notices(search_profile)
    pretty_print_notices(relevant_notices)


if __name__ == "__main__":
    main()
