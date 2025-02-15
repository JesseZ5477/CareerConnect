from pydantic import BaseModel, Field

class MatchScore(BaseModel):
    """
    A data model representing key professional and educational metadata extracted from a resume.
    This class captures essential candidate information including technical/professional skills
    and the geographical distribution of their educational background.

    Attributes:
        score (int): Match score for the candidate regarding the job description
        comment (str): Supporting analysis result for the match score of the candidate

    Example:
        {
            "score": 82,
            "comment": "The candidate is experted in ..."
        }
    """

    score: int = Field(..., ge=0, le=100,
                        description="Match score for the candidate regarding the job description. Returns score between 0 to 100")

    comment: str = Field(..., description="Supporting analysis result for the match score of the candidate. Returns an empty string if no comment is identified.")