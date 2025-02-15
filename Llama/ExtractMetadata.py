from llama_index.core.prompts import PromptTemplate
from llama_index.core import Document
from PydanticModel import Metadata
from llama_index.core.vector_stores import (
    MetadataFilter,
    MetadataFilters,
    FilterOperator,
    FilterCondition
)

async def get_metadata(llm, text):
    """Function to get the metadata from the given resume of the candidate"""
    prompt_template = PromptTemplate("""Generate skills, and country of the education for the given candidate resume.

    Resume of the candidate:

    {text}""")

    metadata = await llm.astructured_predict(
        Metadata,
        prompt_template,
        text=text,
    )

    return metadata


# extract and update metadata aligning with Resume key attribute model and merge parsed chunks
async def update_metadata(document, llm):
    """For every resume, feed its chuncks to LLM, get the metadata and save/update to vector store"""
    full_text = "\n\n".join([doc.text for doc in document])

    # Get the file path of the resume
    file_path = document[0].metadata['filepath']

    # Extract metadata from the resume
    extracted_metadata = await get_metadata(llm, full_text)

    skills = list(set(getattr(extracted_metadata, 'skills', [])))
    country = list(set(getattr(extracted_metadata, 'country', [])))
    domain = getattr(extracted_metadata, 'domain', '')

    # Maintain attributes in database
    ...
    ...
    ...
    global_skills.extend(skills)
    global_countries.extend(country)
    global_domains.append(domain)

    return Document(
                text=full_text,
                metadata={
                    'skills': skills,
                    'country': country,
                    'domain': domain,
                    'file_path': file_path
                }
            )

async def candidates_retriever_from_jd(index, job_description: str):
    # Use structured predict to infer the metadata filters and query string.
    metadata_info = await get_metadata(job_description)
    filters = MetadataFilters(
    filters=[
        MetadataFilter(key="domain", operator=FilterOperator.EQ, value=metadata_info.domain),
        MetadataFilter(key="country", operator=FilterOperator.IN, value=metadata_info.country),
        MetadataFilter(key="skills", operator=FilterOperator.IN, value=metadata_info.skills)
    ],
    condition=FilterCondition.OR
)
    print(f"> Inferred filters: {filters.json()}")
    retriever = index.as_retriever(
    retrieval_mode="chunks",
    metadata_filters=filters,
    )
    # run query
    return retriever.retrieve(job_description)