def parse_log(raw_log: str):
    """
    Very simple parser (you'll improve later)
    """

    if "Failed" in raw_log or "failed" in raw_log:
        return "AUTH_FAILURE", "HIGH"

    if "Accepted" in raw_log or "success" in raw_log:
        return "AUTH_SUCCESS", "LOW"

    return "INFO", "LOW"