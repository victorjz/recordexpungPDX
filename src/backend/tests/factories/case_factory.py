from expungeservice.models.case import Case, CaseCreator, CaseSummary


class CaseSummaryFactory:
    @staticmethod
    def create(
        versus="John Doe",
        info=["John Doe", "1990"],
        case_number="1",
        citation_number=None,
        date_location=["1/1/1995", "Multnomah"],
        type_status=["Offense Misdemeanor", "Closed"],
        case_detail_link="?404",
        balance="0",
    ) -> CaseSummary:
        return CaseCreator.create(
            versus, info, case_number, citation_number, date_location, type_status, case_detail_link, balance, 
        )


class CaseFactory:
    @staticmethod
    def create(
        versus="John Doe",
        info=["John Doe", "1990"],
        case_number="1",
        citation_number=None,
        date_location=["1/1/1995", "Multnomah"],
        type_status=["Offense Misdemeanor", "Closed"],
        charges=[],
        case_detail_link="?404",
        balance="0",
    ) -> Case:
        case_summary = CaseSummaryFactory.create(
            versus, info, case_number, citation_number, date_location, type_status, case_detail_link, balance, 
        )
        return Case(case_summary, tuple(charges))
