from CareerConnect.Llama.ExtractMetadata import candidates_retriever_from_jd
from CareerConnect.PydanticModel.MatchScore import MatchScore

def jd_match(llm, job_description, full_text_list):
  sllm = llm.as_structured_llm(MatchScore)
  analyses_reponses = []
  for candidates_resumes_text in full_text_list:
    query = f"""Based on the following job description, please make a score and share the analysis of why specific candidates are suitable for the job.

          Job Description:
          {job_description}

          Candidates:
          {candidates_resumes_text}
          """

    
    response = sllm.complete(query)
    analyses_reponses.append(response)

  return analyses_reponses


def filter_candidates(index, job_description, updated_documents):
  candidates = candidates_retriever_from_jd(index, job_description)
  files_paths = get_candidates_file_paths(candidates)
  full_text_list = get_full_text_from_updated_documents(files_paths, updated_documents)

  return full_text_list

def get_candidates_file_paths(candidates):

  file_paths = []
  for candidate in candidates:
    file_paths.append(candidate.metadata['file_path'])

  return list(set(file_paths))

def get_full_text_from_updated_documents(files_paths, updated_documents):
  full_text_list = []
  # Alternatively, we could save the file path in database for fast retrival
  ...
  for file_path in files_paths:
    for document in updated_documents:
      if document.metadata['file_path'] == file_path:
        full_text_list.append(document.text)
  return full_text_list