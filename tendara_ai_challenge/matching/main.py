from tendara_ai_challenge.matching.matching import find_relevant_notices
from tendara_ai_challenge.matching.search_profile import CompanySearchProfile
from tendara_ai_challenge.matching.utils import load_notices, pretty_print_notices


def main():
    search_profile = CompanySearchProfile()
    all_notices = load_notices()

    relevant_notices = find_relevant_notices(search_profile, all_notices)

    pretty_print_notices(relevant_notices)

if __name__ == "__main__":
    main()
