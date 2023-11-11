from langchain.pydantic_v1 import BaseModel, Field
from PIL import Image  # type: ignore

from funcchain import chain, settings

settings.MODEL_NAME = "gpt-4-vision-preview"


class AnalysisResult(BaseModel):
    """The result of an image analysis."""

    theme: str = Field(..., description="The theme of the image")
    description: str = Field(..., description="A description of the image")
    objects: list[str] = Field(..., description="A list of objects found in the image")


def analyse_image(image: Image.Image) -> AnalysisResult:
    """
    Analyse the image and extract its
    theme, description and objects.
    """
    return chain()


if __name__ == "__main__":
    example_image = Image.open("examples/assets/cyberspace_landscape.jpg")

    result = analyse_image(example_image)

    print("Theme:", result.theme)
    print("Description:", result.description)

    for obj in result.objects:
        print("Found this object:", obj)
