from pydantic import BaseModel, Field, FilePath, validators
from typing import Union
from enum import Enum


class OutputTypeType(str, Enum):
    xcom = "xcom"
    file = "file"


class InputModel(BaseModel):
    """
    Input data for TextSummarizerOperator
    """
    input_file_path: str = Field(
        description='The path to the text file to summarize.',
        default=""
    )
    input_text: str = Field(
        description='The text to summarize.',
        default=""
    )
    output_type: OutputTypeType = Field(
        description='The type of output fot the result text.',
        default=OutputTypeType.xcom
    )
    use_gpu: bool = Field(
        description='Use GPU for inference.',
        default=False
    )


class OutputModel(BaseModel):
    """
    Output data for TextSummarizerOperator
    """
    message: str = Field(
        default="",
        description="Output message to log."
    )
    summary_result: str = Field(
        default="",
        description="The result summarized text."
    )
    file_path: FilePath = Field(
        default="",
        description="The path to the resulting summarized text file."
    )